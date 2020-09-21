import praw
import discord
import random




client = discord.Client()
reddit = praw.Reddit()



class redditscrapper:

    def __init__(self):
        self.storage = {}
        self.used = []
        self.posted = []


    def update(self,sub):
        print('reddit: UPDATING POSTS..')
        subreddit = reddit.subreddit(sub)
        tmp = []
        for submission in subreddit.hot(limit=100):
            tmp.append(submission.url)
        self.storage[sub] = tmp



    def random(self):
        sub = random.choice(list(self.storage.keys()))
        posts = self.storage[sub]
        post = random.choice(posts)
        if post in self.used:
            self.random()
        else:
            print('sending post')
            self.used.append(post)
            return post


redditsc = redditscrapper()

devsubs = ['programmerhumor','linuxmemes']

for i in devsubs:
    redditsc.update(i)





        

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!짤'):
        que = redditsc.random()
        print(que)
        await message.channel.send(que)
    
    elif message.content.startswith('!도움'):
        await message.channel.send('그딴건 아직 없어요 \n\n 개발자들에게 물어보세요!!')

client.run('NzU3NTg5NTkwODg5NzI2MDUy.X2imSQ.wWddZnDqSJqgeqfjYfQSV5Hato4')