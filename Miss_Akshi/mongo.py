import asyncio
import sys

from motor import motor_asyncio
from Miss_Akshi import MONGO_DB_URI 
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Miss_Akshi.Config import get_int_key, get_str_key
from Miss_Akshi import LOGGER as log

MONGO_PORT = get_int_key("27018")
MONGO_DB_URI = get_str_key("MONGO_DB_URI")
MONGO_DB = "Miss_Akshi"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["Miss_Akshi"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
