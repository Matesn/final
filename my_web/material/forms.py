from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nazev', 'cena', 'sklad',]
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter material nazev'}),
            'cena': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cena za kus'}),
            'sklad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pocet kusu',}),
                    }


class MaterialSearchForm(forms.Form):
    material_name = forms.CharField(
        label='Material name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search for a book'})
    )