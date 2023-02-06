from django import forms

from core.models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

""" widget = {
    'nome': forms.TextInput(attrs={'class':'form-control'}),
    'matricula': forms.TextInput(attrs={'class':'form-control'}),
    'curso': forms.Select(attrs={'class':'form-control'}),
    'semestreInicio': forms.TextInput(attrs={'class':'form-control'}),
    'situacao': forms.Select(attrs={'class':'form-control'}),
} """