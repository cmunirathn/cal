from django import forms
class LovesForm(forms.Form):
    boyfrnd_name=forms.CharField(
        label='Enter Boy Frnd Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Boy Frnd name'
            }
        )
    )
    girlfrnd_name = forms.CharField(
    label='Enter Girl Frnd Name',
    widget=forms.TextInput(
        attrs={
            'class': 'from-control',
            'placeholder': 'Girl Frnd Name'
        }
    )
)

