"""
Generate High-Quality Icons for Khaata Mobile PWA / APK
"""
import os
from PIL import Image, ImageDraw, ImageFont

def generate_app_icon(size, filename):
    # Create image with smooth emerald gradient background
    img = Image.new("RGBA", (size, size), (15, 23, 42, 255)) # Slate 900
    draw = ImageDraw.Draw(img)

    # Rounded rectangle padding
    pad = int(size * 0.1)
    corner_radius = int(size * 0.22)
    
    # Draw emerald gradient or rounded background tile
    tile_bbox = [pad, pad, size - pad, size - pad]
    draw.rounded_rectangle(tile_bbox, radius=corner_radius, fill=(16, 185, 129, 255)) # Emerald 500

    # Draw inner circle / highlight
    inner_pad = int(size * 0.18)
    draw.ellipse([inner_pad, inner_pad, size - inner_pad, size - inner_pad], fill=(5, 150, 105, 255))

    # Draw Wallet / Rupee icon styling
    # Let's draw a stylish "Rs" or Wallet shape
    w_left = int(size * 0.28)
    w_top = int(size * 0.35)
    w_right = int(size * 0.72)
    w_bottom = int(size * 0.68)
    w_rad = int(size * 0.06)

    # Wallet body
    draw.rounded_rectangle([w_left, w_top, w_right, w_bottom], radius=w_rad, fill=(255, 255, 255, 255))
    
    # Wallet flap
    f_left = int(size * 0.52)
    f_top = int(size * 0.45)
    f_right = int(size * 0.76)
    f_bottom = int(size * 0.58)
    draw.rounded_rectangle([f_left, f_top, f_right, f_bottom], radius=int(size*0.04), fill=(15, 23, 42, 255))
    
    # Gold coin / dot on wallet clasp
    dot_x = int(size * 0.68)
    dot_y = int(size * 0.515)
    dot_r = int(size * 0.025)
    draw.ellipse([dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r], fill=(245, 158, 11, 255)) # Amber coin

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename, "PNG")
    print(f"Generated {filename} ({size}x{size})")

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    icons_dir = os.path.join(base_dir, "icons")
    generate_app_icon(192, os.path.join(icons_dir, "icon-192.png"))
    generate_app_icon(512, os.path.join(icons_dir, "icon-512.png"))
    generate_app_icon(512, os.path.join(icons_dir, "icon-512-maskable.png"))
    generate_app_icon(64, os.path.join(icons_dir, "favicon.png"))
