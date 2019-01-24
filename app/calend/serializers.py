from rest_framework import serializers
from core.models import Calendar


class CalendarSerializer(serializers.ModelSerializer):
    """Serializer an event"""
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'desc')
        read_only_fields = ('id',)
