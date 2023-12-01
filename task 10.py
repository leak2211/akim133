from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import os

BOT_TOKEN = os.getenv('Struk_token')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ Эхо-бот!\nНапиши мне что-нибудь')

@dp.message_handler(commands=['help'])
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo_echo(message: Message):
    await message.answer_photo(message.photo[0].file_id)

@dp.message_handler(content_types=types.ContentType.VOICE)
async def send_voice_echo(message: types.Message):
    await message.answer_voice(message.voice.file_id)

@dp.message_handler()
async def send_echo(message: Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
