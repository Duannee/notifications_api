from typing import Any
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model


@database_sync_to_async
def get_user_from_token(token_key):
    from django.contrib.auth.models import AnonymousUser
    from rest_framework.authtoken.models import Token

    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()


class TokenauthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        from django.contrib.auth.models import AnonymousUser

        query_string = parse_qs(scope["query_string"].decode())
        token_key = query_string.get("token")

        if token_key:
            scope["user"] = await get_user_from_token(token_key[0])
        else:
            scope["user"] = AnonymousUser()

        return await self.inner(scope, receive, send)


def TokenAuthMiddlewareStack(inner):
    return TokenauthMiddleware(inner)
