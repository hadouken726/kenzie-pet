from rest_framework.serializers import Serializer, CharField, FloatField, IntegerField


class CharacteristicSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=255)


class GroupSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=100)
    scientific_name = CharField(max_length=100)


class AnimalSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=100)
    age = FloatField()
    weight = FloatField()
    sex = CharField(max_length=30)
    group = GroupSerializer(read_only=True)
    characteristics = CharacteristicSerializer(many=True, read_only=True)