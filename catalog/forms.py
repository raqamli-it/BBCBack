from django import forms
from catalog.models import InstallmentPlan


class InstallmentPlanForm(forms.ModelForm):
    class Meta:
        model = InstallmentPlan
        fields = ['car_model', 'duration', 'prepayment_percentage']

    duration = forms.IntegerField(label='Duration (months)', min_value=1)
    prepayment_percentage = forms.IntegerField(label='Prepayment percentage', min_value=0, max_value=100)
