from django.urls import path
from .views import CourseCreateView, CourseUpdateView

urlpatterns = [
    path("course/create/", CourseCreateView.as_view(), name="course-list-create"),
    path(
        "course/<int:pk>/update/",
        CourseUpdateView.as_view(),
        name="course-retrieve-update-destroy",
    ),
]
