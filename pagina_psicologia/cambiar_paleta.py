import re
import shutil
import colorsys

SRC = "index.html"
shutil.copy(SRC, SRC + ".bak")  # respaldo por si quieres revertir
html = open(SRC, encoding="utf-8").read()

# Colores de la paleta anterior (RGB) -> nueva paleta
# petróleo #365B58 | arena #EDE4D8 | blanco roto #FAF8F4 | gris #77736E | carbón #303735
MAP = {
    (244, 247, 245): (250, 248, 244),  # sage-50   -> blanco roto
    (234, 240, 236): (237, 228, 216),  # sage-100  -> arena
    (210, 224, 215): (220, 208, 192),  # sage-200  -> arena oscura (bordes/acentos)
    (107, 142, 123): (54, 91, 88),     # sage-500  -> petróleo
    (88, 119, 102):  (42, 71, 68),     # sage-600  -> petróleo oscuro (hover)
    (70, 96, 82):    (54, 91, 88),     # sage-700  -> petróleo
    (55, 75, 64):    (42, 71, 68),     # sage-800  -> petróleo oscuro
    (253, 251, 247): (250, 248, 244),  # beige-50  -> blanco roto
    (247, 243, 235): (237, 228, 216),  # beige-100 -> arena
    (239, 234, 225): (220, 208, 192),  # beige-200 -> arena oscura
    (227, 218, 205): (220, 208, 192),  # beige-300 -> arena oscura
    (44, 53, 49):    (48, 55, 53),     # charcoal-800 -> carbón
    (28, 35, 32):    (48, 55, 53),     # charcoal-900 -> carbón
}

HEX_MAP = {
    "6B8E7B": "365B58",
    "FDFBF7": "FAF8F4",
    "2C3531": "303735",
    "1C2320": "303735",
}


def nearest(rgb):
    best, best_d = None, 1e9
    for src, dst in MAP.items():
        d = sum((a - b) ** 2 for a, b in zip(rgb, src)) ** 0.5
        if d < best_d:
            best, best_d = dst, d
    return best if best_d <= 4 else None


def sub_rgb(m):
    rgb = (int(m.group(2)), int(m.group(4)), int(m.group(6)))
    new = nearest(rgb)
    if not new:
        return m.group(0)
    return f"{m.group(1)}{new[0]}{m.group(3)}{new[1]}{m.group(5)}{new[2]}"


def sub_hsla(m):
    h, s, l, a = float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    rgb = (round(r * 255), round(g * 255), round(b * 255))
    new = nearest(rgb)
    if not new:
        return m.group(0)
    return f"rgba({new[0]},{new[1]},{new[2]},{a})"


# 1) Colores en formato rgb()/rgba() del CSS compilado
html = re.sub(r"(rgba?\()(\d+)([\s,]+)(\d+)([\s,]+)(\d+)", sub_rgb, html)

# 2) Colores en formato hsla()
html = re.sub(r"hsla\(([\d.]+),\s*([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)\)", sub_hsla, html)

# 3) Colores en hexadecimal (meta theme-color, favicon, body, focus, sombras)
for old, new in HEX_MAP.items():
    html = re.sub(old, new, html, flags=re.IGNORECASE)

# 4) Textos secundarios: carbón con opacidad -> gris cálido
html = re.sub(r"text-charcoal-800/(50|60|70|75|80)\b", "text-gris", html)
html = html.replace(
    "</head>",
    "<style>.text-gris{--tw-text-opacity:1;color:#77736E}</style>\n</head>",
    1,
)

open(SRC, "w", encoding="utf-8").write(html)
print("Listo: index.html actualizado. Respaldo en index.html.bak")
