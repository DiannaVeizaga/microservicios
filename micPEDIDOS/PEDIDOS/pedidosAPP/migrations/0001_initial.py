# Generated by Django 5.1.4 on 2024-12-09 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50)),
                ('precio', models.PositiveIntegerField()),
                ('cliente', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
            ],
        ),
    ]
