from django.urls import path
from .views import EventCreateView, EventUpdateView

urlpatterns = [
    path("event/create/", EventCreateView.as_view(), name="event-create"),
    path(
        "event/<int:pk>/update/",
        EventUpdateView.as_view(),
        name="event-update",
    ),
]
