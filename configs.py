# (c) @AbirHasan2005 & @HuzunluArtemis

import os

# If it works on a cloud platform like heroku, you can use enviroment variables.
# If you use environmental variables, you should not make any changes to this file.

class Config(object):
    # if you will use enviroment variable, dont touch anything from here.
    DEFAULT_BLOCKED_EXTENSIONS = "srt txt html aio pdf lnk url"
    # DEFAULT_BLOCKED_EXTENSIONS = "srt txt jpg jpeg png torrent html aio pdf"
    
    
    #
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
    API_ID = int(os.environ.get('API_ID', 1111111))
    API_HASH = os.environ.get('API_HASH', None)
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    DB_CHANNEL_ID = int(os.environ.get('DB_CHANNEL_ID',''))
    FORCE_SUB_CHANNEL = os.environ.get('FORCE_SUB_CHANNEL', None)
    MONGODB_URI = os.environ.get('MONGODB_URI','')
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", DEFAULT_BLOCKED_EXTENSIONS).split()))
    BOT_USERNAME = os.environ.get('BOT_USERNAME','SaverBot')
    MIN_FILE_SIZE = int(os.environ.get('MIN_FILE_SIZE', 0)) # for save everything:0 for save nothing:200000 5242880
    SEND_AS_COPY = os.environ.get('SEND_AS_COPY', True) # if you want to send files to users as a copy
    SAVE_AS_COPY = os.environ.get('SAVE_AS_COPY', True) # if you want to save files to db as a copy
    CONTACT_ADRESS = os.environ.get('CONTACT_ADRESS','@HuzunluArtemis')
    URL_PREFIX = os.environ.get('URL_PREFIX','HA')
    AUTO_DELETE = os.environ.get('AUTO_DELETE',True)
    AUTO_DELETE_TIME = int(os.environ.get('AUTO_DELETE_TIME',10))
    AUTO_KICK_TIME = int(os.environ.get('AUTO_KICK_TIME',10))
    ACCEPT_FROM_PRIVATE = os.environ.get('ACCEPT_FROM_PRIVATE', False)
    START_MESSAGE = os.environ.get('START_MESSAGE', "Bot is running.")


    # if you want to config from here, uncomment this lines and edit:

    # BOT_TOKEN = "315269696969:sdv31imamhatiplerhapatılsın-dfg"
    # API_ID = 313131
    # API_HASH = "sdfsdfvssv65s56v"
    # STRING_SESSION = "asdf+63sadf+6sadf26sadf262asdf"
    # DB_CHANNEL_ID = -100232626
    # FORCE_SUB_CHANNEL = "@HuzunluArtemis" # example: -10026526 example: @HuzunluArtemis
    # MONGODB_URI = "mongodb+srv://hgg-gh-h:ghg@fghfgh.fgh.mongodb.net/fhgfh?retryWrites=true&w=majority"
    # BLOCKED_EXTENSIONS = "srt txt html aio pdf lnk url"
    # BOT_USERNAME = "SaverBot"
    # MIN_FILE_SIZE = 0 # for save everything:0 for save nothing:200000 5242880
    # SEND_AS_COPY = True # if you want to send files to users as a copy
    # SAVE_AS_COPY = True # if you want to save files to db as a copy
    # CONTACT_ADRESS = "@HuzunluArtemis"
    # URL_PREFIX = "HA"
    # AUTO_DELETE = True
    # AUTO_DELETE_TIME = 10
    # AUTO_KICK_TIME = 10
    # ACCEPT_FROM_PRIVATE = False
    # START_MESSAGE = "Bot is running."
