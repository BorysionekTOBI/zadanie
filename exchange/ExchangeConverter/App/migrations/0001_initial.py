# Generated by Django 5.0.3 on 2024-03-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyConversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_currency', models.CharField(max_length=3)),
                ('target_currency', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('conversion_rate', models.DecimalField(decimal_places=6, max_digits=10)),
                ('result', models.DecimalField(decimal_places=2, max_digits=10)),
                ('conversion_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
