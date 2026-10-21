import os, base64, io
from PIL import Image, ImageDraw

BASE_DIR = r"C:\Users\snehal\.gemini\antigravity-ide\scratch\snehalghadge59-blip"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# ─── 1. PROCESS FORMAL USER PHOTO (Exact Match to Profile Avatar) ────────────
photo_path = r"C:\Users\snehal\.gemini\antigravity-ide\brain\8141d071-d340-4a41-b36f-feee0a5f8e99\.user_uploaded\media_1792602228673.jpg"

img = Image.open(photo_path).convert('RGB')
w, h = img.size

# A) Generate circular assets/snehal-profile.png for Markdown
min_dim = min(w, h)
left = (w - min_dim) // 2
top = (h - min_dim) // 2
img_square = img.crop((left, top, left + min_dim, top + min_dim))

TARGET_SIZE = 400
SCALE = 4
RENDER_SIZE = TARGET_SIZE * SCALE

img_scaled = img_square.resize((RENDER_SIZE - 40 * SCALE, RENDER_SIZE - 40 * SCALE), Image.Resampling.LANCZOS)
canvas = Image.new('RGBA', (RENDER_SIZE, RENDER_SIZE), (0, 0, 0, 0))
draw = ImageDraw.Draw(canvas)
center = RENDER_SIZE // 2
radius = (RENDER_SIZE // 2) - 8 * SCALE

for i in range(12 * SCALE):
    r = radius + i
    alpha = int(max(0, 180 * (1 - i / (12 * SCALE))))
    draw.ellipse([center - r, center - r, center + r, center + r], outline=(124, 58, 237, alpha), width=SCALE)

draw.ellipse([center - radius, center - radius, center + radius, center + radius], fill=(20, 13, 36, 255), outline=(167, 139, 250, 255), width=6 * SCALE)
inner_border_r = radius - 8 * SCALE
draw.ellipse([center - inner_border_r, center - inner_border_r, center + inner_border_r, center + inner_border_r], outline=(124, 58, 237, 255), width=3 * SCALE)

photo_r = inner_border_r - 6 * SCALE
photo_mask = Image.new('L', (photo_r * 2, photo_r * 2), 0)
mask_draw = ImageDraw.Draw(photo_mask)
mask_draw.ellipse([0, 0, photo_r * 2, photo_r * 2], fill=255)

photo_cropped = img_scaled.resize((photo_r * 2, photo_r * 2), Image.Resampling.LANCZOS)
canvas.paste(photo_cropped, (center - photo_r, center - photo_r), photo_mask)
final_png = canvas.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)
final_png.save(os.path.join(ASSETS_DIR, "snehal-profile.png"), format='PNG', optimize=True)
print("Generated assets/snehal-profile.png from exact formal portrait!")

# B) Crop for arch in Hero Banner SVG
arch_aspect = 232.0 / 308.0
arch_w = int(h * arch_aspect)
arch_left = (w - arch_w) // 2
arch_img = img.crop((arch_left, 0, arch_left + arch_w, h))
arch_img = arch_img.resize((350, 464), Image.Resampling.LANCZOS)
buf = io.BytesIO()
arch_img.save(buf, format='JPEG', quality=88, optimize=True)
b64_portrait = base64.b64encode(buf.getvalue()).decode('ascii')

