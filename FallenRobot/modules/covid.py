import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FallenRobot import pbot


API = "https://api.safone.tech/countryinfo?country=India"


@pbot.on_message(filters.private & filters.text)
async def reply_info(client, message: Message):
    await message.reply_text(
        text=covid_info(message.text),
        disable_web_page_preview=True,
        quote=True,
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**ᴄᴏᴠɪᴅ 𝟷𝟿 ɪɴғᴏʀᴍᴀᴛɪᴏɴ**--

ᴄᴏᴜɴᴛʀʏ : `{country}`
ᴀᴄᴛɪᴠᴇᴅ : `{active}`
ᴄᴏɴғɪʀᴍᴇᴅ : `{confirmed}`
ᴅᴇᴀᴛʜs : `{deaths}`
ɪᴅ : `{info_id}`
ʟᴀsᴛ ᴜᴘᴅᴀᴛᴇ : `{last_update}`
ʟᴀᴛɪᴛᴜᴅᴇ : `{latitude}`
ʟᴏɴɢɪᴛᴜᴅᴇ : `{longitude}`
ʀᴇᴄᴏᴠᴇʀᴇᴅ : `{recovered}`

ᴍᴀᴅᴇ ʙʏ @FallenXRobot"""
        return covid_info
    except Exception as error:
        return error

__help__ = """
ᴅɪʀᴇᴄᴛ sᴇɴᴅ ᴍᴇ ᴀɴʏ sᴛᴀᴛᴇ ɪɴ ɪɴᴅɪᴀ 🇮🇳 ɪᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴄᴏᴠɪᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏғ ᴛʜᴀᴛ sᴛᴀᴛᴇs ᴅᴏɴ'ᴛ ᴜsᴇ ᴀɴʏ ᴛʏᴘᴇ ᴏғғ ᴄᴏᴍᴍᴀɴᴅs ᴅɪʀᴇᴄᴛ sᴇɴᴅ ᴍᴇ sᴛᴀᴛᴇ ɴᴀᴍᴇ.. 
"""
__mod_name__ = "ᴄɪᴠɪᴅ 😷"
