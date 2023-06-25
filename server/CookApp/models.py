from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Cook(models.Model):
    name = models.CharField(max_length=150)
    RANKS = (
        ('Стюарт','Стюарт'),
        ('Линейный повар', 'Линейный повар'),
        ('Заготовщик', 'Заготовщик'),
        ('Старший повар', 'Старший повар'),
        ('Су-шеф', 'Су-шеф'),
        ('Шеф', 'Шеф')
    )
    rank = models.CharField(max_length=50, choices=RANKS)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    CATEGORIES = (
        ('Мясо', 'Мясо'),
        ('Рыба', 'Рыба'),
        ('Горячее', 'Горячее'),
        ('Холодное', 'Холодное')
    )
    category = MultiSelectField(choices=CATEGORIES,max_choices=4,
                                 max_length=50)
    description = models.TextField()
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    CATEGORIES = (
        ('Жидкое', 'Жидкое'),
        ('Твердое', 'Твердое')
    )
    category = models.CharField(max_length=50, choices=CATEGORIES)
    dish = models.ManyToManyField(Dish, null=True, blank=True)

    def __str__(self):
        return self.name
