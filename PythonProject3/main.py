import asyncio
import os
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
from tortoise import Tortoise, fields
from tortoise.models import Model

load_dotenv()

class ChatUser(Model):
    chat_id = fields.BigIntField(unique=True)
    name = fields.CharField(max_length=100)
    is_active = fields.BooleanField(default=True)


bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
if not bot_token:
    raise RuntimeError('Укажите TELEGRAM_BOT_TOKEN в файле .env')

bot = AsyncTeleBot(bot_token)


@bot.message_handler(commands=['start'])
async def start(message):
    user, created = await ChatUser.get_or_create(
        chat_id=message.chat.id,
        defaults={'name': message.from_user.username or 'Аноним'}
    )

    if not user.is_active:
        user.is_active = True
        await user.save()

    await bot.send_message(message.chat.id, f'Привет {user.name}, добро пожаловать в чат!')


@bot.message_handler(func=lambda m: True)
async def broadcast_chat(message):
    if not await ChatUser.filter(chat_id=message.chat.id).exists():
        await bot.send_message(message.chat.id, "Сначала нажмите /start")
    else:
        users = await ChatUser.filter(is_active=True)
        sender = await ChatUser.get(chat_id=message.chat.id)
        name_user = sender.name

        for user in users:
            if not user.chat_id == message.chat.id:
                try:
                    await bot.send_message(user.chat_id, f'{name_user}: {message.text}')
                except Exception:
                    pass


async def main():
    await Tortoise.init(
        db_url='sqlite://bot_database.db',
        modules={'models': ['__main__']}
    )
    await Tortoise.generate_schemas()

    await bot.infinity_polling()


if __name__ == '__main__':
    asyncio.run(main())
