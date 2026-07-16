#!/usr/bin/env python3
"""
oshico profile README generator — Catppuccin Mocha, full animation.
Generates: assets/banner.svg, assets/fastfetch.svg, assets/avatar.svg
Inspired by Wired-Navi0x1F's animated-SVG approach.
"""
import html, os

# ------------------------------------------------------------------ palette
C = {
    "base": "#1e1e2e", "mantle": "#181825", "crust": "#11111b",
    "surface0": "#313244", "surface1": "#45475a", "overlay": "#6c7086",
    "text": "#cdd6f4", "subtext": "#a6adc8",
    "mauve": "#cba6f7", "blue": "#89b4fa", "sapphire": "#74c7ec",
    "teal": "#94e2d5", "sky": "#89dceb", "green": "#a6e3a1",
    "yellow": "#f9e2af", "peach": "#fab387", "red": "#f38ba8",
    "pink": "#f5c2e7", "lavender": "#b4befe",
}
MONO = "'JetBrains Mono','Fira Code','Cascadia Code',Menlo,Consolas,monospace"

def esc(s): return html.escape(s, quote=False)

# ================================================================== fastfetch
ARCH = """\
                  -`
                 .o+`
                `ooo/
               `+oooo:
              `+oooooo:
              -+oooooo+:
            `/:-:++oooo+:
           `/++++/+++++++:
          `/++++++++++++++:
         `/+++ooooooooooooo/`
        ./ooosssso++osssssso+`
       .oossssso-````/ossssss+`
      -osssssso.      :ssssssso.
     :osssssss/        osssso+++.
    /ossssssss/        +ssssooo/-
  `/ossssso+/:-        -:/+osssso+-
 `+sso+:-`                 `.-/+oso:
`++:.                           `-/+/
.`                                 `/""".split("\n")

INFO = [
    ("user", "oshico", "arch"),
    ("sep",),
    ("kv", "OS", "Arch Linux x86_64", "blue"),
    ("kv", "Host", "Portugal", "blue"),
    ("kv", "Kernel", "informatics-engineering 6.22-MSc", "blue"),
    ("kv", "Uptime", "22 years", "blue"),
    ("kv", "Shell", "bash", "blue"),
    ("kv", "DE", "Linux (daily driver)", "blue"),
    ("kv", "Packages", "clean-code, docs, open-source (AUR)", "blue"),
    ("kv", "Languages", "C C++ Rust Go Zig Java Kotlin Python", "mauve"),
    ("kv", "Web", "TypeScript PHP React Spring Laravel", "mauve"),
    ("kv", "Databases", "PostgreSQL MongoDB SQL-Server", "mauve"),
    ("kv", "Tools", "git docker cmake gh-actions postman", "mauve"),
    ("kv", "Now", "MSc + building reliable software", "green"),
]

