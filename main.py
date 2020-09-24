import discord
import reddit #reddit.py
from discord.ext import commands

#load posts from reddit
redditsc = reddit.scrapper()

subque = ['programmerhumor']

for i in subque:
    redditsc.update(i)


game = discord.Game('`짤')

bot = commands.Bot(command_prefix='`', status = discord.Status.online, activity = game, help_command = None)


@bot.event
async def on_ready():
    print('We have logged in!')


@bot.command()
async def 도움(ctx):

    embed = discord.Embed(
        title= '짤봇2000를 사용하주셔서 감사합니다.',
        colour=discord.Colour(0xE5E242),

        description = '테스트123',
    )
    
    await ctx.send(embed=embed)


@bot.command(pass_context = True)
async def 짤(ctx, arg = None):
    if arg is None:
        sub, url, details = redditsc.random()

        print(arg)

    else:
        sub, url, details = redditsc.fromsub(arg)
        print(url)
        
    embed = discord.Embed(
            title = 'r/' +sub +' 에서 온 짤:',
            description = details[0]
    )
    embed.set_image(url= url)
    embed.url = 'https://reddit.com' + details[1]
    embed.set_footer(
        text  = ctx.message.author.name,
        icon_url = ctx.message.author.avatar_url
    )
    
    await ctx.send(embed=embed)


bot.run(open('token').read())

