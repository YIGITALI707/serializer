from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import News,Products,Cats

class NewsSerializers(serializers.Serializer):
    title=serializers.CharField(max_length=150)
    content=serializers.CharField()

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title=validated_data.get("title",instance.title)
        instance.content=validated_data.get("content",instance.content)
        instance.save()
        return instance




class ProductsSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=150)
    description=serializers.CharField()

    def create(self, validated_data):
        return Products.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.description=validated_data.get("description",instance.description)
        instance.save()
        return instance




class CatsSerializers(serializers.Serializer):
    ism = serializers.CharField(max_length=150)
    turi = serializers.CharField()

    def create(self, validated_data):
        return Cats.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.ism=validated_data.get("ism",instance.ism)
        instance.turi=validated_data.get("turi",instance.turi)
        instance.save()
        return instance
