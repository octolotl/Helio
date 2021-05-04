import discord
from discord.ext import commands
import json
import time
from discord.ext.commands import CommandNotFound
import random

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='o!', intents=intents)
bot.remove_command('help')
red = 0xFF0000
green = 0x00FF00
blue = 0x0000ff
yellow = 0xFFFF00


def isping():
    with open('config.json', 'r') as tee:
        js = json.load(tee)
    if js['ping'] == 'True':
        return True
    elif js['ping'] == 'False':
        return False


def isowner(idd):  # Owner Check
    with open('config.json', 'r') as ww:
        jss = json.load(ww)
    if idd in jss['owners']:
        return True
    else:
        return False


def randomline():
    lines = open('splashes.txt', encoding='utf-8').readlines()
    return random.choice(lines)


@bot.event
async def on_ready():
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name="Made by Kimigo#3171"))


@bot.command(pass_context=True, aliases=['mcs'])
async def mcset(ctx):
    if isowner(ctx.author.id):
        with open('config.json', 'r') as ll:
            ada = json.load(ll)

        ada['mchannel'] = ctx.channel.id

        with open('config.json', 'w') as ll:
            json.dump(ada, ll)
        em = discord.Embed(color=green, description='Message channel set!')
        msg = await ctx.send(embed=em)
        time.sleep(5)
        await msg.delete()


@bot.command(pass_context=True, aliases=['mc'])
async def messagechannel(ctx, *, msg):
    if isowner(ctx.author.id):
        with open('config.json', 'r') as ll:
            jss = json.load(ll)
        channel = ctx.guild.get_channel(jss['mchannel'])
        await channel.send(msg)


@bot.command(pass_context=True)
async def on(ctx, *, msg=None):
    if isowner(ctx.author.id):
        with open('config.json', 'r') as tee:
            js = json.load(tee)
        channel = ctx.guild.get_channel(js['mchannel'])
        mesg = await channel.fetch_message(js['message'])
        if msg is None:
            if isping():
                pingg = await channel.send(f'<@&{js["role"]}>')
                await pingg.delete()
            em = discord.Embed(color=green, title='The server is now online!')
            em.set_footer(text=randomline())
            await mesg.edit(embed=em)
        else:
            if isping():
                pingg = await channel.send(f'<@&{js["role"]}>')
                await pingg.delete()
            em = discord.Embed(color=green, title='The server is now online:', description=msg)
            em.set_footer(text=randomline())
            await mesg.edit(embed=em)


@bot.command(pass_context=True)
async def off(ctx, *, msg=None):
    if isowner(ctx.author.id):
        with open('config.json', 'r') as tee:
            js = json.load(tee)
        channel = ctx.guild.get_channel(js['mchannel'])
        mesg = await channel.fetch_message(js['message'])

        if msg is None:
            if isping():
                pingg = await channel.send(f'<@&{js["role"]}>')
                await pingg.delete()
            em = discord.Embed(color=red, title='The server is now offline!')
            em.set_footer(text=randomline())
            await mesg.edit(embed=em)
        else:
            if isping():
                pingg = await channel.send(f'<@&{js["role"]}>')
                await pingg.delete()
            em = discord.Embed(color=red, title='The server is now offline:', description=msg)
            em.set_footer(text=randomline())
            await mesg.edit(embed=em)


@bot.command(pass_context=True, aliases=['re'])
async def restart(ctx, *, msg=None):
    if isowner(ctx.author.id):
        with open('config.json', 'r') as tee:
            js = json.load(tee)
        channel = ctx.guild.get_channel(js['mchannel'])
        mesg = await channel.fetch_message(js['message'])
        if msg is None:
            if isping():
                pingg = await channel.send(f'<@&{js["role"]}>')
                await pingg.delete()
            em = discord.Embed(color=yellow, title='The server is now restarting!')
            em.set_footer(text=randomline())
            await mesg.edit(embed=em)
        else:
            if isping():
                pingg = await channel.send(f'<@&{js["role"]}>')
                await pingg.delete()
            em = discord.Embed(color=yellow, title='The server is now restarting:', description=msg)
            em.set_footer(text=randomline())
            await mesg.edit(embed=em)


@bot.command(pass_context=True, aliases=['c'])
async def custom(ctx, *, arg1):
    if isowner(ctx.author.id):
        await ctx.message.delete()
        em = discord.Embed(color=blue, description=arg1)
        await ctx.send(embed=em)


@bot.command(pass_context=True)
async def rules(ctx, *, rul):
    if isowner(ctx.author.id):
        await ctx.message.delete()
        em = discord.Embed(color=blue)
        em.set_footer(text=rul)
        em.set_image(url="https://cdn.discordapp.com/attachments/795217827707224134/795217884988964894/rules.gif")
        await ctx.send(embed=em)


@bot.command(pass_context=True, aliases=['sm'])
async def setmessage(ctx):
    if isowner(ctx.author.id):
        with open('config.json', 'r') as tee:
            js = json.load(tee)
        channel = ctx.guild.get_channel(js['mchannel'])
        if 'message' in js:
            msg = await channel.fetch_message(js['message'])
            await msg.delete()
        em = discord.Embed(description='.')
        msg = await channel.send(embed=em)

        js['message'] = msg.id

        with open('config.json', 'w') as tee:
            json.dump(js, tee)


@bot.command(pass_context=True, aliases=['p'])
async def ping(ctx, boool):
    if isowner(ctx.author.id):
        inp = boool.lower()
        em = discord.Embed(color=green, description=f'Pinging is now {boool}')
        with open('config.json', 'r') as tee:
            js = json.load(tee)
        if inp == 'true':
            js['ping'] = 'True'
            with open('config.json', 'w') as tee:
                json.dump(js, tee)
            msg = await ctx.send(embed=em)
            time.sleep(5)
            await msg.delete()
        elif inp == 'false':
            js['ping'] = 'False'
            with open('config.json', 'w') as tee:
                json.dump(js, tee)
            msg = await ctx.send(embed=em)
            time.sleep(5)
            await msg.delete()


@bot.command(pass_context=True, aliases=['dm'])
async def delmessage(ctx):
    if isowner(ctx.author.id):
        with open('config.json', 'r') as tee:
            js = json.load(tee)

        channel = ctx.guild.get_channel(js['mchannel'])
        mesg = await channel.fetch_message(js['message'])
        await mesg.delete()

        del js['message']

        with open('config.json', 'w') as tee:
            json.dump(js, tee)


@bot.command(pass_context=True, aliases=['sr'])
async def setrole(ctx, rid):
    if isowner(ctx.author.id):
        try:
            with open('config.json', 'r') as tee:
                js = json.load(tee)

            js['role'] = int(rid)

            with open('config.json', 'w') as tee:
                json.dump(js, tee)
            em = discord.Embed(color=green, description='Role set!')
            msg = await ctx.send(embed=em)
            time.sleep(5)
            await msg.delete()
        except ValueError:
            em = discord.Embed(color=red, description='Invalid Role ID')
            msg = await ctx.send(embed=em)
            time.sleep(5)
            await msg.delete()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return ctx
    elif isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(color=red, description='Missing required argument!')
        error = await ctx.send(embed=em)
        time.sleep(5)
        await error.delete()
    else:
        raise error


with open('config.json', 'r') as tk:
    jsss = json.load(tk)
    if jsss['token'] == "":
        token = input('Token not found, please paste token into this window: ')
        jsss['token'] = token
        with open('config.json', 'w') as tkk:
            json.dump(jsss, tkk)
        bot.run(token)
    else:
        bot.run(jsss['token'])
