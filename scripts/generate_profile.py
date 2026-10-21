import os

BASE_DIR = r"C:\Users\snehal\.gemini\antigravity-ide\scratch\snehalghadge59-blip"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# ─── HERO BANNER (pure SVG, no embedded image — GitHub-safe) ─────────────────
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">Snehal Ghadge — AI and Agentic Systems Engineer.</title>
  <desc id="hero-desc">AI and Agentic Systems Engineer, Machine Learning Developer. B.Tech CSE (AI/ML), Lenovo LEAP NextGen Scholar, AI Intern at Code-A-Nova and Infosys Springboard.</desc>
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
    <!-- Portrait frame gradients -->
    <radialGradient id="h-pf" cx="50%" cy="40%" r="60%">
      <stop offset="0" stop-color="#DDD6FE" stop-opacity=".9"/>
      <stop offset=".5" stop-color="#A78BFA" stop-opacity=".6"/>
      <stop offset="1" stop-color="#5B21B6" stop-opacity=".2"/>
    </radialGradient>
    <radialGradient id="h-pg" cx="50%" cy="30%" r="70%">
      <stop offset="0" stop-color="#E9D5FF"/>
      <stop offset=".5" stop-color="#C084FC"/>
      <stop offset="1" stop-color="#6D28D9"/>
    </radialGradient>
    <clipPath id="h-clip"><rect width="1200" height="480" rx="20"/></clipPath>
    <clipPath id="h-arch"><path d="M850 390 V208 A115 115 0 0 1 1080 208 V390 Z"/></clipPath>
  </defs>
  <style>
    .h-serif { font-family: Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif; }
    .h-mono  { font-family: ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace; }
    .h-sans  { font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; }
    .h-rise  { animation: h-rise 1.4s cubic-bezier(.16,1,.3,1) both; }
    .h-fade  { animation: h-fade 1.6s cubic-bezier(.16,1,.3,1) both; }
    .d1{animation-delay:.15s} .d2{animation-delay:.35s} .d3{animation-delay:.6s}
    .d4{animation-delay:.9s}  .d5{animation-delay:1.2s}
    .h-draw  { stroke-dasharray:900;stroke-dashoffset:900;animation:h-draw 2.4s cubic-bezier(.65,0,.35,1) .9s forwards; }
    .h-trace { stroke-dasharray:600 2760;stroke-dashoffset:3360;animation:h-trace 8s linear infinite; }
    @keyframes h-rise  { from{opacity:0;transform:translateY(18px)} to{opacity:1;transform:none} }
    @keyframes h-fade  { from{opacity:0} to{opacity:1} }
    @keyframes h-draw  { to{stroke-dashoffset:0} }
    @keyframes h-trace { to{stroke-dashoffset:0} }
    .h-float { animation: h-float 6s ease-in-out infinite; }
    @keyframes h-float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
    @media (prefers-reduced-motion:reduce) {
      .h-rise,.h-fade,.h-float{animation:none}
      .h-draw{animation:none;stroke-dashoffset:0}
      .h-trace{display:none}
    }
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
    <!-- Stylised Avatar / Portrait Illustration (pure SVG, no embedded images) -->
    <g class="h-fade d3 h-float">
      <!-- Arch frame -->
      <path d="M838 394 V208 A127 127 0 0 1 1092 208 V394 Z" fill="none" stroke="#A78BFA" stroke-opacity=".3">
        <animate attributeName="stroke-opacity" values=".15;.5;.15" dur="5s" repeatCount="indefinite"/>
      </path>
      <!-- Portrait Background -->
      <g clip-path="url(#h-arch)">
        <rect x="850" y="90" width="232" height="308" fill="url(#h-pg)"/>
        <!-- Stylised person silhouette -->
        <!-- Body/shoulders -->
        <ellipse cx="966" cy="340" rx="110" ry="70" fill="#3B0764" fill-opacity=".9"/>
        <!-- Neck -->
        <rect x="950" y="268" width="32" height="40" rx="8" fill="#C4AE8A"/>
        <!-- Face -->
        <ellipse cx="966" cy="248" rx="52" ry="60" fill="#C4AE8A"/>
        <!-- Hair top -->
        <ellipse cx="966" cy="200" rx="55" ry="28" fill="#2C1A10"/>
        <!-- Hair sides -->
        <path d="M914 230 Q905 200 920 180 Q940 165 966 168 Q992 165 1012 180 Q1027 200 1018 230 Q1010 210 966 208 Q922 210 914 230 Z" fill="#2C1A10"/>
        <!-- Hair falling left -->
        <path d="M914 230 Q900 260 905 300 Q908 320 918 310 Q920 270 930 250 Z" fill="#2C1A10"/>
        <!-- Hair falling right -->
        <path d="M1018 230 Q1032 260 1027 300 Q1024 320 1014 310 Q1012 270 1002 250 Z" fill="#2C1A10"/>
        <!-- Eyes -->
        <ellipse cx="950" cy="248" rx="8" ry="9" fill="#2C1A10"/>
        <ellipse cx="982" cy="248" rx="8" ry="9" fill="#2C1A10"/>
        <circle cx="953" cy="246" r="3" fill="#fff" fill-opacity=".4"/>
        <circle cx="985" cy="246" r="3" fill="#fff" fill-opacity=".4"/>
        <!-- Eyebrows -->
        <path d="M940 234 Q950 229 960 233" fill="none" stroke="#2C1A10" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M972 233 Q982 229 992 234" fill="none" stroke="#2C1A10" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Nose -->
        <path d="M963 255 Q961 268 956 272 Q963 274 970 272 Q965 268 963 255" fill="#B89A78"/>
        <!-- Smile -->
        <path d="M952 284 Q966 296 980 284" fill="none" stroke="#8B6040" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Teeth hint -->
        <path d="M954 285 Q966 292 978 285" fill="white" opacity=".5"/>
        <!-- Collar / top clothing -->
        <path d="M930 310 L850 394 L1082 394 L1052 310 Q1040 300 1020 305 L1010 312 Q986 326 966 326 Q946 326 922 312 L912 305 Q892 300 880 310 Z" fill="#1C1236"/>
        <!-- Collar white -->
        <path d="M940 308 L966 330 L992 308 Q986 300 966 298 Q946 300 940 308 Z" fill="white" opacity=".15"/>
        <!-- Gradient overlay bottom fade -->
        <rect x="850" y="330" width="232" height="64" fill="url(#h-pg)" opacity=".5"/>
      </g>
      <!-- Frame border -->
      <path class="h-draw" d="M850 390 V208 A116 116 0 0 1 1082 208 V390 Z" fill="none" stroke="#DDD6FE" stroke-width="1.5" stroke-opacity=".6"/>
      <!-- Glowing data tags beside portrait -->
      <g class="h-rise d4">
        <rect x="730" y="190" width="108" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="748" cy="204" r="4" fill="#10B981"/>
        <text font-family="ui-monospace,monospace" x="757" y="208" font-size="10" fill="#DDD6FE">AI Engineer</text>
      </g>
      <g class="h-rise d5">
        <rect x="1092" y="240" width="96" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="1110" cy="254" r="4" fill="#F59E0B"/>
        <text font-family="ui-monospace,monospace" x="1119" y="258" font-size="10" fill="#DDD6FE">ML/RAG</text>
      </g>
      <g class="h-rise d5">
        <rect x="730" y="300" width="108" height="28" rx="14" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".4"/>
        <circle cx="748" cy="314" r="4" fill="#EF4444" fill-opacity=".8"/>
        <text font-family="ui-monospace,monospace" x="757" y="318" font-size="10" fill="#DDD6FE">Pune, India</text>
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
        <text class="h-mono" x="24" y="10" font-size="11.5" letter-spacing="2.8" fill="#C4B5FD">AVAILABLE FOR AI/ML &amp; AGENTIC SYSTEMS ROLES</text>
      </g>
    </g>
    <g class="h-rise d2">
      <text class="h-serif" x="58" y="162" font-size="64" font-weight="300" letter-spacing="-1.5" fill="url(#h-ng)">Snehal Ghadge</text>
      <text class="h-serif" x="58" y="162" font-size="64" font-weight="300" letter-spacing="-1.5" fill="url(#h-sh)">Snehal Ghadge</text>
    </g>
    <g class="h-rise d3">
      <text class="h-sans" x="60" y="210" font-size="20" font-weight="400" fill="#EDE9FE">AI &amp; Agentic Systems Engineer <tspan fill="#A78BFA">·</tspan> Machine Learning Developer</text>
      <text class="h-serif" x="60" y="244" font-size="16.5" font-style="italic" fill="#C4B5FD">Building autonomous intelligence. Designing scalable reasoning workflows.</text>
    </g>
    <path class="h-draw" d="M60 274 H720" stroke="url(#h-rule)" stroke-width="1"/>
    <!-- Metadata Chips -->
    <g class="h-rise d4" transform="translate(60 306)">
      <g transform="translate(0 0)">
        <rect width="215" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="107" y="21" text-anchor="middle" font-size="11.5" fill="#DDD6FE">B.Tech CSE (AI/ML)</text>
      </g>
      <g transform="translate(227 0)">
        <rect width="225" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="112" y="21" text-anchor="middle" font-size="11.5" fill="#DDD6FE">Lenovo LEAP Scholar</text>
      </g>
      <g transform="translate(464 0)">
        <rect width="230" height="34" rx="17" fill="#1A1230" stroke="#8B5CF6" stroke-opacity=".35"/>
        <text class="h-mono" x="115" y="21" text-anchor="middle" font-size="11.5" fill="#DDD6FE">AI Intern @ Code-A-Nova</text>
      </g>
    </g>
    <g class="h-rise d5" transform="translate(60 366)">
      <g transform="translate(0 0)">
        <text class="h-serif" font-size="28" font-weight="300" fill="#FFFFFF">30+</text>
        <text class="h-sans" y="22" font-size="12" fill="#A79FB5">public repositories</text>
      </g>
      <g transform="translate(180 0)">
        <text class="h-serif" font-size="28" font-weight="300" fill="#FFFFFF">GenAI &amp; RAG</text>
        <text class="h-sans" y="22" font-size="12" fill="#A79FB5">production pipelines</text>
      </g>
      <g transform="translate(360 0)">
        <text class="h-serif" font-size="28" font-weight="300" fill="#FFFFFF">Pune, India</text>
        <text class="h-sans" y="22" font-size="12" fill="#A79FB5">PCET's NCOE</text>
      </g>
    </g>
    <!-- Frame & Trace -->
    <rect x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>
    <rect class="h-trace" x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="url(#h-tr)" stroke-width="1.8" stroke-linecap="round"/>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "snehal-hero-portrait.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)
