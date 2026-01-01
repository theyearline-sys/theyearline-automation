import os
import tweepy
from datetime import datetime
import pytz
from theyearline import year_progress, render_image

# Load secrets from environment
API_KEY = os.environ["X_API_KEY"]
API_SECRET = os.environ["X_API_SECRET"]
ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["X_ACCESS_SECRET"]

def client():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

if __name__ == "__main__":
    tz = pytz.timezone("Asia/Kolkata")
    now = tz.localize(datetime.now())
    p = year_progress(now)
    pct = round(p*100, 1)
    text = f"{now.year} is {pct}% complete — TheYearLine • By 365Pulse"
    img_path = render_image(p, now.year)

    # Debug checks
    print(f"Image path: {img_path}")
    print(f"Exists: {os.path.exists(img_path)}")
    print(f"Size: {os.path.getsize(img_path)} bytes")
    print(f"Tweet text: {text}")

    api = client()
    media = api.media_upload(img_path)
    api.update_status(status=text, media_ids=[media.media_id])
    print("Posted to X.")
