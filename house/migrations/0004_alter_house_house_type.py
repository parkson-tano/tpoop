# Generated by Django 4.1.4 on 2023-02-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_alter_house_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='house_type',
            field=models.CharField(choices=[('chambre_modern', 'chambre_modern'), ('chambre_simple', 'chambre_simple'), ('studio_modern', 'studio_modern'), ('mini_studio', 'mini_studio'), ('appartement', 'appartement'), ('appartement_meubler', 'appartement_meubler')], max_length=256, null=True),
        ),
    ]
