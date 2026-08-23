def make_ascii_svg():
    width = 370
    height = 360

    # High-quality monochrome ASCII portrait representation
    ascii_art = [
        "   .---------------------------------.  ",
        "  /   _   _   _   _   _   _   _   _   \\ ",
        "  |  (S) (N) (E) (H) (A) (L) (G) (H)  | ",
        "  \\___________________________________/ ",
        "        _        _               _      ",
        "     .-' '-.  .-' '-.         .-' '-.   ",
        "    /   .   \\/   .   \\       /   .   \\  ",
        "   |   / \\  ||  / \\   |     |   / \\   | ",
        "   |  |   | || |   |  |     |  |   |  | ",
        "    \\  \\_/  /\\  \\_/  /       \\  \\_/  /  ",
        "     '-...-'  '-...-'         '-...-'   ",
        "    _________________________________   ",
        "   /                                 \\  ",
        "  |  [+] ARTIFICIAL INTELLIGENCE     |  ",
        "  |  [+] MACHINE LEARNING ENGINEER   |  ",
        "  |  [+] AGENTIC RAG ARCHITECT       |  ",
        "  |  [+] DATA ANALYTICS & SYSTEMS    |  ",
        "  \\_________________________________/   ",
        "    \\_______________________________/   ",
        "       \\                         /      ",
        "        `-----------------------'       "
    ]

    line_svgs = []
    start_y = 55
    line_height = 14

    for idx, line in enumerate(ascii_art):
        y = start_y + idx * line_height
        delay = round(idx * 0.04, 2)
        
        # Escape HTML special chars
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        line_html = f'''<g class="ascii-row" style="animation-delay: {delay}s;">
      <text x="20" y="{y}" class="ascii-text">{escaped_line}</text>
    </g>'''
        line_svgs.append(line_html)

    lines_content = "\n    ".join(line_svgs)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }}
    .title-text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 13px; font-weight: bold; fill: #8b949e; }}
    .ascii-text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 11px; fill: #58a6ff; font-weight: bold; xml:space: preserve; }}
    .ascii-row {{
      opacity: 0;
      animation: typeRow 0.1s linear forwards;
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

    print("Successfully generated snehal-ascii.svg!")

if __name__ == "__main__":
    make_ascii_svg()
