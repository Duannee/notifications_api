from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema_view, extend_schema

urlpatterns = [
    path(
        "token/",
        extend_schema_view(post=extend_schema(tags=["Token"]))(
            TokenObtainPairView.as_view()
        ),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        extend_schema_view(post=extend_schema(tags=["Token"]))(
            TokenRefreshView.as_view()
        ),
        name="token_refresh",
    ),
]
