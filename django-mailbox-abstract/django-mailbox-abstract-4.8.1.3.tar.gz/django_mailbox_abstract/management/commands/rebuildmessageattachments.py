import email
import hashlib
import logging

from django.core.management.base import BaseCommand
from django.apps import apps

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    """ Briefly, a bug existed in a migration that may have caused message
    attachments to become disassociated with their messages.  This management
    command will read through existing message attachments and attempt to
    re-associate them with their original message.

    This isn't foolproof, I'm afraid.  If an attachment exists twice, it will
    be associated only with the most recent e-mail message.  That said,
    I'm quite sure that the bug in the migration is gone (and you'd have to
    have been quite unlucky to have ran the bad migration).

    """
    def add_arguments(self, parser):
        parser.add_argument(
            'message_model_name',
            help="The name of the inherited model of message"
        )
        parser.add_argument(
            'message_attachment_model_name',
            help="The name of the inherited model of message`s attachment"
        )

    def handle(self, message_model_name, message_attachment_model_name, *args, **options):
        message_model = apps.get_model(message_model_name)
        message_attachment_model = apps.get_model(message_attachment_model_name)

        attachment_hash_map = {}

        attachments_without_messages = message_attachment_model.objects.filter(
            message=None
        ).order_by(
            'id'
        )

        if attachments_without_messages.count() < 1:
            return

        for attachment in attachments_without_messages:
            md5 = hashlib.md5()
            for chunk in attachment.document.file.chunks():
                md5.update(chunk)
            attachment_hash_map[md5.hexdigest()] = attachment.pk

        for message_record in message_model.objects.all().order_by('id'):
            message = email.message_from_string(message_record.body)
            if message.is_multipart():
                for part in message.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                    md5 = hashlib.md5()
                    md5.update(part.get_payload(decode=True))
                    digest = md5.hexdigest()
                    if digest in attachment_hash_map:
                        attachment = message_attachment_model.objects.get(
                            pk=attachment_hash_map[digest]
                        )
                        attachment.message = message_record
                        attachment.save()
                        logger.info(
                            "Associated message %s with attachment %s (%s)",
                            message_record.pk,
                            attachment.pk,
                            digest
                        )
                    else:
                        logger.info(
                            "%s(%s) not found in currently-stored attachments",
                            part.get_filename(),
                            digest
                        )
