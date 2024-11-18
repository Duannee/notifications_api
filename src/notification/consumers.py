from channels.generic.websocket import AsyncWebsocketConsumer
import json


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            self.group_name = f"notifications_{self.user.id}"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()
            print(f"User {self.user.username} connected to WebSocket")
        else:
            print("Unauthenticated user attempted to connect")
            await self.close()

    async def disconnect(self, close_code):
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        notification_type = data.get("notification_type")
        content = data.get("content")
        actor = data.get("actor")

        if notification_type == "comment_post":
            await self.handle_comment_post_notification(actor, content)
        elif notification_type == "like_post":
            await self.handle_like_post_notification(actor, content)
        elif notification_type == "reply_comment":
            await self.handle_reply_comment_notification(actor, content)
        elif notification_type == "like_comment":
            await self.handle_like_comment_notification(actor, content)
        else:
            await self.send(
                text_data=json.dumps({"error": "Notification type not recognized"})
            )

    async def handle_comment_post_notification(self, actor, content):
        await self.send(
            text_data=json.dumps(
                {
                    "notification_type": "comment_post",
                    "notification": f"{actor} commented on your post: {content}",
                }
            )
        )

    async def handle_like_post_notification(self, actor, content):
        await self.send(
            text_data=json.dumps(
                {
                    "notification_type": "like_post",
                    "notification": f"{actor} liked your post: {content}",
                }
            )
        )

    async def handle_reply_comment_notification(self, actor, content):
        await self.send(
            text_data=json.dumps(
                {
                    "notification_type": "reply_comment",
                    "notification": f"{actor} replied your post: {content}",
                }
            )
        )

    async def handle_like_comment_notification(self, actor, content):
        await self.send(
            text_data=json.dumps(
                {
                    "notification_type": "like_comment",
                    "notification": f"{actor} liked your comment: {content}",
                }
            )
        )

    async def send_notification(self, event):
        notification_data = event["notification"]
        await self.send(text_data=json.dumps(notification_data))
