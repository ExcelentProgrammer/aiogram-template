# Import necessary modules
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Import configuration data
from data import config

# Create an instance of the Bot class with the bot token and specified parse mode
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Create an instance of the MemoryStorage class for storing data
storage = MemoryStorage()

# Create an instance of the Dispatcher class, passing the bot and storage objects
dp = Dispatcher(bot, storage=storage)

