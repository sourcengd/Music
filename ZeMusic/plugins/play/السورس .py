
import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint


@app.on_message(
    command(["سورس","سورس نجد","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://f.top4top.io/p_3244t98ar0.jpeg",
        caption=f"• 𝘁𝗵𝗲 𝗯𝗲𝘀𝘁 𝗼𝗻 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝘀𝗼𝘂𝗿𝗰𝗲 𝗻𝗴𝗱 🎶",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝗖𝗛𝗔𝗡𝗘𝗟 .", url=f"https://t.me/PR2222"), 
                 InlineKeyboardButton(
                   "sᴏᴜʀᴄᴇ ɴɢᴅ ♪",       url=f"https://t.me/ngd_i"), 
                 
             ],[ 
            InlineKeyboardButton(
                        " ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/RlrlrlrI"), 
                      
             ],[ 
                  InlineKeyboardButton(
                text=" أضفني الى مجموعتك",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )
