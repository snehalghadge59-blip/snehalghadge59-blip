import json
import math

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap():
    with open("data/contributions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    total_contributions = data.get("total_contributions", 0)

    # 53 weeks, 7 days per week
    BOX_SIZE = 11
    BOX_GAP = 3
    OFFSET_X = 25
    OFFSET_Y = 30

    width = 860
    height = 175

    # Group days by week
    weeks = []
    current_week = []
    
    for d in days:
        current_week.append(d)
        if len(current_week) == 7:
            weeks.append(current_week)
            current_week = []
    if current_week:
        weeks.append(current_week)

    # Cut to last 53 weeks
    weeks = weeks[-53:]

    # Build SVG content
    svg_cells = []
    
    for w_idx, week in enumerate(weeks):
        x = OFFSET_X + w_idx * (BOX_SIZE + BOX_GAP)
        for d_idx, day in enumerate(week):
            y = OFFSET_Y + d_idx * (BOX_SIZE + BOX_GAP)
            level = day.get("level", 0)
            if level >= len(PALETTE):
                level = len(PALETTE) - 1
            color = PALETTE[level]
            
            # Animation delay calculation based on diagonal index
            diag_index = w_idx + d_idx
            delay = round(diag_index * 0.02, 2)
            
            cell_svg = f'<rect class="day" x="{x}" y="{y}" width="{BOX_SIZE}" height="{BOX_SIZE}" rx="2" fill="{color}" style="animation-delay: {delay}s;" data-date="{day.get("date")}" data-count="{day.get("count")}"/>'
            svg_cells.append(cell_svg)

    cells_content = "\n    ".join(svg_cells)

    # Month labels
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # Simple month text positioning
    month_svgs = []
    for i in range(12):
        mx = OFFSET_X + i * (width - 60) / 12
        month_name = month_labels[i]
        month_svgs.append(f'<text x="{mx:.1f}" y="18" class="month-label">{month_name}</text>')
    months_content = "\n    ".join(month_svgs)

    # Legend
    legend_x = width - 150
    legend_y = height - 15
    legend_rects = []
    for idx, c in enumerate(PALETTE):
        lx = legend_x + idx * (BOX_SIZE + 2)
        legend_rects.append(f'<rect x="{lx}" y="{legend_y - 9}" width="{BOX_SIZE}" height="{BOX_SIZE}" rx="2" fill="{c}"/>')
    legend_content = "".join(legend_rects)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; }}
    .month-label, .meta-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 11px; fill: #8b949e; }}
    .day {{
      opacity: 0;
      transform: translateY(-8px);
      animation: fadeInSlide 0.4s ease-out forwards;
    }}
    @keyframes fadeInSlide {{
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}
  </style>

  <rect width="{width}" height="{height}" class="bg" />

  <!-- Month Labels -->
  {months_content}

  <!-- Calendar Heatmap Grid -->
  {cells_content}

  <!-- Footer Meta & Legend -->
  <text x="{OFFSET_X}" y="{height - 12}" class="meta-text">{total_contributions:,} contributions in the last year</text>
  <text x="{legend_x - 32}" y="{height - 12}" class="meta-text">Less</text>
  {legend_content}
  <text x="{legend_x + len(PALETTE) * (BOX_SIZE + 2) + 4}" y="{height - 12}" class="meta-text">More</text>
</svg>
"""

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print("Successfully generated contrib-heatmap.svg!")

if __name__ == "__main__":
    render_heatmap()
