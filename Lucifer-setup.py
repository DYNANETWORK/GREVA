#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""
███╗░░░███╗░█████╗░███╗░░░███╗██████╗░░█████╗░
████╗░████║██╔══██╗████╗░████║██╔══██╗██╔══██╗
██╔████╔██║███████║██╔████╔██║██████╦╝███████║
██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
██║░╚═╝░██║██║░░██║██║░╚═╝░██║██████╦╝██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝
 

Running Mamba Fire on Termux 🔥🔥🔥🔥....
""")
print("")

APP_ID = int(input("𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙰𝙿𝙸 𝙷𝙴𝚁𝙴 ➙ "))
API_HASH = input("𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙰𝙿𝙸 𝙷𝙰𝚂𝙷 𝙷𝙴𝚁𝙴 ➙ ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    tele = client.send_message("me", client.session.save())
    tele.reply(
        "✘ Hᴇʀᴇ ɪs ʏᴏᴜʀ `STRING_SESSION` Oғ Mamba ᴜsᴇʀʙᴏᴛ ✘.\n@MAMBA_X_SUPPORT")
    print("")
    print("Bᴇʟᴏᴡ ɪs ʏᴏᴜʀ STRING_SESSION. Wᴇ ʜᴀᴠᴇ ᴀʟsᴏ sᴛᴏʀᴇᴅ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ sᴀᴠᴇ ᴍᴇssᴀɢᴇs")
    print("")
    print("")
    print(client.session.save())
