from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "start_time",
            "end_time",
            "organizer",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at", "start_time", "end_time"]
