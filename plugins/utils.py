from motor import motor_asyncio
import configparser


config = configparser.ConfigParser()
config.read("config.ini")

db_url = config.get("mongo", "url")
owner = config.get("owner", "id")

connect = motor_asyncio.AsyncIOMotorClient(db_url)
create = connect.database

users = create.users
messages = create.messages
bans = create.bans


async def _message_id(message_id):
	message_id = await messages.find_one({"forward_id": f"{message_id}"})
	return message_id
