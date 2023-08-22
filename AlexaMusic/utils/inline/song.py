#
# Copyright (C) 2021-2022 by Alexsacei@Github, < https://github.com/kenta9900 >.
# A Powerful Music Bot Property Of Rocks NIRVANA
# All rights reserved. © Alisha © Alexa © Yukki


from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💌 sᴜᴩᴩᴏʀᴛ 💌",
                url="https://t.me/groupjawanusantara",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
