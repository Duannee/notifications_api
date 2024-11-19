from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class WebSocketNotificationInfoView(GenericAPIView):
    @extend_schema(
        tags=["WebSocket"],
        summary="WebSocket Notifications Info",
        description=(
            "This endpoint provides information on how to use the WebSocket for real-time notifications.\n\n"
            "**WebSocket Connection:**\n"
            "- URL: `ws://localhost:8000/ws/notifications/`\n"
            "- **JWT Authentication:**\n"
            "  - **Query String**: Include the JWT token in the URL: `?token=<JWT>`.\n"
            "  - **Middleware**: The `TokenAuthMiddleware` is used to validate the token.\n\n"
            "**Supported Notification Types:**\n"
            "- `comment_post`: Notification for a comment on a post.\n"
            "- `like_post`: Notification for a like on a post.\n"
            "- `reply_comment`: Notification for a reply to a comment.\n"
            "- `like_comment`: Notification for a like on a comment.\n\n"
            "**Message Format:**\n"
            "- **Message sent by the client:**\n"
            "  ```json\n"
            "  {\n"
            '    "notification_type": "like_post",\n'
            '    "actor": "John",\n'
            '    "content": "Your post is amazing!"\n'
            "  }\n"
            "  ```\n\n"
            "- **Message received by the client:**\n"
            "  ```json\n"
            "  {\n"
            '    "notification_type": "like_post",\n'
            '    "notification": "John liked your post: Your post is amazing!"\n'
            "  }\n"
            "  ```\n\n"
            "**Supported Events:**\n"
            "- `subscribe`: Subscribe to notifications (automatically handled on connection).\n"
            "- `unsubscribe`: Unsubscribe from notifications (not implemented in this example)."
        ),
        responses={
            200: "Detailed information about the WebSocket provided successfully."
        },
    )
    def get(self, request, *args, **kwargs):
        """
        Returns information on how to use the WebSocket for notifications.
        """
        return Response(
            {
                "url": "ws://localhost:8000/ws/notifications/",
                "authentication": {
                    "query_string": "?token=<JWT>",
                    "middleware": "TokenAuthMiddleware",
                },
                "notification_types": [
                    {"type": "comment_post", "description": "Comment on a post."},
                    {"type": "like_post", "description": "Like on a post."},
                    {"type": "reply_comment", "description": "Reply to a comment."},
                    {"type": "like_comment", "description": "Like on a comment."},
                ],
                "message_format": {
                    "client_to_server": {
                        "notification_type": "like_post",
                        "actor": "John",
                        "content": "Your post is amazing!",
                    },
                    "server_to_client": {
                        "notification_type": "like_post",
                        "notification": "John liked your post: Your post is amazing!",
                    },
                },
                "events_supported": ["subscribe", "unsubscribe"],
            }
        )
