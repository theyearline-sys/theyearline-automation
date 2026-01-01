import pytz
import os
import tweepy
from datetime import datetime
from theyearline import year_progress, render_image

API_KEY = os.environ["X_API_KEY"]
API_SECRET = os.environ["X_API_SECRET"]
ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["X_ACCESS_SECRET"]

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

if __name__ == "__main__":
    tz = pytz.timezone("Asia/Kolkata")
    now = tz.localize(datetime.now())
    p = year_progress(now)
    pct = round(p*100, 1)
    text = f"{now.year} is {pct}% complete — TheYearLine • By 365Pulse"
    img_path = render_image(p, now.year)

    print(f"Image path: {img_path}")
    print(f"Exists: {os.path.exists(img_path)}")
    print(f"Size: {os.path.getsize(img_path)} bytes")

    # Upload media using v1.1 API
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    media = api.media_upload(img_path)

    # Post tweet using v2 Client
    client.create_tweet(text=text, media_ids=[media.media_id])
    print("Posted to X.")
