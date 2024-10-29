import websocket
import json


def on_message(ws, message):
    print(f"message received: {message}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


def on_open(ws):
    print("Connection established")
    ws.send(json.dumps({"message": "Test  WebSocket"}))


ws = websocket.WebSocketApp(
    "ws://localhost:8000/ws/notifications/",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)

ws.run_forever()
