import asyncio
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
API_KEY = "YOUR_OPENWEATHER_API_KEY"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Shahar nomini yuboring, men ob-havoni aytaman 🌤️")


@dp.message(F.text)
async def weather_handler(message: Message):
    city = message.text

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        await message.answer("Shahar topilmadi ❌")
        return

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    result = (
        f"🌍 Shahar: {city}\n"
        f"🌡 Harorat: {temp}°C\n"
        f"☁️ Ob-havo: {weather}\n"
        f"💧 Namlik: {humidity}%"
    )

    await message.answer(result)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())