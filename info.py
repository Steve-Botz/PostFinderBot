import os
from os import environ

API_ID       = int(environ.get("API_ID", "29841034"))
API_HASH     = environ.get("API_HASH", "fc533d811f28228e121bbe3901d8f565")
BOT_TOKEN    = environ.get("BOT_TOKEN", "")
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://postfinder088:pBekVdVL0ajzahqv@cluster0.cwb1ps7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_CHANNEL  = int(environ.get("LOG_CHANNEL", "-1002421781174"))
ADMIN        = int(environ.get("ADMIN", "6317211079"))
CHANNEL      = environ.get("CHANNEL", "@SteveBotz")
