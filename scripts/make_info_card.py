def make_info_card():
    width = 490
    height = 360
    
    rows = [
        ("OS", "B.Tech CSE (AI/ML) @ NCOE Pune", "#58a6ff"),
        ("Kernel", "Agentic AI & RAG Pipeline Specialist", "#79c0ff"),
        ("Scholar", "Lenovo LEAP NextGen Scholar", "#d2a8ff"),
        ("Programs", "Infosys Springboard | IBM SkillsBuild", "#bc8cff"),
        ("Shell", "Python, PyTorch, TensorFlow, LangChain", "#7ee787"),
        ("Stack", "React.js, Flask, MySQL, Power BI, FAISS", "#a5d6ff"),
        ("Contact", "snehalghadge59@gmail.com", "#ffa657"),
        ("Portfolio", "snehalsportfolio2027.netlify.app", "#ff7b72"),
        ("LinkedIn", "linkedin.com/in/snehal-g-711587312", "#58a6ff")
    ]

    row_svgs = []
    start_y = 65
    line_height = 30

    for idx, (label, val, color) in enumerate(rows):
        y = start_y + idx * line_height
        delay = round(0.1 + idx * 0.08, 2)
        
        escaped_label = label.ljust(10)
        escaped_val = val.replace("&", "&amp;")
        
        row_html = f'''<g class="row" style="animation-delay: {delay}s;">
      <text x="25" y="{y}" class="label">{escaped_label}:</text>
      <text x="125" y="{y}" class="val" fill="{color}">{escaped_val}</text>
    </g>'''
        row_svgs.append(row_html)

    rows_content = "\n    ".join(row_svgs)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .title-text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 13px; font-weight: bold; fill: #8b949e; }}
    .label {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 12px; font-weight: bold; fill: #8b949e; white-space: pre; }}
    .val {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 12px; font-weight: 500; }}
    .row {{
      opacity: 0;
      animation: fadeInRow 0.25s linear forwards;
    }}
    @keyframes fadeInRow {{
      to {{
        opacity: 1;
      }}
    }}
  </style>

  <rect width="{width}" height="{height}" rx="8" fill="#0d1117" stroke="#30363d" stroke-width="1" />

  <!-- Terminal Title Bar Buttons -->
  <circle cx="20" cy="20" r="6" fill="#ff5f56" />
  <circle cx="38" cy="20" r="6" fill="#ffbd2e" />
  <circle cx="56" cy="20" r="6" fill="#27c93f" />
  <text x="75" y="24" class="title-text">snehal@github: ~ (neofetch)</text>
  <line x1="0" y1="36" x2="{width}" y2="36" stroke="#21262d" stroke-width="1" />

  <!-- Info Rows -->
  {rows_content}
</svg>
'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print("Successfully generated clean info-card.svg!")

if __name__ == "__main__":
    make_info_card()
