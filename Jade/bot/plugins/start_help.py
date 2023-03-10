# (c) adarsh-goel 
from Jade.bot import StreamBot
from Jade.vars import Var
import logging
logger = logging.getLogger(__name__)
from Jade.bot.plugins.stream import MY_PASS
from Jade.utils.human_readable import humanbytes
from Jade.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Jade.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["startβ‘οΈ","helpπ","loginπ","DC"],
                ["pingπ‘","statusπ"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["startβ‘οΈ","helpπ","DC"],
                [pingπ‘","statusπ",]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('startβ‘οΈ')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nα΄α΄‘ Usα΄Κ Jα΄ΙͺΙ΄α΄α΄:** \n\n__MΚ Nα΄α΄‘ FΚΙͺα΄Ι΄α΄__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sα΄α΄Κα΄α΄α΄ Yα΄α΄Κ Bα΄α΄ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__π’ππ‘π‘π¨, π¨ππ€ ππ‘π ππ‘π ππππππ ππ‘ππ π€π’πππ ππ. πα΄Ι΄α΄α΄α΄α΄ α΄Κα΄ πα΄α΄ α΄Κα΄α΄α΄Κ__\n\n  **ππ π¬ππ‘π‘ πππ‘π₯ π?π€πͺ**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/9d94fc0af81234943e1a9.jpg",
                caption="<i>πΉπΎπΈπ½ CHANNEL ππΎ πππ΄ πΌπ΄π</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jα΄ΙͺΙ΄ Ι΄α΄α΄‘ π", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>π’πΈπΆπ?π½π±π²π·π° ππ?π·π½ ππ»πΈπ·π°</i> 
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
        caption =f'Hi {m.from_user.mention(style="md")}!,\nI am Telegram File to Link Generator Bot with Channel support.\nSend me any file and get a direct download link and streamable link.!',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('helpπ')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nα΄α΄‘ Usα΄Κ Jα΄ΙͺΙ΄α΄α΄ **\n\n__MΚ Nα΄α΄‘ FΚΙͺα΄Ι΄α΄__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sα΄ΚΚΚ SΙͺΚ, Yα΄α΄ α΄Κα΄ Bα΄Ι΄Ι΄α΄α΄ FROM USING α΄α΄. Cα΄Ι΄α΄α΄α΄α΄ α΄Κα΄ Dα΄α΄ α΄Κα΄α΄α΄Κ</i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
                Caption="**πΉπΎπΈπ½ πππΏπΏπΎππ πΆππΎππΏ ππΎ πππ΄ α΄ΚΙͺs Bα΄α΄!**\n\n__Dα΄α΄ α΄α΄ Oα΄ α΄ΚΚα΄α΄α΄, OΙ΄ΚΚ CΚα΄Ι΄Ι΄α΄Κ Sα΄Κsα΄ΚΙͺΚα΄Κs α΄α΄Ι΄ α΄sα΄ α΄Κα΄ Bα΄α΄!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("π€ Jα΄ΙͺΙ΄ Uα΄α΄α΄α΄α΄s CΚα΄Ι΄Ι΄α΄Κ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sα΄α΄α΄α΄ΚΙͺΙ΄Ι’ α΄‘α΄Ι΄α΄ WΚα΄Ι΄Ι’. Cα΄Ι΄α΄α΄α΄α΄ α΄α΄__ [ADARSH GOEL](https://telegram.me/dev_shadow).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> Send me any file or video i will give you streamable link and download link.</b>\n
<b> I also support Channels, add me to you Channel and send any media files and see miracleβ¨ also send /list to know all commands""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("πββοΈ DEV", url="https://telegram.me/dev_shadow")],
                [InlineKeyboardButton("π₯ Source Code", txt="Contact Dev @dev_shadow")]
            ]
        )
    )
