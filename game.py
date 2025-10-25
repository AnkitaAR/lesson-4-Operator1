# dungeon_crawler.py

import math, random, json, os, time, sys

from dataclasses import dataclass, field

from typing import List, Tuple, Optional, Dict, Any

import pygame

# ---------------------- CONFIG ----------------------

WIDTH, HEIGHT = 1280, 800

SIDEBAR_W = 360

PLAY_W = WIDTH - SIDEBAR_W

TILE_SIZE = 24

GRID_W = PLAY_W // TILE_SIZE

GRID_H = HEIGHT // TILE_SIZE

FPS = 60

FOV_RADIUS = 9

MAX_ROOMS = 28

ROOM_MIN = 4

ROOM_MAX = 9

SAVE_FILE = "savegame.json"

# Colors

COL_BG = (13, 16, 24)

COL_WALL = (40, 48, 62)

COL_FLOOR = (25, 30, 41)

COL_SEEN = (18, 22, 30)

COL_TEXT = (220, 230, 240)

COL_UI = (90, 110, 150)

COL_HP = (220, 70, 70)

COL_XP = (90, 200, 255)

COL_GOLD = (240, 200, 90)

COL_POISON = (110, 200, 120)

# ---------------------- UTILS ----------------------

def clamp(v,a,b): return max(a, min(b, v))

def bresenham(x0, y0, x1, y1):

"""Grid line between points (inclusive)."""

dx = abs(x1-x0); sx = 1 if x0 < x1 else -1

dy = -abs(y1-y0); sy = 1 if y0 < y1 else -1

err = dx+dy

x,y = x0,y0

while True:

yield x,y

if x==x1 and y==y1: break

e2 = 2*err

if e2 >= dy:

err += dy

x += sx

if e2 <= dx:

err += dx

y += sy