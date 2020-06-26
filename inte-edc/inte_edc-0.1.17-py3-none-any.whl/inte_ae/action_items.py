from django.apps import apps as django_apps
from django.conf import settings
from django.utils.safestring import mark_safe
from edc_action_item import ActionWithNotification, site_action_items
from edc_adverse_event.constants import (
    AE_INITIAL_ACTION,
    AE_FOLLOWUP_ACTION,
    DEATH_REPORT_ACTION,
    AE_TMG_ACTION,
    AE_SUSAR_ACTION,
    DEATH_REPORT_TMG_ACTION,
)
from edc_constants.constants import (
    DEAD,
    LOST_TO_FOLLOWUP,
    YES,
    HIGH_PRIORITY,
    NO,
    CLOSED,
)
from edc_reportable import GRADE5, GRADE4, GRADE3
from edc_visit_schedule.utils import get_offschedule_models
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from inte_prn.constants import END_OF_STUDY_ACTION


class AeFollowupAction(ActionWithNotification):
    name = AE_FOLLOWUP_ACTION
    display_name = "Submit AE Followup Report"
    notification_display_name = "AE Followup Report"
    parent_action_names = [AE_INITIAL_ACTION, AE_FOLLOWUP_ACTION]
    reference_model = "inte_ae.aefollowup"
    related_reference_model = "inte_ae.aeinitial"
    related_reference_fk_attr = "ae_initial"
    create_by_user = False
    show_link_to_changelist = True
    admin_site_name = "inte_ae_admin"
    instructions = mark_safe(
        f"Upon submission the TMG group will be notified "
        f'by email at <a href="mailto:{settings.EMAIL_CONTACTS.get("tmg") or "#"}">'
        f'{settings.EMAIL_CONTACTS.get("tmg") or "unknown"}</a>'
    )
    priority = HIGH_PRIORITY

    def get_next_actions(self):
        next_actions = []

        # add AE followup to next_actions if followup.
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_name=self.name,
            required=self.reference_obj.followup == YES,
        )

        # add Death report to next_actions if G5/Death
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_name=DEATH_REPORT_ACTION,
            required=(
                self.reference_obj.outcome == DEAD
                or self.reference_obj.ae_grade == GRADE5
            ),
        )

        # add Study termination to next_actions if LTFU
        if self.reference_obj.outcome == LOST_TO_FOLLOWUP:
            for offschedule_model in get_offschedule_models(
                subject_identifier=self.subject_identifier,
                report_datetime=self.reference_obj.report_datetime,
            ):
                action_cls = site_action_items.get_by_model(model=offschedule_model)
                next_actions = self.append_to_next_if_required(
                    next_actions=next_actions,
                    action_name=action_cls.name,
                    required=True,
                )
        return next_actions


class AeInitialAction(ActionWithNotification):
    name = AE_INITIAL_ACTION
    display_name = "Submit AE Initial Report"
    notification_display_name = "AE Initial Report"
    parent_action_names = []
    reference_model = "inte_ae.aeinitial"
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = "inte_ae_admin"
    instructions = "Complete the initial AE report"
    priority = HIGH_PRIORITY

    def get_next_actions(self):
        """Returns next actions.

        1. Add death report action if death
        """
        next_actions = []
        deceased = (
            self.reference_obj.ae_grade == GRADE5
            or self.reference_obj.sae_reason.name == DEAD
        )

        # add next AeFollowup if not deceased
        if not deceased:
            next_actions = self.append_to_next_if_required(
                action_name=AE_FOLLOWUP_ACTION, next_actions=next_actions
            )

        # add next AE_SUSAR_ACTION if SUSAR == YES
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_name=AE_SUSAR_ACTION,
            required=(
                self.reference_obj.susar == YES
                and self.reference_obj.susar_reported == NO
            ),
        )

        # add next Death report if G5/Death
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_name=DEATH_REPORT_ACTION,
            required=deceased,
        )

        # add next AE Tmg if G5/Death
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions, action_name=AE_TMG_ACTION, required=deceased
        )
        # add next AeTmgAction if G4
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_name=AE_TMG_ACTION,
            required=self.reference_obj.ae_grade == GRADE4,
        )
        # add next AeTmgAction if G3 and is an SAE
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_name=AE_TMG_ACTION,
            required=(
                self.reference_obj.ae_grade == GRADE3 and self.reference_obj.sae == YES
            ),
        )

        return next_actions


class AeSusarAction(ActionWithNotification):
    name = AE_SUSAR_ACTION
    display_name = "Submit AE SUSAR Report"
    notification_display_name = "AE SUSAR Report"
    parent_action_names = [AE_INITIAL_ACTION]
    reference_model = "inte_ae.aesusar"
    related_reference_model = "inte_ae.aeinitial"
    related_reference_fk_attr = "ae_initial"
    create_by_user = False
    show_link_to_changelist = True
    admin_site_name = "inte_ae_admin"
    instructions = "Complete the AE SUSAR report"
    priority = HIGH_PRIORITY


