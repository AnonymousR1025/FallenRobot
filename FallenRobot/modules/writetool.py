# Remodified The Uploading msg is now deleted automatically 
# I commited this bcz that msg sucks me 😤
# Credits www.github.com/Legend-Mukund
# <https://github.com/AnonymousR1025/FallenRobot>

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from FallenRobot import pbot as bot, BOT_USERNAME, SUPPORT_CHAT

SHREYXD = [
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
]

@bot.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ɪᴛ ᴏɴ ᴍʏ ᴄᴏᴩʏ...")
    m = await message.reply_text("» ᴡᴀɪᴛ ᴀ sᴇᴄ, ʟᴇᴛ ᴍᴇ ᴡʀɪᴛᴇ ᴛʜᴀᴛ ᴛᴇxᴛ...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("» ᴜᴩʟᴏᴀᴅɪɴɢ...")
    await m.delete()
    await bot.send_chat_action(message.chat.id, "upload_photo")
    await message.reply_photo(
        hand, 
        caption="ᴡʀɪᴛᴛᴇɴ ᴡɪᴛʜ 🖊 ʙʏ [ғᴀʟʟᴇɴ](t.me/FallenXRobot)",
        reply_markup=InlineKeyboardMarkup(SHREYXD)
    )

__mod_name__ = "Hᴀɴᴅᴡʀɪᴛᴇ"

__help__ = """

 Writes the given text on white page with a pen 🖊

❍ /write <text> *:* Writes the given text.
 """
