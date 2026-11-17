# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tilelight as mod  # noqa: E402

def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_hex(path):
    with open(path, encoding="utf-8") as f:
        return f.read().strip()


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def test_attenuation_monotone():
    vals = [tilelight.attenuation(d) for d in range(5)]
    assert all(a >= b for a, b in zip(vals, vals[1:]))


def test_no_lights():
    m = tilelight.load_map("data/tilemap.txt")
    out = tilelight.propagate(m, [])
    assert all(v == 0 for row in out for v in row)
