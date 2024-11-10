from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    path("event/create/", EventListCreateView.as_view(), name="event-list-create"),
    path(
        "event/<int:pk>/update/",
        EventRetrieveUpdateDestroyView.as_view(),
        name="event-retrieve-update-destroy",
    ),
]
