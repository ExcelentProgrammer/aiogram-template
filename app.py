from aiogram import executor  # Importing the executor module from aiogram

from loader import dp  # Importing the dispatcher from loader
import middlewares, filters, handlers  # Importing middlewares, filters and handlers
from utils.notify_admins import on_startup_notify  # Importing the on_startup_notify function from notify_admins
from utils.set_bot_commands import set_default_commands  # Importing the set_default_commands function from set_bot_commands

# This is an asynchronous function that runs when the bot starts up
async def on_startup(dispatcher):
    # This sets the default commands for the bot
    await set_default_commands(dispatcher)

    # This sends a notification to the admins when the bot starts up
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    # This starts the polling loop for the bot
    executor.start_polling(dp, on_startup=on_startup)
