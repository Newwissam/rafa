#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MONGO_DB_URI, OWNER_ID, NAME_AMR
from strings import get_command
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import add_sudo, remove_sudo
from YukkiMusic.utils.decorators.language import language

# Commandd
ADDSUDO_COMMAND = get_command("ADDSUDO_COMMAND")
DELSUDO_COMMAND = get_command("DELSUDO_COMMAND")
SUDOUSERS_COMMAND = get_command("SUDOUSERS_COMMAND")


@app.on_message(command(["رفع_مطور", "/add"]) & filters.user(OWNER_ID)
)
@language
async def useradd(client, message: Message, _):
    if MONGO_DB_URI is None:
        return await message.reply_text(
            "**• قول لمطور السورس يضيف رابط التخزين !**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("•** ياحلو رد على المستخدم او حط يوزره مع الامر !**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in SUDOERS:
            return await message.reply_text(f"**• معليش بس ذا {user.mention} مطور من قبل !**")
        added = await add_sudo(user.id)
        if added:
            SUDOERS.add(user.id)
            await message.reply_text(f"**• ابشر تم اضافة {user.mention} مطور في بوت {NAME_AMR}")
        else:
            await message.reply_text("•** حصل خطا عيد المحاولة !**")
        return
    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(f"**• معليش بس ذا {message.reply_to_message.from_user.mention} مطور من قبل !**"
        )
    added = await add_sudo(message.reply_to_message.from_user.id)
    if added:
        SUDOERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(f"**• ابشر تم اضافة {message.reply_to_message.from_user.mention} مطور في بوت {NAME_AMR}"
        )
    else:
        await message.reply_text("Failed")
    return


@app.on_message(command(["تنزيل_مطور", "/del"]) & filters.user(OWNER_ID)
)
@language
async def userdel(client, message: Message, _):
    if MONGO_DB_URI is None:
        return await message.reply_text(
                        "**• قول لمطور السورس يضيف رابط التخزين !**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("•** ياحلو رد على المستخدم او حط يوزره مع الامر !**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id not in SUDOERS:
            return await message.reply_text(f"**• معليش هو مو مطور من اول !**")
        removed = await remove_sudo(user.id)
        if removed:
            SUDOERS.remove(user.id)
            await message.reply_text(f"**• ابشر تم تنزيله من مطورين {NAME_AMR}**")
            return
        await message.reply_text(f"**حدث خطأ ما !**")
        return
    user_id = message.reply_to_message.from_user.id
    if user_id not in SUDOERS:
        return await message.reply_text(f"**• معليش هو مو مطور من اول !**")
    removed = await remove_sudo(user_id)
    if removed:
        SUDOERS.remove(user_id)
        await message.reply_text(f"**• ابشر تم تنزيله من مطورين {NAME_AMR}**")
        return
    await message.reply_text(f"**• حدث خطا عيد المحاولة**")


@app.on_message(command(["المطورين", "/sudo"]) & ~BANNED_USERS)
@language
async def sudoers_list(client, message: Message, _):
    text = f"**• المطور الاساسي لـ {NAME_AMR}**\n\n"
    count = 0
    for x in OWNER_ID:
        try:
            user = await app.get_users(x)
            user = (
                user.first_name if not user.mention else user.mention
            )
            count += 1
        except Exception:
            continue
        text += f"{count}➤ {user}\n"
    smex = 0
    for user_id in SUDOERS:
        if user_id not in OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = (
                    user.first_name
                    if not user.mention
                    else user.mention
                )
                if smex == 0:
                    smex += 1
                    text += "المطورين :"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("**• معليش ياعيني مافي مطورين في بوت ..**")
    else:
        await message.reply_text(text)
