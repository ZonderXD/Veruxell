import discord
import asyncio
import datetime
import random as r
import io
import os
import wikipedia
import time
import sys
from discord.ext import commands
from discord.utils import get

class errors(commands.Cog):

    def init(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            await ctx.send(embed=discord.Embed(description=f'**Извините, но такой команды не существует. :x:\n Посмотрите в `+help` и узнайте все существующие команды. ⭕**', color=0xa400fc))

def setup(bot):
    bot.add_cog(errors(bot))
