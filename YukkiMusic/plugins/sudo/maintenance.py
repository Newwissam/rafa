
from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from strings import get_command, get_string
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import (get_lang, is_maintenance,
                                       maintenance_off,
                                       maintenance_on)
from YukkiMusic.utils.decorators.language import language

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")


@app.on_message(command(["صيانة"]) & SUDOERS)
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
    usage = "**• استخدم الامر كذا ياعيني ..\nصيانة + تفعيل او تعطيل**"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "تفعيل":
        if await is_maintenance() is False:
            await message.reply_text(
                "**• وضع الصيانة مفعل بالفعل !**"
            )
        else:
            await maintenance_on()
            await message.reply_text("**• تم تفعيل وضع الصيانة بنجاح ..**")
    elif state == "تعطيل":
        if await is_maintenance() is False:
            await maintenance_off()
            await message.reply_text("•** تم تعطيل وضع الصيانة ..**")
        else:
            await message.reply_text(
                "**وضع الصيانة معطل بالفعل !**"
            )
    else:
        await message.reply_text(usage)
