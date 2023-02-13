import uuid
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from random import randint

# Create your models here.
class Situacao(models.Model):
    situacao = models.CharField('Situação do aluno', max_length=255)

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'
        ordering = ['situacao']

    def __str__(self):
        return str(self.situacao)

class Curso(models.Model):
    codigo = models.CharField('Código do curso', max_length=255, unique = True)
    nome = models.CharField('Curso', max_length=255)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']

    def __str__(self):
        return f'{self.codigo} - {self.nome}'

class Aluno(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nome = models.CharField('Nome do Aluno', max_length=255)
    matricula = models.CharField('Matrícula do aluno', max_length=11, unique = True, validators=[MinLengthValidator(11)])
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name = 'Curso')
    semestreInicio = models.CharField('Semestre de início', max_length=4, validators=[MinLengthValidator(4)])
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE, verbose_name = 'Situação')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        order_with_respect_to = 'nome'
        #ordering = ['nome'] cannot be used along order_with_respect
        #get_last_by = 'nome'

    def __str__(self):
        return self.nome
    
    def clean(self):
        if not len(self.nome) > 5:
            raise ValidationError({"nome":"cant be used as a name"})
        
        if (int(self.semestreInicio[2]) > 2) | (int(self.semestreInicio[1]) > 2):
            raise ValidationError({"semestreInicio":"invalid semestre"})
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)