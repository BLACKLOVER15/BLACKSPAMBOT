import os
import asyncio
import config
from telethon import events, Button
from telethon.tl.custom import button
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9

ALIVE_IMG = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_IMG = ALIVE_IMG
else:
    DEADLY_IMG = "https://te.legra.ph/file/11adba95c2c26ae877ccf.jpg"

OWNER_INFO = config.OWNER_NAME
if config.OWNER_NAME:
    OWNER_NAME = OWNER_INFO
else:
    OWNER_NAME = "BLACK LOVER ALONE"

OWNER_ID = config.OWNER_ID

Deadly_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/BlackMusicSupport"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/Exampur20")
        ],
        [
        Button.url("• Lele Bsdk Repo•", "https://t.me/saikosaiyan")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[『𝗕𝗟𝗔𝗖𝗞』| ͢ ̶ͥ ̶ ̶ͣ ͓ ̶ͫ 𝗟𝗢𝗩𝗘𝗥𓄂⃝🔱 𝗕 ❤️ 𝗟](tg://user?id={6950353753})"
        DEADLY_ON = f"""
ʜᴇʏ {mention},
ᴛʜɪs ɪs ᴋɪɴɢ x ʙʟᴀᴄᴋ ʟᴏᴠᴇʀ sᴘᴀᴍʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- {creator}!

ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- {myOwner}

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- {creator}

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, DEADLY_IMG, caption=DEADLY_ON, buttons=Deadly_Button)
