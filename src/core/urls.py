"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from notification.consumers import NotificationConsumer
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Notification API!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("api/", include("course.urls")),
    path("api/", include("authentication.urls")),
    path("api/", include("event.urls")),
    path("api/", include("notification.urls")),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/notification/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="notification-docs",
    ),
]

websocket_urlpatterns = [path("ws/notifications/", NotificationConsumer.as_asgi())]
