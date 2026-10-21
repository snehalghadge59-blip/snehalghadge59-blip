import os
import base64
from PIL import Image
import io

BASE_DIR = r"C:\Users\snehal\.gemini\antigravity-ide\scratch\snehalghadge59-blip"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Process portrait photo from data/source-prepped.png
photo_path = os.path.join(BASE_DIR, "data", "source-prepped.png")
if os.path.exists(photo_path):
    with Image.open(photo_path) as im:
        # ensure RGB
        rgb_im = im.convert("RGB")
        # Resize to fit portrait frame crisply (e.g. 260x340)
        rgb_im = rgb_im.resize((260, 340), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        rgb_im.save(buf, format="JPEG", quality=92)
        photo_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
else:
    photo_b64 = ""

print(f"Photo processed, b64 length: {len(photo_b64)}")

# Theme palette:
# Dark obsidian base: #0E0A1A, #150F26, #1A1330
# Deep accent: #4C1D95, #5B21B6
# Mid accent: #7C3AED, #8B5CF6, #A78BFA
# Highlight text: #EDE9FE, #F5F3FF, #FFFFFF
# Muted text: #A79FB5, #C4B5FD
# Border trace: #8B5CF6, #C084FC

# ----------------- 1. HERO PORTRAIT -----------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">Snehal Ghadge — Engineering intelligence. Designing autonomous systems.</title>
  <desc id="hero-desc">AI and Agentic Systems Engineer, Machine Learning Developer. B.Tech in Computer Science and Engineering (AI/ML), Lenovo LEAP NextGen Scholar.</desc>

  <defs>
    <radialGradient id="hero-bg" cx="72%" cy="38%" r="80%">
      <stop offset="0" stop-color="#24143D"/>
      <stop offset=".55" stop-color="#140D24"/>
      <stop offset="1" stop-color="#0B0714"/>
    </radialGradient>
    <radialGradient id="hero-light-a" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#7C3AED" stop-opacity=".75"/>
      <stop offset="1" stop-color="#7C3AED" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-light-b" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#A78BFA" stop-opacity=".25"/>
      <stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hero-name-grad" gradientUnits="userSpaceOnUse" x1="60" y1="0" x2="520" y2="0">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".55" stop-color="#DDD6FE"/>
      <stop offset="1" stop-color="#A78BFA"/>
    </linearGradient>
    <linearGradient id="hero-sheen" gradientUnits="userSpaceOnUse" x1="-260" y1="0" x2="-40" y2="0">
      <stop offset="0" stop-color="#EDE9FE" stop-opacity="0"/>
      <stop offset=".5" stop-color="#FFFFFF" stop-opacity=".9"/>
      <stop offset="1" stop-color="#EDE9FE" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;840 0;840 0" keyTimes="0;.35;1" dur="8s" begin="2.5s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="hero-scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#A78BFA" stop-opacity="0"/>
      <stop offset=".5" stop-color="#A78BFA" stop-opacity=".06"/>
      <stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#A78BFA" stop-opacity="0"/>
      <stop offset=".2" stop-color="#C4B5FD"/>
      <stop offset=".75" stop-color="#6D28D9"/>
      <stop offset="1" stop-color="#6D28D9" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-orbit-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#C4B5FD" stop-opacity=".7"/>
      <stop offset="1" stop-color="#5B21B6" stop-opacity=".05"/>
    </linearGradient>
    <pattern id="hero-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#8B5CF6" stroke-opacity=".08" stroke-width="1"/>
    </pattern>
    <radialGradient id="hero-grid-fade" cx="68%" cy="45%" r="55%">
      <stop offset="0" stop-color="#fff"/>
      <stop offset="1" stop-color="#000"/>
    </radialGradient>
    <mask id="hero-grid-mask">
      <rect width="1200" height="480" fill="url(#hero-grid-fade)"/>
    </mask>
    <clipPath id="hero-arch"><path d="M847 386 V202 A118 118 0 0 1 1083 202 V386 Z"/></clipPath>
    <radialGradient id="hero-photo-wash" cx="50%" cy="30%" r="80%">
      <stop offset="0" stop-color="#E9D5FF"/>
      <stop offset=".6" stop-color="#C084FC"/>
      <stop offset="1" stop-color="#7E22CE"/>
    </radialGradient>
    <linearGradient id="hero-photo-grade" x1="0" y1="0" x2="0" y2="1">
      <stop offset=".6" stop-color="#1E1136" stop-opacity="0"/>
      <stop offset=".85" stop-color="#150B27" stop-opacity=".6"/>
      <stop offset="1" stop-color="#0B0714" stop-opacity=".92"/>
    </linearGradient>
    <clipPath id="hero-clip"><rect width="1200" height="480" rx="20"/></clipPath>
    <linearGradient id="hero-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#EDE9FE"/><stop offset=".45" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <style>
    .hero-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .hero-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .hero-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}

    .hero-rise {{ animation: hero-rise 1.4s cubic-bezier(.16,1,.3,1) both; }}
    .hero-fade {{ animation: hero-fade 1.6s cubic-bezier(.16,1,.3,1) both; }}
    .d1 {{ animation-delay: .15s; }} .d2 {{ animation-delay: .35s; }} .d3 {{ animation-delay: .6s; }}
    .d4 {{ animation-delay: .9s; }} .d5 {{ animation-delay: 1.2s; }}

    .hero-draw {{ stroke-dasharray: 900; stroke-dashoffset: 900; animation: hero-draw 2.4s cubic-bezier(.65,0,.35,1) .9s forwards; }}
    .hero-portrait {{ animation: hero-photo 1.6s cubic-bezier(.16,1,.3,1) .5s both; }}
    .hero-trace {{ stroke-dasharray: 600 2760; stroke-dashoffset: 3360; animation: hero-trace 8s linear infinite; }}

    @keyframes hero-photo {{ from {{ opacity: 0; transform: translateY(22px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes hero-rise {{ from {{ opacity: 0; transform: translateY(18px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes hero-fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes hero-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes hero-trace {{ to {{ stroke-dashoffset: 0; }} }}

    @media (prefers-reduced-motion: reduce) {{
      .hero-rise, .hero-fade, .hero-portrait {{ animation: none; }}
      .hero-draw {{ animation: none; stroke-dashoffset: 0; }}
      .hero-trace {{ display: none; }}
    }}
  </style>

  <g clip-path="url(#hero-clip)">
    <!-- Canvas Base -->
    <rect width="1200" height="480" fill="url(#hero-bg)"/>

    <!-- Light Fields -->
    <ellipse cx="920" cy="140" rx="420" ry="300" fill="url(#hero-light-a)">
      <animateTransform attributeName="transform" type="translate" values="0 0; -50 25; 0 0" dur="20s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
    </ellipse>
    <ellipse cx="180" cy="460" rx="360" ry="220" fill="url(#hero-light-b)">
      <animateTransform attributeName="transform" type="translate" values="0 0; 60 -20; 0 0" dur="26s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
    </ellipse>

    <!-- Technical Grid -->
    <rect width="1200" height="480" fill="url(#hero-grid)" mask="url(#hero-grid-mask)"/>

    <!-- Slow scan line -->
    <rect x="0" y="-140" width="1200" height="140" fill="url(#hero-scan)">
      <animate attributeName="y" values="-140;480" dur="11s" begin="2s" repeatCount="indefinite"/>
    </rect>

    <!-- Drifting particles -->
    <g fill="#DDD6FE">
      <circle cx="560" cy="120" r="1.5"><animate attributeName="opacity" values="0;.9;0" dur="4.2s" repeatCount="indefinite"/><animate attributeName="cy" values="120;96" dur="4.2s" repeatCount="indefinite"/></circle>
      <circle cx="700" cy="70" r="1.2"><animate attributeName="opacity" values="0;.8;0" dur="5.6s" begin="1s" repeatCount="indefinite"/><animate attributeName="cy" values="70;48" dur="5.6s" begin="1s" repeatCount="indefinite"/></circle>
      <circle cx="1120" cy="380" r="1.6"><animate attributeName="opacity" values="0;.9;0" dur="4.8s" begin="2s" repeatCount="indefinite"/><animate attributeName="cy" values="380;352" dur="4.8s" begin="2s" repeatCount="indefinite"/></circle>
      <circle cx="760" cy="420" r="1.3"><animate attributeName="opacity" values="0;.7;0" dur="6s" begin=".5s" repeatCount="indefinite"/><animate attributeName="cy" values="420;396" dur="6s" begin=".5s" repeatCount="indefinite"/></circle>
    </g>

    <!-- Orbital System Circling Portrait -->
    <g transform="translate(965 232)" class="hero-fade d3">
      <circle r="212" fill="none" stroke="#8B5CF6" stroke-opacity=".12" stroke-dasharray="1 10">
        <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="140s" repeatCount="indefinite"/>
      </circle>
      <circle r="190" fill="none" stroke="url(#hero-orbit-grad)" stroke-width="1.2"/>
      <circle r="162" fill="none" stroke="#A78BFA" stroke-opacity=".18" stroke-dasharray="2 7"/>
      <g>
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="90s" repeatCount="indefinite"/>
        <circle cx="0" cy="162" r="3" fill="#EDE9FE"/>
        <circle cx="-162" cy="0" r="2.2" fill="#A78BFA" fill-opacity=".8"/>
      </g>
    </g>

    <!-- Portrait Arch -->
    <g class="hero-portrait">
      <path d="M835 398 V202 A130 130 0 0 1 1095 202 V398 Z" fill="none" stroke="#A78BFA" stroke-opacity=".3">
        <animate attributeName="stroke-opacity" values=".15;.5;.15" dur="5s" repeatCount="indefinite"/>
      </path>
      <g clip-path="url(#hero-arch)">
        <rect x="847" y="84" width="236" height="302" fill="url(#hero-photo-wash)"/>
        <image href="data:image/jpeg;base64,{photo_b64}" x="847" y="80" width="236" height="310" preserveAspectRatio="xMidYMid slice"/>
        <rect x="847" y="84" width="236" height="302" fill="url(#hero-photo-grade)"/>
      </g>
      <path class="hero-draw" d="M847 386 V202 A118 118 0 0 1 1083 202 V386 Z" fill="none" stroke="#DDD6FE" stroke-width="1.5" stroke-opacity=".6"/>
    </g>

    <!-- Left Header Typography -->
    <g class="hero-rise d1">
      <g transform="translate(60 74)">
        <circle cx="6" cy="6" r="4" fill="#10B981"/>
        <circle cx="6" cy="6" r="9" fill="none" stroke="#10B981" stroke-opacity=".4">
          <animate attributeName="r" values="6;14;6" dur="3s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0;1" dur="3s" repeatCount="indefinite"/>
        </circle>
        <text class="hero-mono" x="24" y="10" font-size="11.5" letter-spacing="2.8" fill="#C4B5FD">AVAILABLE FOR AI/ML &amp; AGENTIC SYSTEMS ROLES</text>
      </g>
    </g>

    <g class="hero-rise d2">
      <text class="hero-serif" x="58" y="162" font-size="64" font-weight="300" letter-spacing="-1.5" fill="url(#hero-name-grad)">Snehal Ghadge</text>
      <text class="hero-serif" x="58" y="162" font-size="64" font-weight="300" letter-spacing="-1.5" fill="url(#hero-sheen)">Snehal Ghadge</text>
    </g>

    <g class="hero-rise d3">
      <text class="hero-sans" x="60" y="210" font-size="20" font-weight="400" fill="#EDE9FE">AI &amp; Agentic Systems Engineer <tspan fill="#A78BFA">·</tspan> Machine Learning Developer</text>
      <text class="hero-serif" x="60" y="244" font-size="16.5" font-style="italic" fill="#C4B5FD">Building autonomous intelligence. Designing scalable reasoning workflows.</text>
    </g>

    <path class="hero-draw" d="M60 274 H740" stroke="url(#hero-rule)" stroke-width="1"/>

    <!-- Key Metadata Chips -->
    <g class="hero-rise d4" transform="translate(60 306)">
      <g transform="translate(0 0)">
        <rect width="210" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="hero-mono" x="105" y="21" text-anchor="middle" font-size="11.5" fill="#DDD6FE">🎓 B.Tech CSE (AI/ML)</text>
      </g>
      <g transform="translate(222 0)">
        <rect width="225" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="hero-mono" x="112" y="21" text-anchor="middle" font-size="11.5" fill="#DDD6FE">⭐ Lenovo LEAP Scholar</text>
      </g>
      <g transform="translate(459 0)">
        <rect width="210" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="hero-mono" x="105" y="21" text-anchor="middle" font-size="11.5" fill="#DDD6FE">💼 AI Intern @ Code-A-Nova</text>
      </g>
    </g>

    <g class="hero-rise d5" transform="translate(60 366)">
      <g transform="translate(0 0)">
        <text class="hero-serif" font-size="28" font-weight="300" fill="#FFFFFF">30+</text>
        <text class="hero-sans" y="22" font-size="12" fill="#A79FB5">public repositories</text>
      </g>
      <g transform="translate(180 0)">
        <text class="hero-serif" font-size="28" font-weight="300" fill="#FFFFFF">GenAI &amp; RAG</text>
        <text class="hero-sans" y="22" font-size="12" fill="#A79FB5">production pipelines</text>
      </g>
      <g transform="translate(360 0)">
        <text class="hero-serif" font-size="28" font-weight="300" fill="#FFFFFF">Pune, India</text>
        <text class="hero-sans" y="22" font-size="12" fill="#A79FB5">PCET's NCOE</text>
      </g>
    </g>

    <!-- Outer Frame & Trace -->
    <rect x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
    <rect class="hero-trace" x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="url(#hero-trace)" stroke-width="1.8" stroke-linecap="round"/>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "snehal-hero-portrait.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)

print("snehal-hero-portrait.svg generated")

# ----------------- SECTION TITLE BUILDER -----------------
def make_title_svg(num, title_mono, title_serif_main, title_serif_italic, subtitle_right):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="{num} {title_mono}: {title_serif_main} {title_serif_italic}">
  <defs>
    <linearGradient id="ta-line-{num}" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="1160" y2="0">
      <stop offset="0" stop-color="#A78BFA"/><stop offset=".6" stop-color="#6D28D9"/><stop offset="1" stop-color="#6D28D9" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ta-sheen-{num}" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#DDD6FE"/><stop offset=".5" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DDD6FE"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1500 0;1500 0" keyTimes="0;.4;1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="ta-pulse-{num}"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#DDD6FE" stop-opacity=".6"/><stop offset="1" stop-color="#A78BFA" stop-opacity="0"/></radialGradient>
  </defs>
  <style>
    .ta-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .ta-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .ta-in {{ animation: ta-in 1.1s cubic-bezier(.16,1,.3,1) both; }}
    .ta-d2 {{ animation-delay: .2s; }} .ta-d3 {{ animation-delay: .45s; }}
    .ta-draw {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: ta-draw 1.8s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes ta-in {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ta-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ta-in {{ animation: none; }} .ta-draw {{ animation: none; stroke-dashoffset: 0; }} }}
  </style>
  <g class="ta-in">
    <text class="ta-mono" x="40" y="34" font-size="12" letter-spacing="3" fill="#A78BFA"><tspan fill="#DDD6FE">{num}</tspan>   {title_mono}</text>
  </g>
  <g class="ta-in ta-d2">
    <text class="ta-serif" x="38" y="84" font-size="44" font-weight="300" letter-spacing="-1" fill="#F5F3FF">{title_serif_main} <tspan font-style="italic" fill="url(#ta-sheen-{num})">{title_serif_italic}</tspan></text>
  </g>
  <g class="ta-in ta-d3">
    <text class="ta-mono" x="1160" y="34" text-anchor="end" font-size="10.5" letter-spacing="2.4" fill="#A79FB5">{subtitle_right}</text>
  </g>
  <path class="ta-draw" d="M40 106 H1160" stroke="url(#ta-line-{num})" stroke-width="1"/>
  <circle cx="40" cy="106" r="7" fill="url(#ta-pulse-{num})" opacity="0">
    <animate attributeName="cx" values="40;1160" dur="6s" begin="2.3s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>
    <animate attributeName="opacity" values="0;1;0" keyTimes="0;.15;1" dur="6s" begin="2.3s" repeatCount="indefinite"/>
  </circle>
</svg>'''

titles = [
    ("01", "ABOUT", "Hello, I'm", "Snehal.", "WHO I AM", "title-about.svg"),
    ("02", "RECOGNITION", "Proof, on the", "record.", "HONORS & SCHOLARS", "title-recognition.svg"),
    ("03", "SELECTED WORK", "Products, not", "assignments.", "FLAGSHIP REPOSITORIES", "title-work.svg"),
    ("04", "TOOLKIT", "The tools I", "reach for.", "CORE CAPABILITIES", "title-toolkit.svg"),
    ("05", "COMMIT LOG", "A year of", "continuous building.", "DAILY CADENCE", "title-commits.svg"),
    ("06", "CERTIFICATIONS", "Verified credentials &", "accreditations.", "SIX CREDENTIALS", "title-certifications.svg"),
    ("07", "CONNECT", "Let's build something", "worth explaining.", "GET IN TOUCH", "title-connect.svg"),
]

for num, mono, main, ital, right, fname in titles:
    with open(os.path.join(ASSETS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(make_title_svg(num, mono, main, ital, right))
    print(f"{fname} generated")

# ----------------- 2. ABOUT INTRO TERMINAL + 3 CARDS -----------------
about_intro_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="ab-t ab-d">
  <title id="ab-t">About Snehal Ghadge</title>
  <desc id="ab-d">AI and Agentic Systems Engineer, Machine Learning Developer. B.Tech in CSE (AI/ML) at Nutan College of Engineering, Pune. Intern at Code-A-Nova and Infosys Springboard. Primary language Python and C++; drawn to autonomous agents, RAG architectures, and distributed systems.</desc>
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
    .ab-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .ab-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .ab-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .ab-type { transform-box: fill-box; transform-origin: left center; animation-name: ab-type; animation-fill-mode: both; }
    .ab-card { animation: ab-in 1s cubic-bezier(.16,1,.3,1) both; }
    .ab-fade { animation: ab-fade 1s ease both; }
    @keyframes ab-type { 0% { transform: scaleX(0); } 85%, 100% { transform: scaleX(1); } }
    @keyframes ab-in { from { opacity: 0; transform: translateX(24px); } to { opacity: 1; transform: none; } }
    @keyframes ab-fade { from { opacity: 0; } to { opacity: 1; } }
    @media (prefers-reduced-motion: reduce) { .ab-type, .ab-card, .ab-fade { animation: none; } }
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
    <g clip-path="url(#ab-c1)"><text x="72" y="153" fill="#6D28D9">→</text><text x="94" y="153" fill="#DDD6FE">Snehal Ghadge · AI &amp; Agentic Systems Engineer · B.Tech AI/ML</text></g>
    <g clip-path="url(#ab-c2)"><text x="72" y="178" fill="#A78BFA">$</text><text x="94" y="178" fill="#FFFFFF">cat education.txt</text></g>
    <g clip-path="url(#ab-c3)"><text x="72" y="203" fill="#6D28D9">→</text><text x="94" y="203" fill="#DDD6FE">B.Tech CSE (AI &amp; ML) · PCET's Nutan College of Engineering, Pune</text></g>
    <g clip-path="url(#ab-c4)"><text x="72" y="228" fill="#A78BFA">$</text><text x="94" y="228" fill="#FFFFFF">cat experience.txt</text></g>
    <g clip-path="url(#ab-c5)"><text x="72" y="253" fill="#6D28D9">→</text><text x="94" y="253" fill="#DDD6FE">AI Intern @ Code-A-Nova · Infosys Springboard Virtual Intern</text></g>
    <g clip-path="url(#ab-c6)"><text x="72" y="278" fill="#A78BFA">$</text><text x="94" y="278" fill="#FFFFFF">ls ./shipped</text></g>
    <g clip-path="url(#ab-c7)"><text x="72" y="303" fill="#6D28D9">→</text><text x="94" y="303" fill="#DDD6FE">AgentFlow-AI   InsightRAG   AeroFaultAI   devpulse-visualizer</text></g>
    <g clip-path="url(#ab-c8)"><text x="72" y="328" fill="#A78BFA">$</text><text x="94" y="328" fill="#FFFFFF">echo $PRINCIPLE</text></g>
    <g clip-path="url(#ab-c9)"><text x="72" y="353" fill="#6D28D9">→</text><text x="94" y="353" fill="#DDD6FE">autonomous agents that reason · pipelines that deliver real-world impact</text></g>
  </g>
  <rect x="72" y="364" width="8" height="16" fill="#DDD6FE" class="ab-fade" style="animation-delay:7.4s">
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>

  <!-- Right Highlight Cards -->
  <g class="ab-card" style="animation-delay:1.2s"><g transform="translate(836 70)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#8B5CF6"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#A78BFA">PRIMARY LANGUAGE</text>
    <text class="ab-serif" x="22" y="58" font-size="28" font-weight="300" fill="#FFFFFF">Python &amp; C++</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">Core AI/ML · LeetCode DSA · Fast APIs</text>
  </g></g>
  <g class="ab-card" style="animation-delay:1.7s"><g transform="translate(836 174)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#8B5CF6"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#A78BFA">WHERE AI LIVES</text>
    <text class="ab-serif" x="22" y="58" font-size="28" font-weight="300" fill="#FFFFFF">Agentic AI &amp; RAG</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">LangChain · LangGraph · FAISS · PyTorch</text>
  </g></g>
  <g class="ab-card" style="animation-delay:2.2s"><g transform="translate(836 278)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#8B5CF6"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#A78BFA">DRAWN TO</text>
    <text class="ab-serif" x="22" y="58" font-size="28" font-weight="300" fill="#FFFFFF">Autonomous Systems</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">distributed workflows · LLM Ops · telemetry</text>
  </g></g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "about-intro.svg"), "w", encoding="utf-8") as f:
    f.write(about_intro_svg)
print("about-intro.svg generated")

# ----------------- 3. RECOGNITION MOTIF -----------------
achievement_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-labelledby="ach-title ach-desc">
  <title id="ach-title">Recognition and Honors</title>
  <desc id="ach-desc">Lenovo LEAP NextGen Scholar via AICTE; Infosys Springboard Virtual Intern; AI Intern at Code-A-Nova; Certified AI Specialist in Generative AI and RAG architectures; 30+ GitHub projects; LeetCode algorithmic problem solver.</desc>
  <defs>
    <linearGradient id="ach-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>
    <radialGradient id="ach-glow" cx="80%" cy="20%" r="70%"><stop offset="0" stop-color="#7C3AED" stop-opacity=".65"/><stop offset="1" stop-color="#4C1D95" stop-opacity="0"/></radialGradient>
    <linearGradient id="ach-trace" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#EDE9FE"/><stop offset=".45" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></linearGradient>
  </defs>
  <style>
    .ach-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .ach-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .ach-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .ach-trace { stroke-dasharray: 600 2600; stroke-dashoffset: 3200; animation: ach-trace 8s linear infinite; }
    @keyframes ach-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .ach-trace { display: none; } }
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
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Engineered 2 agentic workflow prototypes applying multi-stage reasoning.</text>
    </g>

    <!-- Card 2 -->
    <g transform="translate(580 0)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#8B5CF6"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#A78BFA">VIRTUAL INDUSTRY INTERNSHIP</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">Infosys Springboard</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Generative AI &amp; Agentic Systems Intern (Jun 2026 – Jul 2026).</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Built production GenAI workflows, prompt optimization &amp; RAG architectures.</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(0 175)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#8B5CF6"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#A78BFA">AI &amp; NLP INTERNSHIP</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">Code-A-Nova AI Intern</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Intelligent AI models, NLP pipelines &amp; web automation systems.</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Document intelligence, semantic search and enterprise backend integration.</text>
    </g>

    <!-- Card 4 -->
    <g transform="translate(580 175)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#8B5CF6"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#A78BFA">ALGORITHMIC SKILLS &amp; CODEBASE</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">30+ Repos &amp; LeetCode Solver</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Active competitive problem solving across DSA in Python &amp; C++.</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Full-stack apps, autonomous agents, and end-to-end data pipelines.</text>
    </g>
  </g>

  <!-- Outer Frame & Trace -->
  <rect x=".5" y=".5" width="1199" height="399" rx="17.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
  <rect class="ach-trace" x=".5" y=".5" width="1199" height="399" rx="17.5" fill="none" stroke="url(#ach-trace)" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

with open(os.path.join(ASSETS_DIR, "achievement-motif.svg"), "w", encoding="utf-8") as f:
    f.write(achievement_svg)
print("achievement-motif.svg generated")

# ----------------- 4. PROJECT CARDS (AgentFlow, InsightRAG, AeroFault) -----------------
def make_project_card(pnum, tag, title, tagline, built_line, stat1_val, stat1_lbl, stat2_val, stat2_lbl, stat3_val, stat3_lbl, chips, diagram_svg, filename):
    chip_elements = []
    x_offset = 56
    for i, chip in enumerate(chips):
        w = max(50, len(chip) * 9 + 24)
        chip_elements.append(f'''<g class="p-chip" style="animation-delay:{1.0 + i*0.12:.2f}s">
          <rect x="{x_offset}" y="314" width="{w}" height="26" rx="13" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".35"/>
          <text class="p-mono" x="{x_offset + w/2}" y="331" text-anchor="middle" font-size="11.5" fill="#DDD6FE">{chip}</text>
        </g>''')
        x_offset += w + 10
    chips_html = "\\n".join(chip_elements)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="{filename}-t">
  <title id="{filename}-t">{title}: {tagline}</title>
  <defs>
    <linearGradient id="{filename}-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>
    <radialGradient id="{filename}-glow" cx="82%" cy="30%" r="55%"><stop offset="0" stop-color="#7C3AED" stop-opacity=".7"/><stop offset="1" stop-color="#3B0764" stop-opacity="0"/></radialGradient>
    <pattern id="{filename}-grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#8B5CF6" stroke-opacity=".08"/></pattern>
    <clipPath id="{filename}-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="{filename}-trace" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></linearGradient>
  </defs>
  <style>
    .p-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .p-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .p-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .p-in {{ animation: p-in 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .p-d1 {{ animation-delay: .15s; }} .p-d2 {{ animation-delay: .4s; }}
    .p-draw {{ stroke-dasharray: 600; stroke-dashoffset: 600; animation: p-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    .p-trace {{ stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: p-trace 7s linear infinite; }}
    @keyframes p-in {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes p-trace {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p-in {{ animation: none; }} .p-draw {{ animation: none; stroke-dashoffset: 0; }} .p-trace {{ display: none; }} }}
  </style>
  <g clip-path="url(#{filename}-clip)">
    <rect width="1200" height="370" fill="url(#{filename}-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#{filename}-grid)"/>
    <rect width="1200" height="370" fill="url(#{filename}-glow)"/>
    <g class="p-in p-d1">
      <text class="p-mono" x="56" y="62" font-size="12" letter-spacing="2.6" fill="#A78BFA">{tag}</text>
      <text class="p-serif" x="54" y="126" font-size="52" font-weight="300" letter-spacing="-1.5" fill="#FFFFFF">{title}</text>
      <text class="p-sans" x="56" y="166" font-size="17" fill="#C4B5FD">{tagline}</text>
      <text class="p-mono" x="56" y="200" font-size="12.5" fill="#DDD6FE"><tspan fill="#A78BFA">BUILT ›</tspan> {built_line}</text>
      <line class="p-draw" x1="56" y1="226" x2="680" y2="226" stroke="#8B5CF6" stroke-opacity=".3"/>
      <g transform="translate(56 266)"><text class="p-serif" font-size="34" font-weight="300" fill="#FFFFFF">{stat1_val}</text><text class="p-sans" y="24" font-size="12.5" fill="#A79FB5">{stat1_lbl}</text></g>
      <g transform="translate(261 266)"><text class="p-serif" font-size="34" font-weight="300" fill="#FFFFFF">{stat2_val}</text><text class="p-sans" y="24" font-size="12.5" fill="#A79FB5">{stat2_lbl}</text></g>
      <g transform="translate(466 266)"><text class="p-serif" font-size="34" font-weight="300" fill="#FFFFFF">{stat3_val}</text><text class="p-sans" y="24" font-size="12.5" fill="#A79FB5">{stat3_lbl}</text></g>
      {chips_html}
    </g>
    <!-- Right Diagram Area -->
    <g class="p-in p-d2">
      {diagram_svg}
    </g>
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
    <rect class="p-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#{filename}-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>'''
    return svg

# AgentFlow Diagram
agentflow_diag = '''<g transform="translate(780 40)">
  <rect x="0" y="0" width="370" height="290" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".35"/>
  <!-- Central Planner Node -->
  <g transform="translate(185 60)">
    <circle r="36" fill="#1C1236" stroke="#C084FC" stroke-width="1.5"/>
    <text class="p-mono" text-anchor="middle" y="4" font-size="11" fill="#FFFFFF">PLANNER</text>
  </g>
  <!-- Executor Node -->
  <g transform="translate(80 180)">
    <circle r="32" fill="#1C1236" stroke="#8B5CF6" stroke-width="1.2"/>
    <text class="p-mono" text-anchor="middle" y="4" font-size="10.5" fill="#DDD6FE">EXECUTOR</text>
  </g>
  <!-- Critic Node -->
  <g transform="translate(290 180)">
    <circle r="32" fill="#1C1236" stroke="#8B5CF6" stroke-width="1.2"/>
    <text class="p-mono" text-anchor="middle" y="4" font-size="10.5" fill="#DDD6FE">VERIFIER</text>
  </g>
  <!-- Tool Execution Box -->
  <g transform="translate(115 240)">
    <rect width="140" height="36" rx="8" fill="#140D24" stroke="#A78BFA" stroke-opacity=".4"/>
    <text class="p-mono" x="70" y="22" text-anchor="middle" font-size="10" fill="#C4B5FD">TOOL INVOCATION</text>
  </g>
  <!-- Connecting lines -->
  <line x1="160" y1="85" x2="105" y2="152" stroke="#8B5CF6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <line x1="210" y1="85" x2="265" y2="152" stroke="#8B5CF6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <line x1="105" y1="205" x2="155" y2="240" stroke="#C084FC" stroke-width="1.5"/>
  <line x1="265" y1="205" x2="215" y2="240" stroke="#C084FC" stroke-width="1.5"/>
  <circle cx="185" cy="180" r="4" fill="#10B981">
    <animate attributeName="opacity" values=".3;1;.3" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text class="p-mono" x="185" y="200" text-anchor="middle" font-size="9" fill="#10B981">DISPATCH ACTIVE</text>
</g>'''

agentflow_svg = make_project_card(
    "01", "01 · AUTONOMOUS AGENTS · MULTI-STAGE REASONING · 2026",
    "AgentFlow-AI", "Multi-agent orchestration framework for autonomous task execution.",
    "Dynamic state-graph, automated sub-task decomposition, and tool delegation",
    "15+", "tools integrated",
    "<1.2s", "agent dispatch latency",
    "99.4%", "workflow reliability",
    ["Python", "LangGraph", "FastAPI", "Redis", "Docker Compose"],
    agentflow_diag, "project-agentflow"
)
with open(os.path.join(ASSETS_DIR, "project-agentflow.svg"), "w", encoding="utf-8") as f:
    f.write(agentflow_svg)
print("project-agentflow.svg generated")

# InsightRAG Diagram
insightrag_diag = '''<g transform="translate(780 40)">
  <rect x="0" y="0" width="370" height="290" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".35"/>
  <!-- Document Ingestion Layers -->
  <g transform="translate(30 30)">
    <rect width="310" height="42" rx="8" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".3"/>
    <text class="p-mono" x="155" y="26" text-anchor="middle" font-size="11" fill="#FFFFFF">1. Chunking &amp; Hybrid Ingestion</text>
  </g>
  <g transform="translate(30 90)">
    <rect width="145" height="46" rx="8" fill="#140D24" stroke="#A78BFA" stroke-opacity=".3"/>
    <text class="p-mono" x="72" y="22" text-anchor="middle" font-size="10" fill="#DDD6FE">Vector Index</text>
    <text class="p-mono" x="72" y="38" text-anchor="middle" font-size="9" fill="#A79FB5">FAISS Dense</text>
    
    <rect x="165" width="145" height="46" rx="8" fill="#140D24" stroke="#A78BFA" stroke-opacity=".3"/>
    <text class="p-mono" x="237" y="22" text-anchor="middle" font-size="10" fill="#DDD6FE">Sparse Index</text>
    <text class="p-mono" x="237" y="38" text-anchor="middle" font-size="9" fill="#A79FB5">BM25 Keyword</text>
  </g>
  <g transform="translate(30 156)">
    <rect width="310" height="42" rx="8" fill="#1C1236" stroke="#C084FC" stroke-opacity=".4"/>
    <text class="p-mono" x="155" y="26" text-anchor="middle" font-size="11" fill="#FFFFFF">2. Reranking &amp; Semantic Cache</text>
  </g>
  <g transform="translate(30 218)">
    <rect width="310" height="46" rx="8" fill="#140D24" stroke="#10B981" stroke-opacity=".4"/>
    <text class="p-mono" x="155" y="24" text-anchor="middle" font-size="11" fill="#10B981">3. Grounded LLM Response</text>
    <text class="p-mono" x="155" y="38" text-anchor="middle" font-size="9" fill="#A79FB5">Zero Hallucination Guardrail</text>
  </g>
</g>'''

insightrag_svg = make_project_card(
    "02", "02 · ENTERPRISE RAG · HYBRID SEARCH · VECTOR DBS · 2026",
    "InsightRAG", "Production-grade enterprise RAG with semantic cache and hybrid search.",
    "Hybrid vector & BM25 retrieval, document re-ranking, and low-latency cache",
    "10k+", "chunks indexed",
    "94.8%", "retrieval precision",
    "4x", "faster response time",
    ["Python", "LlamaIndex", "FAISS", "LangChain", "Streamlit"],
    insightrag_diag, "project-insightrag"
)
with open(os.path.join(ASSETS_DIR, "project-insightrag.svg"), "w", encoding="utf-8") as f:
    f.write(insightrag_svg)
print("project-insightrag.svg generated")

# AeroFaultAI Diagram
aerofault_diag = '''<g transform="translate(780 40)">
  <rect x="0" y="0" width="370" height="290" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".35"/>
  <text class="p-mono" x="30" y="36" font-size="11" letter-spacing="1.5" fill="#A78BFA">LIVE TELEMETRY STREAM</text>
  <!-- Telemetry waveform -->
  <path d="M30 110 L80 110 L100 85 L120 135 L140 110 L190 110 L210 60 L230 160 L250 110 L300 110 L340 110" fill="none" stroke="#8B5CF6" stroke-width="2"/>
  <circle cx="220" cy="110" r="28" fill="#EF4444" fill-opacity=".15" stroke="#EF4444" stroke-width="1.2">
    <animate attributeName="r" values="20;32;20" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text class="p-mono" x="220" y="50" text-anchor="middle" font-size="10" fill="#EF4444">FAULT SPIKE DETECTED</text>
  <!-- Diagnostics box -->
  <g transform="translate(30 190)">
    <rect width="310" height="74" rx="10" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".3"/>
    <text class="p-mono" x="18" y="26" font-size="11" fill="#FFFFFF">STATUS: Component #4 Failure Risk</text>
    <text class="p-mono" x="18" y="46" font-size="10.5" fill="#DDD6FE">Confidence: 98.2% · Time to Failure: 48h</text>
    <text class="p-mono" x="18" y="64" font-size="10" fill="#10B981">Action: Auto-Ticket Dispatched to Maintenance</text>
  </g>
</g>'''

aerofault_svg = make_project_card(
    "03", "03 · PREDICTIVE ML · TIME-SERIES TELEMETRY · 2026",
    "AeroFaultAI", "Real-time aerospace telemetry anomaly detection and predictive diagnostics.",
    "Multi-sensor time-series modeling, anomaly classification, and automated alerts",
    "98.2%", "anomaly F1-score",
    "<50ms", "inference latency",
    "100k+", "telemetry records",
    ["Python", "PyTorch", "Scikit-Learn", "FastAPI", "Plotly"],
    aerofault_diag, "project-aerofault"
)
with open(os.path.join(ASSETS_DIR, "project-aerofault.svg"), "w", encoding="utf-8") as f:
    f.write(aerofault_svg)
print("project-aerofault.svg generated")

# ----------------- 5. TECH CONSTELLATION -----------------
tech_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="tc-title tc-desc">
  <title id="tc-title">Snehal's Tech Stack</title>
  <desc id="tc-desc">Languages: Python (primary), C++, TypeScript, JavaScript, SQL. AI/ML and RAG: PyTorch, LangChain, LangGraph, LlamaIndex, FAISS, Transformers. Backend: FastAPI, Flask, Node.js, Express, REST APIs. Data: PostgreSQL, MongoDB, MySQL, Redis, Vector DBs. Cloud and DevOps: AWS, Docker, Git, GitHub Actions, Linux. Tools: Postman, PowerBI, Streamlit, Jupyter.</desc>
  <defs>
    <linearGradient id="tc-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>
    <radialGradient id="tc-glow" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#5B21B6" stop-opacity=".7"/><stop offset="1" stop-color="#24143D" stop-opacity="0"/></radialGradient>
    <linearGradient id="tc-trace" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></linearGradient>
  </defs>
  <style>
    .tc-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .tc-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .tc-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .tc-trace { stroke-dasharray: 600 2760; stroke-dashoffset: 3360; animation: tc-trace 8s linear infinite; }
    @keyframes tc-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .tc-trace { display: none; } }
  </style>
  <rect width="1200" height="480" rx="18" fill="url(#tc-bg)"/>
  <rect width="1200" height="480" rx="18" fill="url(#tc-glow)"/>

  <!-- 6 Categorized Panels -->
  <g transform="translate(40 40)">
    <!-- 1. Languages -->
    <g transform="translate(0 0)">
      <rect width="350" height="180" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="180" rx="1.5" fill="#8B5CF6"/>
      <text class="tc-mono" x="22" y="28" font-size="10.5" letter-spacing="2" fill="#A78BFA">01 · PROGRAMMING LANGUAGES</text>
      <text class="tc-serif" x="22" y="60" font-size="22" fill="#FFFFFF">Python &amp; C++</text>
      <text class="tc-sans" x="22" y="86" font-size="12.5" fill="#C4B5FD">Primary languages for AI, Machine Learning, algorithm design and backend microservices.</text>
      <text class="tc-mono" x="22" y="124" font-size="11" fill="#DDD6FE">Python · C++ · TypeScript · JavaScript · SQL</text>
    </g>

    <!-- 2. AI & RAG -->
    <g transform="translate(385 0)">
      <rect width="350" height="180" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="180" rx="1.5" fill="#8B5CF6"/>
      <text class="tc-mono" x="22" y="28" font-size="10.5" letter-spacing="2" fill="#A78BFA">02 · AI, GENAI &amp; RAG</text>
      <text class="tc-serif" x="22" y="60" font-size="22" fill="#FFFFFF">Agentic &amp; Reasoning AI</text>
      <text class="tc-sans" x="22" y="86" font-size="12.5" fill="#C4B5FD">Multi-agent frameworks, hybrid retrieval RAG, semantic caching, vector search &amp; LLM fine-tuning.</text>
      <text class="tc-mono" x="22" y="124" font-size="11" fill="#DDD6FE">PyTorch · LangChain · LangGraph · FAISS · LlamaIndex</text>
    </g>

    <!-- 3. Backend -->
    <g transform="translate(770 0)">
      <rect width="350" height="180" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="180" rx="1.5" fill="#8B5CF6"/>
      <text class="tc-mono" x="22" y="28" font-size="10.5" letter-spacing="2" fill="#A78BFA">03 · BACKEND &amp; APIS</text>
      <text class="tc-serif" x="22" y="60" font-size="22" fill="#FFFFFF">Distributed Backends</text>
      <text class="tc-sans" x="22" y="86" font-size="12.5" fill="#C4B5FD">Asynchronous high-throughput microservices, rate-limiters, event systems &amp; REST APIs.</text>
      <text class="tc-mono" x="22" y="124" font-size="11" fill="#DDD6FE">FastAPI · Flask · Node.js · Express · REST · Redis</text>
    </g>

    <!-- 4. Data & Storage -->
    <g transform="translate(0 210)">
      <rect width="350" height="180" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="180" rx="1.5" fill="#8B5CF6"/>
      <text class="tc-mono" x="22" y="28" font-size="10.5" letter-spacing="2" fill="#A78BFA">04 · DATA &amp; STORAGE</text>
      <text class="tc-serif" x="22" y="60" font-size="22" fill="#FFFFFF">Relational &amp; Vector</text>
      <text class="tc-sans" x="22" y="86" font-size="12.5" fill="#C4B5FD">Structured SQL, document stores, in-memory caching and high-dimensional vector databases.</text>
      <text class="tc-mono" x="22" y="124" font-size="11" fill="#DDD6FE">PostgreSQL · MongoDB · MySQL · Redis · Vector DBs</text>
    </g>

    <!-- 5. Cloud & DevOps -->
    <g transform="translate(385 210)">
      <rect width="350" height="180" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="180" rx="1.5" fill="#8B5CF6"/>
      <text class="tc-mono" x="22" y="28" font-size="10.5" letter-spacing="2" fill="#A78BFA">05 · CLOUD &amp; DEVOPS</text>
      <text class="tc-serif" x="22" y="60" font-size="22" fill="#FFFFFF">Containerized Deployments</text>
      <text class="tc-sans" x="22" y="86" font-size="12.5" fill="#C4B5FD">Automated CI/CD pipelines, container orchestration, Linux environments &amp; cloud hosting.</text>
      <text class="tc-mono" x="22" y="124" font-size="11" fill="#DDD6FE">AWS · Docker · GitHub Actions · Linux · Git</text>
    </g>

    <!-- 6. Developer Tools -->
    <g transform="translate(770 210)">
      <rect width="350" height="180" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="180" rx="1.5" fill="#8B5CF6"/>
      <text class="tc-mono" x="22" y="28" font-size="10.5" letter-spacing="2" fill="#A78BFA">06 · TOOLS &amp; ANALYTICS</text>
      <text class="tc-serif" x="22" y="60" font-size="22" fill="#FFFFFF">Developer Productivity</text>
      <text class="tc-sans" x="22" y="86" font-size="12.5" fill="#C4B5FD">Interactive dashboards, API testing suites, telemetry visualization &amp; data analysis.</text>
      <text class="tc-mono" x="22" y="124" font-size="11" fill="#DDD6FE">Streamlit · PowerBI · Jupyter · Postman · Plotly</text>
    </g>
  </g>

  <rect x=".5" y=".5" width="1199" height="479" rx="17.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
  <rect class="tc-trace" x=".5" y=".5" width="1199" height="479" rx="17.5" fill="none" stroke="url(#tc-trace)" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

with open(os.path.join(ASSETS_DIR, "tech-constellation.svg"), "w", encoding="utf-8") as f:
    f.write(tech_svg)
print("tech-constellation.svg generated")

# ----------------- 6. CERTIFICATIONS SVG -----------------
cert_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="1200" height="380" role="img" aria-labelledby="ce-t ce-d">
  <title id="ce-t">Snehal Ghadge's Certifications</title>
  <desc id="ce-d">Lenovo LEAP NextGen Scholar (AICTE); Infosys Springboard Generative AI and Agentic Systems; Code-A-Nova Artificial Intelligence Internship; Edunet Foundation AI and Analytics; Data Visualization and Analytics; B.Tech Computer Science and Engineering.</desc>
  <defs>
    <linearGradient id="ce-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>
    <radialGradient id="ce-glow" cx="15%" cy="100%" r="70%"><stop offset="0" stop-color="#6D28D9" stop-opacity=".5"/><stop offset="1" stop-color="#3B0764" stop-opacity="0"/></radialGradient>
    <linearGradient id="ce-edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></linearGradient>
  </defs>
  <style>
    .ce-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .ce-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .ce-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .ce-edge { stroke-dasharray: 600 2500; stroke-dashoffset: 3100; animation: ce-edge 8s linear infinite; }
    @keyframes ce-edge { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .ce-edge { display: none; } }
  </style>
  <rect width="1200" height="380" rx="18" fill="url(#ce-bg)"/>
  <rect width="1200" height="380" rx="18" fill="url(#ce-glow)"/>

  <!-- 6 Cert Cards Grid (3x2) -->
  <g transform="translate(40 40)">
    <!-- Cert 1 -->
    <g transform="translate(0 0)">
      <rect width="350" height="135" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="135" rx="1.5" fill="#8B5CF6"/>
      <text class="ce-mono" x="20" y="28" font-size="10.5" letter-spacing="1.8" fill="#A78BFA">AICTE &amp; LENOVO</text>
      <text class="ce-serif" x="20" y="58" font-size="20" fill="#FFFFFF">Lenovo LEAP NextGen Scholar</text>
      <text class="ce-sans" x="20" y="84" font-size="12" fill="#C4B5FD">Selected national scholar for AI and multi-stage agentic workflow prototyping.</text>
      <text class="ce-mono" x="20" y="112" font-size="10" fill="#10B981">✓ VERIFIED CREDENTIAL</text>
    </g>

    <!-- Cert 2 -->
    <g transform="translate(385 0)">
      <rect width="350" height="135" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="135" rx="1.5" fill="#8B5CF6"/>
      <text class="ce-mono" x="20" y="28" font-size="10.5" letter-spacing="1.8" fill="#A78BFA">INFOSYS SPRINGBOARD</text>
      <text class="ce-serif" x="20" y="58" font-size="20" fill="#FFFFFF">Generative AI &amp; Agentic Systems</text>
      <text class="ce-sans" x="20" y="84" font-size="12" fill="#C4B5FD">Advanced training and virtual internship in GenAI, RAG, and LLM applications.</text>
      <text class="ce-mono" x="20" y="112" font-size="10" fill="#10B981">✓ VERIFIED CREDENTIAL</text>
    </g>

    <!-- Cert 3 -->
    <g transform="translate(770 0)">
      <rect width="350" height="135" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="135" rx="1.5" fill="#8B5CF6"/>
      <text class="ce-mono" x="20" y="28" font-size="10.5" letter-spacing="1.8" fill="#A78BFA">CODE-A-NOVA</text>
      <text class="ce-serif" x="20" y="58" font-size="20" fill="#FFFFFF">AI &amp; NLP Systems Internship</text>
      <text class="ce-sans" x="20" y="84" font-size="12" fill="#C4B5FD">3-month industrial AI internship developing intelligent NLP automation systems.</text>
      <text class="ce-mono" x="20" y="112" font-size="10" fill="#10B981">✓ VERIFIED CREDENTIAL</text>
    </g>

    <!-- Cert 4 -->
    <g transform="translate(0 165)">
      <rect width="350" height="135" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="135" rx="1.5" fill="#8B5CF6"/>
      <text class="ce-mono" x="20" y="28" font-size="10.5" letter-spacing="1.8" fill="#A78BFA">EDUNET FOUNDATION</text>
      <text class="ce-serif" x="20" y="58" font-size="20" fill="#FFFFFF">Artificial Intelligence &amp; Analytics</text>
      <text class="ce-sans" x="20" y="84" font-size="12" fill="#C4B5FD">Hands-on applied machine learning algorithms and predictive data pipelines.</text>
      <text class="ce-mono" x="20" y="112" font-size="10" fill="#10B981">✓ VERIFIED CREDENTIAL</text>
    </g>

    <!-- Cert 5 -->
    <g transform="translate(385 165)">
      <rect width="350" height="135" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="135" rx="1.5" fill="#8B5CF6"/>
      <text class="ce-mono" x="20" y="28" font-size="10.5" letter-spacing="1.8" fill="#A78BFA">BUSINESS INTELLIGENCE</text>
      <text class="ce-serif" x="20" y="58" font-size="20" fill="#FFFFFF">Data Visualization &amp; BI</text>
      <text class="ce-sans" x="20" y="84" font-size="12" fill="#C4B5FD">Interactive dashboards, telemetry tracking and data visualization pipelines.</text>
      <text class="ce-mono" x="20" y="112" font-size="10" fill="#10B981">✓ VERIFIED CREDENTIAL</text>
    </g>

    <!-- Cert 6 -->
    <g transform="translate(770 165)">
      <rect width="350" height="135" rx="12" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="135" rx="1.5" fill="#8B5CF6"/>
      <text class="ce-mono" x="20" y="28" font-size="10.5" letter-spacing="1.8" fill="#A78BFA">ACADEMIC DEGREE</text>
      <text class="ce-serif" x="20" y="58" font-size="20" fill="#FFFFFF">B.Tech CSE (AI &amp; ML)</text>
      <text class="ce-sans" x="20" y="84" font-size="12" fill="#C4B5FD">PCET's Nutan College of Engineering, Pune. Specialization in Artificial Intelligence.</text>
      <text class="ce-mono" x="20" y="112" font-size="10" fill="#10B981">✓ CANDIDATE IN GOOD STANDING</text>
    </g>
  </g>

  <rect x=".5" y=".5" width="1199" height="379" rx="17.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
  <rect class="ce-edge" x=".5" y=".5" width="1199" height="379" rx="17.5" fill="none" stroke="url(#ce-edge)" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

with open(os.path.join(ASSETS_DIR, "certifications.svg"), "w", encoding="utf-8") as f:
    f.write(cert_svg)
print("certifications.svg generated")

# ----------------- 7. FOOTER SIGNATURE -----------------
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 230" width="1200" height="230" role="img" aria-labelledby="sig-title">
  <title id="sig-title">Snehal — Engineering intelligence that creates real-world impact.</title>
  <defs>
    <linearGradient id="sig-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B0714"/><stop offset="1" stop-color="#140D24"/></linearGradient>
    <radialGradient id="sig-glow" cx="50%" cy="100%" r="70%"><stop offset="0" stop-color="#6D28D9" stop-opacity=".7"/><stop offset="1" stop-color="#3B0764" stop-opacity="0"/></radialGradient>
    <linearGradient id="sig-line" gradientUnits="userSpaceOnUse" x1="100" y1="0" x2="1100" y2="0">
      <stop offset="0" stop-color="#6D28D9" stop-opacity="0"/>
      <stop offset=".5" stop-color="#A78BFA"/>
      <stop offset="1" stop-color="#6D28D9" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .sig-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .sig-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .sig-name {
      stroke: #DDD6FE; stroke-width: 1.2; fill: #FFFFFF; fill-opacity: 0;
      stroke-dasharray: 900; stroke-dashoffset: 900;
      animation: sig-write 3.6s cubic-bezier(.65,0,.35,1) .3s forwards;
    }
    .sig-rule { stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: sig-draw 2.4s cubic-bezier(.65,0,.35,1) 1.6s forwards; }
    .sig-in { animation: sig-in 1.4s cubic-bezier(.16,1,.3,1) 2s both; }
    @keyframes sig-write { to { stroke-dashoffset: 0; fill-opacity: 1; } }
    @keyframes sig-draw { to { stroke-dashoffset: 0; } }
    @keyframes sig-in { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
    @media (prefers-reduced-motion: reduce) {
      .sig-name { animation: none; stroke-dashoffset: 0; fill-opacity: 1; }
      .sig-rule { animation: none; stroke-dashoffset: 0; }
      .sig-in { animation: none; }
    }
  </style>
  <rect width="1200" height="230" fill="url(#sig-bg)"/>
  <rect width="1200" height="230" fill="url(#sig-glow)"/>
  <path class="sig-rule" d="M100 40 H1100" stroke="url(#sig-line)" stroke-width="1"/>
  
  <g transform="translate(600 115)">
    <text class="sig-serif sig-name" text-anchor="middle" font-size="52" font-style="italic" font-weight="300" letter-spacing="-1">Snehal Ghadge</text>
  </g>
  <g class="sig-in">
    <text class="sig-mono" x="600" y="162" text-anchor="middle" font-size="12" letter-spacing="2.8" fill="#C4B5FD">BUILDING AUTONOMOUS SYSTEMS THAT CREATE REAL-WORLD IMPACT</text>
    <text class="sig-mono" x="600" y="188" text-anchor="middle" font-size="10.5" letter-spacing="1.8" fill="#A79FB5">PUNE, INDIA · AVAILABLE FOR FULL-TIME ROLES &amp; RESEARCH COLLABORATIONS</text>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "footer-signature.svg"), "w", encoding="utf-8") as f:
    f.write(footer_svg)
print("footer-signature.svg generated")

# ----------------- 8. ASSEMBLE README.MD -----------------
readme_content = '''<a href="https://snehalsportfolio2027.netlify.app">
  <img src="assets/snehal-hero-portrait.svg" width="100%" alt="Snehal Ghadge — AI &amp; Agentic Systems Engineer. Building autonomous intelligence. Designing scalable reasoning workflows.">
</a>

<p align="center">
  <a href="https://snehalsportfolio2027.netlify.app"><img src="https://img.shields.io/badge/Portfolio-snehalsportfolio2027-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=netlify" alt="Portfolio website"></a>
  <a href="https://linkedin.com/in/snehal-g-711587312"><img src="https://img.shields.io/badge/LinkedIn-snehal--g-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI0VERTlGRSIgZD0iTTIwLjQ1IDIwLjQ1aC0zLjU2di01LjU3YzAtMS4zMy0uMDItMy4wNC0xLjg1LTMuMDQtMS44NiAwLTIuMTQgMS40NS0yLjE0IDIuOTR2NS42N0g5LjM1VjloMy40MXYxLjU2aC4wNWMuNDgtLjkgMS42NC0xLjg1IDMuMzctMS44NSAzLjYgMCA0LjI3IDIuMzcgNC4yNyA1LjQ2djYuMjhaTTUuMzQgNy40M2EyLjA2IDIuMDYgMCAxIDEgMC00LjEzIDIuMDYgMi4wNiAwIDAgMSAwIDQuMTNaTTcuMTIgMjAuNDVIMy41NlY5aDMuNTZ2MTEuNDVaTTIyLjIyIDBIMS43N0MuNzkgMCAwIC43NyAwIDEuNzN2MjAuNTRDMCAyMy4yMy43OSAyNCAxLjc3IDI0aDIwLjQ1Yy45OCAwIDEuNzgtLjc3IDEuNzgtMS43M1YxLjczQzI0IC43NyAyMy4yIDAgMjIuMjIgMFoiLz48L3N2Zz4=" alt="LinkedIn profile"></a>
  <a href="https://leetcode.com/u/snehalghadge/"><img src="https://img.shields.io/badge/LeetCode-snehalghadge-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=leetcode" alt="LeetCode profile"></a>
  <a href="mailto:snehalghadge59@gmail.com"><img src="https://img.shields.io/badge/Email-snehalghadge59@gmail.com-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=gmail" alt="Email snehalghadge59@gmail.com"></a>
  <a href="https://github.com/snehalghadge59-blip"><img src="https://img.shields.io/badge/GitHub-snehalghadge59--blip-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=github" alt="GitHub snehalghadge59-blip"></a>
</p>

<img src="assets/title-about.svg" width="100%" alt="01 About — Hello, I'm Snehal.">
<img src="assets/about-intro.svg" width="100%" alt="About: AI &amp; Agentic Systems Engineer and Machine Learning Developer. B.Tech in CSE (AI/ML) at Nutan College of Engineering, Pune. Lenovo LEAP NextGen Scholar, AI Intern at Code-A-Nova, Generative AI Intern at Infosys Springboard. Shipped AgentFlow-AI, InsightRAG, AeroFaultAI and devpulse-visualizer. Primary language Python and C++; drawn to autonomous systems and enterprise RAG.">

<img src="assets/title-recognition.svg" width="100%" alt="02 Recognition — Proof, on the record.">
<img src="assets/achievement-motif.svg" width="100%" alt="Lenovo LEAP NextGen Scholar via AICTE; Infosys Springboard Virtual Intern; AI Intern at Code-A-Nova; 30+ GitHub projects; LeetCode algorithmic problem solver.">

<img src="assets/title-work.svg" width="100%" alt="03 Selected work — Products, not assignments.">

<a href="https://github.com/snehalghadge59-blip/AgentFlow-AI">
  <img src="assets/project-agentflow.svg" width="100%" alt="AgentFlow-AI: Multi-agent orchestration framework for autonomous task execution. Dynamic state-graph execution, automated task decomposition and tool delegation.">
</a>
<p align="center">
  <a href="https://github.com/snehalghadge59-blip/AgentFlow-AI"><img src="https://img.shields.io/badge/Repository-AgentFlow--AI-4C1D95?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=github" alt="AgentFlow-AI repository"></a>
</p>

<a href="https://github.com/snehalghadge59-blip/InsightRAG">
  <img src="assets/project-insightrag.svg" width="100%" alt="InsightRAG: Enterprise production RAG with hybrid search and semantic caching. 10k+ chunks indexed, 94.8% retrieval precision, 4x faster response times.">
</a>
<p align="center">
  <a href="https://github.com/snehalghadge59-blip/InsightRAG"><img src="https://img.shields.io/badge/Repository-InsightRAG-4C1D95?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=github" alt="InsightRAG repository"></a>
</p>

<a href="https://github.com/snehalghadge59-blip/AeroFaultAI">
  <img src="assets/project-aerofault.svg" width="100%" alt="AeroFaultAI: Real-time aerospace telemetry anomaly detection and predictive diagnostics. 98.2% anomaly F1-score, sub-50ms inference, 100k+ telemetry points.">
</a>
<p align="center">
  <a href="https://github.com/snehalghadge59-blip/AeroFaultAI"><img src="https://img.shields.io/badge/Repository-AeroFaultAI-4C1D95?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=github" alt="AeroFaultAI repository"></a>
</p>

<img src="assets/title-toolkit.svg" width="100%" alt="04 Toolkit — The tools I reach for.">
<img src="assets/tech-constellation.svg" width="100%" alt="Tech stack. Languages: Python, C++, TypeScript, JavaScript, SQL. AI/ML: PyTorch, LangChain, LangGraph, LlamaIndex, FAISS, Transformers. Backend: FastAPI, Flask, Node.js, Express, REST APIs, Redis. Data: PostgreSQL, MongoDB, MySQL, Vector DBs. DevOps: AWS, Docker, GitHub Actions, Linux. Tools: Streamlit, PowerBI, Jupyter, Postman.">

<img src="assets/title-commits.svg" width="100%" alt="05 Commit log — A year of continuous building.">

<p align="center">
  <img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%" alt="Snehal's GitHub Contribution Grid Snake Animation" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=snehalghadge59-blip&show_icons=true&hide_rank=true&hide_border=true&border_radius=16&bg_color=0B0714&title_color=DDD6FE&text_color=A79FB5&icon_color=A78BFA&custom_title=GitHub%20at%20a%20glance" width="410" alt="GitHub stats for Snehal Ghadge: stars, commits, PRs and issues" />
  &nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=snehalghadge59-blip&layout=compact&hide_border=true&border_radius=16&bg_color=0B0714&title_color=DDD6FE&text_color=A79FB5" width="370" alt="Top languages used by Snehal Ghadge" />
</p>

<img src="assets/title-certifications.svg" width="100%" alt="06 Certifications — Verified credentials &amp; accreditations.">
<a href="https://snehalsportfolio2027.netlify.app">
  <img src="assets/certifications.svg" width="100%" alt="Certifications: Lenovo LEAP NextGen Scholar (AICTE); Infosys Springboard Generative AI &amp; Agentic Systems; Code-A-Nova AI &amp; NLP Systems Internship; Edunet Foundation AI &amp; Analytics; Data Visualization Professional; B.Tech Computer Science &amp; Engineering (AI/ML).">
</a>

<img src="assets/title-connect.svg" width="100%" alt="07 Connect — Let's build something worth explaining.">

<p align="center">
  <a href="mailto:snehalghadge59@gmail.com"><img src="https://img.shields.io/badge/Email-snehalghadge59@gmail.com-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=gmail" alt="Email snehalghadge59@gmail.com"></a>
  <a href="https://linkedin.com/in/snehal-g-711587312"><img src="https://img.shields.io/badge/LinkedIn-snehal--g-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI0VERTlGRSIgZD0iTTIwLjQ1IDIwLjQ1aC0zLjU2di01LjU3YzAtMS4zMy0uMDItMy4wNC0xLjg1LTMuMDQtMS44NiAwLTIuMTQgMS40NS0yLjE0IDIuOTR2NS42N0g5LjM1VjloMy40MXYxLjU2aC4wNWMuNDgtLjkgMS42NC0xLjg1IDMuMzctMS44NSAzLjYgMCA0LjI3IDIuMzcgNC4yNyA1LjQ2djYuMjhaTTUuMzQgNy40M2EyLjA2IDIuMDYgMCAxIDEgMC00LjEzIDIuMDYgMi4wNiAwIDAgMSAwIDQuMTNaTTcuMTIgMjAuNDVIMy41NlY5aDMuNTZ2MTEuNDVaTTIyLjIyIDBIMS43N0MuNzkgMCAwIC43NyAwIDEuNzN2MjAuNTRDMCAyMy4yMy43OSAyNCAxLjc3IDI0aDIwLjQ1Yy45OCAwIDEuNzgtLjc3IDEuNzgtMS43M1YxLjczQzI0IC43NyAyMy4yIDAgMjIuMjIgMFoiLz48L3N2Zz4=" alt="LinkedIn profile"></a>
  <a href="https://leetcode.com/u/snehalghadge/"><img src="https://img.shields.io/badge/LeetCode-snehalghadge-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=leetcode" alt="LeetCode profile snehalghadge"></a>
  <a href="https://snehalsportfolio2027.netlify.app"><img src="https://img.shields.io/badge/Portfolio-snehalsportfolio2027-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=netlify" alt="Portfolio website"></a>
  <a href="https://github.com/snehalghadge59-blip"><img src="https://img.shields.io/badge/GitHub-snehalghadge59--blip-6D28D9?style=for-the-badge&labelColor=140D24&logoColor=EDE9FE&logo=github" alt="GitHub snehalghadge59-blip"></a>
</p>

<a href="https://snehalsportfolio2027.netlify.app">
  <img src="assets/footer-signature.svg" width="100%" alt="Snehal — Engineering intelligence that creates real-world impact.">
</a>
'''

with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md assembled and written!")
