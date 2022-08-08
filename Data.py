from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can download profile pictures, videos, images and reels from instagram along with post caption.
You can also authorize me to download private posts.

Use below buttons to learn more.

Created By @join2bk
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("💥 More Amazing Bots 💥", url="https://t.me/BotsByBk")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("💫 Free Online Courses 💫", url="https://t.me/onlinecoursesforyou_bot")],
    ]

    # Help Message
    HELP = """
1) **Images, Videos and Reels**
Send me the link to get the post contents including the caption.

2) **Profile Pictures**
Use the command `/profile_pic` or `/dp` along with instagram username to get its profile picture.
Example : `/dp techcrazebk`

3) **Private Posts**
Authorize (login) the bot to download private posts. Use /auth

**Note** : Stories and IGTV are not supported.

Use /auth to authorize and /unauth to unauthorize.
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to download instagram content, created by @join22bk

Source Code : [Click Here](https://github.com/techcrazebk/InstagramTGBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : I'm not a developer (@join2bk)
    """
