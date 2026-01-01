from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

def year_progress(now):
    year = now.year
    start = datetime(year, 1, 1, tzinfo=now.tzinfo)
    end = datetime(year + 1, 1, 1, tzinfo=now.tzinfo)
    return (now - start).total_seconds() / (end - start).total_seconds()

def render_image(progress, year, out_path="/home/runner/work/theyearline-automation/theyearline-automation/theyearline.png"):
    WIDTH, HEIGHT = 1200, 630
    img = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 0))  # yellow background
    d = ImageDraw.Draw(img)

    # Title
    d.text((50, 50), f"TheYearLine — {year}", fill=(0,0,0), font=ImageFont.load_default())
    d.text((50, 100), "By 365Pulse", fill=(0,0,0), font=ImageFont.load_default())

    # Progress bar
    bar_top = HEIGHT // 2
    bar_width = WIDTH - 100
    bar_height = 40
    d.rectangle([50, bar_top, 50 + bar_width, bar_top + bar_height], fill=(200,200,200))
    d.rectangle([50, bar_top, 50 + int(bar_width * progress), bar_top + bar_height], fill=(0,0,0))

    # Percent text
    pct = round(progress * 100, 1)
    d.text((50, bar_top + 60), f"{year} is {pct}% complete", fill=(0,0,0), font=ImageFont.load_default())

    img.save(out_path)
    return out_path
