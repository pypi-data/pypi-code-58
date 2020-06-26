from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_crf.admin import crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin, TabularInlineMixin
from inte_subject.forms import DrugSupplyHypertensionForm

from ..admin_site import inte_subject_admin
from ..forms import DrugRefillHypertensionForm
from ..models import DrugRefillHypertension, DrugSupplyHypertension
from .modeladmin_mixins import CrfModelAdminMixin, DrugSupplyInlineMixin


class DrugSupplyHypertensionInline(
    DrugSupplyInlineMixin, TabularInlineMixin, admin.TabularInline
):
    model = DrugSupplyHypertension
    form = DrugSupplyHypertensionForm
    min_num = 1

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj=None, **kwargs)
        formset.validate_min = True
        return formset


@admin.register(DrugRefillHypertension, site=inte_subject_admin)
class DrugRefillHypertensionAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = DrugRefillHypertensionForm

    inlines = [DrugSupplyHypertensionInline]

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Hypertension Drug Refill Today",
            {
                "fields": (
                    "rx",
                    "rx_other",
                    "rx_modified",
                    "modifications",
                    "modifications_other",
                    "modifications_reason",
                    "modifications_reason_other",
                    "return_in_days",
                )
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    filter_horizontal = ["rx", "modifications", "modifications_reason"]

    radio_fields = {
        "crf_status": admin.VERTICAL,
        "rx_modified": admin.VERTICAL,
    }
