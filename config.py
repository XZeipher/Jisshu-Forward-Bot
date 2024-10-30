# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "9176863")
    API_HASH = environ.get("API_HASH", "afff208ad0de11acfc946ca6dcd74aec")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7890642537:AAH16HSoWnHYgGXHAEIhOUyKwIFkDQ4SeSU") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6501024238').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://alphaxcoders:6D4IK0e4d4nOxapE@cluster0.lkpqx.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '7890642537'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002352659712") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
