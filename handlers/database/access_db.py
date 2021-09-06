# (c) @AbirHasan2005 & @HuzunluArtemis

from configs import Config
from handlers.database.database import Database

db = Database(Config.MONGODB_URI, "AutoGroup-PrivateChatFilesStoreBot-0")
