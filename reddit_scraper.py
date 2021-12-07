from sys import getsizeof

import praw
from praw.models import *

reddit = praw.Reddit(
    client_id="q2OvBrofByL3ab6SNpZjzg",
    client_secret="fOThryEyZF5oYAll0j3hQ6EjbYpEOw",
    password="",
    user_agent="testscript by u/carohanhan",
    username="carohanhan",
)

plain_text = ""
num_sub = 1
for submission in reddit.subreddit("wallstreetbets+stocks").top(limit=1000):
    # submission.comments.replace_more()
    count = 0
    for comment in submission.comments.list():
        if type(comment) != MoreComments:
            plain_text += comment.body
            count += 1
    print("Current submissions: {} "
          "\n\tTotal # of comments of this submission: {} "
          "\n\tTitle: {}".format(num_sub, count, submission.title))
    num_sub += 1

print("Total number of characters: {}".format(len(plain_text)))
print("Memory usage for the text: {} MB!".format(getsizeof(plain_text) / (2 ** 20)))

file = open("scraped_text.txt", "w")
file.write(plain_text)
file.close()
