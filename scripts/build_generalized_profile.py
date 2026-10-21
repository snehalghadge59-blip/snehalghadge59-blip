import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Read the base64 photo already in assets/snehal-hero-portrait.svg
hero_file = os.path.join(ASSETS_DIR, "snehal-hero-portrait.svg")
with open(hero_file, "r", encoding="utf-8") as f:
    old_hero = f.read()

import re
b64_match = re.search(r'data:image/jpeg;base64,([A-Za-z0-9+/=]+)', old_hero)
if not b64_match:
    raise ValueError("Could not find base64 portrait photo in old hero svg!")
b64_data = b64_match.group(1)

# ─── 1. HERO PORTRAIT SVG ────────────────────────────────────────────────────
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="h-title h-desc">
  <title id="h-title">Snehal Ghadge — Data &amp; AI Developer</title>
  <desc id="h-desc">Snehal Ghadge: Data &amp; AI Developer, Machine Learning Engineer. Building intelligent systems, data-driven applications, and scalable machine learning workflows.</desc>
  <defs>
    <linearGradient id="h-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0B0714"/>
      <stop offset=".45" stop-color="#140D24"/>
      <stop offset="1" stop-color="#1E1035"/>
    </linearGradient>
    <radialGradient id="h-glow-right" cx="80%" cy="40%" r="55%">
      <stop offset="0" stop-color="#7C3AED" stop-opacity=".7"/>
      <stop offset=".5" stop-color="#4C1D95" stop-opacity=".3"/>
      <stop offset="1" stop-color="#0B0714" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="h-glow-left" cx="20%" cy="20%" r="45%">
      <stop offset="0" stop-color="#4C1D95" stop-opacity=".35"/>
      <stop offset="1" stop-color="#0B0714" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="h-ng" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".6" stop-color="#EDE9FE"/>
      <stop offset="1" stop-color="#C4B5FD"/>
    </linearGradient>
    <linearGradient id="h-sh" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset=".5" stop-color="#FFFFFF" stop-opacity=".9"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 1600 0; 1600 0" keyTimes="0; .45; 1" dur="7s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="h-rule" gradientUnits="userSpaceOnUse" x1="60" y1="0" x2="720" y2="0">
      <stop offset="0" stop-color="#7C3AED"/>
      <stop offset=".6" stop-color="#A78BFA"/>
      <stop offset="1" stop-color="#7C3AED" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="h-tr" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".35" stop-color="#C4B5FD"/>
      <stop offset=".7" stop-color="#7C3AED"/>
      <stop offset="1" stop-color="#7C3AED" stop-opacity="0"/>
    </linearGradient>
    <!-- True Arch Clip Path -->
    <clipPath id="h-arch">
      <path d="M850 390 V202 A116 116 0 0 1 1082 202 V390 Z"/>
    </clipPath>
  </defs>
  <style>
    .h-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .h-sans  {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
    .h-mono  {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .h-rise  {{ animation: h-rise 1s ease both; }}
    .d1 {{ animation-delay: .1s; }}
    .d2 {{ animation-delay: .25s; }}
    .d3 {{ animation-delay: .4s; }}
    .d4 {{ animation-delay: .55s; }}
    .d5 {{ animation-delay: .7s; }}
    @keyframes h-rise {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    .h-draw {{ stroke-dasharray: 800; stroke-dashoffset: 800; animation: h-draw 2s cubic-bezier(.16,1,.3,1) .3s forwards; }}
    @keyframes h-draw {{ to {{ stroke-dashoffset: 0; }} }}
    .h-trace {{ stroke-dasharray: 600 2760; stroke-dashoffset: 3360; animation: h-trace 9s linear infinite; }}
    @keyframes h-trace {{ to {{ stroke-dashoffset: 0; }} }}
    .h-spin-cw  {{ transform-origin: 966px 208px; animation: h-cw 40s linear infinite; }}
    .h-spin-ccw {{ transform-origin: 966px 208px; animation: h-ccw 55s linear infinite; }}
    @keyframes h-cw  {{ to {{ transform: rotate(360deg); }} }}
    @keyframes h-ccw {{ to {{ transform: rotate(-360deg); }} }}
    @media (prefers-reduced-motion: reduce) {{
      .h-rise {{ animation: none; opacity: 1; }}
      .h-draw {{ stroke-dashoffset: 0; }}
      .h-trace, .h-spin-cw, .h-spin-ccw {{ animation: none; }}
    }}
  </style>
  <rect width="1200" height="480" rx="20" fill="url(#h-bg)"/>
  <rect width="1200" height="480" rx="20" fill="url(#h-glow-right)"/>
  <rect width="1200" height="480" rx="20" fill="url(#h-glow-left)"/>
  <g opacity=".1">
    <line x1="0" y1="80" x2="1200" y2="80" stroke="#EDE9FE" stroke-dasharray="2 6"/>
    <line x1="0" y1="160" x2="1200" y2="160" stroke="#EDE9FE" stroke-dasharray="2 6"/>
    <line x1="0" y1="240" x2="1200" y2="240" stroke="#EDE9FE" stroke-dasharray="2 6"/>
    <line x1="0" y1="320" x2="1200" y2="320" stroke="#EDE9FE" stroke-dasharray="2 6"/>
    <line x1="0" y1="400" x2="1200" y2="400" stroke="#EDE9FE" stroke-dasharray="2 6"/>
  </g>
  <g>
    <!-- Right Arch Orbit Graphic -->
    <g class="h-rise d2">
      <!-- Orbit Rings -->
      <circle class="h-spin-cw" cx="966" cy="208" r="170" fill="none" stroke="#7C3AED" stroke-opacity=".25" stroke-dasharray="4 8"/>
      <circle class="h-spin-ccw" cx="966" cy="208" r="215" fill="none" stroke="#A78BFA" stroke-opacity=".18" stroke-dasharray="2 10"/>
      <!-- Arch Backing Halo -->
      <path d="M844 394 V204 A122 122 0 0 1 1088 204 V394 Z" fill="#24143D" fill-opacity=".7"/>
      <!-- Arch frame -->
      <path d="M838 394 V208 A127 127 0 0 1 1092 208 V394 Z" fill="none" stroke="#A78BFA" stroke-opacity=".3">
        <animate attributeName="stroke-opacity" values=".15;.5;.15" dur="5s" repeatCount="indefinite"/>
      </path>
      <!-- Real Portrait Photo -->
      <g clip-path="url(#h-arch)">
        <rect x="850" y="86" width="232" height="308" fill="#140D24"/>
        <image href="data:image/jpeg;base64,{b64_data}" x="850" y="86" width="232" height="308" preserveAspectRatio="xMidYMin slice"/>
        <linearGradient id="h-photo-fade" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="#7C3AED" stop-opacity=".15"/>
          <stop offset=".6" stop-color="#140D24" stop-opacity="0"/>
          <stop offset="1" stop-color="#0B0714" stop-opacity=".85"/>
        </linearGradient>
        <rect x="850" y="86" width="232" height="308" fill="url(#h-photo-fade)"/>
      </g>
      <!-- Frame border -->
      <path class="h-draw" d="M850 390 V208 A116 116 0 0 1 1082 208 V390 Z" fill="none" stroke="#DDD6FE" stroke-width="1.5" stroke-opacity=".6"/>
      <!-- Data tags beside portrait -->
      <g class="h-rise d4">
        <rect x="714" y="190" width="124" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="730" cy="204" r="4" fill="#38BDF8"/>
        <text font-family="ui-monospace,monospace" x="742" y="208" font-size="10.5" fill="#DDD6FE">Data &amp; Analytics</text>
      </g>
      <g class="h-rise d5">
        <rect x="1092" y="240" width="86" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="1108" cy="254" r="4" fill="#10B981"/>
        <text font-family="ui-monospace,monospace" x="1118" y="258" font-size="10.5" fill="#DDD6FE">AI &amp; ML</text>
      </g>
      <g class="h-rise d5">
        <rect x="730" y="300" width="108" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="746" cy="314" r="4" fill="#A78BFA"/>
        <text font-family="ui-monospace,monospace" x="756" y="318" font-size="10.5" fill="#DDD6FE">Pune, India</text>
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
        <text class="h-mono" x="24" y="10" font-size="11.5" letter-spacing="2.8" fill="#C4B5FD">OPEN TO OPPORTUNITIES IN DATA &amp; AI</text>
      </g>
    </g>
    <g class="h-rise d2">
      <text class="h-serif" x="58" y="162" font-size="64" font-weight="300" letter-spacing="-1.5" fill="url(#h-ng)">Snehal Ghadge</text>
      <text class="h-serif" x="58" y="162" font-size="64" font-weight="300" letter-spacing="-1.5" fill="url(#h-sh)">Snehal Ghadge</text>
    </g>
    <g class="h-rise d3">
      <text class="h-sans" x="60" y="210" font-size="20" font-weight="400" fill="#EDE9FE">Data &amp; AI Developer <tspan fill="#A78BFA">·</tspan> Machine Learning Engineer</text>
      <text class="h-serif" x="60" y="244" font-size="16" font-style="italic" fill="#C4B5FD">Transforming data into insights, building intelligent models &amp; scalable workflows.</text>
    </g>
    <path class="h-draw" d="M60 274 H720" stroke="url(#h-rule)" stroke-width="1"/>
    <!-- Metadata Chips -->
    <g class="h-rise d4" transform="translate(60 306)">
      <g transform="translate(0 0)">
        <rect width="180" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="90" y="21" text-anchor="middle" font-size="11" fill="#DDD6FE">Data Analytics &amp; BI</text>
      </g>
      <g transform="translate(192 0)">
        <rect width="190" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="95" y="21" text-anchor="middle" font-size="11" fill="#DDD6FE">Machine Learning &amp; AI</text>
      </g>
      <g transform="translate(394 0)">
        <rect width="180" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="90" y="21" text-anchor="middle" font-size="11" fill="#DDD6FE">B.Tech CSE (AI/ML)</text>
      </g>
    </g>
    <g class="h-rise d5" transform="translate(60 366)">
      <g transform="translate(0 0)">
        <text class="h-serif" font-size="26" font-weight="300" fill="#FFFFFF">30+</text>
        <text class="h-sans" y="22" font-size="11.5" fill="#A79FB5">repos &amp; projects</text>
      </g>
      <g transform="translate(170 0)">
        <text class="h-serif" font-size="26" font-weight="300" fill="#FFFFFF">Data &amp; AI</text>
        <text class="h-sans" y="22" font-size="11.5" fill="#A79FB5">analytics &amp; pipelines</text>
      </g>
      <g transform="translate(360 0)">
        <text class="h-serif" font-size="26" font-weight="300" fill="#FFFFFF">Industry Experience</text>
        <text class="h-sans" y="22" font-size="11.5" fill="#A79FB5">Infosys &amp; Code-A-Nova</text>
      </g>
    </g>
    <!-- Frame & Trace -->
    <rect x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
    <rect class="h-trace" x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="url(#h-tr)" stroke-width="1.8" stroke-linecap="round"/>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "snehal-hero-portrait.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)
print("snehal-hero-portrait.svg updated")

# ─── 2. SECTION TITLE HELPER ─────────────────────────────────────────────────
def make_title_svg(num_str, mono_label, serif_main, serif_italic, right_label, filename):
    safe_aria = (num_str + " " + mono_label + ": " + serif_main + " " + serif_italic).replace("&", "&amp;")
    safe_main = serif_main.replace("&", "&amp;")
    safe_italic = serif_italic.replace("&", "&amp;")
    safe_right = right_label.replace("&", "&amp;")
    safe_mono = mono_label.replace("&", "&amp;")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="{safe_aria}">
  <defs>
    <linearGradient id="ta-line" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="1160" y2="0">
      <stop offset="0" stop-color="#A78BFA"/><stop offset=".6" stop-color="#6D28D9"/><stop offset="1" stop-color="#6D28D9" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ta-sheen" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#DDD6FE"/><stop offset=".5" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DDD6FE"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1500 0;1500 0" keyTimes="0;.4;1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <style>
    .ta-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .ta-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
  </style>
  <g transform="translate(40 40)">
    <text class="ta-mono" font-size="11" letter-spacing="2.8" fill="#C4B5FD">{num_str} · {safe_mono}</text>
    <text class="ta-serif" y="44" font-size="34" font-weight="300" fill="#FFFFFF">{safe_main} <tspan fill="#C4B5FD" font-style="italic">{safe_italic}</tspan></text>
    <text class="ta-serif" y="44" font-size="34" font-weight="300" fill="url(#ta-sheen)">{safe_main} <tspan fill="#C4B5FD" font-style="italic">{safe_italic}</tspan></text>
    <text class="ta-mono" x="1120" y="14" text-anchor="end" font-size="10.5" letter-spacing="2" fill="#A79FB5">{safe_right}</text>
  </g>
  <line x1="40" y1="104" x2="1160" y2="104" stroke="url(#ta-line)" stroke-width="1"/>
</svg>
'''
    with open(os.path.join(ASSETS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{filename} generated")

make_title_svg("01", "ABOUT", "Hello, I'm", "Snehal.", "WHO I AM", "title-about.svg")
make_title_svg("02", "RECOGNITION", "Proof,", "on the record.", "HONORS & FELLOWSHIPS", "title-recognition.svg")
make_title_svg("03", "SELECTED WORK", "Featured Systems,", "tested & deployed.", "APPLICATIONS", "title-work.svg")
make_title_svg("04", "TOOLKIT", "The tools", "I build & analyze with.", "TECH STACK", "title-toolkit.svg")
make_title_svg("05", "COMMIT LOG", "A year of", "continuous building.", "CONTRIBUTIONS", "title-commits.svg")
make_title_svg("06", "CERTIFICATIONS", "Verified credentials", "and accreditations.", "SIX CREDENTIALS", "title-certifications.svg")
make_title_svg("07", "CONNECT", "Let's build", "something impactful.", "GET IN TOUCH", "title-connect.svg")

# ─── 3. ABOUT INTRO SVG ───────────────────────────────────────────────────────
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="ab-t ab-d">
  <title id="ab-t">About Snehal Ghadge</title>
  <desc id="ab-d">Data &amp; AI Developer. B.Tech in CSE (AI/ML) at Nutan College of Engineering, Pune. Experience with Infosys Springboard and Code-A-Nova. Specialized in SQL, Python, Power BI, EDA, predictive modeling, and AI systems.</desc>
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
    <g clip-path="url(#ab-c1)"><text x="72" y="153" fill="#6D28D9">→</text><text x="94" y="153" fill="#DDD6FE">Snehal Ghadge · Data &amp; AI Developer · B.Tech CSE (AI/ML)</text></g>
    <g clip-path="url(#ab-c2)"><text x="72" y="178" fill="#A78BFA">$</text><text x="94" y="178" fill="#FFFFFF">cat core_domains.txt</text></g>
    <g clip-path="url(#ab-c3)"><text x="72" y="203" fill="#6D28D9">→</text><text x="94" y="203" fill="#DDD6FE">Data Analytics (SQL, Power BI, EDA) · Machine Learning &amp; AI Systems</text></g>
    <g clip-path="url(#ab-c4)"><text x="72" y="228" fill="#A78BFA">$</text><text x="94" y="228" fill="#FFFFFF">cat experience.txt</text></g>
    <g clip-path="url(#ab-c5)"><text x="72" y="253" fill="#6D28D9">→</text><text x="94" y="253" fill="#DDD6FE">Infosys Springboard (Analytics &amp; GenAI) · Code-A-Nova (AI Systems)</text></g>
    <g clip-path="url(#ab-c6)"><text x="72" y="278" fill="#A78BFA">$</text><text x="94" y="278" fill="#FFFFFF">ls ./projects</text></g>
    <g clip-path="url(#ab-c7)"><text x="72" y="303" fill="#6D28D9">→</text><text x="94" y="303" fill="#DDD6FE">AeroFaultAI (Telemetry ML)  AgentFlow-AI   InsightRAG   CustomerIQ</text></g>
    <g clip-path="url(#ab-c8)"><text x="72" y="328" fill="#A78BFA">$</text><text x="94" y="328" fill="#FFFFFF">echo $PRINCIPLE</text></g>
    <g clip-path="url(#ab-c9)"><text x="72" y="353" fill="#6D28D9">→</text><text x="94" y="353" fill="#DDD6FE">engineering data-driven insights and reliable, intelligent software</text></g>
  </g>
  <rect x="72" y="364" width="8" height="16" fill="#DDD6FE" class="ab-fade" style="animation-delay:7.4s">
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>

  <!-- Right Highlight Cards -->
  <g class="ab-card" style="animation-delay:1.2s"><g transform="translate(836 70)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#38BDF8"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#38BDF8">DATA &amp; ANALYTICS</text>
    <text class="ab-serif" x="22" y="58" font-size="26" font-weight="300" fill="#FFFFFF">SQL, Python &amp; Power BI</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">Exploratory Analysis · Dashboards · Data Insights</text>
  </g></g>
  <g class="ab-card" style="animation-delay:1.7s"><g transform="translate(836 174)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#10B981"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#10B981">AI &amp; MACHINE LEARNING</text>
    <text class="ab-serif" x="22" y="58" font-size="26" font-weight="300" fill="#FFFFFF">Predictive Models &amp; GenAI</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">Scikit-Learn · PyTorch · LangChain · FAISS</text>
  </g></g>
  <g class="ab-card" style="animation-delay:2.2s"><g transform="translate(836 278)">
    <rect width="324" height="88" rx="14" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".32"/>
    <rect x="0" y="0" width="3.5" height="88" rx="1.5" fill="#A78BFA"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#A78BFA">SOFTWARE &amp; PIPELINES</text>
    <text class="ab-serif" x="22" y="58" font-size="26" font-weight="300" fill="#FFFFFF">Full-Stack &amp; Cloud APIs</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#A79FB5">FastAPI · Databases · Clean Code &amp; Algorithms</text>
  </g></g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "about-intro.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)
print("about-intro.svg updated")

# ─── 4. ACHIEVEMENT MOTIF SVG ─────────────────────────────────────────────────
ach_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-labelledby="ach-title ach-desc">
  <title id="ach-title">Recognition and Honors</title>
  <desc id="ach-desc">Lenovo LEAP NextGen Scholar via AICTE; Infosys Springboard Virtual Intern (Data Analytics, Power BI &amp; GenAI); Code-A-Nova AI Intern; 30+ GitHub projects and algorithmic problem solver.</desc>
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
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Engineered agentic &amp; analytical workflow prototypes with structured reasoning.</text>
    </g>

    <!-- Card 2 -->
    <g transform="translate(580 0)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#38BDF8"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#38BDF8">VIRTUAL INTERNSHIP</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">Infosys Springboard</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Data Analytics, Power BI &amp; Generative AI.</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Built interactive Power BI dashboards, ETL pipelines &amp; prompt optimization systems.</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(0 175)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#10B981"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#10B981">INDUSTRY INTERNSHIP</text>
      <text class="ach-serif" x="26" y="66" font-size="24" font-weight="300" fill="#FFFFFF">Code-A-Nova</text>
      <text class="ach-sans" x="26" y="94" font-size="13" fill="#C4B5FD">Artificial Intelligence, NLP &amp; Analytics Automation.</text>
      <text class="ach-mono" x="26" y="118" font-size="11" fill="#A79FB5">Document intelligence, semantic search and enterprise backend integration.</text>
    </g>

    <!-- Card 4 -->
    <g transform="translate(580 175)">
      <rect width="540" height="145" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".32"/>
      <rect x="0" y="0" width="3.5" height="145" rx="1.5" fill="#A78BFA"/>
      <text class="ach-mono" x="26" y="32" font-size="11" letter-spacing="2.2" fill="#A78BFA">ANALYTICS &amp; PROBLEM SOLVING</text>
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
print("achievement-motif.svg updated")

# ─── 5. FOOTER SIGNATURE SVG ──────────────────────────────────────────────────
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 230" width="1200" height="230" role="img" aria-labelledby="sig-title">
  <title id="sig-title">Snehal — Engineering data-driven intelligence and high-impact AI solutions.</title>
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
    <text class="sig-mono" x="600" y="162" text-anchor="middle" font-size="12" letter-spacing="2.8" fill="#C4B5FD">BUILDING DATA-DRIVEN INTELLIGENCE &amp; SCALABLE AI WORKFLOWS</text>
    <text class="sig-mono" x="600" y="188" text-anchor="middle" font-size="10.5" letter-spacing="1.8" fill="#A79FB5">PUNE, INDIA · OPEN TO OPPORTUNITIES IN DATA &amp; AI</text>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "footer-signature.svg"), "w", encoding="utf-8") as f:
    f.write(footer_svg)
print("footer-signature.svg updated")

# ─── 6. ASSEMBLE README.md ───────────────────────────────────────────────────
readme = '''<a href="https://snehalsportfolio2027.netlify.app">
  <img src="assets/snehal-hero-portrait.svg" width="100%" alt="Snehal Ghadge — Data &amp; AI Developer. Transforming data into insights and building scalable machine learning systems.">
</a>

<p align="center">
  <img src="assets/snehal-profile.png" width="140" height="140" alt="Snehal Ghadge" />
</p>

<p align="center">
  <a href="https://snehalsportfolio2027.netlify.app"><img src="https://img.shields.io/badge/Portfolio-snehalsportfolio2027-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=netlify" alt="Portfolio"></a>
  <a href="https://linkedin.com/in/snehal-g-711587312"><img src="https://img.shields.io/badge/LinkedIn-snehal--g-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=linkedin" alt="LinkedIn"></a>
  <a href="https://leetcode.com/u/snehalghadge/"><img src="https://img.shields.io/badge/LeetCode-snehalghadge-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=leetcode" alt="LeetCode"></a>
  <a href="mailto:snehalghadge59@gmail.com"><img src="https://img.shields.io/badge/Email-snehalghadge59@gmail.com-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=gmail" alt="Email"></a>
  <a href="https://github.com/snehalghadge59-blip"><img src="https://img.shields.io/badge/GitHub-snehalghadge59--blip-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="GitHub"></a>
</p>

<img src="assets/title-about.svg" width="100%" alt="01 About - Hello, Im Snehal.">
<img src="assets/about-intro.svg" width="100%" alt="About: Snehal Ghadge. Data &amp; AI Developer. B.Tech in CSE (AI/ML) at Nutan College of Engineering, Pune.">

<img src="assets/title-recognition.svg" width="100%" alt="02 Recognition - Proof, on the record.">
<img src="assets/achievement-motif.svg" width="100%" alt="Lenovo LEAP NextGen Scholar via AICTE; Infosys Springboard Virtual Intern (Data Analytics, Power BI &amp; GenAI); Code-A-Nova; 30+ GitHub projects and dashboards.">

<img src="assets/title-work.svg" width="100%" alt="03 Selected work - Products, not assignments.">

<a href="https://github.com/snehalghadge59-blip/AeroFaultAI">
  <img src="assets/project-aerofault.svg" width="100%" alt="AeroFaultAI: Real-time aerospace telemetry anomaly detection, exploratory data analysis and predictive diagnostics.">
</a>
<p align="center">
  <a href="https://github.com/snehalghadge59-blip/AeroFaultAI"><img src="https://img.shields.io/badge/Repository-AeroFaultAI-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="AeroFaultAI repository"></a>
</p>

<a href="https://github.com/snehalghadge59-blip/AgentFlow-AI">
  <img src="assets/project-agentflow.svg" width="100%" alt="AgentFlow-AI: Multi-agent orchestration framework for autonomous decision intelligence and task execution.">
</a>
<p align="center">
  <a href="https://github.com/snehalghadge59-blip/AgentFlow-AI"><img src="https://img.shields.io/badge/Repository-AgentFlow--AI-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="AgentFlow-AI repository"></a>
</p>

<a href="https://github.com/snehalghadge59-blip/InsightRAG">
  <img src="assets/project-insightrag.svg" width="100%" alt="InsightRAG: Production-grade enterprise analytics and RAG with hybrid search and semantic cache.">
</a>
<p align="center">
  <a href="https://github.com/snehalghadge59-blip/InsightRAG"><img src="https://img.shields.io/badge/Repository-InsightRAG-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="InsightRAG repository"></a>
</p>

<img src="assets/title-toolkit.svg" width="100%" alt="04 Toolkit - The tools I reach for.">
<img src="assets/tech-constellation.svg" width="100%" alt="Full tech stack listing.">

<!-- Tech Stack Skill Icons with Logos -->
<p align="center">
  <b>📊 Data Analytics &amp; Business Intelligence</b><br/>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,postgres,mysql,mongodb&amp;perline=6" alt="Python PostgreSQL MySQL MongoDB" /></a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&amp;logo=powerbi&amp;logoColor=black" alt="Power BI" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&amp;logo=pandas&amp;logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&amp;logo=numpy&amp;logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&amp;logo=tableau&amp;logoColor=white" alt="Tableau" />
</p>
<p align="center">
  <b>🤖 AI, Machine Learning &amp; Deep Learning</b><br/>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn,fastapi,flask" alt="PyTorch TensorFlow Scikit-Learn FastAPI Flask" /></a>
</p>
<p align="center">
  <b>💻 Programming Languages &amp; Core</b><br/>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,cpp,c,ts,js,html,css,bash" alt="Python C++ C TypeScript JavaScript HTML5 CSS3 Bash" /></a>
</p>
<p align="center">
  <b>☁️ Cloud, Databases &amp; DevOps</b><br/>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=aws,docker,linux,git,github,githubactions,redis" alt="AWS Docker Linux Git GitHub GitHub Actions Redis" /></a>
</p>
<p align="center">
  <b>🛠️ Developer &amp; Data Tools</b><br/>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=vscode,postman,figma" alt="VS Code Postman Figma" /></a>
</p>

<img src="assets/title-commits.svg" width="100%" alt="05 Commit log - A year of continuous building.">

<p align="center">
  <img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%" alt="GitHub Contribution Grid Snake Animation" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=snehalghadge59-blip&amp;show_icons=true&amp;hide_rank=true&amp;hide_border=true&amp;border_radius=16&amp;bg_color=0B0714&amp;title_color=DDD6FE&amp;text_color=A79FB5&amp;icon_color=A78BFA&amp;custom_title=GitHub%20at%20a%20glance" width="410" alt="GitHub stats" />
  &nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=snehalghadge59-blip&amp;layout=compact&amp;hide_border=true&amp;border_radius=16&amp;bg_color=0B0714&amp;title_color=DDD6FE&amp;text_color=A79FB5" width="370" alt="Top languages" />
</p>

<img src="assets/title-certifications.svg" width="100%" alt="06 Certifications - Verified credentials and accreditations.">
<a href="https://snehalsportfolio2027.netlify.app">
  <img src="assets/certifications.svg" width="100%" alt="Certifications: Lenovo LEAP NextGen Scholar, Infosys Springboard GenAI, Code-A-Nova AI Internship, Edunet Foundation AI, Data Visualization, B.Tech CSE AI/ML.">
</a>

<img src="assets/title-connect.svg" width="100%" alt="07 Connect - Lets build something worth explaining.">

<p align="center">
  <a href="mailto:snehalghadge59@gmail.com"><img src="https://img.shields.io/badge/Email-snehalghadge59@gmail.com-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=gmail" alt="Email"></a>
  <a href="https://linkedin.com/in/snehal-g-711587312"><img src="https://img.shields.io/badge/LinkedIn-snehal--g-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=linkedin" alt="LinkedIn"></a>
  <a href="https://leetcode.com/u/snehalghadge/"><img src="https://img.shields.io/badge/LeetCode-snehalghadge-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=leetcode" alt="LeetCode"></a>
  <a href="https://snehalsportfolio2027.netlify.app"><img src="https://img.shields.io/badge/Portfolio-snehalsportfolio2027-6D28D9?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=netlify" alt="Portfolio"></a>
</p>

<a href="https://snehalsportfolio2027.netlify.app">
  <img src="assets/footer-signature.svg" width="100%" alt="Snehal - Delivering data-driven intelligence and high-impact AI solutions.">
</a>
'''

with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)
print("README.md updated")

# Validate all SVGs
import glob
print("\nValidating SVGs:")
for f in glob.glob(os.path.join(ASSETS_DIR, "*.svg")):
    try:
        ET.parse(f)
        print("OK:", os.path.basename(f))
    except Exception as e:
        print("ERROR in", os.path.basename(f), ":", e)
