from django import forms
from django.core.exceptions import ValidationError
from core.models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

    def clean(self):
 
        # data from the form is fetched using super function
        super(AlunoForm, self).clean()
         
        # extract the username and text field from the data
        nome = self.cleaned_data.get('nome')
        
        # conditions to be met for the username length
        if len(nome) < 5:
            self._errors['nome'] = self.error_class([
                'Minimum 5 characters required'])
 
        # return any errors if found
        return self.cleaned_data

widget = {
    'nome': forms.TextInput(attrs={'class':'form-control'}),
    'matricula': forms.TextInput(attrs={'class':'form-control'}),
    'curso': forms.Select(attrs={'class':'form-control'}),
    'semestreInicio': forms.TextInput(attrs={'class':'form-control'}),
    'situacao': forms.Select(attrs={'class':'form-control'}),
}