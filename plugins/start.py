from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        f"** Welcome {message.from_user.mention}!**\n\n",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Bots Channel", url="t.me/mnbots"),
             InlineKeyboardButton("dev", url="github.com/mntgxo")]
        ])
    )
