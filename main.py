# from aiogram import Bot, Dispatcher, filters, types, F
# import asyncio
#
# bot = Bot(token="7247226092:AAEqcpkbJN6QeHutbn30FHZx7nxMgBMuZRc")
# dp = Dispatcher(bot=bot)
#
#
# @dp.message(filters.Command("start"))
# async def start_function(message: types.Message):
#     await message.answer("Добро пожаловать")
#
#
# @dp.message(F.text)
# async def echo_function(message: types.Message):
#     await message.answer(message.text)
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

# uy ishi
from aiogram import Bot, Dispatcher, types, filters
import asyncio

bot = Bot(token="7328288791:AAH0xCHBP9IJz009CUn9lPMiVWaeU-H3GKA")
dp = Dispatcher(bot=bot)


@dp.message(filters.Command("start"))
async def start_our_bot(message: types.Message):
    await message.answer("Добро пожаловать")


our_help = "Запустить бот: /start \nПомощь: /help \nИнформация: /info"


@dp.message(filters.Command("help"))
async def answer_for_help(message: types.Message):
    await message.answer(our_help)


info_our_bot = "Создатель: Анвар Абдурашидов, это бот который я сделал для д/з по программированию"


@dp.message(filters.Command("info"))
async def info_bot(message: types.Message):
    await message.answer(info_our_bot)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
