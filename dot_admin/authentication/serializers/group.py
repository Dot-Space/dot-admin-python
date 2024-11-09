from email.headerregistry import Group

from rest_framework import serializers

from .permission import BasePermissionSerializer


class BaseGroupSerializer(serializers.ModelSerializer):
    permissions = BasePermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')