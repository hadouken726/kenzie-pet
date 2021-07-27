from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from api.models import Animal, Characteristic, Group
from rest_framework.serializers import Serializer, CharField, FloatField, IntegerField


class CharacteristicSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=255)
    def create(self, validated_data):
        return Characteristic.objects.create(**validated_data)


class GroupSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=100)
    scientific_name = CharField(max_length=100)
    def create(self, validated_data):
        return Group.objects.create(**validated_data)


class AnimalSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=100)
    age = FloatField()
    weight = FloatField()
    sex = CharField(max_length=30)
    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)
    def create(self, validated_data):
        group_data = validated_data.pop('group')
        chars_data = validated_data.pop('characteristics')
        try:
            group = Group.objects.get(scientific_name=group_data.get('scientific_name'))
        except ObjectDoesNotExist:
            group = GroupSerializer().create(group_data)
        characteristics = []
        for char in chars_data:
            try:
                characteristic = Characteristic.objects.get(name=char.get('name'))
            except ObjectDoesNotExist:
                characteristic = CharacteristicSerializer().create(char)    
            characteristics.append(characteristic)
        animal = Animal.objects.create(**validated_data)
        animal.group = group
        animal.characteristics.set(characteristics) 
        return animal