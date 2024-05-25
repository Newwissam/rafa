

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, NAME_AMR
from strings import get_command
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import add_gban_user, remove_gban_user
from YukkiMusic.utils.decorators.language import language

# Command
BLOCK_COMMAND = get_command("BLOCK_COMMAND")
UNBLOCK_COMMAND = get_command("UNBLOCK_COMMAND")
BLOCKED_COMMAND = get_command("BLOCKED_COMMAND")


@app.on_message(command(["حظر"]) & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("•** يا حلو رد على المستخدم او حط اليوزر مع الامر !**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in BANNED_USERS:
            return await message.reply_text(f"**يا حلو ترا ذا {user.mention} ممنوع من استخدام بوتك من زمان !**")
        await add_gban_user(user.id)
        BANNED_USERS.add(user.id)
        await message.reply_text(_["block_2"].format(user.mention))
        return
    if message.reply_to_message.from_user.id in BANNED_USERS:
        return await message.reply_text(f"**يا حلو ترا ذا {message.reply_to_message.from_user.mention} ممنوع من استخدام بوتك من زمان !**")
    await add_gban_user(message.reply_to_message.from_user.id)
    BANNED_USERS.add(message.reply_to_message.from_user.id)
    await message.reply_text(f"**• ابشر تم حظر {message.reply_to_message.from_user.mention} ومنعه من استخدام {NAME_AMR}\n\n• عشان تشوف الممنوعين من استخدام بوتك اكتب المحظورين**")


@app.on_message(command(["الغاء_الحظر"]) & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("•** يا حلو رد على المستخدم او حط اليوزر مع الامر !**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id not in BANNED_USERS:
            return await message.reply_text("• **ياعيني هو مو محظور من قبل !**")
        await remove_gban_user(user.id)
        BANNED_USERS.remove(user.id)
        await message.reply_text("•** ابشر تم السماح له بأستخدام بوتك ياعيني**")
        return
    user_id = message.reply_to_message.from_user.id
    if user_id not in BANNED_USERS:
        return await message.reply_text("• **ياعيني هو مو محظور من قبل !**")
    await remove_gban_user(user_id)
    BANNED_USERS.remove(user_id)
    await message.reply_text("•** ابشر تم السماح له بأستخدام بوتك ياعيني**")


@app.on_message(command(["المحظورين"]) & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not BANNED_USERS:
        return await message.reply_text("**• مافي محظورين ياحلو ..**")
    mystic = await message.reply_text("•** ابشر جاري احظار المستخدمين الممنوعين من استخدام بوتك ..**")
    msg = "•** الممنوعين من استخدام {NAME_AMR} :\n\n**"
    count = 0
    for users in BANNED_USERS:
        try:
            user = await app.get_users(users)
            user = (
                user.first_name if not user.mention else user.mention
            )
            count += 1
        except Exception:
            continue
        msg += f"{count}➤ {user}\n"
    if count == 0:
        return await mystic.edit_text("**• مافي محظورين يا حلو ..**")
    else:
        return await mystic.edit_text(msg)
