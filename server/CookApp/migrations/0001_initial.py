# Generated by Django 4.2.2 on 2023-06-25 12:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('rank', models.CharField(choices=[('Стюарт', 'Стюарт'), ('Линейный повар', 'Линейный повар'), ('Заготовщик', 'Заготовщик'), ('Старший повар', 'Старший повар'), ('Су-шеф', 'Су-шеф'), ('Шеф', 'Шеф')], max_length=50)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('Мясо', 'Мясо'), ('Рыба', 'Рыба'), ('Горячее', 'Горячее'), ('Холодное', 'Холодное')], max_length=50)),
                ('description', models.TextField()),
                ('cook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CookApp.cook')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('category', models.CharField(choices=[('Жидкое', 'Жидкое'), ('Твердое', 'Твердое')], max_length=50)),
                ('dish', models.ManyToManyField(to='CookApp.dish')),
            ],
        ),
    ]