def gen_fastfetch():
    W, H = 840, 470
    LH, FS = 17, 13
    CW = 7.9
    top, logo_x = 92, 30
    info_x = logo_x + int(38 * CW) + 26
    cmd = "fastfetch"

    # --- timings
    t_type0, t_char = 0.5, 0.09                      # command typing
    t_out = t_type0 + len(cmd) * t_char + 0.25       # output begins
    t_logo_step, t_info_step = 0.045, 0.09
    t_pal = t_out + len(INFO) * t_info_step + 0.3    # palette blocks
    t_prompt = t_pal + 0.9                           # final prompt

    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}" font-size="{FS}px">')
    s.append(f'''<style>
  .ln{{opacity:0;animation:in .35s ease-out forwards}}
  .ch{{opacity:0;animation:pop .01s steps(1) forwards}}
  .pb{{opacity:0;transform-origin:center;animation:in .3s ease-out forwards}}
  .glow{{text-shadow:0 0 6px rgba(203,166,247,.55)}}
  .bglow{{text-shadow:0 0 6px rgba(137,180,250,.5)}}
  @keyframes in{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
  @keyframes pop{{to{{opacity:1}}}}
  @keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
  .cur{{animation:blink 1.1s steps(1) infinite}}
</style>''')

    # bezel + screen
    s.append(f'<rect width="{W}" height="{H}" rx="12" fill="{C["crust"]}"/>')
    s.append(f'<rect x="3" y="3" width="{W-6}" height="{H-6}" rx="10" fill="{C["base"]}" stroke="{C["surface1"]}" stroke-width="1.5"/>')

    # title bar
    s.append(f'<rect x="3" y="3" width="{W-6}" height="34" rx="10" fill="{C["mantle"]}"/>')
    s.append(f'<rect x="3" y="27" width="{W-6}" height="10" fill="{C["mantle"]}"/>')
    for cx, col in ((26, "red"), (46, "yellow"), (66, "green")):
        s.append(f'<circle cx="{cx}" cy="20" r="5.5" fill="{C[col]}"/>')
    s.append(f'<text x="{W/2}" y="24" text-anchor="middle" fill="{C["subtext"]}" font-size="11.5px">oshico@arch: ~</text>')

    # typed command:  ❯ fastfetch
    py = 62
    s.append(f'<text x="{logo_x}" y="{py}" class="glow"><tspan fill="{C["green"]}" font-weight="bold">❯ </tspan></text>')
    for i, ch in enumerate(cmd):
        x = logo_x + (2 + i) * CW
        s.append(f'<text x="{x:.1f}" y="{py}" fill="{C["text"]}" class="ch" style="animation-delay:{t_type0 + i*t_char:.2f}s">{ch}</text>')
    # typing caret that disappears when output starts
    s.append(f'<rect x="{logo_x + 2*CW:.0f}" y="{py-11}" width="8" height="14" fill="{C["mauve"]}" opacity="0">'
             f'<animate attributeName="opacity" values="0;1;1;0;1;1;0" keyTimes="0;0.001;0.3;0.35;0.65;0.7;1" dur="{t_out}s" begin="0s" fill="freeze"/>'
             f'<animate attributeName="x" values="{logo_x + 2*CW:.0f};{logo_x + (2+len(cmd))*CW:.0f}" calcMode="discrete" dur="{len(cmd)*t_char:.2f}s" begin="{t_type0}s" fill="freeze"/>'
             f'</rect>')

    # arch logo (staggered, blue glow)
    for i, line in enumerate(ARCH):
        y = top + i * LH
        d = t_out + i * t_logo_step
        s.append(f'<text x="{logo_x}" y="{y}" xml:space="preserve" fill="{C["blue"]}" class="ln bglow" style="animation-delay:{d:.2f}s">{esc(line)}</text>')

    # info column (staggered)
    y = top
    for i, item in enumerate(INFO):
        d = t_out + 0.1 + i * t_info_step
        if item[0] == "user":
            _, u, h = item
            s.append(f'<text x="{info_x}" y="{y}" class="ln glow" style="animation-delay:{d:.2f}s">'
                     f'<tspan fill="{C["mauve"]}" font-weight="bold">{u}</tspan>'
                     f'<tspan fill="{C["text"]}">@</tspan>'
                     f'<tspan fill="{C["mauve"]}" font-weight="bold">{h}</tspan></text>')
        elif item[0] == "sep":
            s.append(f'<text x="{info_x}" y="{y}" fill="{C["overlay"]}" class="ln" style="animation-delay:{d:.2f}s">-----------</text>')
        else:
            _, k, v, col = item
            s.append(f'<text x="{info_x}" y="{y}" class="ln" style="animation-delay:{d:.2f}s">'
                     f'<tspan fill="{C[col]}" font-weight="bold">{esc(k)}</tspan>'
                     f'<tspan fill="{C["text"]}">: {esc(v)}</tspan></text>')
        y += LH

    # palette blocks pop in
    pal = ["surface1", "red", "green", "yellow", "blue", "mauve", "teal", "text"]
    pal2 = ["overlay", "pink", "teal", "peach", "sapphire", "lavender", "sky", "subtext"]
    bw, bh = 26, 12
    for r, row in enumerate((pal, pal2)):
        for i, col in enumerate(row):
            d = t_pal + (r * 8 + i) * 0.05
            s.append(f'<rect x="{info_x + i*bw}" y="{y - 8 + r*bh}" width="{bw}" height="{bh}" fill="{C[col]}" class="pb" style="animation-delay:{d:.2f}s"/>')

    # final prompt + blinking cursor (inline █ so it tracks the text exactly)
    fy = top + len(ARCH) * LH + LH + 2
    s.append(f'<g class="ln" style="animation-delay:{t_prompt:.2f}s">'
             f'<text x="{logo_x}" y="{fy}" class="glow"><tspan fill="{C["green"]}" font-weight="bold">❯ </tspan>'
             f'<tspan fill="{C["subtext"]}">./hire_me --clean-code </tspan>'
             f'<tspan fill="{C["mauve"]}" class="cur">█</tspan></text></g>')

    s.append('</svg>')
    return "\n".join(s)

