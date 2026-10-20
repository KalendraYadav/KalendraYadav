import math, os, base64
BG="#060B18";LINE="#1B3A7A";BLUE="#2F7BFF";RED="#FF2D55";TXT="#E6EDFF";DIM="#7F90B8"
F="font-family=\"Impact,'Arial Black',Haettenschweiler,sans-serif\" font-weight=\"bold\""
M="font-family=\"'Courier New',ui-monospace,monospace\""
S="font-family=\"'Segoe UI',Arial,sans-serif\""
os.makedirs("assets",exist_ok=True)
PH=None
for n in ("photo.png","photo.jpg","photo.jpeg"):
    p=os.path.join("assets",n)
    if os.path.exists(p):
        PH="data:image/%s;base64,%s"%("png" if n.endswith("png") else "jpeg",base64.b64encode(open(p,"rb").read()).decode());break
def wrap(w,h,body,extra=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="#7AD0FF"/></linearGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{LINE}" stroke-opacity=".25"/></pattern>
<radialGradient id="glow" cx=".8" cy=".3" r=".7"><stop offset="0" stop-color="{BLUE}" stop-opacity=".35"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<radialGradient id="glow2" cx=".1" cy=".9" r=".6"><stop offset="0" stop-color="{RED}" stop-opacity=".25"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></radialGradient>{extra}</defs>
<rect width="{w}" height="{h}" rx="14" fill="{BG}"/><rect width="{w}" height="{h}" rx="14" fill="url(#grid)"/>
<rect width="{w}" height="{h}" rx="14" fill="url(#glow)"/><rect width="{w}" height="{h}" rx="14" fill="url(#glow2)"/>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="14" fill="none" stroke="{LINE}"/>{body}</svg>'''
def w(n,s): open(f"assets/{n}.svg","w",encoding="utf-8").write(s)

# 1 HERO
w("hero",wrap(900,300,f'''
<rect x="40" y="38" width="130" height="24" rx="4" fill="none" stroke="{BLUE}"/><circle cx="56" cy="50" r="4" fill="#27E08A"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
<text x="68" y="55" {M} font-size="12" fill="{TXT}">OPEN TO BUILD</text>
<text x="40" y="100" {S} font-size="22" fill="{DIM}">Hi there, I'm</text>
<text x="38" y="170" {F} font-size="76" fill="{TXT}" letter-spacing="2">KALENDRA</text>
<text x="38" y="245" {F} font-size="76" fill="url(#g)" letter-spacing="2">YADAV</text>
<text x="560" y="150" {F} font-size="30" fill="{TXT}">BUILD.</text><text x="560" y="182" {F} font-size="30" fill="{RED}">SHIP.</text><text x="560" y="214" {F} font-size="30" fill="{BLUE}">SCALE.</text>
<text x="40" y="278" {S} font-size="15" fill="{DIM}">Developer · Solo founder · Turning ideas into production software</text>
<g {M} font-size="12" fill="{DIM}"><text x="720" y="56">// NeuralHack</text><text x="720" y="74">// Startup Mindset</text></g>'''))

# 2 BUILD CARD
def step(x,n,t,c): return f'<rect x="{x}" y="0" width="120" height="70" rx="8" fill="#0F1D3D" stroke="{c}"/><text x="{x+12}" y="26" {M} font-size="13" fill="{c}">{n}</text><text x="{x+12}" y="52" {M} font-size="13" fill="{TXT}">{t}</text>'
w("build",wrap(440,330,f'''
<text x="24" y="40" {M} font-size="12" fill="{BLUE}">01 / FROM THOUGHT TO THING</text>
<text x="24" y="84" {F} font-size="27" fill="{TXT}">IDEAS. BUILT DIFFERENT.</text>
<rect x="24" y="104" width="392" height="108" rx="10" fill="#0A1530" stroke="{LINE}"/>
<text x="38" y="128" {M} font-size="12" fill="{DIM}">&gt; turn_curiosity_into_impact()</text>
<g transform="translate(38,142)">{step(0,"01","CREATE",BLUE)}</g><g transform="translate(168,142)">{step(0,"02","ITERATE",BLUE)}</g><g transform="translate(298,142)">{step(0,"03","SHIP",RED)}</g>
<g {S} font-size="14" fill="{TXT}"><circle cx="34" cy="240" r="5" fill="{BLUE}"/><text x="50" y="245">Modern Web &amp; App Dev</text>
<circle cx="34" cy="270" r="5" fill="{BLUE}"/><text x="50" y="275">AI &amp; Cloud Integration</text>
<circle cx="34" cy="300" r="5" fill="{RED}"/><text x="50" y="305">Hackathons &amp; Startups</text></g>'''))

# 3 BEYOND CARD (photo slot)
if PH:
    ph_def='<clipPath id="pc"><rect x="24" y="116" width="150" height="170" rx="10"/></clipPath>'
    ph=f'<image href="{PH}" x="24" y="116" width="150" height="170" preserveAspectRatio="xMidYMid slice" clip-path="url(#pc)"/><rect x="24" y="116" width="150" height="170" rx="10" fill="none" stroke="{LINE}"/>'
else:
    ph_def='';ph=f'<rect x="24" y="116" width="150" height="170" rx="10" fill="#0F1D3D" stroke="{LINE}"/><circle cx="99" cy="178" r="30" fill="#16285A"/><path d="M45 286c0-34 24-52 54-52s54 18 54 52z" fill="#16285A"/><text x="99" y="276" {M} font-size="10" fill="{DIM}" text-anchor="middle">YOUR PHOTO</text>'
w("beyond",wrap(440,330,f'''
<text x="24" y="40" {M} font-size="12" fill="{BLUE}">02 / LIFE OUTSIDE THE COMMIT</text>
<text x="24" y="84" {F} font-size="27" fill="{TXT}">MORE THAN A JOB TITLE.</text>
<rect x="24" y="94" width="120" height="3" fill="{BLUE}"/><rect x="150" y="94" width="60" height="3" fill="{RED}"/>
{ph}
<g {M} font-size="14"><text x="200" y="140" fill="{RED}">01</text><text x="232" y="140" fill="{TXT}">FIND THE GAP</text>
<text x="200" y="180" fill="{RED}">02</text><text x="232" y="180" fill="{TXT}">BUILD THE FIX</text>
<text x="200" y="220" fill="{RED}">03</text><text x="232" y="220" fill="{TXT}">TAKE IT LIVE</text></g>
<text x="200" y="262" {M} font-size="11" fill="{DIM}">MAKE THE NEXT MOVE.</text>
<text x="200" y="284" {F} font-size="16" fill="{BLUE}">COLLAB &amp; OPEN SOURCE</text>''',ph_def))

# 4 STACK / ORBIT
def chip(x,y,t): return f'<rect x="{x}" y="{y}" width="108" height="34" rx="6" fill="#0F1D3D" stroke="{LINE}"/><text x="{x+54}" y="{y+22}" {M} font-size="13" fill="{TXT}" text-anchor="middle">{t}</text>'
orb="".join(f'<circle cx="{150+110*math.cos(a)}" cy="{170+110*math.sin(a)}" r="9" fill="{c}"><animateTransform attributeName="transform" type="rotate" from="0 150 170" to="360 150 170" dur="14s" repeatCount="indefinite"/></circle>' for a,c in [(0.4,RED),(2.4,BLUE),(4.3,"#7AD0FF")])
w("stack",wrap(900,330,f'''
<text x="24" y="40" {M} font-size="12" fill="{BLUE}">03 / MY ENGINE ROOM</text>
<text x="24" y="84" {F} font-size="30" fill="{TXT}">TOOLS CHANGE. CURIOSITY DOESN'T.</text>
<circle cx="150" cy="190" r="100" fill="none" stroke="{LINE}" stroke-dasharray="4 6"/><circle cx="150" cy="190" r="60" fill="none" stroke="{LINE}"/>
<g transform="translate(0,20)">{orb}</g>
<rect x="118" y="158" width="64" height="64" rx="12" fill="#0F1D3D" stroke="{BLUE}"/><text x="150" y="198" {F} font-size="26" fill="{BLUE}" text-anchor="middle">KY</text>
<g transform="translate(330,110)"><text y="-6" {M} font-size="11" fill="{DIM}">LANGUAGES</text>{chip(0,0,"Java")}{chip(120,0,"TypeScript")}{chip(240,0,"Python")}{chip(360,0,"JavaScript")}
<text y="68" {M} font-size="11" fill="{DIM}">FRONTEND &amp; RUNTIME</text><g transform="translate(0,74)">{chip(0,0,"React")}{chip(120,0,"Next.js")}{chip(240,0,"Node.js")}{chip(360,0,"HTML/CSS")}</g>
<text y="148" {M} font-size="11" fill="{DIM}">BACKEND, CLOUD &amp; AI</text><g transform="translate(0,154)">{chip(0,0,"Prisma")}{chip(120,0,"Railway")}{chip(240,0,"Express")}{chip(360,0,"LLM APIs")}</g></g>'''))

# 5 IMPACT (real numbers only)
def stat(x,n,l,c): return f'<rect x="{x}" y="0" width="130" height="84" rx="10" fill="#0F1D3D" stroke="{LINE}"/><text x="{x+65}" y="46" {F} font-size="40" fill="{c}" text-anchor="middle">{n}</text><text x="{x+65}" y="68" {M} font-size="11" fill="{DIM}" text-anchor="middle">{l}</text>'
w("impact",wrap(900,230,f'''
<text x="24" y="40" {M} font-size="12" fill="{BLUE}">04 / BUILDER ESSENTIALS</text>
<text x="24" y="84" {F} font-size="30" fill="{TXT}">REAL WORK. REAL IMPACT.</text>
<g transform="translate(24,110)">{stat(0,"37","REPOSITORIES",RED)}{stat(150,"5","STARS",BLUE)}{stat(300,"13","TELEBOT ★",BLUE)}</g>
<text x="500" y="128" {M} font-size="11" fill="{DIM}">FEATURED REPOSITORIES</text>
<g {M} font-size="13" fill="{TXT}"><text x="500" y="154">telebot</text><rect x="600" y="144" width="280" height="8" rx="4" fill="#0F1D3D"/><rect x="600" y="144" width="200" height="8" rx="4" fill="{BLUE}"/>
<text x="500" y="182">aibharat</text><rect x="600" y="172" width="280" height="8" rx="4" fill="#0F1D3D"/><rect x="600" y="172" width="150" height="8" rx="4" fill="{BLUE}"/>
<text x="500" y="210">campusex</text><rect x="600" y="200" width="280" height="8" rx="4" fill="#0F1D3D"/><rect x="600" y="200" width="110" height="8" rx="4" fill="{RED}"/></g>'''))

# 6 BUILDER PASS (photo slot)
if PH:
    p_def='<clipPath id="pp"><circle cx="150" cy="160" r="48"/></clipPath>'
    p_img=f'<circle cx="150" cy="160" r="50" fill="#16285A"/><image href="{PH}" x="102" y="112" width="96" height="96" preserveAspectRatio="xMidYMid slice" clip-path="url(#pp)"/>'
else:
    p_def='';p_img='<circle cx="150" cy="160" r="48" fill="#16285A"/><path d="M80 262c0-48 32-66 70-66s70 18 70 66z" fill="#16285A"/>'
bars="".join(f'<rect x="{40+i*5}" y="338" width="{2 if i%3 else 3}" height="36" opacity=".7"/>' for i in range(44))
w("pass",wrap(300,420,f'''
<rect x="125" y="0" width="50" height="46" fill="{BLUE}"/><rect x="138" y="14" width="24" height="8" rx="4" fill="{BG}"/>
<rect x="24" y="46" width="252" height="350" rx="14" fill="#0F1D3D" stroke="{RED}"/>
<text x="40" y="76" {M} font-size="11" fill="{DIM}">05 / BUILDER PASS</text><text x="236" y="76" {M} font-size="11" fill="{BLUE}">BETA</text>
{p_img}
<text x="40" y="300" {F} font-size="24" fill="{TXT}">KALENDRA YADAV</text>
<text x="40" y="320" {M} font-size="11" fill="{DIM}">DEVELOPER / FOUNDER</text>
<g fill="{TXT}">{bars}</g>
<rect x="228" y="82" width="32" height="24" rx="4" fill="#E6B84C"/>''',p_def))

# 7 CONNECT
def link(y,t,sub): return f'<rect x="460" y="{y}" width="416" height="52" rx="10" fill="#0F1D3D" stroke="{LINE}"/><text x="480" y="{y+24}" {F} font-size="18" fill="{TXT}">{t}</text><text x="480" y="{y+42}" {M} font-size="11" fill="{DIM}">{sub}</text><text x="850" y="{y+32}" {S} font-size="20" fill="{BLUE}">→</text>'
w("connect",wrap(900,260,f'''
<text x="24" y="40" {M} font-size="12" fill="{BLUE}">06 / START A CONVERSATION</text>
<text x="24" y="120" {F} font-size="64" fill="{TXT}">LET'S</text><text x="24" y="188" {F} font-size="64" fill="url(#g)">CONNECT.</text>
<text x="24" y="226" {S} font-size="14" fill="{DIM}">Ideas. Opportunities. Your next hack.</text>
<text x="460" y="50" {F} font-size="26" fill="{TXT}">BUILD SOMETHING GREAT.</text>
{link(70,"LINKEDIN","linkedin.com/in/kalendra-yadav")}{link(130,"INSTAGRAM","@kalyadavv")}{link(190,"EMAIL","kalendrak527@gmail.com")}'''))

open("README.md","w",encoding="utf-8").write('''<div align="center">

<img src="assets/hero.svg" alt="Kalendra Yadav - Build. Ship. Scale." width="100%"/>

<table>
<tr>
<td width="50%"><img src="assets/build.svg" alt="Ideas. Built different." width="100%"/></td>
<td width="50%"><img src="assets/beyond.svg" alt="More than a job title." width="100%"/></td>
</tr>
</table>

<img src="assets/stack.svg" alt="Tools change. Curiosity doesn't." width="100%"/>

<table>
<tr>
<td width="25%"><img src="assets/pass.svg" alt="Builder pass" width="100%"/></td>
<td width="75%"><img src="assets/impact.svg" alt="Real work. Real impact." width="100%"/></td>
</tr>
</table>

<img src="assets/connect.svg" alt="Let's connect" width="100%"/>

<a href="https://github.com/KalendraYadav"><img src="https://github-readme-stats.vercel.app/api?username=KalendraYadav&show_icons=true&theme=dark&bg_color=060B18&border_color=1B3A7A&title_color=2F7BFF&icon_color=FF2D55" height="150" alt="GitHub stats"/></a>
<a href="https://github.com/KalendraYadav"><img src="https://streak-stats.demolab.com/?user=KalendraYadav&theme=dark&background=060B18&border=1B3A7A&ring=2F7BFF&fire=FF2D55&currStreakLabel=2F7BFF" height="150" alt="Contribution streak"/></a>

</div>
''')
print("done")
