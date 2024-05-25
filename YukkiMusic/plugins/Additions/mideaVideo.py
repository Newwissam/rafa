import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery, InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InputMediaPhoto, InputMediaVideo
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS, NAME_BOT
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic import check_client
from YukkiMusic.utils.database import (add_served_chat,  add_served_user, blacklisted_chats, get_assistant, get_lang, get_userss, is_on_off, is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel, start_pannel)







    
    

@app.on_callback_query(filters.regex("tele"))
async def eslam(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/3f991cf109e90c025f35a.mp4",None,
           f"**✧ شرح تشغيل الصوتيات او الفويسات\n- ترد على الفويس او الصوت المطلوب بأحد هاذي الاوامر :\n• {NAME_BOT} شغلي\n• /play\n• وبرضو هالاوامر تشتغل على الفيديو ترد على الفيديو ويشتغل بالمكالمة**\n\n**وللتوضيح اكثر تابعو الفيديو الي فوق (: .**"
       ),
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    
                    InlineKeyboardButton("رجوع", callback_data="ko")

               ],
          ]
        ),
    )  


@app.on_callback_query(filters.regex("ko"))
async def back1(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/06f578ffcacbfea71ad30.mp4",None,
           "**اهلين فيك في قسم تشغيل المنصات**\n- **المنصات المدعومة هي ↓**\n\n**• Telegram\n• Youtube\n• SoundCloud\n• AppleMusic\n• Spotify\n\n- بتلقى شرح لكل هالمنصات بالزرار تحت ..**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "• Telegram", callback_data=f"tele"),
                     InlineKeyboardButton(
                        "• YouTube", callback_data=f"yout"),
                     InlineKeyboardButton(
                        "• Spotify", callback_data=f"spo"),
                ],[
                     InlineKeyboardButton(
                        "• AppleMusic", callback_data=f"apple"),
                     InlineKeyboardButton(
                        "• SoundCloud", callback_data=f"sound"),
                ],[
                     InlineKeyboardButton(
                        "", callback_data=f"fft"),
                ],[

                     InlineKeyboardButton(
                        "رجوع", callback_data=f"am"),
                
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("don"))
async def don(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/417746bcdb462a48ea974.mp4",None,
           "**اهلين فيك في قسم التحميل ♪\nللبحث عن اغنية او فيديو استخدم الامر التالي ↓\n\n[ بحث + اسم المطلوب ..]\n\nمثال -› بحث بحبك وحشتني**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                     
                     InlineKeyboardButton(
                        "رجوع", callback_data=f"am")
                        
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("save"))
async def dont(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/417746bcdb462a48ea974.mp4",None,
           "✧ **اهلين فيك في قسم حفظ التشغيل**\n\n- **حفظ التشغيل هو حفظ الاغاني الي اشتغلت بالمجموعة وحفظها يعني انك تقدر تشغلها بدون ما ترجع تبحث عنها مرة ثانية وتبقى محفوظة لك فقط**\n\n- عشان تحفظ الاغنية او المُشغل الحالي بالمكالمة لازم تضغط على زر -› ( **حفظ التشغيل** )\n\n- عشان تشوف الاغاني او الصوتيات الي حفظتها اكتب امر -› ( **قائمة تشغيلي** )\n\n- وطريقة تشغيل قائمتك تكتب فقط امر -› ( **تشغيل قائمتي** )\n\n- طريقة حذف اغنية او مقطع من محفوظاتك تكتب امر -› ( **حذف تشغيلي** ) وتكمل الخطوات بخاص البوت ..\n\n✶ **ملاحظة : اذا حفظت اغنية بتكون محفوظة عندك فقط يعني كل شخص عنده قائمة تشغيل خاصة فيه ومحد يقدر يحفظ اغنية عندك والعكس ايضا\n✶ لو ما فهمت تابع الفيديو الي فوق عشان تفهم اكثر ❤️**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                     InlineKeyboardButton(
                        "رجوع", callback_data=f"am"),

                     
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("yout"))
async def donnr(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/7300df6491dfcbe571680.mp4",None,
          f"**هلا فيك في قسم تشغيل روابط اليوتيوب\n\n• عندك طريقتين للتشغيل وهي :\n\n1 - وضع الرابط مع الامر \n2 - بالرد على الرابط بأمر التشغيل وهو [ {NAME_BOT} شغلي ]\n\n◌ مثال : {NAME_BOT} شغلي https://youtu.be/UuEPuVjsoG4\n- تابع الفيديو فوق للتوضيح اكثر ،**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      

                     InlineKeyboardButton(
                        "رجوع", callback_data=f"ko")
                ],[

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("apple"))
async def apple(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/76b82a7b8df689a169182.mp4",None,
          f"هلا فيك في قسم تشغيل اغاني Apple Music ♪\n\n• تقدر تشغيل الاغاني عن طريق الرد على الرابط او وضعه مع الامر .\n\n• مثال : [ `{NAME_BOT} شغلي https://music.apple.com/sa/album/ipad/1616715862?i=1616715870&l=ar` ]\n\n**تابع الفيديو للتوضيح اكثير .**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                     InlineKeyboardButton(
                        "رجوع", callback_data=f"ko")
                ],[

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("spo"))
async def spo(_, query: CallbackQuery):
    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)
    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/bc01ebc69dc2ff1f380d9.mp4",None,
          f"هلا فيك في قسم تشغيل اغاني Spotify ♪\n\n• تقدر تشغيل الاغاني عن طريق الرد على الرابط او وضعه مع الامر .\n\n• مثال : [ `{NAME_BOT} شغلي https://open.spotify.com/track/2GQB3Xe1J9D2sK90AtHfhI?si=aIuly9l-T-Gy5GvfZxpUiw&context=spotify%3Aplaylist%3A37i9dQZF1DXcJUwMZo8Ss1i=1616715870&l=ar` ]\n\n**تابع الفيديو للتوضيح اكثير .**"
       ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                     InlineKeyboardButton(
                        "رجوع", callback_data=f"ko")
                ],[

                ],
            ]
        ),
    )
