from django.urls import path
from .views import WebSocketNotificationInfoView

urlpatterns = [
    path("ws/notifications/", WebSocketNotificationInfoView.as_view(), name="ws_info"),
]
