import praw, random, json

reddit = praw.Reddit()

class scrapper:

    def __init__(self):
        with open('db.json', 'r') as fp:
            storage = json.load(fp)
    
        with open('postedurls.json', 'r') as fp:
            posted = json.load(fp)

    
        self.storage = storage
        self.posted = [posted]



    def update(self, sub , lmt = 100):
        print('reddit.py: UPDATING POSTS..')

        subreddit = reddit.subreddit(sub)
        tmp = {}

        for submission in subreddit.hot(limit= lmt):
            tmp[submission.url] = [submission.title, submission.permalink ]
        
        self.storage[sub] = tmp
        
        with open('db.json','w') as db:
            json.dump(self.storage,db)

        print('\n')



    def random(self, subname = None):
        ''' Returns and stores details of a random hot post from the sub requested.'''

        if subname == None:
            sub = random.choice(list(self.storage.keys()))

        else: 
            sub = subname

        posts = self.storage[sub]
        url = random.choice(list(posts.keys()))
        details = posts[url]

        if url in self.posted:
            self.random()

        else:
            print('sending post')
            self.posted.append(url)

            with open('postedurls.json', 'w') as fp:
                json.dump(self.posted, fp)

            return sub, url, details


    def stripsub(self,sub):
        if sub.startswith('r/'):
            return sub[2:]
        
        elif sub.startswith('/r/'):
            return sub[3:]


    def fromsub(self, sub):
        if self.stripsub(sub) in self.storage.keys():
            return self.random(subname = sub)
            
        else:
            self.update(sub, lmt=50)
            return self.random(subname = sub)

