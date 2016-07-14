import praw
global items, r
def seperate():
    seperator = '=' * 60
    return seperator
    
file = open('subreddits.txt', 'r')
items = file.read().splitlines()
for item in items:
    if item == '':
        items.remove(item)
file.close()
r = praw.Reddit("User Agent 007")

def run():
    global items, r
    for item in items:
    
        print(item + ":\n")
        subreddit = r.get_subreddit(item)
        enter = input("")
    

        try:
            for submission in subreddit.get_hot(limit=5):
                print(submission.title + "\n" + submission.url + "\n" + submission.permalink + "\n" + submission.selftext + "\n" + seperate() + "\n")
                
        except praw.errors.InvalidSubreddit:
                print(str(subreddit) + " is private or does not exist")
run()
