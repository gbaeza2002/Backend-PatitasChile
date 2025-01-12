# Generated by Django 4.2.3 on 2024-10-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_confirmed_user_verification_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='reset_code_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
