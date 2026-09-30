"""NEXA 'Super Blue grade' for photography (matches the brandbook's in-situ imagery):
luminance mapped onto Space Black -> Super Blue -> pale blue, with a little of the original colour kept.
python3 grade.py <src> <dst> [max_width]"""
import sys
from PIL import Image, ImageOps, ImageEnhance
STOPS = [(0, (2, 1, 20)), (.42, (31, 31, 204)), (.78, (120, 130, 255)), (1, (236, 238, 255))]
def lut(ch):
    out = []
    for i in range(256):
        t = i / 255
        for (a, ca), (b, cb) in zip(STOPS, STOPS[1:]):
            if t <= b:
                k = (t - a) / (b - a); out.append(round(ca[ch] + (cb[ch] - ca[ch]) * k)); break
    return out
def grade(src, dst, maxw=1600, keep=.14):
    im = Image.open(src).convert('RGB'); im.thumbnail((maxw, maxw))
    g = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(1.12)
    duo = Image.merge('RGB', [g.point(lut(c)) for c in range(3)])
    Image.blend(duo, im, keep).save(dst, quality=84)
if __name__ == '__main__':
    grade(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1600)
