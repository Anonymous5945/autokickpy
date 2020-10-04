import os


class Config:
    LOGGER = True
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", None)
    # Get these values from my.telegram.org
    TG_COMPANION_BOT = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    # SuDo User
    OWNER_ID = int(os.environ.get("OWNER_ID", "395357593"))
    # Array to store users who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "").split())
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    lD_LIMIT = int(os.environ.get("lD_LIMIT", 12345))

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
