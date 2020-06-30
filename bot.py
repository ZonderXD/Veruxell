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

bot = commands.Bot(command_prefix='+')
bot.remove_command('help')

conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Я бот Lyrics, напиши "+help" и получи список моих команд'))
    print(f'          [Lyrics]')
    print(f"[Lyrics] Bot successfully launched!;")
    print(f"[Lyrics] Name: [{bot.user}];")
    print(f'[Lyrics] ID: [{bot.user.id}];')

def owner(ctx):
    return ctx.message.author.id == 719605055547768894

@bot.command()
@commands.check(owner)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(embed = discord.Embed(description = f"**{ctx.author.mention}, модуль `{extension}` был успешно загружен!**", color = 0x00ffff))

@bot.command()
@commands.check(owner)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(embed = discord.Embed(description = f"**{ctx.author.mention}, модуль `{extension}` был успешно выгружен!**", color = 0x00ffff))

@bot.command()
@commands.check(owner)
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(embed = discord.Embed(description = f"**{ctx.author.mention}, модуль `{extension}` был успешно перезагружен!**", color = 0x00ffff))

def random_meme():
    with open('memes_data.txt', 'r') as file:
        memes = file.read().split(',')
    picked_meme = random.choice(memes)
    return picked_meme

@bot.command()
async def cat(ctx):
    meow = random.randint(1, 100000)
    embed = discord.Embed(title='**Вот тебе кот:**' ,colour=0x00ffff)
    embed.set_image(url = f'https://cataas.com/cat?{meow}')
    await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
    emb = discord.Embed(description = f"**Вот тебе мем:**", color = 0xda4a)
    emb.set_image(url= random_meme())
    await ctx.send(embed=emb)

@bot.command()
async def suggest( ctx , * , agr ):
    await ctx.message.add_reaction('<a:Yes:719995062095839366>')
    suggest_chanell = bot.get_channel( 725476146627739698 ) #Айди канала предложки
    embed = discord.Embed(title=f"Новое предложение:", description= f"{ctx.author.mention} предложил: **{agr}** \n\n")

    embed.set_thumbnail(url=ctx.guild.icon_url)

    message = await suggest_chanell.send(embed=embed)
    await message.add_reaction('<a:Yes:719995062095839366>')
    await message.add_reaction('<a:No:719995078059229336>')

@bot.command(aliases=['bot'])
async def botinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Информация о боте **Lyrics#7065**.\n Я был сделан для Вашего удобства,\n Подробнее о командах: **`+help`**", color = 0x00ffff)
    embed.add_field(name=f'**Меня создал:**', value="`Needly#0001`(<@719605055547768894>)", inline=False)  # Создает строку
    embed.add_field(name=f'**Лицензия:**', value="DiscordHosting-V3.5.7", inline=False)  # Создает строку
    embed.add_field(name=f'**Я написан на:**', value="Discord.py", inline=False)  # Создает строку
    embed.add_field(name=f'**Версия:**', value="V1.0.0", inline=False)  # Создает строку
    embed.add_field(name=f'**Патч:**', value="1", inline=False)  # Создает строку
    embed.set_thumbnail( url = bot.user.avatar_url)
    embed.set_footer(text=f"Needly#0001 © | Все права защищены", icon_url="https://cdn.discordapp.com/avatars/719605055547768894/a_9a069cce7b003d72a18bc790a36de1ef.gif?size=1024")
    await ctx.send(embed=embed)

@bot.command() # Декоратор команды
async def ran_avatar(ctx): # Название команды
    emb = discord.Embed(description= 'Вот подобраная Вам аватарка.', color=0x6fdb9e) # Переменная ембеда и его описание
    emb.set_image(url=nekos.img('avatar')) # Тут мы с помощью новой библиотеки ищем картинку на тему аватар и ставим её в ембед
    await ctx.send(embed=emb)  # Отпрвака ембеда

@bot.command() # Декоратор команды
async def slap(ctx, member : discord.Member): # Название команды и аргумент
    if member == ctx.message.author: # Проверка кого упомянули
        await ctx.send('<a:No:719995078059229336> Вы не можете ударить сами себя.')
    else:
        emb = discord.Embed(description= f'{member.mention}, Вас ударил(-а) {ctx.message.author.mention}.', color=0x6fdb9e) # Переменная ембеда и описание
        emb.set_image(url=nekos.img('slap')) # Ищем картинку и ставим её в ембед
 
        await ctx.send(embed=emb) # Отпрвака ембед

@bot.command() # Декоратор команды
async def goose(ctx): # Название команды и аргумент
        emb = discord.Embed(description= f'**Вот твой гусь:**', color=0x6fdb9e) # Переменная ембеда и описание
        emb.set_image(url=nekos.img('goose')) # Ищем картинку и ставим её в ембед
 
        await ctx.send(embed=emb) # Отпрвака ембед

