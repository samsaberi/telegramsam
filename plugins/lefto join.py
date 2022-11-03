from pyrogram import Client,filters
import asyncio

text = """kjhghjkjhjk"""
@Client.on_message(filters.new_chat_members,group=1)
async def newmwmber(c,m):
    await m.delete()

    await c.send_message("text")



@Client.on_message(filters.left_chat_member,group=2)
async def leftmwmber(c,m):
    await m.delete()
    print("ok")



