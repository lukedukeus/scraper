import praw
import pandas as pd
import datetime as dt 
import re
import os

reddit = praw.Reddit(client_id='14_CHARS_IDENTIFIER', 
                     client_secret='27_CHARS_SECRET_ID', 
                     user_agent='SCRIPT_NAME', 
                     username='REDDIT_USER_NAME', 
                     password='REDDIT_LOGIN_PASSWORD')
#found at https://medium.com/@plog397/webscraping-reddit-python-reddit-api-wrapper-praw-tutorial-for-windows-a9106397d75e

subreddit = reddit.subreddit('MicrosoftRewards')
new = subreddit.new(limit=1000)
bad_words = ['imgur', 'bitbucket', 'reddit']

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
            line = line.replace("[","\n")
            line = line.replace("(","\n")
            if line.startswith('http'):
                p.write(line)
with open("email_links.txt", "w", encoding="utf-8") as f:           
    with open('temp.txt','r', encoding="utf-8") as file:
            for line in file:
                if line.startswith('http'):
                    if not any(bad_word in line for bad_word in bad_words):
                        f.write(line)
                
                

                