@bot.command() # Декоратор команды
async def dog(ctx): # Название команды и аргумент
        emb = discord.Embed(description= f'**Вот твоя собака:**', color=0x6fdb9e) # Переменная ембеда и описание
        emb.set_image(url=nekos.img('woof')) # Ищем картинку и ставим её в ембед
 
        await ctx.send(embed=emb) # Отпрвака ембед

@bot.command() # Декоратор команды
async def hug(ctx, member : discord.Member): # Название команды и аргумент
    if member == ctx.message.author: # Проверка кого упомянули
        await ctx.send('<a:No:719995078059229336> Вы не можете обнять сами себя.')
    else:
        emb = discord.Embed(description= f'{member.mention}, Вас обнял(-а) {ctx.message.author.mention}.', color=0x6fdb9e) # Переменная ембеда и описание
        emb.set_image(url=nekos.img('hug')) # Ищем картинку и ставим её в ембед
 
        await ctx.send(embed=emb) # Отпрвака ембед

@bot.command()
async def kill(ctx, member : discord.Member = None):
	if member == None:
		emb = discord.Embed(description= f'{ctx.message.author.mention} Прыгает с крыши.', color=0x6fdb9e) # Переменная ембеда и описание
		emb.set_image(url='https://pa1.narvii.com/7081/7f5f49cf4e6c0a06614d7cda9bd5954b257a2151r1-500-296_hq.gif')
		
		await ctx.send(embed=emb)
	else:
		emb = discord.Embed(description= f'{member.mention}, Вас убил(-а) {ctx.message.author.mention}.', color=0x6fdb9e) # Переменная ембеда и описание
		emb.set_image(url='https://cdn.discordapp.com/attachments/693515715646324796/707582757144100894/tenor.gif') # Ищем картинку и ставим её в ембед
 	
		await ctx.send(embed=emb) # Отпрвака ембед

@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title = '⚙ Навигация по командам:\n 🦴 Чтоб посмотреть команды, нажимайте на реакции ниже.\n ❗ Обязательные параметры: `()`\n ❓ Необязательные параметры: `[]`', color=0x6fdb9e )
    embed2 = discord.Embed(title ='💎 Базовые:', description='**``+user [@user]`` - Узнать информацию о пользователе 🎭\n ``+server`` - Узнать информацию о сервере 🧿\n `+bot` - Информация о боте 🤖\n `+avatar [@user]` - Аватар пользователя 🖼\n `+wiki (text)` - Википедия 📖\n `+covid (country)` - Информация о вирусе Covid-19 🦠\n `+invite` - Приглашение бота 👻\n `+suggest (text)` - Идея для бота **', color=0x6fdb9e )
    embed3 = discord.Embed(title ='🎉 Весёлости:', description='**``+coin`` - Бросить монетку 🌈\n ``+math (2*2/2+2-2)`` - Решить пример :infinity:\n `+8ball (question)` - Волшебный шар 🔮\n `+meme` - Рандомный мем 🤣\n `+sapper` - Типичный сапёр ♻\n `+ttt (user)` - Крестики-нолики ⭕\n `+bunting` - Угадай флаг 🏴**', color=0x6fdb9e)
    embed4 = discord.Embed(title ='🧊 Для админов:', description='**`+say (text)` - Написать текст от лица бота ⚖**', color=0x6fdb9e)
    embed5 = discord.Embed(title ='💋 Некос:', description='**`+hug (@user)` - Обнять 😜\n `+slap (@user)` - Ударить 😡\n `+kill [@user]` - Убить 🔪\n `+dog` - Собака :dog:\n `+goose` - Гусь :duck:\n `+cat` - Кот 🐱**', color=0x6fdb9e)
    embeds = [embed1, embed2, embed3, embed4, embed5]
    message = await ctx.send(embed=embed1)
    page = Paginator(bot, message, only=ctx.author, use_more=False, embeds=embeds, reactions = ['<a:Left:720717981499261008>', '<a:Right:720717967343485020>'])
    await page.start()

@bot.command()
async def invite(ctx):
    await ctx.send(embed = discord.Embed(description = f"https://discord.com/oauth2/authorize?client_id=722389231917334588&scope=bot&permissions=980937982", color=0x6fdb9e))

