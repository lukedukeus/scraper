import praw
import pandas as pd
import datetime as dt 
import re
import os

reddit = praw.Reddit(client_id='IFXhYoANBON5gg', 
                     client_secret='EHTLxLBUEkJtJpG-Szri_A8Atpg', 
                     user_agent='SCRIPT_NAME', 
                     username='lukedukeus', 
                     password='1vanzweden')


subreddit = reddit.subreddit('MicrosoftRewards')
new = subreddit.new(limit=1000)

dict =        { "body":[]}
f= open("temp.txt","w+")
for submission in new:
    with open("temp.txt", "a", encoding="utf-8") as f:
        f.write(submission.selftext)


with open("temp.txt", "r", encoding="utf-8") as f:
        for line in f:
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
            for url in urls:
                with open("email_links.txt", "a", encoding="utf-8") as f:
                    f.write(url + '\n')
with open("email_links.txt", "r", encoding="utf-8") as f:
    with open("temp.txt", "w", encoding="utf-8") as p:
        for line in f:                  
            line = line.replace("]","\n")
            line = line.replace(")","\n")
            line = line.replace("(","\n")
            p.write(line)
with open("email_links.txt", "w", encoding="utf-8") as f:           
    with open('temp.txt','r', encoding="utf-8") as file:
        for line in file:
            if not line.isspace():
                f.write(line)

os.remove("temp.txt") 
