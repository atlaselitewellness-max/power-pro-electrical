from PIL import Image, ImageDraw, ImageFont

NAVY = (15, 30, 46, 255)
NAVY_DARK = (10, 20, 32, 255)
AMBER_LIGHT = (245, 184, 61, 255)
AMBER_DARK = (212, 135, 15, 255)
WHITE = (255, 255, 255, 255)

FONT_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
FONT_BLACK = "C:/Windows/Fonts/arialbd.ttf"


def rounded_rect_gradient(size, radius, c1, c2):
    w, h = size
    base = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    grad = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    for y in range(h):
        t = y / max(1, h - 1)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        for x in range(w):
            grad.putpixel((x, y), (r, g, b, 255))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    base.paste(grad, (0, 0), mask)
    return base


def bolt_path(cx, cy, scale):
    pts = [
        (0.55, -0.85), (-0.05, -0.05), (0.30, -0.05), (-0.20, 0.85),
        (0.55, 0.05), (0.15, 0.05),
    ]
    return [(cx + x * scale, cy + y * scale) for x, y in pts]


def make_icon(path, size=512, badge_only=True):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    badge = rounded_rect_gradient((size, size), int(size * 0.22), AMBER_LIGHT, AMBER_DARK)
    img.paste(badge, (0, 0), badge)
    draw = ImageDraw.Draw(img)
    bolt = bolt_path(size / 2, size / 2 + size * 0.02, size * 0.42)
    draw.polygon(bolt, fill=NAVY_DARK)
    img.save(path)


def make_horizontal_logo(path, height=420):
    pad = int(height * 0.12)
    icon_size = height - pad * 2
    gap = int(height * 0.18)
    text_lines = ["POWER PRO", "ELECTRICAL"]

    f1 = ImageFont.truetype(FONT_BLACK, int(height * 0.30))
    f2 = ImageFont.truetype(FONT_BOLD, int(height * 0.18))

    tmp = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(tmp)
    w1 = d.textbbox((0, 0), text_lines[0], font=f1)[2]
    w2 = d.textbbox((0, 0), text_lines[1], font=f2)[2]
    text_w = max(w1, w2)

    width = pad + icon_size + gap + text_w + pad
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    badge = rounded_rect_gradient((icon_size, icon_size), int(icon_size * 0.22), AMBER_LIGHT, AMBER_DARK)
    img.paste(badge, (pad, pad), badge)
    draw = ImageDraw.Draw(img)
    bolt = bolt_path(pad + icon_size / 2, pad + icon_size / 2 + icon_size * 0.02, icon_size * 0.42)
    draw.polygon(bolt, fill=NAVY_DARK)

    tx = pad + icon_size + gap
    line1_y = height / 2 - int(height * 0.22)
    line2_y = height / 2 + int(height * 0.09)
    draw.text((tx, line1_y), text_lines[0], font=f1, fill=NAVY)
    draw.text((tx, line2_y), text_lines[1], font=f2, fill=AMBER_DARK)

    img.save(path)


make_icon("logo-icon.png", 512)
make_horizontal_logo("logo-horizontal.png", 420)
print("done")
