import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
OWNER_NAME = getenv("OWNER_NAME", "AddyxD")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AddyUpdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/eb87def61ea2baa7423d9.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(os.environ.get("OWNER_ID"))
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MusicAssistantOfCarnival")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AddySupport")
PROJECT_NAME = getenv("PROJECT_NAME", "Carvinal Music")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/AddyxD/MusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
