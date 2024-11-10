from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class EventListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "New event created", "data": response.data},
            status=status.HTTP_201_CREATED,
        )


class EventRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Event updated", "data": response.data},
            status=status.HTTP_200_OK,
        )
