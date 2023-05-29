from django import forms

from core import models

class UserForm(forms.ModelForm):
    name = forms.CharField(label='Имя', required=True)

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isnumeric():
            raise forms.ValidationError('Имя не должно состоять только из чисел')
        return name

    class Meta:
        model = models.User
        fields = '__all__'