# ================================================================== banner
BANNER = """\
 ██████╗ ███████╗██╗  ██╗██╗ ██████╗ ██████╗
██╔═══██╗██╔════╝██║  ██║██║██╔════╝██╔═══██╗
██║   ██║███████╗███████║██║██║     ██║   ██║
██║   ██║╚════██║██╔══██║██║██║     ██║   ██║
╚██████╔╝███████║██║  ██║██║╚██████╗╚██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝""".split("\n")

def gen_banner():
    FS, LH = 15, 17
    W, H = 620, 40 + len(BANNER) * LH
    y0 = 34
    width = max(len(l) for l in BANNER)
    lines = [l.ljust(width) for l in BANNER]

    def layer(fill, cls, extra=""):
        out = [f'<g class="{cls}" {extra}>']
        for i, ln in enumerate(lines):
            out.append(f'<text x="{W//2}" y="{y0 + i*LH}" text-anchor="middle" xml:space="preserve" fill="{fill}">{esc(ln)}</text>')
        out.append('</g>')
        return "\n".join(out)

    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}" font-size="{FS}px" font-weight="bold">')
    s.append(f'''<style>
  .main{{text-shadow:0 0 10px rgba(203,166,247,.65)}}
  .gR{{animation:gr 6s steps(2) infinite;opacity:0}}
  .gB{{animation:gb 6s steps(2) infinite;opacity:0}}
  .main{{animation:jit 6s steps(2) infinite}}
  @keyframes gr{{0%,88%{{opacity:0;transform:none}}89%,92%{{opacity:.75;transform:translate(3px,-1px)}}93%,100%{{opacity:0}}}}
  @keyframes gb{{0%,88%{{opacity:0;transform:none}}89%,92%{{opacity:.75;transform:translate(-3px,1px)}}93%,100%{{opacity:0}}}}
  @keyframes jit{{0%,88%,94%,100%{{transform:none}}90%,92%{{transform:translate(1px,0)}}}}
  @keyframes sweep{{from{{transform:translateX(-{W}px)}}to{{transform:translateX({W}px)}}}}
  .sw{{animation:sweep 5s linear infinite}}
</style>''')
    s.append(f'<defs><linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">'
             f'<stop offset="0%" stop-color="#fff" stop-opacity="0"/>'
             f'<stop offset="50%" stop-color="{C["lavender"]}" stop-opacity=".16"/>'
             f'<stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>'
             f'<clipPath id="bclip"><rect width="{W}" height="{H}"/></clipPath></defs>')
    s.append(layer(C["red"], "gR"))
    s.append(layer(C["blue"], "gB"))
    s.append(layer(C["mauve"], "main"))
    s.append(f'<g clip-path="url(#bclip)"><rect class="sw" width="{W//2}" height="{H}" fill="url(#sheen)"/></g>')
    s.append('</svg>')
    return "\n".join(s)

# ================================================================== main
def main():
    os.makedirs("assets", exist_ok=True)
    for name, gen in (("fastfetch", gen_fastfetch), ("banner", gen_banner)):
        svg = gen()
        path = f"assets/{name}.svg"
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"wrote {path} ({len(svg)} bytes)")

if __name__ == "__main__":
    main()