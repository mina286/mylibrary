# Generated by Django 4.0.1 on 2022-02-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mls_app', '0007_login_alter_category_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AddField(
            model_name='book',
            name='totol_renatl',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]