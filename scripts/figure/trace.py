#!/usr/bin/env python3
"""Regenerates ink_path.txt and acc_path.txt from the dissertation's Figure 1.1.

The figure is a raster image on page 17 of the dissertation PDF. Extract it with
    pdfimages -j -f 17 -l 17 Rajprabhu_Dissertation.pdf fig11
then run
    pip install opencv-python-headless numpy potracer
    python3 scripts/figure/trace.py fig11-000.jpg

The script removes the labels and dashed boxes (the site redraws those as SVG),
moves the two sets of expression marks into a separate accent layer, traces both
layers with potrace and writes compact SVG path data next to this file.
Box coordinates in build.py (thesis_fig) use the same pixel space as the image.
"""
import os, re, sys
import cv2
import numpy as np
import potrace

HERE = os.path.dirname(os.path.abspath(__file__))
BOXES = [(56, 256, 1800, 767), (782, 301, 1191, 723), (1938, 256, 2420, 767)]  # group, individual, synthesis
ACCENT_REGIONS = [(1080, 495, 1155, 595), (1945, 495, 2065, 655)]  # expression marks: person, robot
LABEL_BAND = 245  # everything above this row is label text
BAND = 9


def clean(b):
    b[:LABEL_BAND, :] = 0
    n, lab, stats, _ = cv2.connectedComponentsWithStats(b, connectivity=8)
    for i in range(1, n):
        x, y, w, h, a = stats[i]
        x1, y1 = x + w, y + h
        for bx0, by0, bx1, by1 in BOXES:
            within = bx0 - BAND <= x and x1 <= bx1 + BAND and by0 - BAND <= y and y1 <= by1 + BAND
            inner = x > bx0 + BAND and x1 < bx1 - BAND and y > by0 + BAND and y1 < by1 - BAND
            if a < 1500 and (w < 60 or h < 60) and within and not inner:
                b[lab == i] = 0
                break
    # dash pixels that touch drawing strokes: drop them unless the stroke continues across the border
    for bx0, by0, bx1, by1 in BOXES:
        for yy in (by0, by1):
            for r in range(yy - 4, yy + 5):
                for x in range(bx0 - 4, bx1 + 5):
                    if b[r, x] and not b[yy - 8, x] and not b[yy + 8, x]:
                        b[r, x] = 0
        for xx in (bx0, bx1):
            for c in range(xx - 4, xx + 5):
                for y in range(by0 - 4, by1 + 5):
                    if b[y, c] and not b[y, xx - 8] and not b[y, xx + 8]:
                        b[y, c] = 0
    acc = np.zeros_like(b)
    for x0, y0, x1, y1 in ACCENT_REGIONS:
        acc[y0:y1, x0:x1] = b[y0:y1, x0:x1]
        b[y0:y1, x0:x1] = 0
    n, lab, stats, _ = cv2.connectedComponentsWithStats(b, connectivity=8)
    for i in range(1, n):
        if stats[i][4] < 400:
            b[lab == i] = 0
    b = cv2.morphologyEx(b, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    return b, acc


def trace(arr, W, H):
    plist = potrace.Bitmap(arr.astype(bool)).trace(
        turdsize=12, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY,
        alphamax=1.0, opticurve=True, opttolerance=0.4)
    out = []
    for curve in plist:
        pts = [curve.start_point] + [p for s in curve.segments for p in ((s.c, s.end_point) if s.is_corner else (s.c1, s.c2, s.end_point))]
        xs = [p.x for p in pts]; ys = [p.y for p in pts]
        if min(xs) <= 0.5 and min(ys) <= 0.5 and max(xs) >= W - 1 and max(ys) >= H - 1:
            continue  # potracer emits the image frame as a curve; drop it
        cx, cy = round(curve.start_point.x), round(curve.start_point.y)
        d = [f"M{cx} {cy}"]
        for s in curve.segments:
            if s.is_corner:
                for p in (s.c, s.end_point):
                    x, y = round(p.x), round(p.y)
                    d.append(f"l{x - cx} {y - cy}")
                    cx, cy = x, y
            else:
                v = [(round(p.x), round(p.y)) for p in (s.c1, s.c2, s.end_point)]
                d.append("c" + " ".join(f"{x - cx} {y - cy}" for x, y in v))
                cx, cy = v[-1]
        d.append("z")
        out.append("".join(d))
    return re.sub(r" -", "-", "".join(out))


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "fig11-000.jpg")
    im = cv2.imread(src, 0)
    H, W = im.shape
    ink, acc = clean((im < 150).astype(np.uint8))
    for name, arr in (("ink_path.txt", ink), ("acc_path.txt", acc)):
        with open(os.path.join(HERE, name), "w") as f:
            f.write(trace(arr, W, H))
        print("wrote", name)
