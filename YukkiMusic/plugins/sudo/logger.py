

from pyrogram import filters
from strings.filters import command
import config
from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import add_off, add_on
from YukkiMusic.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(command(["/Log"]) & SUDOERS)
@language
async def logger(client, message, _):
    usage = "•** استخدم الامر كذا ياعيني ..\n- /Log + تفعيل او تعطيل"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "تفعيل":
        await add_on(config.LOG)
        await message.reply_text("• **تم تفعيل السجل بنجاح ..**")
    elif state == "تعطيل":
        await add_off(config.LOG)
        await message.reply_text("•** تم تعطيل السجل ..**")
    else:
        await message.reply_text(usage)
