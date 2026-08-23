import os
import cv2

RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)

def image_to_ascii(img_path, width=65):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return []
    
    h, w = img.shape
    aspect_ratio = h / w
    new_height = int(width * aspect_ratio * 0.52)
    resized = cv2.resize(img, (width, new_height))
    
    ascii_rows = []
    ramp_len = len(RAMP)
    
    for row in resized:
        line = ""
        for pixel in row:
            idx = int((255 - pixel) / 255 * (ramp_len - 1))
            line += RAMP[idx]
        ascii_rows.append(line)
        
    return ascii_rows

def make_ascii_svg():
    prepped_path = "data/source-prepped.png"
    if os.path.exists(prepped_path):
        ascii_lines = image_to_ascii(prepped_path, width=65)
    else:
        ascii_lines = [
            "               .---.              ",
            "              /     \\             ",
            "             |  O O  |            ",
            "             |   ^   |            ",
            "              \\  -  /             ",
            "               '---'              ",
            "          .---------------.       ",
            "         /  S N E H A L    \\      ",
            "        |  AI / ML ENGINEER |     ",
            "         \\_________________/      "
        ]

    width = 370
    height = 360

    line_svgs = []
    start_y = 50
    line_height = 11

    for idx, line in enumerate(ascii_lines):
        y = start_y + idx * line_height
        delay = round(idx * 0.03, 2)
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        line_html = f'''<g class="ascii-row" style="animation-delay: {delay}s;">
      <text x="15" y="{y}" class="ascii-text">{escaped_line}</text>
    </g>'''
        line_svgs.append(line_html)

    lines_content = "\n    ".join(line_svgs)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }}
    .title-text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 13px; font-weight: bold; fill: #8b949e; }}
    .ascii-text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 9px; fill: #58a6ff; font-weight: bold; xml:space: preserve; }}
    .ascii-row {{
      opacity: 0;
      animation: typeRow 0.08s linear forwards;
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

    with open("snehal-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print("Successfully updated snehal-ascii.svg!")

if __name__ == "__main__":
    make_ascii_svg()
