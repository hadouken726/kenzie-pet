from django.db.models import Model, CharField, FloatField
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField


class Group(Model):
    name = CharField(max_length=100)
    scientific_name = CharField(max_length=100)


class Characteristic(Model):
    name = CharField(max_length=255)


class Animal(Model):
    name = CharField(max_length=100)
    age = FloatField()
    weight = FloatField()
    sex = CharField(max_length=30)
    group = ForeignKey('Group', on_delete=CASCADE, default=None)
    characteristics = ManyToManyField(Characteristic)