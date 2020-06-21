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

    def init(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, ctx, guild):
        embed = discord.Embed(
            title=("Бот Veruxell - Мало функциональный, но весёлый бот."),
            description=f"**\nСпасибо что добавили бота `Veruxell` на сервер {guild.name}.\nЕсли у Вас возникнут проблеммы, сообщите создателю.\nПрочитайте ниже маленькую информацию о боте.**",
            color=0x800080
        )
        embed.add_field(
            name="Полезная информация:",
            value=f"**Сервер создателя бота - https://discord.gg/XT5E8ft\nСоздатель бота - `𝙳𝚎𝚅𝚒𝚒#2576`\nПрефикс бота - `+`\nПомощь по командам - `+help`**"
        )
        embed.set_footer(text=f"𝙳𝚎𝚅𝚒𝚒#2576 © | Все права защищены", icon_url="https://cdn.discordapp.com/avatars/719605055547768894/812745a344a780f8927aefd49fb66329.webp?size=1024")

        await guild.owner.send(embed=embed)
        messagechannel = "724368421910741223"
        channel = ctx.bot.get_channel(messagechannel)
        j_e = discord.Embed(
            title=f"Бот присоединился к серверу {guild.name}",
            description=f"**Информация о сервере:**\n\nСервер - {guild.name}\nID сервера - {guild.id}\nВладелец сервера - {guild.owner}",
        )
        await channel.send(embed=j_e)

def setup(bot):
    bot.add_cog(join(bot))
