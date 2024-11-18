from django.forms import ValidationError
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class EventCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "New event created", "data": response.data},
            status=status.HTTP_201_CREATED,
        )


class EventUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Event updated", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def partial_update(self, request, *args, **kwargs):
        invalid_fields = [
            key for key in request.data if key not in self.serializer_class().fields
        ]

        if invalid_fields:
            raise ValidationError({"invalid_fields": invalid_fields})

        return super().partial_update(request, *args, **kwargs)
