from pymongo import MongoClient
from pymongo.collection import Collection

from app.utils.settings import SETTINGS

client = MongoClient(SETTINGS().MONGO_URI)
database = client.fast_food_simulator

food_collection: Collection = database.get_collection('foods')
client_collection: Collection = database.get_collection('clients')
order_collection: Collection = database.get_collection('orders')
