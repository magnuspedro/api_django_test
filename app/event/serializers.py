from rest_framework import serializers
from core.models import Event, Group, Calendar
from group.serializers import GroupDetailSerializer
from calend.serializers import CalendarSerializer


class EventSerializer(serializers.ModelSerializer):
    """Serializer an event"""

    visitors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Group.objects.all()
    )

    calendars = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Calendar.objects.all()
    )

    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'desc',
            'star',
            'end',
            'address',
            'visitors',
            'calendars'
        )
        read_only_fields = ('id',)


class EventDetailSerializer(EventSerializer):
    """Serializer with details"""
    visitors = GroupDetailSerializer(many=True, read_only=True)
    calendars = CalendarSerializer(many=True, read_only=True)
