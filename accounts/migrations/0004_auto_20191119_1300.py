# Generated by Django 2.2.7 on 2019-11-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191119_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='a88f72cb69e14774a64442a327891b234cb82f8697544cf99f50821c8d210c5f', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='d700c8ce426e41a1a58343e6764b72d51c47edc085ad4124a873241e6022032c', max_length=300, null=True),
        ),
    ]