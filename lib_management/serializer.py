from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework.serializers import (
    ValidationError,
    ModelSerializer,
    SerializerMethodField,
    DateTimeField,
    PrimaryKeyRelatedField,
    SlugRelatedField,
)

from .models import *

class BaseModelSerializer(ModelSerializer):
    class Meta:
        abstract = True

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['uid', 'name', 'email', 'phone', 'roles', 'created_at', 'updated_at']


class AddressSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Address
        fields = ['profile', 'city', 'state', 'line1', 'line2']
   
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['uid', 'name']

class BookDetailSerializer(ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = BookDetail
        fields = ['uid', 'name', 'authors', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        book_detail = BookDetail.objects.create(**validated_data)
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(name=author_data['name'])
            book_detail.authors.add(author)
        return book_detail

    def update(self, instance, validated_data):
        authors_data = validated_data.pop('authors')
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # Clear existing authors and add new ones
        instance.authors.clear()
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(name=author_data['name'])
            instance.authors.add(author)
        return instance    


class BookRecordSerializer(ModelSerializer):
    book = BookDetailSerializer()

    class Meta:
        model = BookRecord
        fields = ['uid', 'book', 'edition', 'count', 'price', 'available', 'category', 'created_at', 'updated_at']



class IssueRecordSerializer(ModelSerializer):
    user = ProfileSerializer()
    book = BookDetailSerializer()

    class Meta:
        model = IssueRecord
        fields = ['uid', 'user', 'book', 'status', 'issue_date', 'return_date', 'fine', 'created_at', 'updated_at']

