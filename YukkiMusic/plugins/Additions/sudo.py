from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
    )
from pyrogram.types import CallbackQuery, Message
from config import BANNED_USERS, OWNER_ID, NAME_AMR
from YukkiMusic.misc import SUDOERS
from YukkiMusic import app
from YukkiMusic import check_client


DEV = [[InlineKeyboardButton("اوامر المطور", callback_data="deve")]]

#~

#  if message.from_user.id not in SUDOERS:
    
    
    
@app.on_message(filters.regex("^اوامر المطور$"))
async def devs(client: Client, message: Message):
  if message.from_user.id not in SUDOERS:
    await message.reply_text(f"**• معليش عيني الامر هذا للمطور فقط !**")
  else:    
         user = message.from_user.mention
         await message.reply_text(f"**• اهلا عيني المطور {user} .. أضغط الزر لرؤية اوامرك",reply_markup=InlineKeyboardMarkup(DEV)) 
            
            
            
@app.on_callback_query(filters.regex("deve"))
async def unres(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True) 
   else:
     await q.edit_message_text("""**• اهلين فيك عزيزي المطور .. جميع اوامرك بالأزرار اسفل القائمة !**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("اوامر الحظر", callback_data="ban"),
                    InlineKeyboardButton("اوامر الفارات", callback_data="var")
                ],[
                    InlineKeyboardButton("الرفع والتنزيل", callback_data="add"),
                
                    InlineKeyboardButton("التعطيل والتفعيل", callback_data="pr"),
                ],[
                    InlineKeyboardButton("اوامر الاذاعة والاحصائيات", callback_data="bro"),
                
               ],
            ]
        ),
    )

    
@app.on_callback_query(filters.regex("ban"))
async def ban(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
     await q.edit_message_text("""**- آهلا .. اوامر الحظر تنقسم لثلاث اقسام :

• حظر عام ~ يحظر الشخص من جميع قروبات البوت
• حظر ~ يمنع الشخص من استخدام البوت يعني البوت ما راح يستجيب لاي شي يقوله .. ملاحظه - فقط منع استخدام وليس حظر من المجموعة
• حظر المجموعات ~ ما يقدر يدخل البوت للقروب المحظور من استخدامه واذا انضاف مرة ثانية يطلع لحاله

-› الاوامر الخاصة بالقائمة الي فوق 👆🏻 :

~ اوامر الحظر العام ~

 عام - بالرد على المستخدم او مع اليوزر

- لالغاء الحظر العام :

رالعام - بالرد على المستخدم او مع اليوزر

- لروئية المحظورين عام من بوتك : 

- المحظورين عام 

~ اوامر الحظر او منع الاستخدام ~

• حظر - بالرد على المستخدام او مع اليوزر

- لالغاء الحظر :

• رالحظر - بالرد على المستخدام او مع اليوزر

~ اوامر حظر المجموعات من استخدام البوت ~

- لمنع قروب من استخدام بوتك :

بلاك + ايدي المجموعة

- لسماح بالقروب انه يضيف بوتك مرة ثانية :

وايت + ايدي المجموعة

• ملاحظة .. اذا تبي تعرف ايدي المجموعة الي تبي تحظرها فقط اكتب ( ايدي المجموعة ) بالقروب الي تبي تطلع الايدي حقه**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("رجوع", callback_data="deve"),                                    
               ],
            ]
        ),
    )
            
 
