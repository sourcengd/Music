import os
import re
import requests
import config
import aiohttp
import aiofiles
from config import OWNER_ID
import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtube_search import YoutubeSearch

from ZeMusic import app
from ZeMusic.plugins.play.filters import command
from ZeMusic.utils.database import is_search_enabled1, enable_search1, disable_search1

def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)
        
lnk = config.CHANNEL_LINK
Nem = config.BOT_NAME + " يوت"

@app.on_message(command(["song", "/song", "بحث", Nem,"يوت"]) & filters.private)
async def song_downloader1(client, message: Message):
    if not await is_search_enabled1():
        return await message.reply_text("<b>⟡ عذراً عزيزي اليوتيوب معطل من قبل المطور</b>")
        
    query = " ".join(message.command[1:])
    m = await message.reply_text("<b>⇜ جـارِ البحث ..</b>")
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        await m.edit("- لم يتم العثـور على نتائج حاول مجددا")
        print(str(e))
        return
    
    await m.edit("<b>جاري التحميل ♪</b>")
    
    try:
        audio_file, tre= await YouTube.download(results[0]["id"], None)
        rep = f"⟡ {app.mention}"
        host = str(rep)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        
        await message.reply_audio(
            audio=audio_file,
            caption=rep,
            title=title,
            performer=host,
            thumb=thumb_name,
            duration=dur,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk),
                    ],
                ]
            ),
        )
        await m.delete()

    except Exception as e:
        await m.edit("error, wait for bot owner to fix")
        print(e)

    try:
        remove_if_exists(audio_file)
        remove_if_exists(thumb_name)
    except Exception as e:
        print(e)
        

@app.on_message(command(["تعطيل اليوتيوب بالخاص"]) & filters.user(OWNER_ID))
async def disable_search_command1(client, message: Message):
    if not await is_search_enabled1():
        await message.reply_text("<b>⟡ اليوتيوب معطل من قبل يالطيب</b>")
        return
    await disable_search1()
    await message.reply_text("<b>⟡ تم تعطيل اليوتيوب بنجاح</b>")

@app.on_message(command(["تفعيل اليوتيوب بالخاص"]) & filters.user(OWNER_ID))
async def enable_search_command1(client, message: Message):
    if await is_search_enabled1():
        await message.reply_text("<b>⟡ اليوتيوب مفعل من قبل يالطيب</b>")
        return
    await enable_search1()
    await message.reply_text("<b>⟡ تم تفعيل اليوتيوب بنجاح</b>")
