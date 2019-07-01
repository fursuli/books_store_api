import traceback

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from bs_api.models import Author, Book, Order


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    # def create(self, validated_data):
    #     """ Overwritten serializer.create method to fix user creation with hashed passwword"""
    #
    #     raise_errors_on_nested_writes("create", self, validated_data)
    #
    #     ModelClass = self.Meta.model
    #
    #     info = model_meta.get_field_info(ModelClass)
    #     many_to_many = {}
    #     for field_name, relation_info in info.relations.items():
    #         if relation_info.to_many and (field_name in validated_data):
    #             many_to_many[field_name] = validated_data.pop(field_name)
    #
    #     try:
    #         instance = ModelClass._default_manager.create_user(**validated_data)
    #     except TypeError:
    #         tb = traceback.format_exc()
    #         msg = (
    #             "Got a `TypeError` when calling `%s.%s.create()`. "
    #             "This may be because you have a writable field on the "
    #             "serializer class that is not a valid argument to "
    #             "`%s.%s.create()`. You may need to make the field "
    #             "read-only, or override the %s.create() method to handle "
    #             "this correctly.\nOriginal exception was:\n %s"
    #             % (
    #                 ModelClass.__name__,
    #                 ModelClass._default_manager.name,
    #                 ModelClass.__name__,
    #                 ModelClass._default_manager.name,
    #                 self.__class__.__name__,
    #                 tb,
    #             )
    #         )
    #         raise TypeError(msg)


class BookSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    # def create(self, validated_data):
    #     """ Overwritten serializer.create method to fix user creation with hashed passwword"""
    #
    #     raise_errors_on_nested_writes("create", self, validated_data)
    #
    #     ModelClass = self.Meta.model
    #
    #     info = model_meta.get_field_info(ModelClass)
    #     many_to_many = {}
    #     for field_name, relation_info in info.relations.items():
    #         if relation_info.to_many and (field_name in validated_data):
    #             many_to_many[field_name] = validated_data.pop(field_name)
    #
    #     try:
    #         instance = ModelClass._default_manager.create_user(**validated_data)
    #     except TypeError:
    #         tb = traceback.format_exc()
    #         msg = (
    #             "Got a `TypeError` when calling `%s.%s.create()`. "
    #             "This may be because you have a writable field on the "
    #             "serializer class that is not a valid argument to "
    #             "`%s.%s.create()`. You may need to make the field "
    #             "read-only, or override the %s.create() method to handle "
    #             "this correctly.\nOriginal exception was:\n %s"
    #             % (
    #                 ModelClass.__name__,
    #                 ModelClass._default_manager.name,
    #                 ModelClass.__name__,
    #                 ModelClass._default_manager.name,
    #                 self.__class__.__name__,
    #                 tb,
    #             )
    #         )
    #         raise TypeError(msg)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # def create(self, validated_data):
    #     """ Overwritten serializer.create method to fix user creation with hashed passwword"""
    #
    #     raise_errors_on_nested_writes("create", self, validated_data)
    #
    #     ModelClass = self.Meta.model
    #
    #     info = model_meta.get_field_info(ModelClass)
    #     many_to_many = {}
    #     for field_name, relation_info in info.relations.items():
    #         if relation_info.to_many and (field_name in validated_data):
    #             many_to_many[field_name] = validated_data.pop(field_name)
    #
    #     try:
    #         instance = ModelClass._default_manager.create_user(**validated_data)
    #     except TypeError:
    #         tb = traceback.format_exc()
    #         msg = (
    #             "Got a `TypeError` when calling `%s.%s.create()`. "
    #             "This may be because you have a writable field on the "
    #             "serializer class that is not a valid argument to "
    #             "`%s.%s.create()`. You may need to make the field "
    #             "read-only, or override the %s.create() method to handle "
    #             "this correctly.\nOriginal exception was:\n %s"
    #             % (
    #                 ModelClass.__name__,
    #                 ModelClass._default_manager.name,
    #                 ModelClass.__name__,
    #                 ModelClass._default_manager.name,
    #                 self.__class__.__name__,
    #                 tb,
    #             )
    #         )
    #         raise TypeError(msg)

# class OrdersBooksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrdersBooksRelation
#         fields = '__all__'
