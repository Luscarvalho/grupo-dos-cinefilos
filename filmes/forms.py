from django import forms
from .models import Films


class FilmsForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['nome', 'ano']

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        ano = cleaned_data.get('ano')

        if Films.objects.filter(nome=nome, ano=ano).exists():
            raise forms.ValidationError("Filme já cadastrado.")

        if not ano.isdigit():
            raise forms.ValidationError("O ano deve conter apenas números.")

        return cleaned_data
