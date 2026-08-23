import os
import cv2
import numpy as np
from PIL import Image

INPUT_PHOTO = r"C:\Users\snehal\.gemini\antigravity-ide\brain\2379b4f1-4787-45a9-ba43-2ce1181beec8\.user_uploaded\media_1787487431098.jpg"
PREPPED_OUT = "data/source-prepped.png"
SVG_OUT = "snehal-ascii.svg"

RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)

def process_photo():
    os.makedirs("data", exist_ok=True)
    
    # 1. Open photo
    img_pil = Image.open(INPUT_PHOTO).convert("L")
    img_np = np.array(img_pil)

    # Crop out side blurred bars if present (center crop)
    h, w = img_np.shape
    crop_w = int(w * 0.7)
    left = (w - crop_w) // 2
    cropped = img_np[:, left:left+crop_w]

    # Boost local contrast with CLAHE
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(cropped)
    cv2.imwrite(PREPPED_OUT, enhanced)

    # 2. Downsample for ASCII
    GRID_WIDTH = 64
    eh, ew = enhanced.shape
    aspect_ratio = eh / ew
    grid_height = int(GRID_WIDTH * aspect_ratio * 0.50)

    resized = cv2.resize(enhanced, (GRID_WIDTH, grid_height))

    # 3. Convert to ASCII rows
    ascii_rows = []
    ramp_len = len(RAMP)
    
    for row in resized:
        line = ""
        for pixel in row:
            idx = int((255 - pixel) / 255 * (ramp_len - 1))
            line += RAMP[idx]
        ascii_rows.append(line)

    # 4. Generate valid SVG with row-by-row self-typing animation
    width = 370
    height = 360

    line_svgs = []
    start_y = 52
    line_height = max(7, int((height - 65) / len(ascii_rows)))

    for idx, line in enumerate(ascii_rows):
        y = start_y + idx * line_height
        delay = round(idx * 0.02, 2)
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        line_html = f'''<g class="ascii-row" style="animation-delay: {delay}s;">
      <text x="14" y="{y}" class="ascii-text" xml:space="preserve">{escaped_line}</text>
    </g>'''
        line_svgs.append(line_html)

    lines_content = "\n    ".join(line_svgs)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }}
    .title-text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 13px; font-weight: bold; fill: #8b949e; }}
    .ascii-text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 8.5px; fill: #79c0ff; font-weight: bold; white-space: pre; }}
    .ascii-row {{
      opacity: 0;
      animation: typeRow 0.06s linear forwards;
    }}
    @keyframes typeRow {{
      to {{
        opacity: 1;
      }}
    }}
  </style>

  <rect width="{width}" height="{height}" class="bg" />

  <!-- Terminal Header Bar -->
  <circle cx="20" cy="20" r="6" fill="#ff5f56" />
  <circle cx="38" cy="20" r="6" fill="#ffbd2e" />
  <circle cx="56" cy="20" r="6" fill="#27c93f" />
  <text x="75" y="24" class="title-text">snehal@ascii: ~ (portrait)</text>
  <line x1="0" y1="36" x2="{width}" y2="36" stroke="#21262d" stroke-width="1" />

  <!-- Self-typing ASCII Rows -->
  {lines_content}
</svg>
'''

    with open(SVG_OUT, "w", encoding="utf-8") as f:
        f.write(svg)

    print("Successfully regenerated valid snehal-ascii.svg!")

if __name__ == "__main__":
    process_photo()
