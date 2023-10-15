from settings import settings
import discord
from discord.ext import commands
import os , random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


 
@bot.command()
async def eco(ctx):
    img_name= random.choice(os.listdir("imanges"))
    with open(f'imanges/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)       



bot.run(settings["TOKEN"])
