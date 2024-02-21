# Importing necessary modules and classes
from aiogram import Dispatcher

from loader import dp # Importing dp from loader.py
from .throttling import ThrottlingMiddleware # Importing ThrottlingMiddleware from throttling.py


# Checking if the current module is being run directly or being imported as a module
if __name__ == "middlewares":
    
    # Adding ThrottlingMiddleware as a middleware to the Dispatcher object
    dp.middleware.setup(ThrottlingMiddleware())
