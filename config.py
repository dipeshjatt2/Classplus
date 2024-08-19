import os

API_ID = API_ID = 26451206

API_HASH = os.environ.get("API_HASH", "32984406271d6f3945bb536671b143a7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7422420660:AAFrbLnbw8WMKbi-IwLi3q_6lxWwqD0SnZY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6830450483))

LOG = -1001833358236

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1311808931").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


