import discord
from discord.ext import commands, tasks
import requests
import os
import subprocess
import shutil
import keep_alive
from itertools import cycle

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

token = os.environ['DISCORD_TOKEN']
channel_id = 7389748937123 # random

bot = commands.Bot(command_prefix="/", intents=intents)
bot.remove_command("help")

def obfuscation(path, author):
    copy = f".//obfuscated//{author}.lua"

    if os.path.exists(copy):
        os.remove(copy)

    shutil.copyfile(path, copy)

    text_file = open(f".//obfuscate.lua", "r")
    data = text_file.read()
    text_file.close()
    f = open(copy, "a")
    f.truncate(0)
    f.write(data)
    f.close()

    originalupload = open(path, "r")
    originalupload_data = originalupload.read()
    originalupload.close()

    with open(copy, "r") as in_file:
        buf = in_file.readlines()

    with open(copy, "w") as out_file:
        for line in buf:
            if line == "--SCRIPT\n":
                line = line + originalupload_data + '\n'
            out_file.write(line)

    output = subprocess.getoutput(f'bin/luvit {copy}')

    if os.path.exists(f".//obfuscated//{author}-obfuscated.lua"):
        os.remove(f".//obfuscated//{author}-obfuscated.lua")

    f = open(f".//obfuscated//{author}-obfuscated.lua", "a")
    f.write(output)
    f.close()

    os.remove(copy)

status = cycle(['OBFUSCATED READY'])

@bot.event
async def on_ready():
    change_status.start()
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=next(status)
        )
    )
    keep_alive.keep_alive()

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=next(status)
        )
    )

@bot.event
async def on_message(message):
    author = str(message.author)
    channel = bot.get_channel(channel_id)

    if message.content == "!obfuscate" and message.attachments:
        for attachment in message.attachments:
            url = attachment.url
            if not message.author.bot:
                if '.txt' in url or '.lua' in url:
                    uploads_dir = f".//uploads//"
                    obfuscated_dir = f".//obfuscated//"

                    if not os.path.exists(uploads_dir):
                        os.makedirs(uploads_dir)
                    if not os.path.exists(obfuscated_dir):
                        os.makedirs(obfuscated_dir)

                    response = requests.get(url)
                    path = f".//uploads//{author}.lua"

                    if os.path.exists(path):
                        os.remove(path)

                    open(path, "wb").write(response.content)
                    obfuscation(path, author)

                    await message.channel.send(
                        f"Obfuscated code result for {author}:",
                        file=discord.File(f".//obfuscated//{author}-obfuscated.lua")
                    )

bot.run(token)
