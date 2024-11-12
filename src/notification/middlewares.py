from typing import Any
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import AccessToken


User = get_user_model()


@database_sync_to_async
def get_user_from_jwt_token(token_key):

    try:
        access_token = AccessToken(token_key)
        user_id = access_token["user_id"]
        return User.objects.get(id=user_id)
    except Exception as e:
        print(f"JWT Authentication error : {e}")
        return AnonymousUser()


class TokenauthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):

        query_string = parse_qs(scope["query_string"].decode())
        token_key = query_string.get("token")

        if token_key:
            print(f"Token received {token_key[0]}")
            scope["user"] = await get_user_from_jwt_token(token_key[0])
        else:
            print("No token provided, assigning AnonymousUser")
            scope["user"] = AnonymousUser()

        return await self.inner(scope, receive, send)


def TokenAuthMiddlewareStack(inner):
    return TokenauthMiddleware(inner)
