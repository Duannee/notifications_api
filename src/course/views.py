from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class CourseListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "New course available", "data": response.data},
            status=status.HTTP_201_CREATED,
        )


class CourseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Course updated", "data": response.data},
            status=status.HTTP_200_OK,
        )
