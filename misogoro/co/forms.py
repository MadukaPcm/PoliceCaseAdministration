from django.db.models import Model, fields
from django.forms import ModelForm
from co.models import *

class CaseViewForm(ModelForm):
    class Meta:
        model = CaseStatus
        fields = "__all__"
