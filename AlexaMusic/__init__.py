#
# Copyright (C) 2021-2022 by Alexsacei@Github, < https://github.com/kenta9900 >.
# A Powerful Music Bot Property Of Rocks NIRVANA

# Kanged By © @exsaezz
# Rocks © @groupjawanusantara
# Owner Alexsacei
# Alexsacei
# All rights reserved. © Alexa © Yukki © Alexsacei


from AlexaMusic.core.bot import AlexsaBot
from AlexaMusic.core.dir import dirr
from AlexaMusic.core.bot.core.git import git
from AlexaMusic.core.bot.core.userbot import Userbot
from AlexaMusic.core.bot.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = AlexsaBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
