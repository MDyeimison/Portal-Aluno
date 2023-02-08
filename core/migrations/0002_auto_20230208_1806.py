# Generated by Django 3.2.12 on 2023-02-08 18:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='situacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.situacao', verbose_name='Situação'),
        ),
    ]