@app.on_callback_query(filters.regex("var"))
async def varh(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:   
    await q.edit_message_text("""**- اهلا .. اوامر الفارات تنقسم لخمس اقسام : 

1 ~ فارات البوت الاساسية
2 ~ فارات الصور والوسائط
3 ~ فارات الحسابات المساعده
4 ~ فارات مدة التشغيل والتحميل
5 ~ فارات Spotify 

• اوامر وضع او حذف او رؤية الفارات :

-› لوضع الفارات ..
ضع_فار + الفار المطلوب + قيمة الفار

-› لحذف فار ..
حذف_فار + اسم الفار المطلوب

-› لرؤية فار معين ..
فار + اسم الفار المطلوب

• اضغط الازار اسفل القائمة لروئية فارات بوتك ..**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("الفارات الاساسية", callback_data="vol"),
                    InlineKeyboardButton("فارات الصور", callback_data="img"),
               ],[
                    InlineKeyboardButton("فارات الحساب المساعد", callback_data="ass"),
               ],[
                    InlineKeyboardButton("فارات اخرى", callback_data="lim"),
                    InlineKeyboardButton("فارات Spotify", callback_data="sopti"),
               ],[
                    InlineKeyboardButton("رجوع", callback_data="deve"),                                    
                    
               ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("vol"))
async def vol(_, query: CallbackQuery):
          await query.edit_message_text("""**• اهلا .. الفارات الاساسيه هي : 

1 - API_ID 
2 - API_HASH
3 - TOKEN
4 - MONGO
5 - LOG

{ فقط مطور السورس يستطيع تعديل هذي الفارات }**""",
       reply_markup=InlineKeyboardMarkup(
                    [
                       [
                            InlineKeyboardButton("رجوع", callback_data='var'),
                            InlineKeyboardButton("رجوع للبداية", callback_data='deve'),

                        ]
                    ]
                )
            )
    
  
@app.on_callback_query(filters.regex("img"))
async def add(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""**• اهلا فيك في فارات الصور .. 

- فار صورة التشغيل من اليوتيوب**
-› `YOUTUBE_IMG_URL`

**- فار صورة التشغيل من الساوند**
-› `SOUNCLOUD_IMG_URL`

**- فار صورة تشغيل صوتيات التلي **
-› `TELEGRAM_AUDIO_URL`

**- فار صورة تشغيل فيديوهات التلي **
-› `TELEGRAM_VIDEO_URL`

**- فار صورة الستارت في خاص البوت **
-› `START_IMG_URL`

**- فار صورة امر /ping** 
-› `PING_IMG_URL`

**- فار الصوره الي بالاوامر** 
-› `TAMR`

**- فار صورة البلاي ليست **
-› `PLAYLIST_IMG_URL`

**• لرؤية طريقة استعمال الفارات اضغط الزر الي تحت** """,
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("طريقة الاستعمال", callback_data="how"),
                    ],[
                    InlineKeyboardButton("رجوع", callback_data="var"),
                    InlineKeyboardButton("رجوع للبداية", callback_data="deve"),                                             

               ],
            ]
        ),
    )
  
  
@app.on_callback_query(filters.regex("how"))
async def how(_, query: CallbackQuery):
          await query.edit_message_text("""**• شرح استخدام الفارات ↓**[ㅤ ](https://telegra.ph/file/6b3eaaf09fc303a620bd6.mp4)""",
       reply_markup=InlineKeyboardMarkup(
                    [
                       [
                            InlineKeyboardButton("رجوع", callback_data='img'),
                            InlineKeyboardButton("رجوع للبداية", callback_data='var'),

                        ]
                    ]
                )
            )  
            
            
@app.on_callback_query(filters.regex("ass"))
async def add(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""**• اهلا .. تقدر تضيف خمس مساعدات لبوتك والفارات حقتهم كالتالي : 

- طبعا اول حساب مساعد يضيفه مطور السورس عشان يشتغل البوت والباقي براحتك يعني مو اساسيه فقط تساعدك لو كان على بوتك ضغط** 

`STRING_SESSION2=` { الجلسة } 
`STRING_SESSION3=` { الجلسة } 
`STRING_SESSION4=` { الجلسة } 
`STRING_SESSION5=` { الجلسة }

 **• لمعرفة طريقة استخراج الجلسات اضغط الزر اسفل القائمة**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    
                    InlineKeyboardButton("طريقة استخراج الجلسات", callback_data="str"),                    
                    ],[                    
                    InlineKeyboardButton("رجوع", callback_data="var"),
                    InlineKeyboardButton("رجوع للبداية", callback_data="deve"),                                    

               ],
            ]
        ),
    )
    
@app.on_callback_query(filters.regex("str"))
async def stg(_, query: CallbackQuery):
          await query.edit_message_text("""**• شرح استخراج الجلسة .. لازم تكون الجلسة Pytogram فقط ↓**[ㅤ ](https://telegra.ph/file/559d60d18dbf73fe18141.mp4)""",
       reply_markup=InlineKeyboardMarkup(
                    [
                       [
                            InlineKeyboardButton("رجوع", callback_data='ass'),
                            InlineKeyboardButton("رجوع للبداية", callback_data='var'),

                        ]
                    ]
                )
            )  
  
