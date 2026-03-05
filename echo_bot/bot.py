import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "6440503351:AAF7rA85x20KOvI5yaC_0MAOvUKZ6VwaEFo"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Salom! Men sizning echo botingizman. Menga istalgan xabarni yuboring, men uni sizga qaytarib beraman!")

@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())