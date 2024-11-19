from django.forms import ValidationError
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Course"])
class CourseCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "New course available", "data": response.data},
            status=status.HTTP_201_CREATED,
        )


@extend_schema(tags=["Course"])
class CourseUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Course updated", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def partial_update(self, request, *args, **kwargs):
        invalid_fields = [
            key for key in request.data if key not in self.serializer_class().fields
        ]

        if invalid_fields:
            raise ValidationError({"invalid_fields": invalid_fields})

        return super().partial_update(request, *args, **kwargs)
