
#credits?? I even don't know ... everyone changed owner section so if you need credits pm me.

#And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

#Usage .gamerpfp  Im Not Responsible For Any Ban caused By This

import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot import register
import asyncio

from time import sleep

COLLECTION_STRING = [

  "star-wars-wallpaper-1080p",

  "4k-sci-fi-wallpaper",

  "star-wars-iphone-6-wallpaper",

  "kylo-ren-wallpaper",

  "darth-vader-wallpaper"

]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@register(outgoing=True, pattern="^.randpp(?: |$)(.*)")

async def main(event):

    await event.edit("**Changing random profile pic. Check after 10 secs)

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(7200) #Edit this to your required needs
