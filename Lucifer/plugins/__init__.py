from telethon.tl.types import Channel

from Lucifer import *
from Lucifer import ALIVE_NAME, bot, luciferver
from Lucifer.LuciferConfig import Config, Var

# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

LuciferUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lucifer user"

lucifer = f"luciferππ΄πππΈπΎπ½: {luciferver}\n"
lucifer += f"π»πΎπΆ πΆππΎππΏ: {log}\n"
lucifer += f"πΌπ π°πππΈπππ°π½π π±πΎπ: {bots}\n"
lucifer += f"π»ππ³πΈπ°: {lyd}\n"
lucifer += f"πππ³πΎ πππ΄π: {sudo}\n"
lucifer += f"πΏπΌ ππ΄π²πππΈππ: {pm}\n"
lucifer += f"\nππΈππΈπ @Lucifer π΅πΎπ π°πππΈπππ°π½π.\n"
luciferstats = f"{lucifer}:@Lucifer_support_group"

LUCIFER_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def Lucifer_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
