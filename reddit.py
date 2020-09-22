import praw
import random


reddit = praw.Reddit()


class redditscrapper:

    def __init__(self):
        self.storage = {}
        self.used = []
        self.posted = []



    def update(self,sub):
        print('reddit: UPDATING POSTS..')
        subreddit = reddit.subreddit(sub)
        tmp = {}
        for submission in subreddit.hot(limit=100):
            tmp[submission.url] = [submission.title,submission.permalink]
        self.storage[sub] = tmp
        print(self.storage)
        print('\n\n')



    def random(self):
        sub = random.choice(list(self.storage.keys()))
        posts = self.storage[sub]
        post = random.choice(list(posts.keys()))
        if post in self.used:
            self.random()
        else:
            print('sending post')
            self.used.append(post)
            return sub, post


redditsc = redditscrapper()

subque = ['programmerhumor','linuxmemes']

for i in subque:
    redditsc.update(i)

