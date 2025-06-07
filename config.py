# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "22562874")
API_HASH = os.getenv("API_HASH", "0cbb05c57e36de023a40e45124513f03")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7859887286:AAHGpFa6FzExiKX0Y2S0JeYgeRylSZrAiKA")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://MJxExDB:d6MewqLLIStyy6vH@excluster.hvtovn8.mongodb.net/?retryWrites=true&w=majority&appName=ExCluster")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5693901067").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "MJxExDB")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002637260882")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002658189491")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
