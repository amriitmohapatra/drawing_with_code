"""Flowers in a vase, drawn with matplotlib primitives.

Run:  python3 flower_vase/flower_vase.py
Output: flower_vase/flower_vase.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon, Rectangle

OUT = Path(__file__).with_name("flower_vase.png")

# Palette
WALL = "#f4ecdf"
TABLE = "#b98a5e"
TABLE_EDGE = "#8f6440"
VASE = "#3f6f9a"
VASE_DARK = "#2c4f70"
VASE_LIGHT = "#8fb3d1"
STEM = "#4f7a3a"
LEAF = "#6a9a4a"


def bezier(p0, p1, p2, n=60):
    """Quadratic Bezier curve through control points p0, p1, p2."""
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2 = map(np.asarray, (p0, p1, p2))
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2


def vase_profile(y):
    """Half-width of the vase at height y (y from 0 at base to 1 at lip)."""
    belly = 0.62 * np.exp(-(((y - 0.35) / 0.24) ** 2))
    lip = 0.2 * np.clip((y - 0.8) / 0.2, 0, 1) ** 2
    return 0.3 + belly + lip


def draw_vase(ax, cx=0.0, base=-3.25, height=3.4, scale=1.3):
    ys = np.linspace(0, 1, 200)
    half = vase_profile(ys) * scale
    xs_l, xs_r = cx - half, cx + half
    y_abs = base + ys * height
    outline = np.vstack([np.column_stack([xs_l, y_abs]),
                         np.column_stack([xs_r, y_abs])[::-1]])

    # Shadow on the table
    ax.add_patch(Ellipse((cx + 0.35, base), 3.4, 0.35, color="#000", alpha=0.18, zorder=2))
    ax.add_patch(Polygon(outline, closed=True, fc=VASE, ec=VASE_DARK, lw=2, zorder=5))

    # Simple shading: darker band on the right, highlight on the left
    for frac, colour, alpha in [(0.55, VASE_DARK, 0.45), (0.8, VASE_DARK, 0.35)]:
        band = np.vstack([np.column_stack([cx + half * frac, y_abs]),
                          np.column_stack([xs_r, y_abs])[::-1]])
        ax.add_patch(Polygon(band, closed=True, fc=colour, alpha=alpha, lw=0, zorder=6))
    hl = ys < 0.75
    ax.plot(cx - half[hl] * 0.55, y_abs[hl], color=VASE_LIGHT, lw=6, alpha=0.55,
            solid_capstyle="round", zorder=7)

    # Decorative band and lip
    for yb in (0.35, 0.4):
        w = vase_profile(np.array(yb)) * scale
        ax.plot([cx - w, cx + w], [base + yb * height] * 2, color="#e8d9a8", lw=2.5, zorder=7)
    lip_w = vase_profile(np.array(1.0)) * scale
    ax.add_patch(Ellipse((cx, base + height), 2 * lip_w, 0.22,
                         fc=VASE_DARK, ec=VASE_DARK, zorder=8))
    return base + height  # y of the lip


def draw_leaf(ax, anchor, angle, length=1.1, width=0.38):
    a = np.deg2rad(angle)
    tip = np.array(anchor) + length * np.array([np.cos(a), np.sin(a)])
    normal = width * np.array([-np.sin(a), np.cos(a)])
    mid = (np.array(anchor) + tip) / 2
    upper = bezier(anchor, mid + normal, tip)
    lower = bezier(tip, mid - normal, anchor)
    ax.add_patch(Polygon(np.vstack([upper, lower]), fc=LEAF, ec=STEM, lw=1.2, zorder=3))
    ax.plot(*np.array([anchor, tip]).T, color=STEM, lw=0.8, zorder=3)


def draw_daisy(ax, centre, r, petal_colour, centre_colour, n_petals=14, tilt=0):
    for k in range(n_petals):
        ang = tilt + 360 * k / n_petals
        a = np.deg2rad(ang)
        pos = np.array(centre) + 0.55 * r * np.array([np.cos(a), np.sin(a)])
        ax.add_patch(Ellipse(pos, 1.1 * r, 0.36 * r, angle=ang, fc=petal_colour,
                             ec="#00000030", lw=0.8, zorder=10))
    ax.add_patch(Ellipse(centre, 0.55 * r, 0.55 * r, fc=centre_colour, ec="#5a3b12",
                         lw=1, zorder=11))
    # Seed texture
    rng = np.random.default_rng(1)
    pts = rng.normal(size=(40, 2)) * 0.08 * r + np.array(centre)
    ax.scatter(*pts.T, s=3, color="#5a3b12", zorder=12)


def draw_tulip(ax, centre, r, colour, edge):
    cx, cy = centre
    base = (cx, cy - 0.8 * r)
    # Outer petals first, the centre petal last so it overlaps them
    for dx, z in [(-0.4, 10), (0.4, 10), (0.0, 11)]:
        tip = (cx + dx * r, cy + 0.8 * r)
        left = bezier(base, (cx + (dx - 0.75) * r, cy - 0.2 * r), tip)
        right = bezier(tip, (cx + (dx + 0.75) * r, cy - 0.2 * r), base)
        ax.add_patch(Polygon(np.vstack([left, right]), fc=colour, ec=edge, lw=1.5, zorder=z))


def main():
    fig, ax = plt.subplots(figsize=(7, 9), dpi=150)
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.6, 7)
    ax.set_aspect("equal")
    ax.axis("off")

    # Wall and table
    ax.add_patch(Rectangle((-4.5, -3.2), 9, 10.2, fc=WALL, zorder=0))
    ax.add_patch(Rectangle((-4.5, -4.6), 9, 1.4, fc=TABLE, zorder=1))
    ax.plot([-4.5, 4.5], [-3.2, -3.2], color=TABLE_EDGE, lw=3, zorder=1)

    lip_y = draw_vase(ax)

    # (flower head position, stem bend, drawer)
    flowers = [
        ((-2.0, 4.3), (-1.2, 2.0), lambda c: draw_daisy(ax, c, 1.1, "#f6f1f5", "#f2b632", tilt=8)),
        ((0.3, 5.6), (0.4, 3.0), lambda c: draw_daisy(ax, c, 1.25, "#f28fb1", "#7a3b1a", n_petals=16)),
        ((2.3, 4.0), (1.4, 2.0), lambda c: draw_tulip(ax, c, 0.9, "#f07a4a", "#b84a22")),
        ((-0.6, 3.2), (-0.4, 1.8), lambda c: draw_daisy(ax, c, 0.75, "#f7d046", "#6b3f14", n_petals=12)),
    ]

    stems = []
    for head, bend, _ in flowers:
        start = (head[0] * 0.12, lip_y - 0.3)
        stems.append(bezier(start, bend, head))
        ax.plot(*stems[-1].T, color=STEM, lw=3.2, solid_capstyle="round", zorder=4)

    draw_leaf(ax, stems[0][25], 150)
    draw_leaf(ax, stems[2][22], 25)
    draw_leaf(ax, stems[1][30], 120, length=0.9)

    for head, _, drawer in flowers:
        drawer(head)

    fig.savefig(OUT, bbox_inches="tight", pad_inches=0)
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
