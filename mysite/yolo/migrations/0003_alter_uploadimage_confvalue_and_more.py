# Generated by Django 4.0.3 on 2022-05-08 16:47

from django.db import migrations, models
import yolo.models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0002_remove_uploadimage_caption_uploadimage_confvalue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='confValue',
            field=models.FloatField(default=0.3, validators=[yolo.models.validatorValue], verbose_name='Confidence'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='iouValue',
            field=models.FloatField(default=0.3, validators=[yolo.models.validatorValue], verbose_name='IoU'),
        ),
    ]