import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://te.legra.ph/file/11adba95c2c26ae877ccf.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ 𝗕𝗟𝗔𝗖𝗞 𝗟𝗢𝗩𝗘𝗥 𝗔𝗟𝗢𝗡𝗘 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ʙʟᴀᴄᴋ x ᴛᴀ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/BlackMusicSupport"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Exampur20")], [Button.url("• ʀᴇᴘᴏ •", "https://te.legra.ph/file/11adba95c2c26ae877ccf.jpg")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ʙʟᴀᴄᴋ x ᴛᴇᴀᴍ ʙʟᴀᴄᴋʟᴏᴠᴇʀ-ꜱᴘᴀᴍʙᴏᴛ!**") 
