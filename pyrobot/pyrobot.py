#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


from pyrogram import (
    Client,
    __version__
)
from pyrogram.errors import MessageNotModified
from pyrogram.raw.all import layer
from pyrobot import (
    APP_ID,
    API_HASH,
    LOGGER,
    # OWNER_ID,
    # SUDO_USERS,
    TG_COMPANION_BOT,
    AUTH_CHANNEL
)
class PyroBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=TG_COMPANION_BOT,
            workers=343
        )

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        LOGGER.info(
            f"PyroGramBot based on Pyrogram v{__version__} "
            f"(Layer {layer}) started on @{usr_bot_me.username}. "
            "Hi."
        )

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("PyroGramBot stopped. Bye.")
