# Originally from Bothub
# Port to UserBot by @heyworld
#Copyright (C) 2020 azrim.

from telethon import events
import subprocess
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
import glob
import os
try:
 import subprocess
except:
 os.system("pip install instantmusic")
 


os.system("rm -rf *.mp3")


def bruh(name):
    
    os.system("instantmusic -q -s "+name)
    

@register(outgoing=True, pattern="^.song(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit("searching song..please wait")    
    bruh(str(cmd))
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("sending song")
    await bot.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)

@register(outgoing=True, pattern="^.spd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Downloading music taking some times,  Stay Tuned.....`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              await bot.send_message(chat, link)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @SpotifyMusicDownloaderBot and try again```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)

@register(outgoing=True, pattern="^.netease(?: |$)(.*)")
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    await netase.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await netase.edit("`Downloading...Please wait`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await netase.reply("```Please unblock @WooMaiBot and try again```")
              return
          await netase.edit("`Sending Your Music...`")
          await asyncio.sleep(3)
          await bot.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await netase.delete()


@register(outgoing=True, pattern="^.dzd(?: |$)(.*)")
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await Deezlod.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await Deezlod.edit("**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
          try:
              msg_start = await conv.send_message("/start")
              response = await conv.get_response()
              r = await conv.get_response()
              msg = await conv.send_message(d_link)
              details = await conv.get_response()
              song = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await Deezlod.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
              return
          await bot.send_file(Deezlod.chat_id, song, caption=details.text)
          await Deezlod.client.delete_messages(conv.chat_id,
                                             [msg_start.id, response.id, r.id, msg.id, details.id, song.id])
          await Deezlod.delete()          
    
CMD_HELP.update({
        "music":
        "`.song` <search title>\
            \nUsage: For searching songs.\
            \n\n`.spd`<Artist - Song Title>\
            \nUsage:For searching songs from Spotify.\
            \n\n`.netease` <Artist - Song Title>\
            \nUsage:Download music with @WooMaiBot\
            \n\n`.dzd` <Spotify/Deezer Link>\
            \nUsage:Download music from Spotify or Deezer."
})
