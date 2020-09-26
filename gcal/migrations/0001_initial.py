# Generated by Django 3.1 on 2020-09-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GCalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_event', models.DateTimeField()),
                ('end_event', models.DateTimeField()),
                ('all_day', models.BooleanField(choices=[('No', 'Not all day'), ('Yes', 'All day')])),
                ('repeat_event', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Every year')], max_length=10)),
                ('notification', models.CharField(choices=[('email', 'Email'), ('notification', 'Notificaton'), ('none', 'None')], max_length=100)),
                ('state', models.CharField(choices=[('busy', 'Busy'), ('free', 'Free')], max_length=100)),
                ('privacy', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], max_length=100)),
                ('active', models.BooleanField(choices=[('active', 'Active'), ('not_active', 'Not active')], max_length=50)),
            ],
        ),
    ]