# ─── 2. HERO BANNER SVG (Data Analyst & AI Intern Target) ─────────────────────
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">Snehal Ghadge — Data Analyst and AI Intern</title>
  <desc id="hero-desc">Data Analyst &amp; AI Intern. B.Tech in CSE (AI/ML), Lenovo LEAP NextGen Scholar, AI Intern at Code-A-Nova, Infosys Springboard Virtual Intern (Power BI &amp; Analytics).</desc>
  <defs>
    <radialGradient id="h-bg" cx="72%" cy="38%" r="80%">
      <stop offset="0" stop-color="#24143D"/>
      <stop offset=".55" stop-color="#140D24"/>
      <stop offset="1" stop-color="#0B0714"/>
    </radialGradient>
    <radialGradient id="h-la" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#7C3AED" stop-opacity=".75"/>
      <stop offset="1" stop-color="#7C3AED" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="h-lb" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#A78BFA" stop-opacity=".25"/>
      <stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="h-ng" gradientUnits="userSpaceOnUse" x1="60" y1="0" x2="520" y2="0">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".55" stop-color="#DDD6FE"/>
      <stop offset="1" stop-color="#A78BFA"/>
    </linearGradient>
    <linearGradient id="h-sh" gradientUnits="userSpaceOnUse" x1="-260" y1="0" x2="-40" y2="0">
      <stop offset="0" stop-color="#EDE9FE" stop-opacity="0"/>
      <stop offset=".5" stop-color="#FFFFFF" stop-opacity=".9"/>
      <stop offset="1" stop-color="#EDE9FE" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;840 0;840 0" keyTimes="0;.35;1" dur="8s" begin="2.5s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="h-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#A78BFA" stop-opacity="0"/>
      <stop offset=".2" stop-color="#C4B5FD"/>
      <stop offset=".75" stop-color="#6D28D9"/>
      <stop offset="1" stop-color="#6D28D9" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="h-og" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#C4B5FD" stop-opacity=".7"/>
      <stop offset="1" stop-color="#5B21B6" stop-opacity=".05"/>
    </linearGradient>
    <pattern id="h-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#8B5CF6" stroke-opacity=".08" stroke-width="1"/>
    </pattern>
    <radialGradient id="h-gf" cx="68%" cy="45%" r="55%">
      <stop offset="0" stop-color="#fff"/>
      <stop offset="1" stop-color="#000"/>
    </radialGradient>
    <mask id="h-gm"><rect width="1200" height="480" fill="url(#h-gf)"/></mask>
    <linearGradient id="h-sc" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#A78BFA" stop-opacity="0"/>
      <stop offset=".5" stop-color="#A78BFA" stop-opacity=".06"/>
      <stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="h-tr" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#EDE9FE"/>
      <stop offset=".45" stop-color="#C4B5FD"/>
      <stop offset="1" stop-color="#7C3AED" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="h-clip"><rect width="1200" height="480" rx="20"/></clipPath>
    <clipPath id="h-arch"><path d="M850 390 V208 A115 115 0 0 1 1080 208 V390 Z"/></clipPath>
  </defs>
  <style>
    .h-serif {{ font-family: Georgia,\"Iowan Old Style\",\"Palatino Linotype\",\"Times New Roman\",serif; }}
    .h-mono  {{ font-family: ui-monospace,SFMono-Regular,Menlo,Consolas,\"Liberation Mono\",monospace; }}
    .h-sans  {{ font-family: -apple-system,BlinkMacSystemFont,\"Segoe UI\",Helvetica,Arial,sans-serif; }}
    .h-rise  {{ animation: h-rise 1.4s cubic-bezier(.16,1,.3,1) both; }}
    .h-fade  {{ animation: h-fade 1.6s cubic-bezier(.16,1,.3,1) both; }}
    .d1{{animation-delay:.15s}} .d2{{animation-delay:.35s}} .d3{{animation-delay:.6s}}
    .d4{{animation-delay:.9s}}  .d5{{animation-delay:1.2s}}
    .h-draw  {{ stroke-dasharray:900;stroke-dashoffset:900;animation:h-draw 2.4s cubic-bezier(.65,0,.35,1) .9s forwards; }}
    .h-trace {{ stroke-dasharray:600 2760;stroke-dashoffset:3360;animation:h-trace 8s linear infinite; }}
    @keyframes h-rise  {{ from{{opacity:0}} to{{opacity:1}} }}
    @keyframes h-fade  {{ from{{opacity:0}} to{{opacity:1}} }}
    @keyframes h-draw  {{ to{{stroke-dashoffset:0}} }}
    @keyframes h-trace {{ to{{stroke-dashoffset:0}} }}
    .h-float {{ animation: h-float 6s ease-in-out infinite; }}
    @keyframes h-float {{ 0%,100%{{transform:translateY(0)}} 50%{{transform:translateY(-8px)}} }}
    @media (prefers-reduced-motion:reduce) {{
      .h-rise,.h-fade,.h-float{{animation:none}}
      .h-draw{{animation:none;stroke-dashoffset:0}}
      .h-trace{{display:none}}
    }}
  </style>
  <g clip-path="url(#h-clip)">
    <rect width="1200" height="480" fill="url(#h-bg)"/>
    <ellipse cx="920" cy="140" rx="420" ry="300" fill="url(#h-la)">
      <animateTransform attributeName="transform" type="translate" values="0 0;-50 25;0 0" dur="20s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1"/>
    </ellipse>
    <ellipse cx="180" cy="460" rx="360" ry="220" fill="url(#h-lb)">
      <animateTransform attributeName="transform" type="translate" values="0 0;60 -20;0 0" dur="26s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1"/>
    </ellipse>
    <rect width="1200" height="480" fill="url(#h-grid)" mask="url(#h-gm)"/>
    <rect x="0" y="-140" width="1200" height="140" fill="url(#h-sc)">
      <animate attributeName="y" values="-140;480" dur="11s" begin="2s" repeatCount="indefinite"/>
    </rect>
    <!-- Drifting particles -->
    <g fill="#DDD6FE">
      <circle cx="560" cy="120" r="1.5"><animate attributeName="opacity" values="0;.9;0" dur="4.2s" repeatCount="indefinite"/><animate attributeName="cy" values="120;96" dur="4.2s" repeatCount="indefinite"/></circle>
      <circle cx="700" cy="70" r="1.2"><animate attributeName="opacity" values="0;.8;0" dur="5.6s" begin="1s" repeatCount="indefinite"/><animate attributeName="cy" values="70;48" dur="5.6s" begin="1s" repeatCount="indefinite"/></circle>
      <circle cx="760" cy="420" r="1.3"><animate attributeName="opacity" values="0;.7;0" dur="6s" begin=".5s" repeatCount="indefinite"/><animate attributeName="cy" values="420;396" dur="6s" begin=".5s" repeatCount="indefinite"/></circle>
    </g>
    <!-- Orbital System -->
    <g transform="translate(965 232)" class="h-fade d3">
      <circle r="210" fill="none" stroke="#8B5CF6" stroke-opacity=".12" stroke-dasharray="1 10">
        <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="140s" repeatCount="indefinite"/>
      </circle>
      <circle r="188" fill="none" stroke="url(#h-og)" stroke-width="1.2"/>
      <circle r="160" fill="none" stroke="#A78BFA" stroke-opacity=".18" stroke-dasharray="2 7"/>
      <g>
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="90s" repeatCount="indefinite"/>
        <circle cx="0" cy="160" r="3" fill="#EDE9FE"/>
        <circle cx="-160" cy="0" r="2.2" fill="#A78BFA" fill-opacity=".8"/>
      </g>
    </g>
    <!-- Formal Portrait in Arch -->
    <g class="h-fade d3 h-float">
      <!-- Arch frame -->
      <path d="M838 394 V208 A127 127 0 0 1 1092 208 V394 Z" fill="none" stroke="#A78BFA" stroke-opacity=".3">
        <animate attributeName="stroke-opacity" values=".15;.5;.15" dur="5s" repeatCount="indefinite"/>
      </path>
      <!-- Real Portrait Photo -->
      <g clip-path="url(#h-arch)">
        <rect x="850" y="86" width="232" height="308" fill="#140D24"/>
        <image href="data:image/jpeg;base64,{b64_portrait}" x="850" y="86" width="232" height="308" preserveAspectRatio="xMidYMin slice"/>
        <linearGradient id="h-photo-fade" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="#7C3AED" stop-opacity=".15"/>
          <stop offset=".6" stop-color="#140D24" stop-opacity="0"/>
          <stop offset="1" stop-color="#0B0714" stop-opacity=".85"/>
        </linearGradient>
        <rect x="850" y="86" width="232" height="308" fill="url(#h-photo-fade)"/>
      </g>
      <!-- Frame border -->
      <path class="h-draw" d="M850 390 V208 A116 116 0 0 1 1082 208 V390 Z" fill="none" stroke="#DDD6FE" stroke-width="1.5" stroke-opacity=".6"/>
      <!-- Glowing data tags beside portrait -->
      <g class="h-rise d4">
        <rect x="724" y="190" width="114" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="740" cy="204" r="4" fill="#38BDF8"/>
        <text font-family="ui-monospace,monospace" x="750" y="208" font-size="10" fill="#DDD6FE">Data Analyst</text>
      </g>
      <g class="h-rise d5">
        <rect x="1092" y="240" width="96" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="1108" cy="254" r="4" fill="#10B981"/>
        <text font-family="ui-monospace,monospace" x="1118" y="258" font-size="10" fill="#DDD6FE">AI Intern</text>
      </g>
      <g class="h-rise d5">
        <rect x="730" y="300" width="108" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="746" cy="314" r="4" fill="#A78BFA"/>
        <text font-family="ui-monospace,monospace" x="756" y="318" font-size="10" fill="#DDD6FE">Pune, India</text>
      </g>
    </g>
    <!-- Left Typography -->
    <g class="h-rise d1">
      <g transform="translate(60 74)">
        <circle cx="6" cy="6" r="4" fill="#10B981"/>
        <circle cx="6" cy="6" r="9" fill="none" stroke="#10B981" stroke-opacity=".4">
          <animate attributeName="r" values="6;14;6" dur="3s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0;1" dur="3s" repeatCount="indefinite"/>
        </circle>
        <text class="h-mono" x="24" y="10" font-size="11.5" letter-spacing="2.8" fill="#C4B5FD">AVAILABLE FOR DATA ANALYST &amp; AI INTERN ROLES</text>
      </g>
    </g>
    <g class="h-rise d2">
      <text class="h-serif" x="58" y="162" font-size="64" font-weight="300" letter-spacing="-1.5" fill="url(#h-ng)">Snehal Ghadge</text>
      <text class="h-serif" x="58" y="162" font-size="64" font-weight="300" letter-spacing="-1.5" fill="url(#h-sh)">Snehal Ghadge</text>
    </g>
    <g class="h-rise d3">
      <text class="h-sans" x="60" y="210" font-size="20" font-weight="400" fill="#EDE9FE">Data Analyst <tspan fill="#A78BFA">·</tspan> AI &amp; Machine Learning Intern</text>
      <text class="h-serif" x="60" y="244" font-size="16" font-style="italic" fill="#C4B5FD">Uncovering actionable intelligence from data. Designing robust ML models &amp; pipelines.</text>
    </g>
    <path class="h-draw" d="M60 274 H720" stroke="url(#h-rule)" stroke-width="1"/>
    <!-- Metadata Chips -->
    <g class="h-rise d4" transform="translate(60 306)">
      <g transform="translate(0 0)">
        <rect width="210" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="105" y="21" text-anchor="middle" font-size="11" fill="#DDD6FE">SQL &amp; Power BI Analytics</text>
      </g>
      <g transform="translate(222 0)">
        <rect width="195" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="97" y="21" text-anchor="middle" font-size="11" fill="#DDD6FE">Python · Pandas · ML</text>
      </g>
      <g transform="translate(429 0)">
        <rect width="185" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="92" y="21" text-anchor="middle" font-size="11" fill="#DDD6FE">B.Tech CSE (AI/ML)</text>
      </g>
    </g>
    <g class="h-rise d5" transform="translate(60 366)">
      <g transform="translate(0 0)">
        <text class="h-serif" font-size="28" font-weight="300" fill="#FFFFFF">30+</text>
        <text class="h-sans" y="22" font-size="12" fill="#A79FB5">repos &amp; analytics dashboards</text>
      </g>
      <g transform="translate(210 0)">
        <text class="h-serif" font-size="28" font-weight="300" fill="#FFFFFF">Power BI &amp; SQL</text>
        <text class="h-sans" y="22" font-size="12" fill="#A79FB5">data pipelines &amp; ETL</text>
      </g>
      <g transform="translate(390 0)">
        <text class="h-serif" font-size="28" font-weight="300" fill="#FFFFFF">AI Intern</text>
        <text class="h-sans" y="22" font-size="12" fill="#A79FB5">Code-A-Nova &amp; Infosys</text>
      </g>
    </g>
    <!-- Frame & Trace -->
    <rect x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
    <rect class="h-trace" x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="url(#h-tr)" stroke-width="1.8" stroke-linecap="round"/>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "snehal-hero-portrait.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)
print("snehal-hero-portrait.svg generated")

# ─── 3. SECTION TITLE HELPER ─────────────────────────────────────────────────
def make_title_svg(num_str, mono_label, serif_main, serif_italic, right_label, filename):
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="'
        + num_str + ' ' + mono_label + ': ' + serif_main + ' ' + serif_italic + '">\n'
        + '  <defs>\n'
        + '    <linearGradient id="ta-line" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="1160" y2="0">\n'
        + '      <stop offset="0" stop-color="#A78BFA"/><stop offset=".6" stop-color="#6D28D9"/><stop offset="1" stop-color="#6D28D9" stop-opacity="0"/>\n'
        + '    </linearGradient>\n'
        + '    <linearGradient id="ta-sheen" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">\n'
        + '      <stop offset="0" stop-color="#DDD6FE"/><stop offset=".5" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DDD6FE"/>\n'
        + '      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1500 0;1500 0" keyTimes="0;.4;1" dur="7s" begin="1.5s" repeatCount="indefinite"/>\n'
        + '    </linearGradient>\n'
        + '  </defs>\n'
        + '  <style>\n'
        + '    .ta-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }\n'
        + '    .ta-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }\n'
        + '  </style>\n'
        + '  <g transform="translate(40 40)">\n'
        + '    <text class="ta-mono" font-size="11" letter-spacing="2.8" fill="#C4B5FD">' + num_str + ' · ' + mono_label + '</text>\n'
        + '    <text class="ta-serif" y="44" font-size="34" font-weight="300" fill="#FFFFFF">' + serif_main + ' <tspan fill="#C4B5FD" font-style="italic">' + serif_italic + '</tspan></text>\n'
        + '    <text class="ta-serif" y="44" font-size="34" font-weight="300" fill="url(#ta-sheen)">' + serif_main + ' <tspan fill="#C4B5FD" font-style="italic">' + serif_italic + '</tspan></text>\n'
        + '    <text class="ta-mono" x="1120" y="14" text-anchor="end" font-size="10.5" letter-spacing="2" fill="#A79FB5">' + right_label + '</text>\n'
        + '  </g>\n'
        + '  <line x1="40" y1="104" x2="1160" y2="104" stroke="url(#ta-line)" stroke-width="1"/>\n'
        + '</svg>\n'
    )
    with open(os.path.join(ASSETS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{filename} generated")

make_title_svg("01", "ABOUT", "Hello, I'm", "Snehal.", "WHO I AM", "title-about.svg")
make_title_svg("02", "RECOGNITION", "Proof,", "on the record.", "HONORS & FELLOWSHIPS", "title-recognition.svg")
make_title_svg("03", "SELECTED WORK", "Analytics & AI Projects,", "tested & deployed.", "FEATURED SYSTEMS", "title-work.svg")
make_title_svg("04", "TOOLKIT", "The tools", "I analyze & build with.", "TECH STACK", "title-toolkit.svg")
make_title_svg("05", "COMMIT LOG", "A year of", "continuous building.", "CONTRIBUTIONS", "title-commits.svg")
make_title_svg("06", "CERTIFICATIONS", "Verified credentials", "and accreditations.", "SIX CREDENTIALS", "title-certifications.svg")
make_title_svg("07", "CONNECT", "Let's build", "something impactful.", "GET IN TOUCH", "title-connect.svg")

# ─── 4. ABOUT INTRO SVG ───────────────────────────────────────────────────────
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="ab-t ab-d">
  <title id="ab-t">About Snehal Ghadge</title>
  <desc id="ab-d">Data Analyst and AI Intern. B.Tech in CSE (AI/ML) at Nutan College of Engineering, Pune. Virtual Intern at Infosys Springboard and Code-A-Nova. Specialized in SQL, Python, Power BI, EDA, and predictive machine learning models.</desc>
  <defs>
    <linearGradient id="ab-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>
    <radialGradient id="ab-glow" cx="80%" cy="20%" r="70%"><stop offset="0" stop-color="#6D28D9" stop-opacity=".55"/><stop offset="1" stop-color="#3B0764" stop-opacity="0"/></radialGradient>
    <pattern id="ab-scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#EDE9FE" opacity=".03"/></pattern>
    <clipPath id="ab-c0"><rect class="ab-type" x="68" y="112" width="89" height="22" style="animation-delay:0.50s;animation-duration:0.41s;animation-timing-function:steps(6)"/></clipPath>
    <clipPath id="ab-c1"><rect class="ab-type" x="68" y="137" width="560" height="22" style="animation-delay:1.00s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
    <clipPath id="ab-c2"><rect class="ab-type" x="68" y="162" width="179" height="22" style="animation-delay:1.80s;animation-duration:0.56s;animation-timing-function:steps(17)"/></clipPath>
    <clipPath id="ab-c3"><rect class="ab-type" x="68" y="187" width="560" height="22" style="animation-delay:2.45s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
    <clipPath id="ab-c4"><rect class="ab-type" x="68" y="212" width="188" height="22" style="animation-delay:3.25s;animation-duration:0.59s;animation-timing-function:steps(18)"/></clipPath>
    <clipPath id="ab-c5"><rect class="ab-type" x="68" y="237" width="560" height="22" style="animation-delay:3.95s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
    <clipPath id="ab-c6"><rect class="ab-type" x="68" y="262" width="138" height="22" style="animation-delay:4.75s;animation-duration:0.41s;animation-timing-function:steps(12)"/></clipPath>
    <clipPath id="ab-c7"><rect class="ab-type" x="68" y="287" width="560" height="22" style="animation-delay:5.30s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
    <clipPath id="ab-c8"><rect class="ab-type" x="68" y="312" width="163" height="22" style="animation-delay:6.10s;animation-duration:0.49s;animation-timing-function:steps(15)"/></clipPath>
    <clipPath id="ab-c9"><rect class="ab-type" x="68" y="337" width="560" height="22" style="animation-delay:6.70s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
  </defs>
  <style>
    .ab-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .ab-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .ab-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .ab-type {{ transform-box: fill-box; transform-origin: left center; animation-name: ab-type; animation-fill-mode: both; }}
    .ab-card {{ animation: ab-in 1s cubic-bezier(.16,1,.3,1) both; }}
    .ab-fade {{ animation: ab-fade 1s ease both; }}
    @keyframes ab-type {{ 0% {{ transform: scaleX(0); }} 85%, 100% {{ transform: scaleX(1); }} }}
    @keyframes ab-in {{ from {{ opacity: 0; transform: translateX(24px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ab-fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ab-type, .ab-card, .ab-fade {{ animation: none; }} }}
  </style>
  <rect width="1200" height="420" rx="20" fill="url(#ab-bg)"/>
  <rect width="1200" height="420" rx="20" fill="url(#ab-glow)"/>
  <rect x=".5" y=".5" width="1199" height="419" rx="19.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>

  <!-- Terminal Window -->
  <g class="ab-fade">
    <rect x="40" y="40" width="760" height="340" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="40" y="40" width="760" height="340" rx="14" fill="url(#ab-scan)"/>
    <path d="M40 54 a14 14 0 0 1 14 -14 H786 a14 14 0 0 1 14 14 V76 H40 Z" fill="#140D24"/>
    <line x1="40" y1="76" x2="800" y2="76" stroke="#8B5CF6" stroke-opacity=".2"/>
    <circle cx="62" cy="58" r="5" fill="#EF4444"/><circle cx="80" cy="58" r="5" fill="#F59E0B"/><circle cx="98" cy="58" r="5" fill="#10B981"/>
    <text class="ab-mono" x="420" y="62" text-anchor="middle" font-size="11" letter-spacing="1.5" fill="#C4B5FD">snehal@portfolio: ~</text>
  </g>
  <g class="ab-mono" font-size="13">
    <g clip-path="url(#ab-c0)"><text x="72" y="128" fill="#A78BFA">$</text><text x="94" y="128" fill="#FFFFFF">whoami</text></g>
    <g clip-path="url(#ab-c1)"><text x="72" y="153" fill="#6D28D9">→</text><text x="94" y="153" fill="#DDD6FE">Snehal Ghadge · Data Analyst &amp; AI Intern · B.Tech AI/ML</text></g>
    <g clip-path="url(#ab-c2)"><text x="72" y="178" fill="#A78BFA">$</text><text x="94" y="178" fill="#FFFFFF">cat core_domains.txt</text></g>
    <g clip-path="url(#ab-c3)"><text x="72" y="203" fill="#6D28D9">→</text><text x="94" y="203" fill="#DDD6FE">Data Analytics (SQL, Power BI, EDA) · Predictive Modeling &amp; ML</text></g>
    <g clip-path="url(#ab-c4)"><text x="72" y="228" fill="#A78BFA">$</text><text x="94" y="228" fill="#FFFFFF">cat experience.txt</text></g>
    <g clip-path="url(#ab-c5)"><text x="72" y="253" fill="#6D28D9">→</text><text x="94" y="253" fill="#DDD6FE">Infosys Springboard (Power BI Analytics) · Code-A-Nova AI Intern</text></g>
    <g clip-path="url(#ab-c6)"><text x="72" y="278" fill="#A78BFA">$</text><text x="94" y="278" fill="#FFFFFF">ls ./projects</text></g>
    <g clip-path="url(#ab-c7)"><text x="72" y="303" fill="#6D28D9">→</text><text x="94" y="303" fill="#DDD6FE">AeroFaultAI (Telemetry ML)  AgentFlow-AI   InsightRAG   CustomerIQ</text></g>
    <g clip-path="url(#ab-c8)"><text x="72" y="328" fill="#A78BFA">$</text><text x="94" y="328" fill="#FFFFFF">echo $PRINCIPLE</text></g>
    <g clip-path="url(#ab-c9)"><text x="72" y="353" fill="#6D28D9">→</text><text x="94" y="353" fill="#DDD6FE">uncovering insights from data · delivering high-impact predictive AI</text></g>
  </g>
  <rect x="72" y="364" width="8" height="16" fill="#DDD6FE" class="ab-fade" style="animation-delay:7.4s">
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>

  <!-- Right Highlight Cards -->
  <g class="ab-card" style="animation-delay:1.2s"><g transform="translate(836 70)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#38BDF8"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#38BDF8">DATA ANALYTICS &amp; BI</text>
    <text class="ab-serif" x="22" y="58" font-size="26" font-weight="300" fill="#FFFFFF">SQL, Python &amp; Power BI</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">Pandas · NumPy · EDA · Visual Dashboards</text>
  </g></g>
  <g class="ab-card" style="animation-delay:1.7s"><g transform="translate(836 174)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#10B981"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#10B981">AI &amp; MACHINE LEARNING</text>
    <text class="ab-serif" x="22" y="58" font-size="26" font-weight="300" fill="#FFFFFF">Predictive ML &amp; RAG</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">Scikit-Learn · PyTorch · LangChain · FAISS</text>
  </g></g>
  <g class="ab-card" style="animation-delay:2.2s"><g transform="translate(836 278)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#A78BFA"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#A78BFA">TARGET ROLES</text>
    <text class="ab-serif" x="22" y="58" font-size="26" font-weight="300" fill="#FFFFFF">Data Analyst &amp; AI Intern</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">Business Analytics · ML Pipelines · Insights</text>
  </g></g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "about-intro.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)
print("about-intro.svg generated")

# ─── 5. ACHIEVEMENT MOTIF SVG ─────────────────────────────────────────────────
ach_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-labelledby="ach-title ach-desc">
  <title id="ach-title">Recognition and Honors</title>
  <desc id="ach-desc">Lenovo LEAP NextGen Scholar via AICTE; Infosys Springboard Virtual Intern (Data Analytics, Power BI &amp; GenAI); AI Intern at Code-A-Nova; 30+ GitHub projects and dashboards.</desc>
  <defs>
    <linearGradient id="ach-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>
    <radialGradient id="ach-glow" cx="80%" cy="20%" r="70%"><stop offset="0" stop-color="#7C3AED" stop-opacity=".65"/><stop offset="1" stop-color="#4C1D95" stop-opacity="0"/></radialGradient>
    <linearGradient id="ach-trace" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#EDE9FE"/><stop offset=".45" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></linearGradient>
  </defs>
  <style>
    .ach-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .ach-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .ach-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .ach-trace {{ stroke-dasharray: 600 2600; stroke-dashoffset: 3200; animation: ach-trace 8s linear infinite; }}
    @keyframes ach-trace {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ach-trace {{ display: none; }} }}
  </style>
  <rect width="1200" height="400" rx="18" fill="url(#ach-bg)"/>
  <rect width="1200" height="400" rx="18" fill="url(#ach-glow)"/>

  <!-- Grid of 4 Achievement Cards -->
  <g transform="translate(40 40)">
    <!-- Card 1 -->
    <g transform="translate(0 0)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#8B5CF6"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#A78BFA">NATIONAL SCHOLARSHIP</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">Lenovo LEAP NextGen Scholar</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Selected under AICTE Virtual Remote Initiative.</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Engineered agentic &amp; analytical workflow prototypes with structured reasoning.</text>
    </g>

    <!-- Card 2 -->
    <g transform="translate(580 0)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#38BDF8"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#38BDF8">DATA ANALYTICS INTERNSHIP</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">Infosys Springboard</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Power BI Data Pipelines &amp; Generative AI Virtual Intern.</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Built interactive Power BI dashboards, ETL pipelines &amp; prompt optimization systems.</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(0 175)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#10B981"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#10B981">AI &amp; NLP INTERNSHIP</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">Code-A-Nova AI Intern</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Intelligent AI models, NLP pipelines &amp; analytics automation.</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Document intelligence, semantic search and enterprise backend integration.</text>
    </g>

    <!-- Card 4 -->
    <g transform="translate(580 175)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#A78BFA"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#A78BFA">ANALYTICS &amp; ALGORITHMIC CODEBASE</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">30+ Repos &amp; LeetCode Problem Solver</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Exploratory data analysis, SQL problem solving &amp; Python DSA.</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">End-to-end data pipelines, predictive models &amp; web platforms.</text>
    </g>
  </g>
  <!-- Frame & Trace -->
  <rect x=".5" y=".5" width="1199" height="399" rx="17.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
  <rect class="ach-trace" x=".5" y=".5" width="1199" height="399" rx="17.5" fill="none" stroke="url(#ach-trace)" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

with open(os.path.join(ASSETS_DIR, "achievement-motif.svg"), "w", encoding="utf-8") as f:
    f.write(ach_svg)
print("achievement-motif.svg generated")

# ─── 6. TECH CONSTELLATION SVG ───────────────────────────────────────────────
tech_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" width="1200" height="560" role="img" aria-labelledby="tc-title tc-desc">
  <title id="tc-title">Snehal Ghadge Tech Stack</title>
  <desc id="tc-desc">SQL, Python, Power BI, Pandas, NumPy, Scikit-Learn, PyTorch, LangChain, FastAPI, Flask, PostgreSQL, MySQL, Redis, AWS, Docker, Git.</desc>
  <defs>
    <linearGradient id="tc-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>
    <radialGradient id="tc-glow" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#5B21B6" stop-opacity=".7"/><stop offset="1" stop-color="#24143D" stop-opacity="0"/></radialGradient>
    <linearGradient id="tc-trace" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></linearGradient>
  </defs>
  <style>
    .tc-serif{font-family:Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif}
    .tc-mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace}
    .tc-sans{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
    .tc-trace{stroke-dasharray:600 2760;stroke-dashoffset:3360;animation:tc-trace 8s linear infinite}
    @keyframes tc-trace{to{stroke-dashoffset:0}}
    @media(prefers-reduced-motion:reduce){.tc-trace{display:none}}
  </style>
  <rect width="1200" height="560" rx="18" fill="url(#tc-bg)"/>
  <rect width="1200" height="560" rx="18" fill="url(#tc-glow)"/>
  <g transform="translate(40 30)">
    <text class="tc-mono" x="0" y="22" font-size="10.5" letter-spacing="2" fill="#38BDF8">01 · DATA ANALYTICS &amp; BUSINESS INTELLIGENCE</text>
    <text class="tc-mono" x="0" y="42" font-size="11" fill="#DDD6FE">SQL (PostgreSQL, MySQL)  ·  Python (Pandas, NumPy)  ·  Power BI  ·  Tableau  ·  Excel  ·  EDA  ·  Statistical Modeling</text>
    <text class="tc-mono" x="0" y="82" font-size="10.5" letter-spacing="2" fill="#10B981">02 · AI, MACHINE LEARNING &amp; RAG</text>
    <text class="tc-mono" x="0" y="102" font-size="11" fill="#DDD6FE">Scikit-Learn  ·  PyTorch  ·  TensorFlow  ·  LangChain  ·  LangGraph  ·  FAISS  ·  HuggingFace  ·  Computer Vision (OpenCV)</text>
    <text class="tc-mono" x="0" y="142" font-size="10.5" letter-spacing="2" fill="#A78BFA">03 · DATA PIPELINES &amp; APIS</text>
    <text class="tc-mono" x="0" y="162" font-size="11" fill="#DDD6FE">FastAPI  ·  Flask  ·  Node.js  ·  REST APIs  ·  ETL Pipelines  ·  Data Cleaning  ·  Streamlit</text>
    <text class="tc-mono" x="0" y="202" font-size="10.5" letter-spacing="2" fill="#A78BFA">04 · CORE PROGRAMMING LANGUAGES</text>
    <text class="tc-mono" x="0" y="222" font-size="11" fill="#DDD6FE">Python (Advanced)  ·  SQL (Advanced)  ·  C++  ·  TypeScript  ·  JavaScript  ·  HTML5  ·  CSS3</text>
    <text class="tc-mono" x="0" y="262" font-size="10.5" letter-spacing="2" fill="#A78BFA">05 · DATABASES &amp; STORAGE</text>
    <text class="tc-mono" x="0" y="282" font-size="11" fill="#DDD6FE">PostgreSQL  ·  MySQL  ·  MongoDB  ·  SQLite  ·  Redis  ·  Vector DBs (FAISS, ChromaDB)</text>
    <text class="tc-mono" x="0" y="322" font-size="10.5" letter-spacing="2" fill="#A78BFA">06 · CLOUD &amp; DEVOPS</text>
    <text class="tc-mono" x="0" y="342" font-size="11" fill="#DDD6FE">AWS  ·  Docker  ·  GitHub Actions  ·  Linux  ·  Git  ·  CI/CD</text>
    <text class="tc-mono" x="0" y="382" font-size="10.5" letter-spacing="2" fill="#A78BFA">07 · ANALYTICS &amp; DEVELOPER TOOLS</text>
    <text class="tc-mono" x="0" y="402" font-size="11" fill="#DDD6FE">Jupyter Notebook  ·  Power BI Desktop  ·  VS Code  ·  Postman  ·  Plotly  ·  Matplotlib  ·  Seaborn</text>
  </g>
  <line x1="40" y1="56" x2="1160" y2="56" stroke="#8B5CF6" stroke-opacity=".15"/>
  <line x1="40" y1="116" x2="1160" y2="116" stroke="#8B5CF6" stroke-opacity=".15"/>
  <line x1="40" y1="176" x2="1160" y2="176" stroke="#8B5CF6" stroke-opacity=".15"/>
  <line x1="40" y1="236" x2="1160" y2="236" stroke="#8B5CF6" stroke-opacity=".15"/>
  <line x1="40" y1="296" x2="1160" y2="296" stroke="#8B5CF6" stroke-opacity=".15"/>
  <line x1="40" y1="356" x2="1160" y2="356" stroke="#8B5CF6" stroke-opacity=".15"/>
  <line x1="40" y1="416" x2="1160" y2="416" stroke="#8B5CF6" stroke-opacity=".15"/>
  <rect x=".5" y=".5" width="1199" height="559" rx="17.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
  <rect class="tc-trace" x=".5" y=".5" width="1199" height="559" rx="17.5" fill="none" stroke="url(#tc-trace)" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

with open(os.path.join(ASSETS_DIR, "tech-constellation.svg"), "w", encoding="utf-8") as f:
    f.write(tech_svg)
print("tech-constellation.svg generated")

# ─── 7. ASSEMBLE README.md ───────────────────────────────────────────────────
readme = (
    '<a href="https://snehalsportfolio2027.netlify.app">\n'
    '  <img src="assets/snehal-hero-portrait.svg" width="100%" alt="Snehal Ghadge — Data Analyst and AI Intern. Transforming complex data into actionable intelligence and building scalable ML systems.">\n'
    '</a>\n'
    '\n'
    '<p align="center">\n'
    '  <img src="assets/snehal-profile.png" width="140" height="140" alt="Snehal Ghadge — Data Analyst &amp; AI Intern" />\n'
    '</p>\n'
    '\n'
    '<p align="center">\n'
    '  <a href="https://snehalsportfolio2027.netlify.app"><img src="https://img.shields.io/badge/Portfolio-snehalsportfolio2027-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=netlify" alt="Portfolio"></a>\n'
    '  <a href="https://linkedin.com/in/snehal-g-711587312"><img src="https://img.shields.io/badge/LinkedIn-snehal--g-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=linkedin" alt="LinkedIn"></a>\n'
    '  <a href="https://leetcode.com/u/snehalghadge/"><img src="https://img.shields.io/badge/LeetCode-snehalghadge-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=leetcode" alt="LeetCode"></a>\n'
    '  <a href="mailto:snehalghadge59@gmail.com"><img src="https://img.shields.io/badge/Email-snehalghadge59@gmail.com-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=gmail" alt="Email"></a>\n'
    '  <a href="https://github.com/snehalghadge59-blip"><img src="https://img.shields.io/badge/GitHub-snehalghadge59--blip-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="GitHub"></a>\n'
    '</p>\n'
    '\n'
    '<img src="assets/title-about.svg" width="100%" alt="01 About - Hello, Im Snehal.">\n'
    '<img src="assets/about-intro.svg" width="100%" alt="About: Data Analyst and AI Intern. B.Tech in CSE (AI/ML) at Nutan College of Engineering, Pune.">\n'
    '\n'
    '<img src="assets/title-recognition.svg" width="100%" alt="02 Recognition - Proof, on the record.">\n'
    '<img src="assets/achievement-motif.svg" width="100%" alt="Lenovo LEAP NextGen Scholar via AICTE; Infosys Springboard Virtual Intern (Data Analytics, Power BI &amp; GenAI); AI Intern at Code-A-Nova; 30+ GitHub projects and dashboards.">\n'
    '\n'
    '<img src="assets/title-work.svg" width="100%" alt="03 Selected work - Products, not assignments.">\n'
    '\n'
    '<a href="https://github.com/snehalghadge59-blip/AeroFaultAI">\n'
    '  <img src="assets/project-aerofault.svg" width="100%" alt="AeroFaultAI: Real-time aerospace telemetry anomaly detection, exploratory data analysis and predictive diagnostics.">\n'
    '</a>\n'
    '<p align="center">\n'
    '  <a href="https://github.com/snehalghadge59-blip/AeroFaultAI"><img src="https://img.shields.io/badge/Repository-AeroFaultAI-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="AeroFaultAI repository"></a>\n'
    '</p>\n'
    '\n'
    '<a href="https://github.com/snehalghadge59-blip/AgentFlow-AI">\n'
    '  <img src="assets/project-agentflow.svg" width="100%" alt="AgentFlow-AI: Multi-agent orchestration framework for autonomous decision intelligence and task execution.">\n'
    '</a>\n'
    '<p align="center">\n'
    '  <a href="https://github.com/snehalghadge59-blip/AgentFlow-AI"><img src="https://img.shields.io/badge/Repository-AgentFlow--AI-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="AgentFlow-AI repository"></a>\n'
    '</p>\n'
    '\n'
    '<a href="https://github.com/snehalghadge59-blip/InsightRAG">\n'
    '  <img src="assets/project-insightrag.svg" width="100%" alt="InsightRAG: Production-grade enterprise analytics and RAG with hybrid search and semantic cache.">\n'
    '</a>\n'
    '<p align="center">\n'
    '  <a href="https://github.com/snehalghadge59-blip/InsightRAG"><img src="https://img.shields.io/badge/Repository-InsightRAG-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="InsightRAG repository"></a>\n'
    '</p>\n'
    '\n'
    '<img src="assets/title-toolkit.svg" width="100%" alt="04 Toolkit - The tools I reach for.">\n'
    '<img src="assets/tech-constellation.svg" width="100%" alt="Full tech stack listing.">\n'
    '\n'
    '<!-- Tech Stack Skill Icons with Logos -->\n'
    '<p align="center">\n'
    '  <b>📊 Data Analytics &amp; Business Intelligence</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,postgres,mysql,mongodb&amp;perline=6" alt="Python PostgreSQL MySQL MongoDB" /></a>\n'
    '</p>\n'
    '<p align="center">\n'
    '  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&amp;logo=powerbi&amp;logoColor=black" alt="Power BI" />\n'
    '  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&amp;logo=pandas&amp;logoColor=white" alt="Pandas" />\n'
    '  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&amp;logo=numpy&amp;logoColor=white" alt="NumPy" />\n'
    '  <img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&amp;logo=tableau&amp;logoColor=white" alt="Tableau" />\n'
    '</p>\n'
    '<p align="center">\n'
    '  <b>🤖 AI, Machine Learning &amp; Deep Learning</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn,fastapi,flask" alt="PyTorch TensorFlow Scikit-Learn FastAPI Flask" /></a>\n'
    '</p>\n'
    '<p align="center">\n'
    '  <b>💻 Programming Languages &amp; Core</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,cpp,c,ts,js,html,css,bash" alt="Python C++ C TypeScript JavaScript HTML5 CSS3 Bash" /></a>\n'
    '</p>\n'
    '<p align="center">\n'
    '  <b>☁️ Cloud, Databases &amp; DevOps</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=aws,docker,linux,git,github,githubactions,redis" alt="AWS Docker Linux Git GitHub GitHub Actions Redis" /></a>\n'
    '</p>\n'
    '<p align="center">\n'
    '  <b>🛠️ Developer &amp; Data Tools</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=vscode,postman,figma" alt="VS Code Postman Figma" /></a>\n'
    '</p>\n'
    '\n'
    '<img src="assets/title-commits.svg" width="100%" alt="05 Commit log - A year of continuous building.">\n'
    '\n'
    '<p align="center">\n'
    '  <img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%" alt="GitHub Contribution Grid Snake Animation" />\n'
    '</p>\n'
    '\n'
    '<p align="center">\n'
    '  <img src="https://github-readme-stats.vercel.app/api?username=snehalghadge59-blip&amp;show_icons=true&amp;hide_rank=true&amp;hide_border=true&amp;border_radius=16&amp;bg_color=0B0714&amp;title_color=DDD6FE&amp;text_color=A79FB5&amp;icon_color=A78BFA&amp;custom_title=GitHub%20at%20a%20glance" width="410" alt="GitHub stats" />\n'
    '  &nbsp;\n'
    '  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=snehalghadge59-blip&amp;layout=compact&amp;hide_border=true&amp;border_radius=16&amp;bg_color=0B0714&amp;title_color=DDD6FE&amp;text_color=A79FB5" width="370" alt="Top languages" />\n'
    '</p>\n'
    '\n'
    '<img src="assets/title-certifications.svg" width="100%" alt="06 Certifications - Verified credentials and accreditations.">\n'
    '<a href="https://snehalsportfolio2027.netlify.app">\n'
    '  <img src="assets/certifications.svg" width="100%" alt="Certifications: Lenovo LEAP NextGen Scholar, Infosys Springboard GenAI, Code-A-Nova AI Internship, Edunet Foundation AI, Data Visualization, B.Tech CSE AI/ML.">\n'
    '</a>\n'
    '\n'
    '<img src="assets/title-connect.svg" width="100%" alt="07 Connect - Lets build something worth explaining.">\n'
    '\n'
    '<p align="center">\n'
    '  <a href="mailto:snehalghadge59@gmail.com"><img src="https://img.shields.io/badge/Email-snehalghadge59@gmail.com-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=gmail" alt="Email"></a>\n'
    '  <a href="https://linkedin.com/in/snehal-g-711587312"><img src="https://img.shields.io/badge/LinkedIn-snehal--g-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=linkedin" alt="LinkedIn"></a>\n'
    '  <a href="https://leetcode.com/u/snehalghadge/"><img src="https://img.shields.io/badge/LeetCode-snehalghadge-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=leetcode" alt="LeetCode"></a>\n'
    '  <a href="https://snehalsportfolio2027.netlify.app"><img src="https://img.shields.io/badge/Portfolio-snehalsportfolio2027-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=netlify" alt="Portfolio"></a>\n'
    '</p>\n'
    '\n'
    '<a href="https://snehalsportfolio2027.netlify.app">\n'
    '  <img src="assets/footer-signature.svg" width="100%" alt="Snehal - Delivering data-driven intelligence and high-impact AI solutions.">\n'
    '</a>\n'
)

with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)

print("All Data Analyst & AI Intern assets and README successfully generated!")
