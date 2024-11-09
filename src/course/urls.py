from django.urls import path
from .views import CourseListCreateView, CourseRetrieveUpdateDestroyView

urlpatterns = [
    path("course/create/", CourseListCreateView.as_view(), name="course-list-create"),
    path(
        "course/<int:pk>/update",
        CourseRetrieveUpdateDestroyView.as_view(),
        name="course-retrieve-update-destroy",
    ),
]
