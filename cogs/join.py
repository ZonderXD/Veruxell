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
    async def on_guild_join(self, guild):
        embed = discord.Embed(
            title=("Veruxell"),
            description=f"Добрый день!\n\n Вы получили это сообщение т.к на ваш сервер **{guild.name}** был добавлен Veruxell.\nЭто чисто информативное сообщение, сделанное для того, чтобы вы знали немного больше о том, чем пользуетесь.",
            color=0x800080
        )
        embed.add_field(
            name="Полезная информация:",
            value=f"**Сервер создателя бота - https://discord.gg/XT5E8ft\nСоздатель бота - `𝙳𝚎𝚅𝚒𝚒#2576`\nПрефикс бота - `+`\nПомощь по командам - `+help`**"
        )
        embed.set_footer(text=f"𝙳𝚎𝚅𝚒𝚒#2576 © | Все права защищены", icon_url="https://cdn.discordapp.com/avatars/719605055547768894/812745a344a780f8927aefd49fb66329.webp?size=1024")

        await guild.owner.send(embed=embed)
        channel_id = 724368421910741223
        channel = self.bot.get_channel(channel_id)
        j_e = discord.Embed(
            title=f"Бот присоединился к серверу {guild.name}",
            description=f"**Информация о сервере:**\n\nСервер - {guild.name}\nID сервера - {guild.id}\nВладелец сервера - {guild.owner}",
        )
        await channel.send(embed=j_e)

def setup(bot):
    bot.add_cog(join(bot))
