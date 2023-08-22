#
# Copyright (C) 2021-2022 by Alexsacei @Github, < https://github.com/kenta9900 >.
# A Powerful Music Bot Property Of Rocks Indian NIRVANA

# Kanged By © @exsaezz
# Rocks © @groupjawanusantara
# Owner Alexsacei
# Alexsacei
# All rights reserved. © Alisha © Alexa © Alexsacei


import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AlexaMusic.core.bot import LOGGER, app, userbot
from AlexaMusic.core.bot.core.call import Alexsa
from AlexaMusic.core.bot.plugins import ALL_MODULES
from AlexaMusic.core.bot.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AlexaMusic").error("Add Pyrogram string session and then try...")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AlexaMusic.core.bot.plugins" + all_module)
    LOGGER("AlexaMusic.core.bot.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Alexsa.start()
    try:
        await Alexa.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except NoActiveGroupCall:
        LOGGER("AlexaMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    await Alexa.decorators()
    LOGGER("AlexaMusic").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AlexaMusic").info("Stopping Music Bot")
