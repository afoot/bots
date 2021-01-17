from datetime import datetime, timedelta
import praw
from redvid import Downloader
import requests
import glob
import os.path
import os
import fnmatch

bot_token = ""
bot_chatID = ''
reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="Centos:test_bot:v0.1.0")
an_hour_ago = datetime.utcnow() - timedelta(hours=1)
for submission in reddit.subreddit("tiktokthots").hot():
    if datetime.utcfromtimestamp(submission.created_utc) >= an_hour_ago:
        print(submission.url)
        reddit = Downloader(max_q=True)
        reddit.url = submission.url
        reddit.overwrite = True
        reddit.download()
        url = "https://api.telegram.org/bot"+ bot_token +"/sendVideo";
        data = {"chat_id" : bot_chatID}
        os.chdir("/root/bot_python/")
try:
    for video in glob.glob("*.mp4"):
        if not fnmatch.fnmatch(video, "*240.mp4"):
            files = {"video": open(video, "rb")}
            r = requests.post(url, files=files, data=data)
            print(r.status_code, r.reason, r.content)
except:
    pass
