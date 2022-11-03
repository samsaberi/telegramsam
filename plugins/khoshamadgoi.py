from pyrogram import Client,filters
import asyncio





@Client.on_message(filters.new_chat_members,group=5)

async def my_handler(client, message):
    await message.reply("من سام صابری هستم به گله ی تورگ های خسته خوش اومدی")



