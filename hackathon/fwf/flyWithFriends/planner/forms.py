from django import forms
from .models import Plan, Places

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ["origin", "sdate", "destination", "edate"]
