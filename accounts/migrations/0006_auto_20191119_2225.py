# Generated by Django 2.2.7 on 2019-11-19 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191119_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='bd2dbeaaa4b04a2ea75cb5d3d045b1ff9bb7ec9784704180b088926861c5b708', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='940a013a853e405e84401e3f7d2c4d0e51589eae194c42d4a6574ff2cc7030ec', max_length=300, null=True),
        ),
    ]
