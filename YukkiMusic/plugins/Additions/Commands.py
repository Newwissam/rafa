import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InputMediaPhoto, InputMediaVideo
from config import NAME_BOT, DEV, DEV_USER, USER_CH, TAMR, NAME_AMR
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat, add_served_user, blacklisted_chats, get_assistant, get_lang, get_userss, is_on_off, is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel, start_pannel)
from YukkiMusic import check_client

AMR = f"{NAME_AMR}"


@app.on_message(command([f"{AMR} الاوامر"]) & filters.group & ~filters.edited & ~BANNED_USERS)
async def khalid(client: Client, message: Message):
    await message.reply_text(f"""• اهلين فيك في اوامر بوت {NAME_BOT}\n\n -› **جميع اوامر البوت موجودة بالقائمة هذي ، اضغط الازرار الي تحت  لرؤيتها**\n\n• مطور البوت -› @{DEV_USER}[ ⁪⁬⁮⁮⁮⁮ ‌ㅤ ⁪⁬⁮⁮⁮⁮]({TAMR})""",
                      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بمنصات الاغاني", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),

                    InlineKeyboardButton(
                        "اوامر خدمية", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        f"تحديثات {NAME_BOT} 🥢", url=f"https://t.me/{USER_CH}"),

                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("tt"))
async def tt(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_text(
       f"""✧ **اوامر التشغيل بالقنوات**\n\n• **ق تشغيل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني بالقناة\n\n• **ق ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ق تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ق اص**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ق كمل**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ق ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ق استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    
                    InlineKeyboardButton(
                        "رجوع", callback_data="am"),
                    InlineKeyboardButton(
                        "اغلاق", callback_data="close"),

               ],
          ]
        ),
    )


    
 
@app.on_message(filters.regex(f"^{AMR}$"))
async def namebot(client: Client, message: Message):
    user = message.from_user.mention
    await message.reply_text(f"""**آهلا {user} !\n- اضغط الزر عشان تشوف الاوامر**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر", callback_data=f"am"),
                ],
            ]
        ),
    )
    
@app.on_message(filters.command("{AMR} نادي المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(-1001890281798, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""- **ابشر ياعيوني ارسلت للمطور بيخش القروب ويشوف مشكلتك بأقرب وقت\n\n- تابع قناة البوت عشات تشوف التحديثات** -› [• تحديثات {NAME_BOT}•](t.me/{USER_CH})""", disable_web_page_preview=True     
    )
        
        
@app.on_message(filters.regex("^رابط الحذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين ياحلو\n-› هذي روابط حذف جميع مواقع التواصل بالتوفيق**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),

                ],
            ]
        ),
    )
    
@app.on_callback_query(filters.regex("am"))
async def am(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaPhoto(
           f"{TAMR}",
           f"**✧ اهلين فيك في اوامر بوت {NAME_BOT}**\n\n- عندك خمس ازرار وبعدها بتعرف تستخدم البوت ان شاء الله\n\n• مطور البوت -› @{DEV_USER}  \n• قناة البوت -› @{USER_CH}"
       ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بمنصات الاغاني", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),

                    InlineKeyboardButton(
                        "اوامر خدمية", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        f"تحديثات {NAME_BOT} 🥢", url=f"https://t.me/{USER_CH}"),
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("amm"))
async def amm(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaPhoto(
           f"{TAMR}",
           f"✧ اهلين فيك في اوامر بوت {USER_CH} (:\n\n- **كل اوامر البوت عندك بالازرار تحت استكشفهم بنفسك**\n\n• Developer -› [{DEV}](https://t.me/{USER_DEV})\n•"
       ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بمنصات الاغاني", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),

                    InlineKeyboardButton(
                        "اوامر خدمية", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        f"تحديثات {NAME_BOT} 🥢", url=f"https://t.me/{USER_CH}"),
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("sound"))
async def sound(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph//file/260b627a6c2489b834602.jpg",
           f"✶ **هلا فيك في قسم تشغيل اغاني الساوند ♪**\n\n• **تقدر تشغيل الاغاني عن طريق الرد على الرابط او وضعه مع الامر** .\n\n• مثال : [ `{NAME_BOT} شغل https://soundcloud.app.goo.gl/asiXLu19szSrVLFo9` ]"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
   
                     InlineKeyboardButton(
                        "رجوع", callback_data=f"ko")
                
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("cha"))
async def cha(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph//file/a84c9d93df4e2b19ade89.jpg",
           f"- هلا والله\n**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب **ربط + يوزر القناة**\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..\n\n✶ **للاستفسار** - @{DEV_USER}"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامر التشغيل بالقنوات", callback_data=f"tt"),

                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("kdm"))
async def kdm(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph//file/00cbc655d875535a5b01b.jpg",
           f"✧ **اهلين فيك في قسم الاوامر الخدمية**\n-** عندك اوامر كثيرة للتسلية ومنها ↓**\n\n-› **غنيلي\n-› افتارات بنات\n-› افتارات عيال\n-› افتارات مكس\n -› هيدرات او هيدر\n-› اقتباس او اقتباسات\n-› كت**"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "رجوع", callback_data=f"am"),
                ],[
                 
                     InlineKeyboardButton(
                        f"تحديثات {NAME_BOT}", url=f"T.me/{USER_CH}")

                ],
            ]
        ),
    )

@app.on_message(command(["التشغيل بالقنوات"]) & filters.group & ~filters.edited)
async def channel(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a84c9d93df4e2b19ade89.jpg",
        caption=f"""• **اضغط الزر الي تحت عشان تشوف شرح التشغيل بالقنوات** •""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بالقنوات", callback_data=f"cha"),
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("ddd"))
async def ddd(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك !!", show_alert=True)
    await query.edit_message_text(
       f"""✧ **اوامر التشغيل بالمجموعة**\n\n• ** {NAME_BOT} شغل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• ** {NAME_BOT} طفيها** او ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• ** {NAME_BOT} الي بعده** او **تخطي**\n-› لتشغيل التالي بالانتظار\n\n • ** {NAME_BOT} اص** او **اسكت**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• ** {NAME_BOT} تكلم**\n-› لالغاء الكتم واكمال التشغيل\n\n• ** {NAME_BOT} ايقاف مؤقت** او **ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• ** {NAME_BOT} كمل** او **استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="am"),
               ],
          ]
        ),
    )


