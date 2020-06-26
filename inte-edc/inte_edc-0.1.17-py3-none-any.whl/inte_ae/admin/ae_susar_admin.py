from django.contrib import admin
from edc_adverse_event.modeladmin_mixins import AeSusarModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import inte_ae_admin
from ..forms import AeSusarForm
from ..models import AeSusar


@admin.register(AeSusar, site=inte_ae_admin)
class AeSusarAdmin(AeSusarModelAdminMixin, SimpleHistoryAdmin):

    form = AeSusarForm
