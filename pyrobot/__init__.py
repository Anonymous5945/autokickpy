#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# needed to appropriately, select ENV vars / Config vars
import os

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from pyrobot.sample_config import Config
else:
    from pyrobot.config import Development as Config


# TODO: is there a better way?
LOGGER = logging.getLogger(__name__)
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_COMPANION_BOT = Config.TG_COMPANION_BOT
IS_BOT = True
USE_AS_BOT = True
OWNER_ID = Config.OWNER_ID
SUDO_USERS = list(Config.SUDO_USERS)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS = list(set(SUDO_USERS))
AUTH_CHANNEL = list(Config.SUDO_USERS)
AUTH_CHANNEL.append(-1001426538640)
AUTH_CHANNEL = list(set(AUTH_CHANNEL))
