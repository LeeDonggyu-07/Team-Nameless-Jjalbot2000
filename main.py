import discord
import reddit #reddit.py
from discord.ext import commands

redditsc = reddit.redditsc

game = discord.Game('!도움')

bot = commands.Bot(command_prefix='!', status = discord.Status.online, activity = game, help_command = None)

@bot.event
async def on_ready():
    print('Sucessfully logged in!')


@bot.command()
async def 도움(ctx):
    embed = discord.Embed(title= '짤봇2000를 사용해주셔서 감사합니다!', description=f'test123')
    embed.add_field('짤봇 2000의 기능은 다음과 같습니다')
    await ctx.send(embed)


@bot.command()
async def 짤(ctx):
    sub, post = redditsc.random()

    embed = discord.Embed(
        title = 'reddit에서 푸슝 하고 날아온 짤:',
        description ='r/'+ sub
    )
    embed.set_image(url=post)
    
    await ctx.send(embed=embed)





bot.run(open('token').read())