@bot.command()
async def wiki(ctx, *, text):
    wikipedia.set_lang("ru")
    new_page = wikipedia.page(text)
    summ = wikipedia.summary(text)
    emb = discord.Embed(
        title= new_page.title,
        description= summ,
        color = 0x00ffff
    )
    emb.set_author(name= 'Больше информации тут! Кликай!', url= new_page.url, icon_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')

    await ctx.send(embed=emb)

@bot.command()
async def user(ctx, Member: discord.Member = None ):
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles )
    emb = discord.Embed(title='Информация о пользователе.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
                                                                                      f"**🧬 Имя: `{Member.name}`**\n\n"
                                                                                      f"**⚔ Никнейм: `{Member.nick}`**\n\n"
                                                                                      f"**🌵 Статус: `{Member.status}`**\n\n"
                                                                                      f"**🔑 ID: `{Member.id}`**\n\n"
                                                                                      f"**🌋 Высшая роль: `{Member.top_role}`**\n\n"
                                                                                      f"**🌟 Аккаунт создан: `{Member.created_at.strftime('%A %b %#d, %Y')}`**", 
                                                                                      color=0xff0000, timestamp=ctx.message.created_at)

    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)

@bot.command()
async def avatar(ctx, member : discord.Member = None):

    user = ctx.message.author if (member == None) else member

    embed = discord.Embed(title=f'** Аватар `{user}`**', color= 0x0c0c0c)

    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def coin( ctx ):
    coins = [ 'орел', 'решка' ]
    coins_r = random.choice( coins )
    coin_win = 'орел'

    if coins_r == coin_win:
        await ctx.send(embed = discord.Embed(description= f''':tada: { ctx.message.author.name }, выиграл! 
            Тебе повезло у тебя: ``{ coins_r }``''', color = 0x0c0c0c))

    if coins_r != coin_win:
        await ctx.send(embed = discord.Embed(description= f''':thumbsdown:  { ctx.message.author.name }, проиграл! 
            Тебе не повезло у тебя: ``{ coins_r }``''', color = 0x0c0c0c))

@bot.command()
async def ran_color(ctx):
    clr = (random.randint(0,16777215))
    emb = discord.Embed(
        description= f'Сгенерированый цвет : ``#{hex(clr)[2:]}``',
        colour= clr
    )

    await ctx.send(embed=emb)

@bot.command(name = "8ball")
async def ball(ctx, *, arg):

    message = ['Нет 😑','Да 😎','Возможно 😪','Опредленно нет '] 
    s = random.choice( message )
    await ctx.send(embed = discord.Embed(description = f'**:crystal_ball: Знаки говорят:** {s}', color=0x0c0c0c))
    return

# Работа с ошибками шара

@ball.error 
async def ball_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument ): 
        await ctx.send(embed = discord.Embed(description = f'Пожалуйста, укажите вопрос.', color=0x0c0c0c)) 

@bot.command(aliases = ['count', 'calc', 'вычисли', 'math'])
async def __count(ctx, *, args = None):
    text = ctx.message.content

    if args == None:
        await ctx.send(embed = discord.Embed(description = 'Пожалуйста, укажите выражение для оценки.', color = 0x39d0d6))
    else:
        result = eval(args)
        await ctx.send(embed = discord.Embed(description = f'Результат примера: `{args}`: \n`{result}`', color = 0x39d0d6))

@bot.command()
@commands.has_permissions( administrator = True)
async def say(ctx, *, arg):
    await ctx.send(f'{arg}')

@bot.command()
async def server(ctx):
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"Сервер: `{ctx.guild.name}`", color=0xff0000, timestamp=ctx.message.created_at)
    embed.description=(
        f"<a:Time:719996484237656215> **Сервер создали: `{ctx.guild.created_at.strftime('%A, %b %#d %Y')}`**\n\n"
        f"<:Region:719996506857406525> **Регион: `{ctx.guild.region}`**\n\n"
        f"<:Owner:720001653163425822> **Глава сервера: `{ctx.guild.owner}`**\n\n"
        f"<:Bot:719996225453162618> **Ботов на сервере: `{len([m for m in members if m.bot])}`**\n\n"
        f"<:Online:719996334546878494> **Онлайн: `{online}`**\n\n"
        f"<:Offline:719996377865912342> **Оффлайн: `{offline}`**\n\n"
        f"<:Idle:719996278196666439> **Отошли: `{idle}`**\n\n"
        f"<:Dnd:719996257330004019> **Не трогать: `{dnd}`**\n\n"
        f"<:Shield:719996523823366195> **Уровень верификации: `{ctx.guild.verification_level}`**\n\n"
        f"<:Channels:719996243228753921> **Всего каналов: `{allchannels}`**\n\n"
        f"<:VoiceChannel:719996462305509386> **Голосовых каналов: `{allvoice}`**\n\n"
        f"<:TextChannel:719996437676425358> **Текстовых каналов: `{alltext}`**\n\n"
        f"<a:Roles:719996398044708945> **Всего ролей: `{allroles}`**\n\n"
        f"<:Members:719996296827764786> **Людей на сервере: `{ctx.guild.member_count}`**\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"Информация о сервере: {ctx.guild.name}")
    await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

token = os.environ.get("BotToken")
bot.run(str(token))
