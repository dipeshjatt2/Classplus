import os

API_ID = API_ID = 29640188

API_HASH = os.environ.get("API_HASH", "43c66e3314921552d9330a4b05b18800")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6530435719:AAHAWHqESgxbjZWVfaN8eM6eqXAMA_sWVxo")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER"))

LOG = -1002154901949

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7504263874").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


