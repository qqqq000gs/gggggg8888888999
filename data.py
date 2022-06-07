from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("⚙ Start Generating Session ⚙", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("👨‍💻 Owner 👨‍💻", url="https://t.me/SPA4KY")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("ℹ About ℹ", callback_data="about")
        ],
    ]

    START = """
Hey {}

Welcome to {}

Use This Bot only If You trust this bot, Else Delete this chat and don't use.

I am Session String Generator bot for Pyrogram & Telethon.
Click on Below buttons to know more.
    """

    HELP = """
🔥 *Available Commands** 🔥

`/about` - About this Bot.
`/help` - Shows this message.
`/start` - Starts the Bot.
`/generate` - Generate Session.
`/cancel` - Cancel the process.
`/restart` - Restarts the process.
"""

    ABOUT = """
🔥 **About This Bot** 🔥

**Telegram Bot to generate Pyrogram and Telethon string session.**

**Framework** : [Pyrogram](https://docs.pyrogram.org)

**Language** : [Python](https://www.python.org)
    """
