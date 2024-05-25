import requests
import os
from strings.filters import command
from gpytranslate import Translator
from aiohttp import ClientSession
from pyrogram import filters, Client
import re
import config
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from telegraph import upload_file
from traceback import format_exc
from YukkiMusic import app
from typing import Union
from config import USER_CH, NAME_BOT
from YukkiMusic.misc import SUDOERS



@app.on_message(command(["/tgm", "tgm"]) & SUDOERS)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("**رد على صورة او فيد !**")
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (replied.video and replied.video.file_name.endswith(".mp4") and replied.video.file_size <= 5242880)
        or (replied.document and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")) and replied.document.file_size <= 5242880)):
        return await message.reply("**غير للاسف غير مدعوم !!**")
    download_location = await client.download_media(message=message.reply_to_message,file_name="root/downloads/")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        button_s = InlineKeyboardMarkup([[InlineKeyboardButton(f"تحديثات {NAME_BOT} ♪", url=f"T.me/{USER_CH}")]])
        await message.reply(f"**رابط الصورة »**\n`https://telegra.ph{response[0]}`",disable_web_page_preview=True,reply_markup=button_s)
    finally:
        os.remove(download_location)