class AeTmgAction(ActionWithNotification):
    name = AE_TMG_ACTION
    display_name = "TMG AE Report pending"
    notification_display_name = "TMG AE Report"
    parent_action_names = [AE_INITIAL_ACTION, AE_FOLLOWUP_ACTION, AE_TMG_ACTION]
    reference_model = "inte_ae.aetmg"
    related_reference_model = "inte_ae.aeinitial"
    related_reference_fk_attr = "ae_initial"
    create_by_user = False
    color_style = "info"
    show_link_to_changelist = True
    admin_site_name = "inte_ae_admin"
    instructions = mark_safe("This report is to be completed by the TMG only.")
    priority = HIGH_PRIORITY

    def close_action_item_on_save(self):
        return self.reference_obj.report_status == CLOSED


class DeathReportAction(ActionWithNotification):
    name = DEATH_REPORT_ACTION
    display_name = "Submit Death Report"
    notification_display_name = "Death Report"
    reference_model = "inte_ae.deathreport"
    parent_action_names = [AE_INITIAL_ACTION, AE_FOLLOWUP_ACTION]
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = "inte_ae_admin"
    priority = HIGH_PRIORITY
    singleton = True
    dirty_fields = ["cause_of_death"]

    def get_next_actions(self):
        """Adds 1 DEATHReportTMG if not yet created and
        END_OF_STUDY_ACTION if required.
        """
        # DEATH_REPORT_TMG_ACTION
        try:
            self.action_item_model_cls().objects.get(
                parent_action_item=self.reference_obj.action_item,
                related_action_item=self.reference_obj.action_item,
                action_type__name=DEATH_REPORT_TMG_ACTION,
            )
        except ObjectDoesNotExist:
            next_actions = [DEATH_REPORT_TMG_ACTION]
        else:
            next_actions = []

        off_schedule_cls = django_apps.get_model("inte_prn.endofstudy")
        try:
            off_schedule_cls.objects.get(subject_identifier=self.subject_identifier)
        except ObjectDoesNotExist:
            next_actions.append(END_OF_STUDY_ACTION)
        return next_actions


class DeathReportTmgAction(ActionWithNotification):
    name = DEATH_REPORT_TMG_ACTION
    display_name = "TMG Death Report pending"
    notification_display_name = "TMG Death Report"
    parent_action_names = [DEATH_REPORT_ACTION, DEATH_REPORT_TMG_ACTION]
    reference_model = "inte_ae.deathreporttmg"
    related_reference_model = "inte_ae.deathreport"
    related_reference_fk_attr = "death_report"
    priority = HIGH_PRIORITY
    create_by_user = False
    color_style = "info"
    show_link_to_changelist = True
    admin_site_name = "inte_ae_admin"
    instructions = mark_safe("This report is to be completed by the TMG only.")

    def reopen_action_item_on_change(self):
        """Do not reopen if status is CLOSED.
        """
        return self.reference_obj.report_status != CLOSED

    @property
    def matching_cause_of_death(self):
        """Returns True if cause_of_death on TMG Death Report matches
        cause_of_death on Death Report.
        """
        return (
            self.reference_obj.death_report.cause_of_death
            == self.reference_obj.cause_of_death
        )

    def close_action_item_on_save(self):
        if self.matching_cause_of_death:
            self.delete_children_if_new(parent_action_item=self.action_item)
        return self.reference_obj.report_status == CLOSED

    def get_next_actions(self):
        """Returns an second DeathReportTmgAction if the
        submitted report does not match the cause of death
        of the original death report.

        Also, no more than two DeathReportTmgAction can exist.
        """
        next_actions = []
        try:
            self.action_item_model_cls().objects.get(
                parent_action_item=self.related_action_item,
                related_action_item=self.related_action_item,
                action_type__name=self.name,
            )
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            # because more than one action item has the same
            # parent_action_item and related_action_item. this
            # only occurs for older data.
            pass
        else:
            if (
                self.action_item_model_cls()
                .objects.filter(
                    related_action_item=self.related_action_item,
                    action_type__name=self.name,
                )
                .count()
                < 2
            ):
                if (
                    self.reference_obj.cause_of_death
                    != self.related_action_item.reference_obj.cause_of_death
                ):
                    next_actions = ["self"]
        return next_actions


site_action_items.register(DeathReportAction)
site_action_items.register(DeathReportTmgAction)
site_action_items.register(AeFollowupAction)
site_action_items.register(AeInitialAction)
site_action_items.register(AeSusarAction)
site_action_items.register(AeTmgAction)
