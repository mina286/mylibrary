# Generated by Django 4.0.1 on 2022-01-28 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('retal_price_day', models.DecimalField(decimal_places=2, max_digits=6)),
                ('retal_period', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('availble', 'availble'), ('rental', 'rental'), ('sold', 'sold')], max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mls_app.category')),
            ],
        ),
    ]