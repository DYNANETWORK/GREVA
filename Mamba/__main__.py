import glob
import os
import sys
from sys import argv
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from Mamba import LOGS, bot, Mambaver
from Mamba.MambaConfig import Var
from Mamba.utils import load_module,start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from Mamba import CMD_HNDLR

MAMBA = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT

# let's get the bot ready
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

async def startup_log_all_done():
    try:
        await bot.send_message(MAMBA, f"**мαмвα вσт ιѕ ∂єρℓσує∂.\ηѕєη∂** `{¢м∂_нη∂ℓя}αℓινє` **тσ ѕєє вσт ιѕ ωσякιηg σя ησт.\η\ηα∂∂** @{вσтηαмє} **α∂∂ тσ  тнιѕ ιη уσυя gяσυρ αη∂ мαкє нιм α∂мιη ƒσя єηαвℓιηg αℓℓ тнє ƒєαтυяєѕ σƒ мαмвα вσт**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

# Mambabot starter...
# chal jana bdsk🤧 
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'Mamba/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "Mamba/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    Mamba X 2.0 ʜᴀs ʙᴇᴇɴ ᴅᴇᴘʟᴏʏᴇᴅ, ᴅᴏ ᴠɪsɪᴛ @MAMBA_X_SUPPORT !!
                    Mamba ᴠᴇʀ: V2.2
                    ©ᵀᴱᴬᴹ ᴹᴬᴹᴮᴬ
                ----------------------------------------------------------------------
"""
)

# that's life...
async def mamba_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                HELL_PIC,
                caption=f"#START \n\nDeployed MambaBot Successfully\n\n**Mamba - {Mambaver}**\n\nType {hl}ping or {hl}alive to check! \n\nJoin [Mamba Channel](t.me/MAMBA_NETWORK) for Updates & [Mamba Chat](t.me/MAMBA_X_SUPPORT) for any query regarding MambaBot†",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join Mamba Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@MAMBA_NETWORK"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@MAMBA_X_SUPPORT"))
#    except BaseException:
#        pass


bot.loop.create_task(mamba_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# Mambabot
