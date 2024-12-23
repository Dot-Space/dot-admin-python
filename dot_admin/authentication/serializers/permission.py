from django.contrib.auth.models import Permission
from rest_framework import serializers


class BasePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'codename', 'name', 'content_type')