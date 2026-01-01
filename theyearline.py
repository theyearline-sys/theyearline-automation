from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

def render_image(progress, year, out_path="theyearline.png"):
    # Image size and colors
    width, height = 800, 200
    bg_color = (20, 20, 20)  # dark gray
    bar_color = (0, 200, 255)  # cyan-blue
    text_color = (255, 255, 255)

    # Create image
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Fonts
    font_large = ImageFont.truetype("arial.ttf", 48)
    font_small = ImageFont.truetype("arial.ttf", 32)

    # Labels
    draw.text((50, 50), "Year Progress", font=font_large, fill=text_color)
    pct_text = f"{round(progress * 100, 2)}%"
    draw.text((600, 50), pct_text, font=font_large, fill=text_color)

    # Progress bar
    bar_x, bar_y = 50, 130
    bar_width, bar_height = 700, 20
    draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], fill=(50, 50, 50))
    draw.rectangle([bar_x, bar_y, bar_x + int(bar_width * progress), bar_y + bar_height], fill=bar_color)

    # Save
    img.save(out_path)
    return out_path
