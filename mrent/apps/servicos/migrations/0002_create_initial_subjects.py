# Generated by Django 2.0.1 on 2018-01-18 18:07

from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('servicos', 'Subject')
    Subject.objects.create(name='Eletricista', color='#343a40')
    Subject.objects.create(name='Encanador', color='#007bff')
    Subject.objects.create(name='Instalações', color='#28a745')
    Subject.objects.create(name='Pintura', color='#17a2b8')
    Subject.objects.create(name='Manutenção', color='#ffc107')


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]
