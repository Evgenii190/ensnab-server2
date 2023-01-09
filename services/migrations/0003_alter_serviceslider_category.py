# Generated by Django 4.0.6 on 2022-12-29 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_serviceslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceslider',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='serviceSlug', to='services.service', verbose_name='Услуга'),
        ),
    ]