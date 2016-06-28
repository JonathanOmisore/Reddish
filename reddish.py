import praw
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


for item in items:
     
    print(item + ":\n")
    for x in range(0,len(items)):
        
        subreddit = r.get_subreddit(item)
        try:
            for submission in subreddit.get_hot(limit=10):
                print(submission.title + "\n" + submission.url + "\n" + submission.permalink + "\n" + submission.selftext + "\n" + seperate() )
                enter = input("Press any key to continue")
        except praw.errors.InvalidSubreddit:
             print(str(subreddit) + " is private or does not exist")
            
        
    
    
