from django import forms
from .models import PollingUnit, AnnouncedPuResults

class NewPollingUnitForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPuResults
        fields = ['polling_unit_uniqueid', 'party_abbreviation', 'party_score']
        widgets = {
            'polling_unit_uniqueid': forms.Select(attrs={'class': 'form-control'}),
            'party_abbreviation': forms.TextInput(attrs={'class': 'form-control'}),
            'party_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically populate polling_unit_uniqueid dropdown
        self.fields['polling_unit_uniqueid'].choices = [
            (unit.uniqueid, unit.polling_unit_name) for unit in PollingUnit.objects.all()
        ]
