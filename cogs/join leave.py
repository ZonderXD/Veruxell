import discord
import asyncio
import datetime
import random as r
import random
import io
import os
import wikipedia
import nekos
import sqlite3
import json
import requests
import time
import sys
import traceback
import youtube_dl
from mod import *
from discord.ext import commands
from discord.utils import get
from yandex_music import Client
from Cybernator import Paginator

class join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = discord.Embed(
            title=("Бот Veruxell - Мало функциональный, но весёлый бот."),
            description=f"**\nСпасибо что добавили бота `Veruxell` на Ваш сервер `{guild.name}`.\nЕсли у Вас возникнут проблеммы, сообщите создателю.\nПрочитайте ниже маленькую информацию о боте.**",
            color=0x800080
        )
        embed.add_field(
            name="Полезная информация:",
            value=f"**Сервер создателя бота - [клик](https://discord.gg/4GFQwcN)\nСоздатель бота - `𝙳𝚒𝙻𝚊𝚇#6666`\nПрефикс бота - `+`\nПомощь по командам - `+help`**"
        )
        embed.set_footer(text=f"𝙳𝚒𝙻𝚊𝚇#6666 © | Все права защищены", icon_url="https://cdn.discordapp.com/avatars/719605055547768894/a_df4795a8f60fe1ee9dded63559128724.gif?size=1024")

        await guild.owner.send(embed=embed)
        messagechannel = 725284992221052928
        channel = self.bot.get_channel(messagechannel)
        hi = discord.Embed(
            title=f"Бот присоединился к серверу.",
            description=f"**<a:Nitro:719995105016021142> Информация о сервере:\n\n<a:Cat:719995005111894118> Название сервера - `{guild.name}`\n<a:Discord:719995167096176734> ID сервера - `{guild.id}`\n<:Owner:720001653163425822> Владелец сервера - `{guild.owner}`**",
            color=0x800080
        )
        await channel.send(embed=hi)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        messagechannel = 725284992221052928
        channel = self.bot.get_channel(messagechannel)
        buy = discord.Embed(
            title=f"Бот отсоиденился от сервера.",
            description=f"**<a:Nitro:719995105016021142> Информация о сервере:\n\n<a:Cat:719995005111894118> Название сервера - `{guild.name}`\n<a:Discord:719995167096176734> ID сервера - `{guild.id}`\n<:Owner:720001653163425822> Владелец сервера - `{guild.owner}`**",
            color=0x800080
        )
        await channel.send(embed=buy)

def setup(bot):
    bot.add_cog(join(bot))
