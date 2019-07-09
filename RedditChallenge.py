# coding=utf-8
import praw
import configparser
from utils.Load import load

from RedditModel import Reddit

class RedditChallenge:

    "Create a constructor with reading a local configuration"
    def __init__(self):
        config = configparser.ConfigParser()

        self.configPath = "confi.ini"
        config.read(self.configPath)

        environment = "TEST"
        self.secret = config.get(environment, 'secret')
        self.password = config.get(environment, 'password')
        self.username = config.get(environment, 'username')
        self.client_id = config.get(environment, 'client_id')
        self.subreddits = config.get(environment, 'subreddits')
        self.top = config.get(environment, 'top')
        self.comments = config.get(environment, 'comments')
        self.scoring = config.get(environment, 'scoring')

    "Connection for an API Reddit, this method should be a singleton pattern re-use a connection better performance"
    def redittconnection(self):
        self.reddit = praw.Reddit(client_id=self.client_id,
                     client_secret=self.secret,
                     password=self.password,
                     user_agent='test',
                     username=self.username)

    "lambda function for order and sum with this volume the performance is equal for an iterative method"
    def sumList(self, list):
        return sorted(list, key=lambda x: x, reverse=True)[:5]


    def redditprocess(self, index, ob):
        red = Reddit()
        score = []
        for submission in self.reddit.user.subreddits(limit=1):
            print (submission)
            for post in self.reddit.subreddit(str(submission)).top(limit=1):
                print (post.title)
                for comment in post.comments.list():
                    if comment.id != '_':
                        score.append(comment.score)
        red.set_subreddits(str(submission))
        red.set_post(int(len(score)))
        red.set_points(int(sum(self.sumList(score))))
        red.set_id(index)
        ob.append(red)

" calculate the KPI "
def postrs(ob):
    return (float(ob.get_post())/float(ob.get_points()))

" calculate the KPI "
def subrs(postRS,ob):
    return postRS/ob.get_post()

" main "
def main():
    list = []
    sammy = RedditChallenge()
    sammy.redittconnection()
    index = 0 # this Id is for the question about the restarts and retries of failed tasks
    sammy.redditprocess(index, list)
    for iter in list:
        print('submission: {}, comment per post: {}, score: {}, index: {}'.format(iter.get_subreddits(),
                                                                           iter.get_post(),
                                                                           iter.get_points(),
                                                                           iter.get_id()))
        load(postrs(iter),subrs(postrs(iter), iter))
        print (postrs(iter))
        print (subrs(postrs(iter), iter))

if __name__ == "__main__":
    main()