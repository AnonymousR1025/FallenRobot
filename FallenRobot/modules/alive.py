import random
import asyncio
from pyrogram import filters, __version__ as pver
from sys import version_info
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tver
from telegram import __version__ as lver
from FallenRobot import BOT_USERNAME, OWNER_USERNAME, SUPPORT_CHAT, pbot

PHOTO = [
    "https://telegra.ph/file/8d5ae37f8b4b2b1b64763.jpg",
    "https://telegra.ph/file/2d4d106a4b4ecacb99374.jpg",
    "https://telegra.ph/file/e635ced7273b64341adea.jpg",
    "https://telegra.ph/file/e42dfbac4be6ddbf1d99f.jpg",
    "https://telegra.ph/file/db0a91985e4e963b6ef31.jpg",
]

SHREYXD = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/FallenXRobot?start=help"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
]

@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀʟɪᴠɪɴɢ...")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker("CAACAgUAAxkBAAJFnmK5MrdRLh3BC-061TmzqiIqGV9PAAIaBgACWrfJVa_zM8o84s3VKQQ")
    await umm.delete()
    await asyncio.sleep(0.1)
    await m.reply_photo(
        random.choice(PHOTO),
        caption=f"""**ʜᴇʏ​ ɪ ᴀᴍ ꜰᴀʟʟᴇɴ ✘ ʀᴏʙᴏᴛ​**
        ━━━━━━━━━━━━━━━━━━━
        » **ᴍʏ ᴏᴡɴᴇʀ :** [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](https://t.me/{OWNER_USERNAME})
        » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
        » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
        » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
        » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
        ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(SHREYXD)
    )
