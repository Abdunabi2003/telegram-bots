import asyncio
import wikipedia
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "Tokeningizni bu yerga yozing"

bot = Bot(token=TOKEN)
dp = Dispatcher()

wikipedia.set_lang("uz")


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Salom! So'z yuboring, men Wikipediadan ma'lumot topaman.")


@dp.message(F.text)
async def wiki_handler(message: Message):
    query = message.text

    try:
        result = wikipedia.summary(query, sentences=2)
        await message.answer(result)

    except wikipedia.exceptions.DisambiguationError:
        await message.answer("Aniqroq yozing iltimos.")

    except wikipedia.exceptions.PageError:
        await message.answer("Bunday maqola topilmadi.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())