import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://media.giphy.com/media/3oEjI0naHAj6j8Bn2M/giphy.gif"
pm_caption = "⚠️ NexBOTt is On 🔥 FIRE �⚠️ \n\n"
pm_caption += "🔸**SYSTEM STATU**\n"
pm_caption += "🔹TELETHON VERSION : **6.0.9**\n ⭕️ Python: **3.7.4**\n"
pm_caption += "🔸DATABASE STATUS  : **Functional**\n"
pm_caption += "🔹**Current Branch** : `Master`\n"
pm_caption += "🔸**Nex OS** :   1.14`\n"
pm_caption += f"🔹**My Boss** : {DEFAULTUSER} \n"
pm_caption += "🔸**Made By 😎** : [This Pero](https://t.me/sensei_nex)\n\n"
pm_caption += "🔻Deploy NexBOT : [ℝ𝕖𝕡𝕠](https://github.com/SenseiOfficial/NexBOT)\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