@app.on_callback_query(filters.regex("lim"))
async def add(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""**اهلا هنا بتكون جميع الفارات الاخرى ..**

1 - ( `ASSISTANT_LEAVE_TIME` ) 

**-› فار مغادرة الحساب المساعد بعد وقت معين انت تحدده **

**• مثال **: 
`ضع_فار ASSISTANT_LEAVE_TIME 5400`

**- كذا المساعد بيغادر القروبات بعد مرور 5400 ثانيه يعني بعد ثلاث ساعات تقريبا **

**• وبعد ما تحط الوقت لازم ترسل كذا عشان يتفعل الامر :**

- `ضع_فار AUTO_LEAVING_ASSISTANT True` 

**• ولو تبي تعطلته ترسل** 

- `ضع_فار AUTO_LEAVING_ASSISTANT False`

2 - ( `CLEANMODE_MINS` )
-› **فار مسح رسائل البوت بعد وقت معين انت تحدده**

**• مثال :**

- `ضع_فار CLEANMODE_MINS 5`

• **كذا بيمسح البوت رسائله بعد خمس دقايق**

- **للتعطيل :

`حذف_فار CLEANMODE_MINS`
  """,
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("رجوع", callback_data="var"),
                    InlineKeyboardButton("رجوع للبداية", callback_data="deve"),                                    

               ],
            ]
        ),
    )
    
    
@app.on_callback_query(filters.regex("sopti"))
async def add(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""**• اهلا ياعيني .. فارات Spotify مو مهمة الا لو كنت تبي تشغل من Spotify فا لازم تضيف هالفارات ..

( فقط اضغط للنسخ وارسلهم )**

1 - `ضع_فار SPOTIFY_CLIENT_ID e26f44e2cca34d1794c0fd998fddc4c3`

2 - `ضع_فار SPOTIFY_CLIENT_SECRET 5b060d5403fc4009a7d9e8c435677e93`""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("رجوع", callback_data="var"),
                    InlineKeyboardButton("رجوع للبداية", callback_data="deve"),                                    

               ],
            ]
        ),
    )
  

@app.on_callback_query(filters.regex("add"))
async def add(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""•** اهلا فيك في اوامر الرفع والتنزيل

- الاوامر هذي تنقسم لقسمين وهي :

1 - رفع المطورين 
2 - رفع مشرفين بالمجموعة 

• اوامر رفع المطورين :**

- رفع_مطور او /add

**• للتنزيل :**

- تنزيل_مطور او /del

**• لرؤية مطورين بوتك :**

-  المطورين او /sudo 

**• اوامر رفع المشرفين**

-› وظيفة المشرفين يكون عندهم صلاحيات المشرفين بأستخدام بوتك فقط مثلا لو مالك المجموعة حط التشغيل للمشرفين الي رافعهم بالمجموعة فقط تقدر انت تخلي الاعضاء يشغلون من خلال رفعهم ك مشرف في بوتك ..

**الاوامر :**

• رفع_مشرف او /admin

**للتنزيل :**

• تنزيل_مشرف او /unadmin

**لرؤية المشرفين :**

• المشرفون او /admins""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("رجوع", callback_data="deve"),                                    
               ],
            ]
        ),
    )
            

@app.on_callback_query(filters.regex("pr"))
async def pr(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""**• اهلا فيك في اوامر التفعيل والتعطيل :**

- /autoend + تفعيل او تعطيل
**-› يخلي المساعد يطلع لحاله لو كان لحاله لمدة 3 دقايق**

- /Log + تفعيل او تعطيل
-› **يطلع لك الناس الي ترسل ستارت بخاص بوتك وايضا رسايل التشغيل**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("رجوع", callback_data="deve"),                                    
               ],
            ]
        ),
    )
            
      
@app.on_callback_query(filters.regex("bro"))
async def bro(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""**• اهلا فيك في اوامر الاذاعة والاحصائيات .. اختار من الزر الاوامر الي تبيها**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("اوامر الاذاعة", callback_data="bod"),                         
                    InlineKeyboardButton("اوامر الاحصائيات", callback_data="sta"),                    
                 ],[                    
                    InlineKeyboardButton("رجوع", callback_data="deve"),                  
               ],
            ]
        ),
    )
            
      
@app.on_callback_query(filters.regex("sta"))
async def bro(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""** • آهلا امر الاحصائيات :
- الاحصائيات او /stats
بيطلع لك كل معلومات بوتك**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                   
                    InlineKeyboardButton("رجوع", callback_data="bro"),                  
               ],
            ]
        ),
    )
            
@app.on_callback_query(filters.regex("bod"))
async def brd(_, q: CallbackQuery):
   if q.from_user.id not in SUDOERS:
     await q.answer("الزر هذا للمطور بس !!", show_alert=True)
   else:
    await q.edit_message_text("""**• اهلين اوامر الاذاعه كالتالي :

عندك خمس متغير وهي ..**

`1 -pin
2 -pinloud
3 -user
4 -assistant
5 -nobot`

**-› كل واحد من هالمتغيرات له شي معين .. خيار -pin يعني اذاعه بالتثبيت وخيار -pinloud يعني اذاعه بالتثبيت ويرسل اشعار وخيار -user يذيع للناس الي راسله ستارت بخاص البوت وخيار -assistant يذيع بالحسابات المساعده وخيار -nobot
يذيع بخاص البوت فقط**

**مثلا تبي تسوي اذاعه بخاص البوت تكتب كذا ..*

`اذاعه -user -nobot هلا والله`

**كذا اذاعه بالخاص ولو تبي تذيع بكل الخيارات فقط اكتب اذاعه بالرد على المنشور او اكتب رسالتك بعد كلمة اذاعه**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    
                    InlineKeyboardButton("رجوع", callback_data="bro"),                  
               ],
            ]
        ),
    )
            
      
