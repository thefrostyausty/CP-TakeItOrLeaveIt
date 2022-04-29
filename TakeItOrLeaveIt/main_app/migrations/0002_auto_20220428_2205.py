# Generated by Django 3.0 on 2022-04-28 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='takes',
        ),
        migrations.AddField(
            model_name='take',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='main_app.Event'),
            preserve_default=False,
        ),
    ]
