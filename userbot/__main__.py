import glob
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from . import LOGS, bot
from .Config import Config
from .utils import load_module


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_USER_NAME_BF_HER is not None:
        LOGS.info("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN_BF_HER)
        LOGS.info("Initialisation Finished With No Errors")
        LOGS.info("Starting BadHyperUserBot-X")
        bot.loop.run_until_complete(add_bot(Config.TG_BOT_USER_NAME_BF_HER))
        LOGS.info("Startup Completed")
    else:
        bot.start()

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        if shortname.replace(".py", "") not in Config.NO_LOAD:
            load_module(shortname.replace(".py", ""))

LOGS.info("Yay Your BadHyperUserBot-X Is Officially Working!!!")
LOGS.info(
    "Congratulation, Now Type .alive To See Message If Bot Is Live\n"
    "If You Need Assistance, Head To https://t.me/HyperUserBotXSupport"
)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
