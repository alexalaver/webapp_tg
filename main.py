from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import config as cfg

bot = Bot(cfg.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Открыть веб-страницу", web_app=WebAppInfo(url="https://alexalaver.github.io/webapp_tg//index.html")))
    await message.answer("Привет мой друг", reply_markup=markup)

if __name__ == "__main__":
    executor.start_polling(dp)
