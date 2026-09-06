import os
import asyncio
from twitchAPI.twitch import Twitch
print("Импорт есть!")
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatEvent
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")
client_user_token = os.getenv("TWITCH_USER_TOKEN")

async def on_ready(ready_event: EventData):
    print("Бот подключен!")
    await ready_event.chat.join_room("s6d1k")

async def on_message(msg: ChatMessage):
    print(f"{msg.user.name}: {msg.text}")

async def run():
    print("Шаг 1: создаю twitch")
    twitch = await Twitch(client_id, client_secret)
    print("Шаг 2: twitch создан")

    auth = UserAuthenticator(twitch, [AuthScope.CHAT_READ], url="http://localhost:3000", port=3000)
    print("Шаг 3: начинаю authenticate()")
    token, refresh_token = await auth.authenticate()
    print("Шаг 4: authenticate() завершился, токен получен")

    await twitch.set_user_authentication(token, [AuthScope.CHAT_READ], refresh_token)
    print("Шаг 5: аутентификация установлена")

    chat = await Chat(twitch)
    print("Шаг 6: chat создан")

    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    print("Шаг 7: события зарегистрированы, запускаю chat.start()")

    chat.start()
    print("Шаг 8: chat.start() вызван")

asyncio.run(run())