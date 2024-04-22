import asyncio
import logging
import sys, configparser
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
config = configparser.ConfigParser()
config.read('config.ini')

# Bot token can be obtained via https://t.me/BotFather
TOKEN = config['general']['token']

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()



@dp.message(Command("tech"))
async def command_ping(message: Message):
    await message.answer(f"{html.bold('Пингуются настоящие  сигмы гигачады')} 😎\n {config['general']['tech']}")
@dp.message(Command("bio"))
async def command_ping(message: Message):
    await message.answer(f"{ html.bold('Пингуются хим-био ( что-то смешное не придумал пока )')}\n {config['general']['bio']}")
@dp.message(Command("all"))
async def command_ping(message: Message):
    await message.answer(f"{ html.bold('Пингуются все расы')}\n {config['general']['everybody']}")



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
