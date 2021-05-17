import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def join(ctx):

@client.command()
async def place(ctx):

@client.command()
async def info(ctx):