print("snehal-hero-portrait.svg generated (pure SVG, no embedded images)")

# ─── SECTION TITLE HELPER ────────────────────────────────────────────────────
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
        + '    <radialGradient id="ta-pulse"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#DDD6FE" stop-opacity=".6"/><stop offset="1" stop-color="#A78BFA" stop-opacity="0"/></radialGradient>\n'
        + '  </defs>\n'
        + '  <style>\n'
        + '    .ta-serif{font-family:Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif}\n'
        + '    .ta-mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace}\n'
        + '    .ta-in{animation:ta-in 1.1s cubic-bezier(.16,1,.3,1) both}\n'
        + '    .ta-d2{animation-delay:.2s} .ta-d3{animation-delay:.45s}\n'
        + '    .ta-draw{stroke-dasharray:1200;stroke-dashoffset:1200;animation:ta-draw 1.8s cubic-bezier(.65,0,.35,1) .5s forwards}\n'
        + '    @keyframes ta-in{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}\n'
        + '    @keyframes ta-draw{to{stroke-dashoffset:0}}\n'
        + '    @media(prefers-reduced-motion:reduce){.ta-in{animation:none}.ta-draw{animation:none;stroke-dashoffset:0}}\n'
        + '  </style>\n'
        + '  <g class="ta-in">\n'
        + '    <text class="ta-mono" x="40" y="34" font-size="12" letter-spacing="3" fill="#A78BFA"><tspan fill="#DDD6FE">' + num_str + '</tspan>   ' + mono_label + '</text>\n'
        + '  </g>\n'
        + '  <g class="ta-in ta-d2">\n'
        + '    <text class="ta-serif" x="38" y="84" font-size="44" font-weight="300" letter-spacing="-1" fill="#F5F3FF">' + serif_main + ' <tspan font-style="italic" fill="url(#ta-sheen)">' + serif_italic + '</tspan></text>\n'
        + '  </g>\n'
        + '  <g class="ta-in ta-d3">\n'
        + '    <text class="ta-mono" x="1160" y="34" text-anchor="end" font-size="10.5" letter-spacing="2.4" fill="#A79FB5">' + right_label + '</text>\n'
        + '  </g>\n'
        + '  <path class="ta-draw" d="M40 106 H1160" stroke="url(#ta-line)" stroke-width="1"/>\n'
        + '  <circle cx="40" cy="106" r="7" fill="url(#ta-pulse)" opacity="0">\n'
        + '    <animate attributeName="cx" values="40;1160" dur="6s" begin="2.3s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>\n'
        + '    <animate attributeName="opacity" values="0;1;0" keyTimes="0;.15;1" dur="6s" begin="2.3s" repeatCount="indefinite"/>\n'
        + '  </circle>\n'
        + '</svg>'
    )
    with open(os.path.join(ASSETS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{filename} generated")

titles = [
    ("01", "ABOUT", "Hello, I'm", "Snehal.", "WHO I AM", "title-about.svg"),
    ("02", "RECOGNITION", "Proof, on the", "record.", "HONORS &amp; SCHOLARS", "title-recognition.svg"),
    ("03", "SELECTED WORK", "Products, not", "assignments.", "FLAGSHIP REPOSITORIES", "title-work.svg"),
    ("04", "TOOLKIT", "The tools I", "reach for.", "CORE CAPABILITIES", "title-toolkit.svg"),
    ("05", "COMMIT LOG", "A year of", "continuous building.", "DAILY CADENCE", "title-commits.svg"),
    ("06", "CERTIFICATIONS", "Verified credentials", "and accreditations.", "SIX CREDENTIALS", "title-certifications.svg"),
    ("07", "CONNECT", "Let's build something", "worth explaining.", "GET IN TOUCH", "title-connect.svg"),
]
for args in titles:
    make_title_svg(*args)

# ─── PROJECT CARD HELPER (fixed - no f-string chip join issue) ────────────────
def make_project_svg(slug, tag, title, tagline, built_line,
                     s1v, s1l, s2v, s2l, s3v, s3l,
                     chips, diagram_lines, outfile):
    # Build chip elements manually (no join issues)
    chip_parts = []
    x = 56
    for i, chip in enumerate(chips):
        w = max(50, len(chip) * 9 + 24)
        delay = 1.0 + i * 0.12
        cx = x + w / 2
        part = (
            '<g class="p-chip" style="animation-delay:' + f"{delay:.2f}" + 's">'
            '<rect x="' + str(x) + '" y="314" width="' + str(w) + '" height="26" rx="13" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".35"/>'
            '<text class="p-mono" x="' + f"{cx:.1f}" + '" y="331" text-anchor="middle" font-size="11.5" fill="#DDD6FE">' + chip + '</text>'
            '</g>'
        )
        chip_parts.append(part)
        x += w + 10
    chips_svg = "\n      ".join(chip_parts)
    diag_svg = "\n    ".join(diagram_lines)

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="' + slug + '-t">\n'
        + '  <title id="' + slug + '-t">' + title + ': ' + tagline + '</title>\n'
        + '  <defs>\n'
        + '    <linearGradient id="' + slug + '-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>\n'
        + '    <radialGradient id="' + slug + '-glow" cx="82%" cy="30%" r="55%"><stop offset="0" stop-color="#7C3AED" stop-opacity=".7"/><stop offset="1" stop-color="#3B0764" stop-opacity="0"/></radialGradient>\n'
        + '    <pattern id="' + slug + '-grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#8B5CF6" stroke-opacity=".08"/></pattern>\n'
        + '    <clipPath id="' + slug + '-clip"><rect width="1200" height="370" rx="18"/></clipPath>\n'
        + '    <linearGradient id="' + slug + '-trace" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></linearGradient>\n'
        + '  </defs>\n'
        + '  <style>\n'
        + '    .p-serif{font-family:Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif}\n'
        + '    .p-mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace}\n'
        + '    .p-sans{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}\n'
        + '    .p-in{animation:p-in 1.2s cubic-bezier(.16,1,.3,1) both}\n'
        + '    .p-d1{animation-delay:.15s} .p-d2{animation-delay:.4s}\n'
        + '    .p-draw{stroke-dasharray:600;stroke-dashoffset:600;animation:p-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards}\n'
        + '    .p-trace{stroke-dasharray:564 3136;stroke-dashoffset:3700;animation:p-trace 7s linear infinite}\n'
        + '    .p-chip{animation:p-chip .7s cubic-bezier(.34,1.56,.64,1) both}\n'
        + '    @keyframes p-in{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}\n'
        + '    @keyframes p-draw{to{stroke-dashoffset:0}}\n'
        + '    @keyframes p-trace{to{stroke-dashoffset:0}}\n'
        + '    @keyframes p-chip{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}\n'
        + '    @media(prefers-reduced-motion:reduce){.p-in,.p-chip{animation:none}.p-draw{animation:none;stroke-dashoffset:0}.p-trace{display:none}}\n'
        + '  </style>\n'
        + '  <g clip-path="url(#' + slug + '-clip)">\n'
        + '    <rect width="1200" height="370" fill="url(#' + slug + '-bg)"/>\n'
        + '    <rect x="720" width="480" height="370" fill="url(#' + slug + '-grid)"/>\n'
        + '    <rect width="1200" height="370" fill="url(#' + slug + '-glow)"/>\n'
        + '    <g class="p-in p-d1">\n'
        + '      <text class="p-mono" x="56" y="62" font-size="12" letter-spacing="2.6" fill="#A78BFA">' + tag + '</text>\n'
        + '      <text class="p-serif" x="54" y="126" font-size="52" font-weight="300" letter-spacing="-1.5" fill="#FFFFFF">' + title + '</text>\n'
        + '      <text class="p-sans" x="56" y="166" font-size="17" fill="#C4B5FD">' + tagline + '</text>\n'
        + '      <text class="p-mono" x="56" y="200" font-size="12.5" fill="#DDD6FE"><tspan fill="#A78BFA">BUILT ›</tspan> ' + built_line + '</text>\n'
        + '      <line class="p-draw" x1="56" y1="226" x2="680" y2="226" stroke="#8B5CF6" stroke-opacity=".3"/>\n'
        + '      <g transform="translate(56 266)"><text class="p-serif" font-size="34" font-weight="300" fill="#FFFFFF">' + s1v + '</text><text class="p-sans" y="24" font-size="12.5" fill="#A79FB5">' + s1l + '</text></g>\n'
        + '      <g transform="translate(261 266)"><text class="p-serif" font-size="34" font-weight="300" fill="#FFFFFF">' + s2v + '</text><text class="p-sans" y="24" font-size="12.5" fill="#A79FB5">' + s2l + '</text></g>\n'
        + '      <g transform="translate(466 266)"><text class="p-serif" font-size="34" font-weight="300" fill="#FFFFFF">' + s3v + '</text><text class="p-sans" y="24" font-size="12.5" fill="#A79FB5">' + s3l + '</text></g>\n'
        + '      ' + chips_svg + '\n'
        + '    </g>\n'
        + '    <g class="p-in p-d2">\n'
        + '    ' + diag_svg + '\n'
        + '    </g>\n'
        + '    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>\n'
        + '    <rect class="p-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#' + slug + '-trace)" stroke-width="1.6" stroke-linecap="round"/>\n'
        + '  </g>\n'
        + '</svg>'
    )
    with open(os.path.join(ASSETS_DIR, outfile), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{outfile} generated")

# AgentFlow diagram lines
agentflow_diag = [
    '<g transform="translate(780 35)">',
    '  <rect x="0" y="0" width="380" height="295" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".35"/>',
    '  <text class="p-mono" x="190" y="30" text-anchor="middle" font-size="10.5" letter-spacing="2" fill="#A78BFA">AGENT ORCHESTRATION GRAPH</text>',
    '  <!-- Planner Node -->',
    '  <circle cx="190" cy="80" r="36" fill="#1C1236" stroke="#C084FC" stroke-width="1.5"/>',
    '  <text class="p-mono" x="190" y="84" text-anchor="middle" font-size="11" fill="#FFFFFF">PLANNER</text>',
    '  <!-- Executor Node -->',
    '  <circle cx="90" cy="190" r="32" fill="#1C1236" stroke="#8B5CF6" stroke-width="1.2"/>',
    '  <text class="p-mono" x="90" y="194" text-anchor="middle" font-size="10.5" fill="#DDD6FE">EXECUTOR</text>',
    '  <!-- Critic Node -->',
    '  <circle cx="290" cy="190" r="32" fill="#1C1236" stroke="#8B5CF6" stroke-width="1.2"/>',
    '  <text class="p-mono" x="290" y="194" text-anchor="middle" font-size="10.5" fill="#DDD6FE">VERIFIER</text>',
    '  <!-- Tool Box -->',
    '  <rect x="120" y="248" width="140" height="34" rx="8" fill="#140D24" stroke="#A78BFA" stroke-opacity=".4"/>',
    '  <text class="p-mono" x="190" y="270" text-anchor="middle" font-size="10" fill="#C4B5FD">TOOL INVOCATION</text>',
    '  <!-- Connectors -->',
    '  <line x1="165" y1="106" x2="110" y2="162" stroke="#8B5CF6" stroke-width="1.5" stroke-dasharray="4 4"/>',
    '  <line x1="215" y1="106" x2="268" y2="162" stroke="#8B5CF6" stroke-width="1.5" stroke-dasharray="4 4"/>',
    '  <line x1="105" y1="217" x2="148" y2="248" stroke="#C084FC" stroke-width="1.5"/>',
    '  <line x1="275" y1="217" x2="232" y2="248" stroke="#C084FC" stroke-width="1.5"/>',
    '  <circle cx="190" cy="190" r="5" fill="#10B981">',
    '    <animate attributeName="opacity" values=".3;1;.3" dur="2s" repeatCount="indefinite"/>',
    '  </circle>',
    '  <text class="p-mono" x="190" y="207" text-anchor="middle" font-size="9" fill="#10B981">DISPATCH ACTIVE</text>',
    '</g>',
]

make_project_svg(
    "p-agentflow", "01 · AUTONOMOUS AGENTS · MULTI-STAGE REASONING · 2026",
    "AgentFlow-AI", "Multi-agent orchestration framework for autonomous task execution.",
    "Dynamic state-graph, automated sub-task decomposition, and tool delegation",
    "15+", "tools integrated", "&lt;1.2s", "agent dispatch latency", "99.4%", "workflow reliability",
    ["Python", "LangGraph", "FastAPI", "Redis", "Docker"],
    agentflow_diag, "project-agentflow.svg"
)

# InsightRAG diagram lines
insightrag_diag = [
    '<g transform="translate(780 30)">',
    '  <rect x="0" y="0" width="380" height="305" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".35"/>',
    '  <text class="p-mono" x="190" y="30" text-anchor="middle" font-size="10.5" letter-spacing="2" fill="#A78BFA">HYBRID RAG PIPELINE</text>',
    '  <rect x="35" y="46" width="310" height="38" rx="8" fill="#1C1236" stroke="#8B5CF6" stroke-opacity=".3"/>',
    '  <text class="p-mono" x="190" y="70" text-anchor="middle" font-size="11" fill="#FFFFFF">1. Chunking &amp; Hybrid Ingestion</text>',
    '  <rect x="35" y="100" width="146" height="42" rx="8" fill="#140D24" stroke="#A78BFA" stroke-opacity=".3"/>',
    '  <text class="p-mono" x="108" y="122" text-anchor="middle" font-size="10" fill="#DDD6FE">Vector Index</text>',
    '  <text class="p-mono" x="108" y="136" text-anchor="middle" font-size="9" fill="#A79FB5">FAISS Dense</text>',
    '  <rect x="199" y="100" width="146" height="42" rx="8" fill="#140D24" stroke="#A78BFA" stroke-opacity=".3"/>',
    '  <text class="p-mono" x="272" y="122" text-anchor="middle" font-size="10" fill="#DDD6FE">Sparse Index</text>',
    '  <text class="p-mono" x="272" y="136" text-anchor="middle" font-size="9" fill="#A79FB5">BM25 Keyword</text>',
    '  <rect x="35" y="158" width="310" height="38" rx="8" fill="#1C1236" stroke="#C084FC" stroke-opacity=".4"/>',
    '  <text class="p-mono" x="190" y="182" text-anchor="middle" font-size="11" fill="#FFFFFF">2. Reranking &amp; Semantic Cache</text>',
    '  <rect x="35" y="210" width="310" height="42" rx="8" fill="#140D24" stroke="#10B981" stroke-opacity=".4"/>',
    '  <text class="p-mono" x="190" y="232" text-anchor="middle" font-size="11" fill="#10B981">3. Grounded LLM Response</text>',
    '  <text class="p-mono" x="190" y="246" text-anchor="middle" font-size="9" fill="#A79FB5">Zero Hallucination Guardrail</text>',
    '  <line x1="108" y1="84" x2="108" y2="100" stroke="#8B5CF6" stroke-width="1" stroke-dasharray="3 3"/>',
    '  <line x1="272" y1="84" x2="272" y2="100" stroke="#8B5CF6" stroke-width="1" stroke-dasharray="3 3"/>',
    '  <line x1="190" y1="142" x2="190" y2="158" stroke="#8B5CF6" stroke-width="1" stroke-dasharray="3 3"/>',
    '  <line x1="190" y1="196" x2="190" y2="210" stroke="#8B5CF6" stroke-width="1" stroke-dasharray="3 3"/>',
    '</g>',
]

make_project_svg(
    "p-insightrag", "02 · ENTERPRISE RAG · HYBRID SEARCH · VECTOR DBS · 2026",
    "InsightRAG", "Production-grade enterprise RAG with semantic cache and hybrid search.",
    "Hybrid vector and BM25 retrieval, document re-ranking, and low-latency cache",
    "10k+", "chunks indexed", "94.8%", "retrieval precision", "4x", "faster responses",
    ["Python", "LlamaIndex", "FAISS", "LangChain", "Streamlit"],
    insightrag_diag, "project-insightrag.svg"
)

# AeroFault diagram lines
aerofault_diag = [
    '<g transform="translate(780 35)">',
    '  <rect x="0" y="0" width="380" height="295" rx="14" fill="#0B0714" stroke="#8B5CF6" stroke-opacity=".35"/>',
    '  <text class="p-mono" x="35" y="34" font-size="10.5" letter-spacing="1.5" fill="#A78BFA">LIVE TELEMETRY STREAM</text>',
    '  <!-- Waveform -->',
    '  <path d="M30 110 L80 110 L100 82 L120 138 L140 110 L190 110 L210 58 L230 162 L250 110 L300 110 L350 110" fill="none" stroke="#8B5CF6" stroke-width="2"/>',
    '  <!-- Fault circle pulse -->',
    '  <circle cx="220" cy="110" r="26" fill="#EF4444" fill-opacity=".12" stroke="#EF4444" stroke-width="1.2">',
    '    <animate attributeName="r" values="18;30;18" dur="2s" repeatCount="indefinite"/>',
    '  </circle>',
    '  <text class="p-mono" x="220" y="52" text-anchor="middle" font-size="10" fill="#EF4444">FAULT SPIKE DETECTED</text>',
    '  <!-- Diagnostics -->',
    '  <rect x="30" y="195" width="320" height="72" rx="10" fill="#140D24" stroke="#8B5CF6" stroke-opacity=".3"/>',
    '  <text class="p-mono" x="48" y="220" font-size="11" fill="#FFFFFF">STATUS: Component #4 Failure Risk</text>',
    '  <text class="p-mono" x="48" y="240" font-size="10.5" fill="#DDD6FE">Confidence: 98.2%  ·  TTF: 48h</text>',
    '  <text class="p-mono" x="48" y="258" font-size="10" fill="#10B981">Action: Maintenance Ticket Dispatched</text>',
    '</g>',
]

make_project_svg(
    "p-aerofault", "03 · PREDICTIVE ML · TIME-SERIES TELEMETRY · 2026",
    "AeroFaultAI", "Real-time aerospace telemetry anomaly detection and predictive diagnostics.",
    "Multi-sensor time-series modeling, anomaly classification, and automated alerts",
    "98.2%", "anomaly F1-score", "&lt;50ms", "inference latency", "100k+", "telemetry records",
    ["Python", "PyTorch", "Scikit-Learn", "FastAPI", "Plotly"],
    aerofault_diag, "project-aerofault.svg"
)

print("All project cards generated correctly!")

# ─── TECH STACK WITH SKILLICONS ──────────────────────────────────────────────
# skillicons.dev icon list: https://skillicons.dev
# We'll use an SVG panel + skillicons.dev image URL embed
tech_skills_svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" width="1200" height="560" role="img" aria-labelledby="tc-title tc-desc">\n'
    + '  <title id="tc-title">Snehal Ghadge Tech Stack</title>\n'
    + '  <desc id="tc-desc">Python, C++, PyTorch, LangChain, LangGraph, LlamaIndex, FAISS, FastAPI, Flask, Node.js, PostgreSQL, MongoDB, MySQL, Redis, AWS, Docker, GitHub Actions, Linux, Streamlit, PowerBI.</desc>\n'
    + '  <defs>\n'
    + '    <linearGradient id="tc-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140D24"/><stop offset="1" stop-color="#0B0714"/></linearGradient>\n'
    + '    <radialGradient id="tc-glow" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#5B21B6" stop-opacity=".7"/><stop offset="1" stop-color="#24143D" stop-opacity="0"/></radialGradient>\n'
    + '    <linearGradient id="tc-trace" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#C4B5FD"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></linearGradient>\n'
    + '  </defs>\n'
    + '  <style>\n'
    + '    .tc-serif{font-family:Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif}\n'
    + '    .tc-mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace}\n'
    + '    .tc-sans{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}\n'
    + '    .tc-trace{stroke-dasharray:600 2760;stroke-dashoffset:3360;animation:tc-trace 8s linear infinite}\n'
    + '    @keyframes tc-trace{to{stroke-dashoffset:0}}\n'
    + '    @media(prefers-reduced-motion:reduce){.tc-trace{display:none}}\n'
    + '  </style>\n'
    + '  <rect width="1200" height="560" rx="18" fill="url(#tc-bg)"/>\n'
    + '  <rect width="1200" height="560" rx="18" fill="url(#tc-glow)"/>\n'
    # Section labels
    + '  <g transform="translate(40 30)">\n'
    # Row 1: Languages & Core
    + '    <text class="tc-mono" x="0" y="22" font-size="10.5" letter-spacing="2" fill="#A78BFA">01 · LANGUAGES &amp; CORE</text>\n'
    + '    <text class="tc-mono" x="0" y="42" font-size="11" fill="#DDD6FE">Python  ·  C++  ·  TypeScript  ·  JavaScript  ·  SQL  ·  HTML  ·  CSS</text>\n'
    # Row 2: AI / ML / GenAI
    + '    <text class="tc-mono" x="0" y="82" font-size="10.5" letter-spacing="2" fill="#A78BFA">02 · AI / ML / GENAI &amp; RAG</text>\n'
    + '    <text class="tc-mono" x="0" y="102" font-size="11" fill="#DDD6FE">PyTorch  ·  TensorFlow  ·  Scikit-Learn  ·  LangChain  ·  LangGraph  ·  LlamaIndex  ·  FAISS  ·  HuggingFace  ·  OpenCV</text>\n'
    # Row 3: Backend
    + '    <text class="tc-mono" x="0" y="142" font-size="10.5" letter-spacing="2" fill="#A78BFA">03 · BACKEND &amp; APIS</text>\n'
    + '    <text class="tc-mono" x="0" y="162" font-size="11" fill="#DDD6FE">FastAPI  ·  Flask  ·  Node.js  ·  Express.js  ·  REST APIs  ·  Redis  ·  Streamlit</text>\n'
    # Row 4: Frontend
    + '    <text class="tc-mono" x="0" y="202" font-size="10.5" letter-spacing="2" fill="#A78BFA">04 · FRONTEND</text>\n'
    + '    <text class="tc-mono" x="0" y="222" font-size="11" fill="#DDD6FE">React.js  ·  Next.js  ·  TailwindCSS  ·  TypeScript  ·  JavaScript  ·  HTML  ·  CSS</text>\n'
    # Row 5: Databases
    + '    <text class="tc-mono" x="0" y="262" font-size="10.5" letter-spacing="2" fill="#A78BFA">05 · DATA &amp; DATABASES</text>\n'
    + '    <text class="tc-mono" x="0" y="282" font-size="11" fill="#DDD6FE">PostgreSQL  ·  MongoDB  ·  MySQL  ·  SQLite  ·  Redis  ·  Vector DBs (FAISS, Chroma, Pinecone)</text>\n'
    # Row 6: Cloud / DevOps
    + '    <text class="tc-mono" x="0" y="322" font-size="10.5" letter-spacing="2" fill="#A78BFA">06 · CLOUD &amp; DEVOPS</text>\n'
    + '    <text class="tc-mono" x="0" y="342" font-size="11" fill="#DDD6FE">AWS  ·  Docker  ·  GitHub Actions  ·  Linux  ·  Git  ·  CI/CD Pipelines</text>\n'
    # Row 7: Tools
    + '    <text class="tc-mono" x="0" y="382" font-size="10.5" letter-spacing="2" fill="#A78BFA">07 · TOOLS &amp; ANALYTICS</text>\n'
    + '    <text class="tc-mono" x="0" y="402" font-size="11" fill="#DDD6FE">Jupyter  ·  PowerBI  ·  Plotly  ·  Postman  ·  VS Code  ·  Pandas  ·  NumPy  ·  Matplotlib</text>\n'
    + '  </g>\n'
    # Separator lines between rows
    + '  <line x1="40" y1="56" x2="1160" y2="56" stroke="#8B5CF6" stroke-opacity=".15"/>\n'
    + '  <line x1="40" y1="116" x2="1160" y2="116" stroke="#8B5CF6" stroke-opacity=".15"/>\n'
    + '  <line x1="40" y1="176" x2="1160" y2="176" stroke="#8B5CF6" stroke-opacity=".15"/>\n'
    + '  <line x1="40" y1="236" x2="1160" y2="236" stroke="#8B5CF6" stroke-opacity=".15"/>\n'
    + '  <line x1="40" y1="296" x2="1160" y2="296" stroke="#8B5CF6" stroke-opacity=".15"/>\n'
    + '  <line x1="40" y1="356" x2="1160" y2="356" stroke="#8B5CF6" stroke-opacity=".15"/>\n'
    + '  <line x1="40" y1="416" x2="1160" y2="416" stroke="#8B5CF6" stroke-opacity=".15"/>\n'
    + '  <!-- Border & Trace -->\n'
    + '  <rect x=".5" y=".5" width="1199" height="559" rx="17.5" fill="none" stroke="#8B5CF6" stroke-opacity=".2"/>\n'
    + '  <rect class="tc-trace" x=".5" y=".5" width="1199" height="559" rx="17.5" fill="none" stroke="url(#tc-trace)" stroke-width="1.6" stroke-linecap="round"/>\n'
    + '</svg>'
)
with open(os.path.join(ASSETS_DIR, "tech-constellation.svg"), "w", encoding="utf-8") as f:
    f.write(tech_skills_svg)
print("tech-constellation.svg generated (text-based, GitHub-safe)")

# ─── ASSEMBLE README.md ───────────────────────────────────────────────────────
# skillicons row — this is an external HTTP image so GitHub will allow it
skillicons_row1 = "https://skillicons.dev/icons?i=python,cpp,typescript,js,html,css&perline=6"
skillicons_row2 = "https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn,fastapi,flask,nodejs,express,react,nextjs,tailwind&perline=10"
skillicons_row3 = "https://skillicons.dev/icons?i=postgres,mongodb,mysql,redis,aws,docker,githubactions,linux,git,vscode&perline=10"
skillicons_row4 = "https://skillicons.dev/icons?i=jupyter,postman,figma,streamlit&perline=4"

readme = (
    '<a href="https://snehalsportfolio2027.netlify.app">\n'
    '  <img src="assets/snehal-hero-portrait.svg" width="100%" alt="Snehal Ghadge — AI and Agentic Systems Engineer. Building autonomous intelligence. Designing scalable reasoning workflows.">\n'
    '</a>\n'
    '\n'
    '<p align="center">\n'
    '  <img src="assets/snehal-profile.png" width="140" height="140" alt="Snehal Ghadge — Profile Photo" />\n'
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
    '<img src="assets/about-intro.svg" width="100%" alt="About: AI and Agentic Systems Engineer and Machine Learning Developer. B.Tech in CSE (AI/ML) at Nutan College of Engineering, Pune.">\n'
    '\n'
    '<img src="assets/title-recognition.svg" width="100%" alt="02 Recognition - Proof, on the record.">\n'
    '<img src="assets/achievement-motif.svg" width="100%" alt="Lenovo LEAP NextGen Scholar via AICTE; Infosys Springboard Virtual Intern; AI Intern at Code-A-Nova; 30+ GitHub projects.">\n'
    '\n'
    '<img src="assets/title-work.svg" width="100%" alt="03 Selected work - Products, not assignments.">\n'
    '\n'
    '<a href="https://github.com/snehalghadge59-blip/AgentFlow-AI">\n'
    '  <img src="assets/project-agentflow.svg" width="100%" alt="AgentFlow-AI: Multi-agent orchestration framework for autonomous task execution.">\n'
    '</a>\n'
    '<p align="center">\n'
    '  <a href="https://github.com/snehalghadge59-blip/AgentFlow-AI"><img src="https://img.shields.io/badge/Repository-AgentFlow--AI-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="AgentFlow-AI repository"></a>\n'
    '</p>\n'
    '\n'
    '<a href="https://github.com/snehalghadge59-blip/InsightRAG">\n'
    '  <img src="assets/project-insightrag.svg" width="100%" alt="InsightRAG: Production-grade enterprise RAG with hybrid search and semantic cache.">\n'
    '</a>\n'
    '<p align="center">\n'
    '  <a href="https://github.com/snehalghadge59-blip/InsightRAG"><img src="https://img.shields.io/badge/Repository-InsightRAG-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="InsightRAG repository"></a>\n'
    '</p>\n'
    '\n'
    '<a href="https://github.com/snehalghadge59-blip/AeroFaultAI">\n'
    '  <img src="assets/project-aerofault.svg" width="100%" alt="AeroFaultAI: Real-time aerospace telemetry anomaly detection and predictive diagnostics.">\n'
    '</a>\n'
    '<p align="center">\n'
    '  <a href="https://github.com/snehalghadge59-blip/AeroFaultAI"><img src="https://img.shields.io/badge/Repository-AeroFaultAI-4C1D95?style=for-the-badge&amp;labelColor=140D24&amp;logoColor=EDE9FE&amp;logo=github" alt="AeroFaultAI repository"></a>\n'
    '</p>\n'
    '\n'
    '<img src="assets/title-toolkit.svg" width="100%" alt="04 Toolkit - The tools I reach for.">\n'
    '<img src="assets/tech-constellation.svg" width="100%" alt="Full tech stack listing.">\n'
    '\n'
    '<!-- Tech Stack Skill Icons with Logos -->\n'
    '<p align="center">\n'
    '  <b>Languages &amp; Core</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,cpp,c,ts,js,html,css,bash" alt="Python, C++, C, TypeScript, JavaScript, HTML5, CSS3, Bash" /></a>\n'
    '</p>\n'
    '<p align="center">\n'
    '  <b>AI, Machine Learning &amp; Frameworks</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn,fastapi,flask" alt="PyTorch, TensorFlow, Scikit-Learn, FastAPI, Flask" /></a>\n'
    '</p>\n'
    '<p align="center">\n'
    '  <b>Full-Stack Web Development</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=react,nextjs,nodejs,express,tailwind" alt="React, Next.js, Node.js, Express, Tailwind CSS" /></a>\n'
    '</p>\n'
    '<p align="center">\n'
    '  <b>Databases, Cloud &amp; Infrastructure</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=postgres,mongodb,mysql,redis,aws,docker,linux,git,github,githubactions" alt="PostgreSQL, MongoDB, MySQL, Redis, AWS, Docker, Linux, Git, GitHub, GitHub Actions" /></a>\n'
    '</p>\n'
    '<p align="center">\n'
    '  <b>Developer Tools &amp; Productivity</b><br/>\n'
    '  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=vscode,postman,figma" alt="VS Code, Postman, Figma" /></a>\n'
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
    '  <img src="assets/footer-signature.svg" width="100%" alt="Snehal - Engineering intelligence that creates real-world impact.">\n'
    '</a>\n'
)

with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)

print("README.md assembled and written!")
print("DONE - all files generated without embedded binary data")
