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
            value=f"**Сервер создателя бота - [клик](https://discord.gg/XT5E8ft)\nСоздатель бота - `𝙳𝚎𝚅𝚒𝚒#2576`\nПрефикс бота - `+`\nПомощь по командам - `+help`**"
        )
        embed.set_footer(text=f"𝙳𝚎𝚅𝚒𝚒#2576 © | Все права защищены", icon_url="https://cdn.discordapp.com/avatars/719605055547768894/a_c2e9abd558cd2d4aee76473cb06f30d7.gif?size=1024")

        await guild.owner.send(embed=embed)
        messagechannel = 724368421910741223
        channel = self.bot.get_channel(messagechannel)
        hi = discord.Embed(
            title=f"Бот присоединился к серверу.",
            description=f"**💡 Информация о сервере:\n\n📢 Название сервера - `{guild.name}`\n🎲 ID сервера - `{guild.id}`\n👑 Владелец сервера - `{guild.owner}`**",
            color=0x800080
        )
        await channel.send(embed=hi)

def setup(bot):
    bot.add_cog(join(bot))
