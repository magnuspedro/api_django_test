from rest_framework import serializers
from core.models import Group, User

from user.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    """Serializer group"""
    users = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = Group
        fields = ('id', 'desc', 'users')


class GroupDetailSerializer(GroupSerializer):
    """Serilizer a detail group"""
    users = UserSerializer(many=True, read_only=True)
