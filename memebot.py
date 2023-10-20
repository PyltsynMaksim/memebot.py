import discord

from discord.ext import commands
import os, random
import requests
bot = commands.Bot(command_prefix= '$', intents = discord.Intents.default())

@bot.event
async def on_read():
    print('I am working')

@bot.command()
async def mem(ctx):
    with open('images/brb.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem1(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def mem2(ctx):
    number = random.randint(1, 100)
    if  1 <= number >= 67:
        with open('images/brb.webp', 'rb') as f:
            picture = discord.File(f)
    elif 68 <= number >= 100:
        with open('images/1984.webp', 'rb') as f:
            picture1 = discord.File(f)
    await ctx.send(file=picture)
