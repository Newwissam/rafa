
import asyncio
import time

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from config import BANNED_USERS, NAME_AMR
from strings import get_command
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils import get_readable_time
from YukkiMusic.utils.database import (add_banned_user,
                                       get_banned_count,
                                       get_banned_users,
                                       get_served_chats,
                                       is_banned_user,
                                       remove_banned_user)
from YukkiMusic.utils.decorators.language import language

# Command
GBAN_COMMAND = get_command("GBAN_COMMAND")
UNGBAN_COMMAND = get_command("UNGBAN_COMMAND")
GBANNED_COMMAND = get_command("GBANNED_COMMAND")


@app.on_message(command(["حظر_عام"]) & SUDOERS)
@language
async def gbanuser(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**•معليش ياقلبي ما اقدر احظرك**")
        user = message.text.split(None, 1)[1]
        user = await app.get_users(user)
        user_id = user.id
        mention = user.mention
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    if user_id == message.from_user.id:
        return await message.reply_text("**•معليش ياقلبي ما اقدر احظرك**")
    elif user_id == app.id:
        return await message.reply_text("**• انقلع بس تبيني احظر نفسي ؟؟**")
    elif user_id in SUDOERS:
        return await message.reply_text("**• منجدك تبيني احظر مطور ؟**")
    is_gbanned = await is_banned_user(user_id)
    if is_gbanned:
        return await message.reply_text("• الادمي ذا محظور من اول ياعيني ..**".format(mention))
    if user_id not in BANNED_USERS:
        BANNED_USERS.add(user_id)
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = len(served_chats)
    time_expected = get_readable_time(time_expected)
    mystic = await message.reply_text(f"**• ابشر جاري حظره من جميع مجموعات {NAME_AMR} انتظر ثواني ..**")
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await app.ban_chat_member(chat_id, user_id)
            number_of_chats += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await add_banned_user(user_id)
    await message.reply_text(f"**• تم حظره من جميع مجموعات {NAME_AMR} بنجاح !**")
    await mystic.delete()


@app.on_message(command(["الغاء_العام"]) & SUDOERS)
@language
async def gungabn(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("• معليش ما اقدر احظرك ياقلبي**")
        user = message.text.split(None, 1)[1]
        user = await app.get_users(user)
        user_id = user.id
        mention = user.mention
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    is_gbanned = await is_banned_user(user_id)
    if not is_gbanned:
        return await message.reply_text(_["gban_7"].format(mention))
    if user_id in BANNED_USERS:
        BANNED_USERS.remove(user_id)
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = len(served_chats)
    time_expected = get_readable_time(time_expected)
    mystic = await message.reply_text("•** ابشر جاري الغاء الحظر عنه انتظر ..**")
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await app.unban_chat_member(chat_id, user_id)
            number_of_chats += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await remove_banned_user(user_id)
    await message.reply_text(f"**• تم الغاء حظره من جميع مجموعات {NAME_AMR} بنجاح !**")
    await mystic.delete()


@app.on_message(command(["المحظورين عام"]) & SUDOERS)
@language
async def gbanned_list(client, message: Message, _):
    counts = await get_banned_count()
    if counts == 0:
        return await message.reply_text("•**معليش مافي مستخدمين محظورين عام من بوتك ياعيني**")
    mystic = await message.reply_text("**• ابشر جاري احظار المستخدمين المحظورين ..**")
    msg = f"**المحظورين عام من {NAME_AMR} :\n\n**"
    count = 0
    users = await get_banned_users()
    for user_id in users:
        count += 1
        try:
            user = await app.get_users(user_id)
            user = (
                user.first_name if not user.mention else user.mention
            )
            msg += f"{count} - {user}\n"
        except Exception:
            msg += f"{count} - [حساب محذوف] - {user_id}\n"
            continue
    if count == 0:
        return await mystic.edit_text("•** معليش مافي محظورين عام ..**")
    else:
        return await mystic.edit_text(msg)
