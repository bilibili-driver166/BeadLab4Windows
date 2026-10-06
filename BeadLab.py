# -*- coding: utf-8 -*-
"""拼豆实验室 Bead Lab - Python 桌面版（自由布局）"""

import os
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sys

try:
    from PIL import Image as PILImage
    HAS_PIL = True
except ImportError:
    PILImage = None
    HAS_PIL = False

try:
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False

# ==================== 窗口图标 ====================

ICON_SIZE = 22
ICON_PIXELS = [(127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (255, 255, 255, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (0, 0, 0, 255), (255, 255, 255, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (0, 0, 0, 255), (61, 74, 92, 255), (49, 60, 77, 255), (0, 0, 0, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (127, 127, 127, 255), (127, 127, 127, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (0, 0, 0, 255), (255, 255, 255, 255), (0, 0, 0, 255), (61, 74, 92, 255), (42, 52, 67, 255), (0, 0, 0, 255), (255, 255, 255, 255), (0, 0, 0, 255), (0, 0, 0, 255), (255, 255, 255, 255), (127, 127, 127, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (62, 74, 93, 255), (57, 69, 86, 255), (0, 0, 0, 255), (61, 74, 92, 255), (51, 62, 79, 255), (45, 55, 71, 255), (61, 74, 92, 255), (0, 0, 0, 255), (59, 71, 89, 255), (54, 66, 83, 255), (0, 0, 0, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (57, 69, 86, 255), (57, 69, 86, 255), (63, 76, 95, 255), (51, 62, 79, 255), (45, 55, 71, 255), (45, 55, 71, 255), (45, 55, 71, 255), (46, 56, 72, 255), (51, 62, 79, 255), (20, 25, 36, 255), (0, 0, 0, 255), (255, 255, 255, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (255, 255, 255, 255), (0, 0, 0, 255), (57, 69, 86, 255), (58, 71, 89, 255), (51, 62, 79, 255), (51, 62, 79, 255), (45, 55, 71, 255), (45, 55, 71, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (0, 0, 0, 255), (61, 74, 92, 255), (58, 71, 89, 255), (51, 62, 79, 255), (36, 44, 58, 255), (0, 0, 0, 255), (0, 0, 0, 255), (19, 30, 43, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (255, 255, 255, 255), (0, 0, 0, 255), (61, 74, 92, 255), (40, 50, 65, 255), (58, 71, 89, 255), (51, 62, 79, 255), (45, 55, 71, 255), (0, 0, 0, 255), (127, 127, 127, 255), (127, 127, 127, 255), (19, 30, 43, 255), (202, 222, 236, 255), (186, 210, 229, 255), (174, 200, 223, 255), (174, 200, 223, 255), (174, 200, 223, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (255, 255, 255, 255), (0, 0, 0, 255), (20, 25, 35, 255), (18, 22, 32, 255), (40, 50, 65, 255), (51, 62, 79, 255), (44, 54, 70, 255), (0, 0, 0, 255), (127, 127, 127, 255), (127, 127, 127, 255), (0, 0, 0, 255), (19, 30, 43, 255), (249, 252, 254, 255), (249, 252, 254, 255), (174, 200, 223, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (0, 0, 0, 255), (29, 36, 49, 255), (51, 62, 79, 255), (51, 62, 79, 255), (35, 44, 58, 255), (0, 0, 0, 255), (0, 0, 0, 255), (62, 75, 93, 255), (19, 30, 43, 255), (249, 252, 254, 255), (249, 252, 254, 255), (186, 210, 229, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (255, 255, 255, 255), (0, 0, 0, 255), (61, 74, 92, 255), (42, 52, 68, 255), (51, 62, 79, 255), (51, 62, 79, 255), (51, 62, 79, 255), (43, 53, 68, 255), (19, 30, 43, 255), (249, 252, 254, 255), (249, 252, 254, 255), (186, 210, 229, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (61, 74, 92, 255), (42, 52, 68, 255), (19, 24, 35, 255), (49, 60, 77, 255), (49, 60, 77, 255), (43, 53, 68, 255), (19, 30, 43, 255), (186, 210, 229, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (42, 52, 68, 255), (19, 24, 35, 255), (0, 0, 0, 255), (18, 22, 33, 255), (49, 60, 77, 255), (43, 53, 68, 255), (19, 30, 43, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (186, 210, 229, 255), (249, 252, 254, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (0, 0, 0, 255), (0, 0, 0, 255), (255, 255, 255, 255), (0, 0, 0, 255), (46, 57, 74, 255), (19, 30, 43, 255), (186, 210, 229, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (186, 210, 229, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (127, 127, 127, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (0, 0, 0, 255), (19, 30, 43, 255), (19, 30, 43, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (255, 255, 255, 255), (19, 30, 43, 255), (249, 252, 254, 255), (249, 252, 254, 255), (254, 180, 20, 255), (243, 124, 14, 255), (19, 108, 192, 255), (19, 108, 192, 255), (234, 36, 40, 255), (199, 11, 15, 255), (249, 252, 254, 255), (198, 218, 234, 255), (19, 30, 43, 255), (255, 255, 255, 255), (127, 127, 127, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (255, 255, 255, 255), (19, 30, 43, 255), (249, 252, 254, 255), (249, 252, 254, 255), (44, 172, 87, 255), (243, 124, 14, 255), (243, 124, 14, 255), (243, 78, 151, 255), (44, 172, 87, 255), (3, 129, 82, 255), (199, 11, 15, 255), (249, 252, 254, 255), (198, 218, 234, 255), (249, 252, 254, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (255, 255, 255, 255), (19, 30, 43, 255), (198, 218, 234, 255), (254, 179, 20, 255), (3, 129, 82, 255), (3, 129, 82, 255), (243, 78, 151, 255), (243, 78, 151, 255), (3, 129, 82, 255), (3, 129, 82, 255), (254, 179, 20, 255), (49, 173, 86, 255), (198, 218, 234, 255), (198, 218, 234, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (255, 255, 255, 255), (19, 30, 43, 255), (19, 30, 43, 255), (198, 218, 234, 255), (254, 179, 20, 255), (200, 89, 159, 255), (200, 89, 159, 255), (71, 158, 231, 255), (29, 135, 219, 255), (243, 124, 14, 255), (243, 124, 14, 255), (3, 129, 82, 255), (198, 218, 234, 255), (19, 30, 43, 255), (19, 30, 43, 255), (255, 255, 255, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (255, 255, 255, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (19, 30, 43, 255), (255, 255, 255, 255), (127, 127, 127, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (96, 96, 96, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (255, 255, 255, 255), (127, 127, 127, 255), (127, 127, 127, 255)]


def app_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


ICON_DIR = os.path.join(app_dir(), "config")
ICON_PATH = os.path.join(ICON_DIR, "bead_lab.ico")


def ensure_icon():
    """返回可用图标路径；不存在则用内嵌像素生成。失败返回 None。"""
    if os.path.exists(ICON_PATH):
        return ICON_PATH
    if not HAS_PIL:
        return None
    if len(ICON_PIXELS) != ICON_SIZE * ICON_SIZE:
        return None
    try:
        os.makedirs(ICON_DIR, exist_ok=True)
        img = PILImage.new("RGBA", (ICON_SIZE, ICON_SIZE))
        img.putdata(ICON_PIXELS)
        img.save(ICON_PATH, format="ICO", sizes=[(ICON_SIZE, ICON_SIZE)])
        return ICON_PATH
    except Exception:
        return None


# ==================== 调色板 ====================

CODES = [
    "A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13","A14","A15","A16",
    "A17","A18","A19","A20","A21","A22","A23","A24","A25","A26",
    "B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14","B15","B16",
    "B17","B18","B19","B20","B21","B22","B23","B24","B25","B26","B27","B28","B29","B30","B31","B32",
    "C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16",
    "C17","C18","C19","C20","C21","C22","C23","C24","C25","C26","C27","C28","C29",
    "D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13","D14","D15","D16",
    "D17","D18","D19","D20","D21","D22","D23","D24","D25","D26",
    "E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","E11","E12","E13","E14","E15","E16",
    "E17","E18","E19","E20","E21","E22","E23","E24",
    "F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16",
    "F17","F18","F19","F20","F21","F22","F23","F24","F25",
    "G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12","G13","G14","G15","G16",
    "G17","G18","G19","G20","G21",
    "H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14","H15","H16",
    "H17","H18","H19","H20","H21","H22","H23",
    "M1","M2","M3","M4","M5","M6","M7","M8","M9","M10","M11","M12","M13","M14","M15",
    "P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12","P13","P14","P15","P16",
    "P17","P18","P19","P20","P21","P22","P23",
    "Q1","Q2","Q3","Q4","Q5",
    "R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12","R13","R14","R15","R16",
    "R17","R18","R19","R20","R21","R22","R23","R24","R25","R26","R27","R28",
    "T1","Y1","Y2","Y3","Y4","Y5",
    "ZG1","ZG2","ZG3","ZG4","ZG5","ZG6","ZG7","ZG8",
]
COLORS = [
    0xF9F0CD,0xFBFBD4,0xFAFC9F,0xFFE953,0xF4D738,0xFDAD49,0xFF7C2F,0xEACA49,0xFF995A,0xFF9D55,
    0xFFDD99,0xFCB58F,0xFFBB59,0xFF6D40,0xFDFF44,0xFEF9AE,0xFFE36E,0xFECF98,0xFD7B72,0xEFCD67,
    0xFFE395,0xFFF3A4,0xF3D5BF,0xFBF8C9,0xFFD67D,0xFFBB27,
    0xE6EE32,0x5BE419,0x7CEE9D,0x1EF942,0x00BD35,0x5AE8BA,0x03AC88,0x029D26,0x26523A,0x95D3C2,
    0x5D722A,0x156F40,0xD9F794,0xADE945,0x2E5132,0xC6ED9C,0x9BB13A,0xE6EE49,0x25B88C,0xC2F0CC,
    0x146A6B,0x0B3C43,0x303921,0xEEFCA5,0x4E846D,0x8C7A36,0xD1DCC1,0x9EE5B9,0xC5E254,0xECFBD0,
    0xC4E6B5,0x9BAB5A,
    0xE8FFE7,0xBCF9F6,0xA0E2FB,0x42CCFF,0x01ACEB,0x50A9F0,0x0188D3,0x1054C0,0x314BCA,0x3EBCE2,
    0x03B9B9,0x1C334D,0xCDE8FF,0xD5FDFF,0x23C4C6,0x1757A8,0x50D3EC,0x1C3344,0x1787A2,0x0082BE,
    0xBEDDFF,0x67B4BE,0xC2DCEB,0x7DC4FF,0xA9E5E5,0x2F99B3,0xEBF5FC,0xBBCFED,
    0x4B5BA3,0xAEB4F2,0x858EDD,0x3054AF,0x182A84,0xB843C5,0xAC7BDE,0x6E399A,0xE2D3FF,0xD5B9F8,
    0x361B50,0xB9BAE1,0xDE9AD4,0xB90295,0x8B279B,0x2F1F90,0xE2E1EE,0xC4D4F6,0xA45EC7,0xD8C3D7,
    0x9C32B2,0x9A009B,0x333995,0xEADAFC,0x7786E5,0x484FC7,0xE9C3F6,
    0xFDD3CC,0xFECDDF,0xFF97C3,0xE8649E,0xF551A2,0xFF346B,0xC63578,0xFFDBE9,0xE970CC,0xD33893,
    0xFCDDD2,0xFFA1C5,0xB6006D,0xFFD1BA,0xF2CFD0,0xFFECDE,0xFFE2EA,0xFFC9D6,0xFFD2E7,0xD8C7D1,
    0xBD9DA1,0xCC78A7,0x937A8D,0xF6E4F9,
    0xFD957B,0xFC3D45,0xF74941,0xFC283C,0xD80127,0xB0443D,0x971937,0xBC0127,0xE2677A,0xA74D22,
    0x6F201F,0xFD4D6A,0xDD422F,0xFFA9AD,0xC80020,0xFFD9C8,0xF79B71,0xD37C46,0xC1444A,0xCD9391,
    0xF4B1B4,0xFFD0CB,0xF57E66,0xFCC1C4,0xE54B4F,0xFFE2CE,0xFFCAAA,0xF4C3A5,0xE1B383,0xED9435,
    0xF59734,0x9D5B3E,0x592A21,0xE6B483,0xC88135,0xE0C593,0xEBBB83,0xB7714A,0x8D614C,0xFCF9E0,
    0xF2D9BA,0x56403C,0xFFE4CC,0xE1943A,0xA94023,0xCB8E77,
    0xE2E2E2,0xFFFFFF,0xB3B3B3,0x868686,0x474747,0x2C2C2C,0x000000,0xE7D6DB,0xE4E7E3,0xEEE9EA,
    0xCECDD5,0xFFF5ED,0xF3E1C9,0xCFD7D3,0x98A6A8,0x3B2F23,0xF1EDED,0xFFFDF0,0xF6EFE2,0x949FA3,
    0xF7F3E4,0xCACAD5,0x9A9D94,0xBCC6B8,0x8AA385,0x697D80,0xDACEBE,0xD0CCAA,0xB0A782,0xB4A497,
    0xB38281,0xA58767,0xC5B1BC,0x9F7494,0x644749,0xD19066,0xC77361,0x757D7B,0xFCF8F9,0xBDA9AB,
    0xAEDDA9,0xFDA49E,0xEC8D3D,0x60CFA8,0xEB9271,0xF0D958,0xD9D9D9,0xD5C8E9,0xF3ECC8,0xE6EEF1,
    0xA9CBF1,0x3177B0,0x668575,0xFFBE46,0xFFA324,0xFEB89F,0xFFE0E8,0xFEBECF,0xECBEC0,0xE4A89E,
    0xA56269,0xF2A5E8,0x73B29E,0xFFFF00,0xFFEBFA,0x4F5E5B,0xD50E21,0xF92E83,0xFD8225,0xF8EC31,
    0x34C75B,0x25B891,0x17779D,0x1B60C3,0x9A56B4,0xFFDB4D,0xFFEBFA,0xD8D5CE,0x55514C,0x9EE4DF,
    0x77CEE9,0x3DCFCA,0x4A867A,0x7FCD9D,0xCDE55D,0xE8C7B4,0xAD6F3C,0x6C372F,0xFEB872,0xF2C1C0,
    0xC9675D,0xD293BE,0xEA8CB1,0x9C87D6,0xE2DFD7,0xFD6FB4,0xFEB481,0xD7FAA0,0x8BDBFA,0xE987EA,
    0xDAABB3,0xD6AA87,0xC1BD8D,0x96869F,0x8490A6,0x94BFE2,0xE2A9D2,0xAB91C0,
]
assert len(CODES) == 291 and len(COLORS) == 291
COLORS_RGB = [((c >> 16) & 255, (c >> 8) & 255, c & 255) for c in COLORS]
BOARD_SIZES = [16, 32, 64, 128]
FILE_FORMAT = "beadlab"
FILE_FORMAT_LEGACY = "brainlayers-pegboard"
FILE_VERSION = 1
LAYOUT_FILE = os.path.join(ICON_DIR, "beadlab_layout.json")

DEFAULT_LAYOUT = {
    "palette":   (0.00, 0.00, 0.20, 1.00),
    "canvas":    (0.20, 0.00, 0.55, 1.00),
    "command":   (0.75, 0.00, 0.25, 0.50),
    "stats":     (0.75, 0.50, 0.25, 0.50),
}
REGION_NAMES = {
    "palette": "选拼豆",
    "canvas": "预览",
    "command": "命令生成",
    "stats": "豆子数量列表",
}
SNAP = 5

# ==================== 工具与撤销 ====================

TOOL_BRUSH = "brush"
TOOL_ERASER = "eraser"
TOOL_FILL = "fill"
TOOL_PICKER = "picker"
TOOL_SELECT = "select"

TOOL_NAMES = {
    TOOL_BRUSH: "画笔",
    TOOL_ERASER: "橡皮",
    TOOL_FILL: "填充",
    TOOL_PICKER: "取色",
    TOOL_SELECT: "选区",
}

UNDO_LIMIT = 200
RECENT_LIMIT = 10
RECENT_FILE = os.path.join(ICON_DIR, "recent.json")


def hex_of(rgb):
    return "#%02x%02x%02x" % ((rgb >> 16) & 255, (rgb >> 8) & 255, rgb & 255)


def contrast_fg(rgb):
    r, g, b = (rgb >> 16) & 255, (rgb >> 8) & 255, rgb & 255
    return "#000000" if (0.299 * r + 0.587 * g + 0.114 * b) > 128 else "#ffffff"


def nearest_index(r, g, b):
    best, best_d = 0, 1 << 30
    for i, (cr, cg, cb) in enumerate(COLORS_RGB):
        dr, dg, db = r - cr, g - cg, b - cb
        d = dr * dr + dg * dg + db * db
        if d < best_d:
            best_d, best = d, i
    return best


def load_image_pixels(path):
    if not HAS_PIL:
        raise RuntimeError("需要 Pillow 才能读取图片，请 pip install pillow")
    img = PILImage.open(path).convert("RGBA")
    w, h = img.size
    px = img.load()
    return w, h, [px[x, y] for y in range(h) for x in range(w)]


def nearest_resize(w, h, pixels, nw, nh):
    out = []
    for ny in range(nh):
        sy = min(h - 1, int(ny * h / nh))
        for nx in range(nw):
            sx = min(w - 1, int(nx * w / nw))
            out.append(pixels[sy * w + sx])
    return out


def fit_into(src_w, src_h, dst_w, dst_h):
    if src_w <= 0 or src_h <= 0:
        return 0, 0, 0, 0
    scale = min(dst_w / src_w, dst_h / src_h)
    nw = max(1, round(src_w * scale))
    nh = max(1, round(src_h * scale))
    return nw, nh, (dst_w - nw) // 2, (dst_h - nh) // 2


def safe_filename(name):
    clean = str(name or "").replace("\\", "_").replace("/", "_").replace(":", "_") \
        .replace("*", "_").replace("?", "_").replace('"', "_").replace("<", "_") \
        .replace(">", "_").replace("|", "_").strip()
    return clean or "拼豆图纸"


# ==================== 颜色选择面板 ====================

class ColorPalette(ttk.Frame):
    CELL_W = 52
    GAP = 2

    def __init__(self, master, on_select):
        super().__init__(master)
        self.on_select = on_select
        self.selected = -1
        self.enabled = True
        self.tooltip = None
        self.cols = 4
        self._buttons = []

        bar = ttk.Frame(self)
        bar.pack(fill="x", padx=4, pady=4)
        ttk.Label(bar, text="搜索:").pack(side="left")
        self.search_var = tk.StringVar()
        entry = ttk.Entry(bar, textvariable=self.search_var, width=10)
        entry.pack(side="left", fill="x", expand=True, padx=2)
        entry.bind("<Return>", lambda e: self.do_search())
        ttk.Button(bar, text="查", width=3, command=self.do_search).pack(side="left")
        self.search_entry = entry

        cont = ttk.Frame(self)
        cont.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(cont, bg="#2b2b2b", highlightthickness=0)
        sb = ttk.Scrollbar(cont, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=sb.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        self.inner = ttk.Frame(self.canvas)
        self._win_id = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.canvas.bind("<Configure>", self._on_canvas_resize)
        self.canvas.bind("<MouseWheel>", self._wheel)
        self.inner.bind("<MouseWheel>", self._wheel)

        for i in range(len(CODES)):
            rgb = COLORS[i]
            b = tk.Label(self.inner, text=CODES[i], bg=hex_of(rgb), fg=contrast_fg(rgb),
                         width=4, height=2, relief="raised", borderwidth=1,
                         font=("Arial", 9, "bold"))
            b.bind("<Button-1>", lambda e, idx=i: self._on_click(idx))
            b.bind("<Enter>", lambda e, idx=i: self._show_tip(idx, e))
            b.bind("<Leave>", lambda e: self._hide_tip())
            b.bind("<MouseWheel>", self._wheel)
            self._buttons.append((b, i))
        self._relayout()
        self._bind_wheel_all(self)

    def _bind_wheel_all(self, widget):
        widget.bind("<MouseWheel>", self._wheel)
        for child in widget.winfo_children():
            self._bind_wheel_all(child)

    def _wheel(self, e):
        if not self.enabled:
            return
        self.canvas.yview_scroll(-1 if e.delta > 0 else 1, "units")

    def _on_canvas_resize(self, event):
        self.canvas.itemconfigure(self._win_id, width=event.width)
        cols = max(1, event.width // (self.CELL_W + self.GAP))
        if cols != self.cols:
            self.cols = cols
            self._relayout()

    def _relayout(self):
        for b, _ in self._buttons:
            b.grid_forget()
        for c in range(20):
            self.inner.grid_columnconfigure(c, weight=0, minsize=0)
        for i, (b, _) in enumerate(self._buttons):
            b.grid(row=i // self.cols, column=i % self.cols,
                   padx=self.GAP // 2, pady=self.GAP // 2,
                   sticky="nsew", ipadx=2, ipady=4)
        for c in range(self.cols):
            self.inner.grid_columnconfigure(c, weight=1)
        self.inner.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def set_enabled(self, enabled):
        self.enabled = enabled
        if enabled:
            self.search_entry.configure(state="normal")
            for b, i in self._buttons:
                rgb = COLORS[i]
                b.configure(cursor="", bg=hex_of(rgb), fg=contrast_fg(rgb),
                            relief="solid" if i == self.selected else "raised",
                            borderwidth=3 if i == self.selected else 1)
        else:
            self.search_entry.configure(state="disabled")
            self._hide_tip()
            for b, i in self._buttons:
                b.configure(cursor="X_cursor", relief="flat",
                            bg=self._gray(COLORS[i]), fg="#666666")

    @staticmethod
    def _gray(rgb):
        r, g, b = (rgb >> 16) & 255, (rgb >> 8) & 255, rgb & 255
        y = int(0.299 * r + 0.587 * g + 0.114 * b)
        y = max(20, min(255, int(y * 0.45 + 40)))
        return "#%02x%02x%02x" % (y, y, y)

    def _on_click(self, idx):
        if not self.enabled:
            return
        self.select(idx)

    def select(self, idx):
        if not self.enabled:
            return
        self.selected = idx
        for b, i in self._buttons:
            b.configure(relief="solid" if i == idx else "raised",
                        borderwidth=3 if i == idx else 1)
        self.on_select(idx)

    def _show_tip(self, idx, e):
        if not self.enabled:
            return
        self._hide_tip()
        rgb = COLORS[idx]
        txt = f"{CODES[idx]}\n#{rgb:06X}\n{((rgb>>16)&255)}, {((rgb>>8)&255)}, {rgb&255}"
        t = tk.Toplevel(self)
        t.wm_overrideredirect(True)
        t.wm_geometry(f"+{e.x_root+15}+{e.y_root+10}")
        tk.Label(t, text=txt, bg="white", fg="black", relief="solid",
                 borderwidth=1, font=("Arial", 9), justify="left",
                 padx=4, pady=2).pack()
        self.tooltip = t

    def _hide_tip(self):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    def do_search(self):
        if not self.enabled:
            return
        text = self.search_var.get().strip()
        if not text:
            return
        token = text.upper().replace(" ", "")
        if token in CODES:
            idx = CODES.index(token)
            self.select(idx)
            self._scroll_to(idx)
            return
        try:
            r, g, b = self._parse(text)
        except ValueError:
            messagebox.showerror("错误", "输入色号（如 A1）、#F9F0CD 或 249,240,205")
            return
        idx = nearest_index(r, g, b)
        self.select(idx)
        self._scroll_to(idx)

    def _scroll_to(self, idx):
        total_rows = (len(CODES) + self.cols - 1) // self.cols
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(max(0, (idx // self.cols) / max(1, total_rows) - 0.1))

    @staticmethod
    def _parse(text):
        text = text.strip()
        if text.startswith("#"):
            text = text[1:]
        if len(text) == 6 and all(c in "0123456789abcdefABCDEF" for c in text):
            return int(text[0:2], 16), int(text[2:4], 16), int(text[4:6], 16)
        parts = text.replace(",", " ").split()
        if len(parts) == 3:
            return int(parts[0]), int(parts[1]), int(parts[2])
        raise ValueError("无法解析")


# ==================== 画布 ====================

class PreviewCanvas(tk.Canvas):
    BG = "#1e1e1e"
    EMPTY_FILL = "#2b2b2b"
    EMPTY_OUTLINE = "#3a3a3a"
    HOVER_OUTLINE = "#ff00ff"
    SELECT_OUTLINE = "#00e0ff"
    DIM_A = 0.20
    REF_A = 0.32

    def __init__(self, master, on_cell_change=None, on_hover=None,
                 on_pick_color=None, on_request_redraw=None):
        super().__init__(master, bg=self.BG, highlightthickness=0)
        self.board_size = 16
        self.pixels = [0] * (16 * 16)
        self.ref_pixels = None
        self.current_color = -1
        self.locked = False
        self.show_codes = False
        self.show_highlight = False
        self.show_coords = False
        self.tool = TOOL_BRUSH
        self.hover = None
        self.hover_color = None
        self._cell_items = []
        self._code_items = []
        self._coord_items = []
        self._hover_rect = None
        self._tooltip_items = []
        self._sel_rect = None
        self._sel_drag_start = None
        self._painting_btn = None
        self._applied_hl = -2
        self.offset_x = self.offset_y = 0
        self.cell = 16
        self.zoom = 1.0
        self.pan_x = 0
        self.pan_y = 0
        self.on_cell_change = on_cell_change
        self.on_hover = on_hover
        self.on_pick_color = on_pick_color
        self.on_request_redraw = on_request_redraw

        # 撤销/重做
        self.undo_stack = []
        self.redo_stack = []
        self._cur_stroke = None
        self._panning = False
        self._pan_start = None

        # 选区
        self.selection = None

        self.bind("<Motion>", self._on_motion)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Configure>", self._on_configure)
        self.bind("<Button-1>", self._on_press)
        self.bind("<B1-Motion>", self._on_drag)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Button-3>", self._on_rpress)
        self.bind("<B3-Motion>", self._on_rdrag)
        self.bind("<ButtonRelease-3>", self._on_rrelease)
        self.bind("<Button-2>", self._on_mpress)
        self.bind("<B2-Motion>", self._on_mdrag)
        self.bind("<ButtonRelease-2>", self._on_mrelease)
        self.bind("<MouseWheel>", self._on_wheel)
        self.bind("<Double-Button-1>", self._reset_view)

    # ---------- 基础 ----------

    def set_board_size(self, n):
        self.board_size = n
        self.pixels = [0] * (n * n)
        self.ref_pixels = None
        self.selection = None
        self.undo_stack.clear()
        self.redo_stack.clear()
        self.reset_view()
        self.redraw()

    def set_current_color(self, idx):
        self.current_color = idx
        self._applied_hl = -2

    def set_tool(self, tool):
        self.tool = tool
        if tool != TOOL_SELECT:
            self.selection = None
            self._update_sel_rect()
        self.configure(cursor=self._tool_cursor())

    def _tool_cursor(self):
        return {
            TOOL_BRUSH: "pencil",
            TOOL_ERASER: "dotbox",
            TOOL_FILL: "spraycan",
            TOOL_PICKER: "crosshair",
            TOOL_SELECT: "crosshair",
        }.get(self.tool, "")

    def set_locked(self, locked):
        self.locked = locked

    def set_show_codes(self, show):
        self.show_codes = show
        self.redraw()

    def set_show_highlight(self, show):
        self.show_highlight = show
        self._applied_hl = -2
        self._apply_highlight()

    def set_show_coords(self, show):
        self.show_coords = show
        self.redraw()

    def set_reference(self, ref_pixels):
        self.ref_pixels = ref_pixels
        self.redraw()

    def reset_view(self):
        self.zoom = 1.0
        self.pan_x = 0
        self.pan_y = 0

    def _on_configure(self, e):
        self.redraw()

    # ---------- 撤销 / 重做 ----------

    def _begin_stroke(self):
        self._cur_stroke = {}

    def _record(self, index, old_value):
        if self._cur_stroke is None:
            self._cur_stroke = {}
        if index not in self._cur_stroke:
            self._cur_stroke[index] = old_value

    def _end_stroke(self):
        if self._cur_stroke:
            new_values = {i: self.pixels[i] for i in self._cur_stroke}
            if any(self._cur_stroke[i] != new_values[i] for i in self._cur_stroke):
                self.undo_stack.append((self._cur_stroke, new_values))
                if len(self.undo_stack) > UNDO_LIMIT:
                    self.undo_stack.pop(0)
                self.redo_stack.clear()
        self._cur_stroke = None

    def push_undo_state(self, old_pixels):
        new_pixels = list(self.pixels)
        diff_old = {}
        diff_new = {}
        for i, (a, b) in enumerate(zip(old_pixels, new_pixels)):
            if a != b:
                diff_old[i] = a
                diff_new[i] = b
        if diff_old:
            self.undo_stack.append((diff_old, diff_new))
            if len(self.undo_stack) > UNDO_LIMIT:
                self.undo_stack.pop(0)
            self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return False
        old, new = self.undo_stack.pop()
        for i, v in old.items():
            self.pixels[i] = v
        self.redo_stack.append((old, new))
        self.redraw()
        if self.on_cell_change:
            self.on_cell_change()
        return True

    def redo(self):
        if not self.redo_stack:
            return False
        old, new = self.redo_stack.pop()
        for i, v in new.items():
            self.pixels[i] = v
        self.undo_stack.append((old, new))
        self.redraw()
        if self.on_cell_change:
            self.on_cell_change()
        return True

    # ---------- 布局 / 缩放 / 平移 ----------

    def _base_cell(self):
        cw, ch = self.winfo_width(), self.winfo_height()
        n = self.board_size
        if n <= 0 or cw <= 1 or ch <= 1:
            return 0, cw, ch
        return max(2, min(cw // n, ch // n)), cw, ch

    def _compute_layout(self):
        base, cw, ch = self._base_cell()
        n = self.board_size
        cell = max(2, int(base * self.zoom))
        self.cell = cell
        self.offset_x = (cw - cell * n) // 2 + self.pan_x
        self.offset_y = (ch - cell * n) // 2 + self.pan_y

    def _on_wheel(self, e):
        n = self.board_size
        if n <= 0:
            return
        self._compute_layout()
        mx, my = e.x, e.y
        gx = (mx - self.offset_x) / self.cell
        gy = (my - self.offset_y) / self.cell
        factor = 1.15 if e.delta > 0 else (1 / 1.15)
        new_zoom = max(0.15, min(12.0, self.zoom * factor))
        if abs(new_zoom - self.zoom) < 1e-6:
            return
        self.zoom = new_zoom
        base, cw, ch = self._base_cell()
        new_cell = max(2, int(base * self.zoom))
        self.pan_x = int(mx - gx * new_cell - (cw - new_cell * n) // 2)
        self.pan_y = int(my - gy * new_cell - (ch - new_cell * n) // 2)
        self.redraw()

    def _reset_view(self, e=None):
        self.reset_view()
        self.redraw()

    def _on_mpress(self, e):
        self._panning = True
        self._pan_start = (e.x, e.y, self.pan_x, self.pan_y)
        self.configure(cursor="fleur")

    def _on_mdrag(self, e):
        if not self._panning:
            return
        x0, y0, px0, py0 = self._pan_start
        self.pan_x = px0 + (e.x - x0)
        self.pan_y = py0 + (e.y - y0)
        self._compute_layout()
        self.redraw()

    def _on_mrelease(self, e):
        self._panning = False
        self.configure(cursor=self._tool_cursor())

    # ---------- 绘制 ----------

    def _dim(self, rgb):
        r, g, b = (rgb >> 16) & 255, (rgb >> 8) & 255, rgb & 255
        a = self.DIM_A
        return "#%02x%02x%02x" % (
            int(r * a + 0x2b * (1 - a)),
            int(g * a + 0x2b * (1 - a)),
            int(b * a + 0x2b * (1 - a)))

    def _ref_color(self, x, y):
        if self.ref_pixels is None:
            return None
        px = self.ref_pixels[y * self.board_size + x]
        if px is None:
            return None
        r, g, b, a = px
        if a < 16:
            return None
        a_ = self.REF_A * (a / 255.0)
        return "#%02x%02x%02x" % (
            int(r * a_ + 0x1e * (1 - a_)),
            int(g * a_ + 0x1e * (1 - a_)),
            int(b * a_ + 0x1e * (1 - a_)))

    def redraw(self):
        self.delete("all")
        self._cell_items = []
        self._code_items = []
        self._coord_items = []
        self._hover_rect = None
        self._tooltip_items = []
        self._sel_rect = None
        if self.board_size <= 0:
            return
        cw, ch = self.winfo_width(), self.winfo_height()
        if cw <= 1 or ch <= 1:
            return
        self._compute_layout()
        n = self.board_size
        cell = self.cell
        ol = "#000000" if cell >= 6 else ""

        for y in range(n):
            for x in range(n):
                x0 = self.offset_x + x * cell
                y0 = self.offset_y + y * cell
                v = self.pixels[y * n + x]
                if v > 0:
                    fill = hex_of(COLORS[v - 1])
                    outline = ol
                else:
                    ref = self._ref_color(x, y)
                    fill = ref if ref else self.EMPTY_FILL
                    outline = self.EMPTY_OUTLINE if not ref else ""
                item = self.create_rectangle(x0, y0, x0 + cell, y0 + cell,
                                             fill=fill, outline=outline)
                self._cell_items.append(item)
                if self.show_codes and cell >= 16 and v > 0:
                    fs = max(6, cell // 3)
                    txt = self.create_text(x0 + cell // 2, y0 + cell // 2,
                                           text=CODES[v - 1],
                                           fill=contrast_fg(COLORS[v - 1]),
                                           font=("Arial", fs, "bold"))
                    self._code_items.append((txt, x, y))

        if self.show_coords:
            self._draw_coords()

        self._applied_hl = -2
        self._apply_highlight()
        self._update_sel_rect()

    def _draw_coords(self):
        n = self.board_size
        cell = self.cell
        fs = max(5, min(10, cell // 2))
        for x in range(n):
            cx = self.offset_x + x * cell + cell // 2
            cy = self.offset_y - 2
            t = self.create_text(cx, cy, text=str(x + 1), anchor="s",
                                 fill="#aaaaaa", font=("Arial", fs))
            self._coord_items.append(t)
        for y in range(n):
            cx = self.offset_x - 2
            cy = self.offset_y + y * cell + cell // 2
            t = self.create_text(cx, cy, text=str(y + 1), anchor="e",
                                 fill="#aaaaaa", font=("Arial", fs))
            self._coord_items.append(t)

    def _apply_highlight(self):
        if self.show_highlight and self.hover_color is not None:
            h = self.hover_color
        else:
            h = -1
        if h == self._applied_hl:
            return
        self._applied_hl = h
        for i, item in enumerate(self._cell_items):
            v = self.pixels[i]
            if v == 0:
                continue
            ci = v - 1
            if h < 0 or ci == h:
                self.itemconfig(item, fill=hex_of(COLORS[ci]))
            else:
                self.itemconfig(item, fill=self._dim(COLORS[ci]))

    # ---------- 鼠标 ----------

    def _update_hover(self, x, y):
        c = self._cell_at(x, y)
        self.hover = c
        if c is None:
            self.hover_color = None
        else:
            v = self.pixels[c[1] * self.board_size + c[0]]
            self.hover_color = (v - 1) if v > 0 else None
        self._apply_highlight()
        self._update_hover_rect()
        if self.on_hover:
            self.on_hover(c)

    def _on_motion(self, e):
        self._update_hover(e.x, e.y)

    def _on_leave(self, e):
        self.hover = None
        self.hover_color = None
        self._apply_highlight()
        self._update_hover_rect()

    def _update_hover_rect(self):
        if self._hover_rect is not None:
            self.delete(self._hover_rect)
            self._hover_rect = None
        for it in self._tooltip_items:
            self.delete(it)
        self._tooltip_items = []
        if self.hover is None:
            return
        hx, hy = self.hover
        x0 = self.offset_x + hx * self.cell
        y0 = self.offset_y + hy * self.cell
        self._hover_rect = self.create_rectangle(
            x0, y0, x0 + self.cell, y0 + self.cell,
            outline=self.HOVER_OUTLINE, width=2)
        n = self.board_size
        v = self.pixels[hy * n + hx]
        if v > 0:
            rgb = COLORS[v - 1]
            code = CODES[v - 1]
        else:
            rgb = 0x2b2b2b
            code = "(空)"
        tx = x0 + self.cell + 8
        ty = y0 + self.cell + 8
        bw, bh = 180, 84
        cw = self.winfo_width()
        if tx + bw > cw:
            tx = x0 - bw - 8
        bg = self.create_rectangle(tx, ty, tx + bw, ty + bh,
                                   fill="#f0f0f0", outline="#000000")
        self._tooltip_items.append(bg)
        sw = self.create_rectangle(tx + 6, ty + 6, tx + 54, ty + bh - 6,
                                   fill=hex_of(rgb), outline="#333333")
        self._tooltip_items.append(sw)
        r, g, b = (rgb >> 16) & 255, (rgb >> 8) & 255, rgb & 255
        lines = [code, f"#{rgb:06X}", f"RGB {r},{g},{b}",
                 f"坐标 ({hx+1}, {hy+1})"]
        for k, line in enumerate(lines):
            t = self.create_text(tx + 62, ty + 8 + k * 18, anchor="nw",
                                 text=line, fill="#000000",
                                 font=("Consolas", 9))
            self._tooltip_items.append(t)

    def _cell_at(self, x, y):
        if self.board_size == 0:
            return None
        cx = (x - self.offset_x) // self.cell
        cy = (y - self.offset_y) // self.cell
        if 0 <= cx < self.board_size and 0 <= cy < self.board_size:
            return cx, cy
        return None

    # ---------- 绘制操作 ----------

    def _set_pixel(self, cx, cy, new_v):
        i = cy * self.board_size + cx
        old = self.pixels[i]
        if old == new_v:
            return False
        self._record(i, old)
        self.pixels[i] = new_v        
        item = self._cell_items[i]
        if new_v > 0:
            self.itemconfig(item, fill=hex_of(COLORS[new_v - 1]),
                            outline="#000000" if self.cell >= 6 else "")
        else:
            ref = self._ref_color(cx, cy)
            self.itemconfig(item, fill=ref if ref else self.EMPTY_FILL,
                            outline=self.EMPTY_OUTLINE if not ref else "")
        self._applied_hl = -2
        self._apply_highlight()
        return True

    def _paint(self, x, y, erase=False):
        c = self._cell_at(x, y)
        if c is None or self.locked:
            return
        cx, cy = c
        if erase:
            new_v = 0
        else:
            if self.current_color < 0:
                return
            new_v = self.current_color + 1
        if self._set_pixel(cx, cy, new_v):
            if self.on_cell_change:
                self.on_cell_change()

    def flood_fill(self, cx, cy, new_v):
        n = self.board_size
        target = self.pixels[cy * n + cx]
        if target == new_v:
            return
        stack = [(cx, cy)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            if not (0 <= x < n and 0 <= y < n):
                continue
            i = y * n + x
            if self.pixels[i] != target:
                continue
            visited.add((x, y))
            self._set_pixel(x, y, new_v)
            stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

    # ---------- 选区 ----------

    def _update_sel_rect(self):
        if self._sel_rect is not None:
            self.delete(self._sel_rect)
            self._sel_rect = None
        if not self.selection:
            return
        x0, y0, x1, y1 = self.selection
        c = self.cell
        self._sel_rect = self.create_rectangle(
            self.offset_x + x0 * c, self.offset_y + y0 * c,
            self.offset_x + (x1 + 1) * c, self.offset_y + (y1 + 1) * c,
            outline=self.SELECT_OUTLINE, width=2, dash=(4, 2))

    def delete_selection(self):
        if not self.selection:
            return False
        x0, y0, x1, y1 = self.selection
        self._begin_stroke()
        for yy in range(y0, y1 + 1):
            for xx in range(x0, x1 + 1):
                self._set_pixel(xx, yy, 0)
        self._end_stroke()
        if self.on_cell_change:
            self.on_cell_change()
        return True

    # ---------- 鼠标事件 ----------

    def _on_press(self, e):
        if self.locked:
            return
        self.focus_set()
        c = self._cell_at(e.x, e.y)

        if self.tool == TOOL_BRUSH:
            self._painting_btn = "L"
            self._begin_stroke()
            self._paint(e.x, e.y)
        elif self.tool == TOOL_ERASER:
            self._painting_btn = "L"
            self._begin_stroke()
            self._paint(e.x, e.y, erase=True)
        elif self.tool == TOOL_PICKER:
            if c is not None:
                v = self.pixels[c[1] * self.board_size + c[0]]
                if v > 0 and self.on_pick_color:
                    self.on_pick_color(v - 1)
        elif self.tool == TOOL_FILL:
            if c is not None and self.current_color >= 0:
                self._begin_stroke()
                self.flood_fill(c[0], c[1], self.current_color + 1)
                self._end_stroke()
                if self.on_cell_change:
                    self.on_cell_change()
        elif self.tool == TOOL_SELECT:
            if c is None:
                self.selection = None
                self._update_sel_rect()
                return
            self._painting_btn = "L"
            self._sel_drag_start = c
            self.selection = (c[0], c[1], c[0], c[1])
            self._update_sel_rect()

    def _on_drag(self, e):
        if self._painting_btn != "L":
            return
        self._update_hover(e.x, e.y)
        if self.tool == TOOL_BRUSH:
            self._paint(e.x, e.y)
        elif self.tool == TOOL_ERASER:
            self._paint(e.x, e.y, erase=True)
        elif self.tool == TOOL_SELECT and self._sel_drag_start:
            c = self._cell_at(e.x, e.y)
            if c is not None:
                x0, y0 = self._sel_drag_start
                x1, y1 = c
                self.selection = (min(x0, x1), min(y0, y1),
                                  max(x0, x1), max(y0, y1))
                self._update_sel_rect()

    def _on_release(self, e):
        if self._painting_btn == "L":
            self._end_stroke()
        self._painting_btn = None
        self._sel_drag_start = None

    def _on_rpress(self, e):
        if self.locked:
            return
        self._painting_btn = "R"
        self._begin_stroke()
        self._paint(e.x, e.y, erase=True)

    def _on_rdrag(self, e):
        if self._painting_btn != "R":
            return
        self._update_hover(e.x, e.y)
        self._paint(e.x, e.y, erase=True)

    def _on_rrelease(self, e):
        self._end_stroke()
        self._painting_btn = None


# ==================== PDF / PNG 导出 ====================

def _register_chinese_font():
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception:
        pass
    for path, name in [
        ("C:/Windows/Fonts/msyh.ttc", "MicrosoftYaHei"),
        ("C:/Windows/Fonts/msyh.ttf", "MicrosoftYaHei"),
        ("C:/Windows/Fonts/simhei.ttf", "SimHei"),
        ("C:/Windows/Fonts/simsun.ttc", "SimSun"),
        ("/System/Library/Fonts/PingFang.ttc", "PingFang"),
        ("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", "WenQuanYi"),
    ]:
        if os.path.exists(path):
            try:
                from reportlab.pdfbase.ttfonts import TTFont
                pdfmetrics.registerFont(TTFont(name, path))
                return name
            except Exception:
                continue
    return "Helvetica"


def export_png(pixels, board_size, title, path):
    if not HAS_PIL:
        raise RuntimeError("需要 Pillow 才能生成 PNG")
    CELL = 24
    PAD = 40
    HEAD = 60
    FOOT = 40
    W = CELL * board_size + PAD * 2
    H = HEAD + CELL * board_size + FOOT

    from PIL import ImageDraw, ImageFont

    img = PILImage.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    _font_cache = {}

    def get_font(size):
        if size in _font_cache:
            return _font_cache[size]
        for p in ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf",
                  "/System/Library/Fonts/PingFang.ttc",
                  "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"]:
            if os.path.exists(p):
                try:
                    f = ImageFont.truetype(p, size)
                    _font_cache[size] = f
                    return f
                except Exception:
                    pass
        f = ImageFont.load_default()
        _font_cache[size] = f
        return f

    draw.text((W // 2, 30), title, fill="black", anchor="mm", font=get_font(24))

    x0 = PAD
    y0 = HEAD
    for gy in range(board_size):
        for gx in range(board_size):
            v = pixels[gy * board_size + gx]
            cx = x0 + gx * CELL
            cy = y0 + gy * CELL
            if v > 0:
                rgb = COLORS[v - 1]
                fill = (rgb >> 16 & 255, rgb >> 8 & 255, rgb & 255)
            else:
                fill = (245, 245, 245)
            draw.rectangle([cx, cy, cx + CELL, cy + CELL],
                           fill=fill, outline=(80, 80, 80))
            if v > 0:
                fg = "black" if sum(fill) > 380 else "white"
                draw.text((cx + CELL // 2, cy + CELL // 2),
                          CODES[v - 1], fill=fg, anchor="mm", font=get_font(12))

    draw.text((W // 2, H - 20), f"{board_size} × {board_size}", fill="gray",
              anchor="mm", font=get_font(14))

    img.save(path)


def export_pdf(pixels, board_size, title, path):
    if not HAS_REPORTLAB:
        raise RuntimeError("需要 reportlab，请 pip install reportlab")

    font_name = _register_chinese_font()
    PAGE_MAX = 32
    pages_x = (board_size + PAGE_MAX - 1) // PAGE_MAX
    pages_y = (board_size + PAGE_MAX - 1) // PAGE_MAX
    total = pages_x * pages_y
    PAGE_W, PAGE_H = landscape(A4)
    MM = 72.0 / 25.4

    c = rl_canvas.Canvas(path, pagesize=(PAGE_W, PAGE_H))

    first = True
    for py in range(pages_y):
        for px in range(pages_x):
            if not first:
                c.showPage()
            first = False
            page_idx = py * pages_x + px + 1
            _draw_page(c, pixels, board_size, title, font_name,
                       PAGE_W, PAGE_H, MM, px, py, PAGE_MAX, page_idx, total)
    c.save()


def _draw_page(c, pixels, board_size, title, font, pw, ph, MM, px, py, psize, page_idx, total):
    MARGIN = 6 * MM
    TOP = 13 * MM
    BOTTOM = 8 * MM
    AXIS_MM = 5 * MM

    c.setFont(font, 14)
    c.drawCentredString(pw / 2, ph - 7 * MM, f"{title} - 第 {page_idx} / {total} 页")

    x_start = px * psize
    y_start = py * psize
    x_end = min(x_start + psize, board_size)
    y_end = min(y_start + psize, board_size)
    pw_cells = x_end - x_start
    ph_cells = y_end - y_start

    counts = {}
    for gy in range(y_start, y_end):
        for gx in range(x_start, x_end):
            v = pixels[gy * board_size + gx]
            if v > 0:
                counts[v - 1] = counts.get(v - 1, 0) + 1
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

    usable_h = ph - TOP - BOTTOM
    table_row_h = 5 * MM
    table_header_h = 6 * MM
    table_col_w = 32 * MM
    table_rows_per_col = max(1, int((usable_h - table_header_h) / table_row_h))
    table_cols = max(1, -(-len(items) // table_rows_per_col))
    if table_cols > 3:
        table_cols = 3
    table_w = table_cols * table_col_w

    grid_area_x = MARGIN
    grid_area_y = BOTTOM
    grid_area_w = pw - MARGIN * 2 - table_w - 2 * MM
    grid_area_h = usable_h

    cell_area_w = grid_area_w - AXIS_MM
    cell_area_h = grid_area_h - AXIS_MM

    cell = min(cell_area_w / pw_cells, cell_area_h / ph_cells)
    grid_w = cell * pw_cells
    grid_h = cell * ph_cells

    grid_x = grid_area_x + AXIS_MM
    grid_y = grid_area_y + AXIS_MM + (cell_area_h - grid_h) / 2

    for gy in range(ph_cells):
        for gx in range(pw_cells):
            v = pixels[(y_start + gy) * board_size + (x_start + gx)]
            cx = grid_x + gx * cell
            cy = grid_y + (ph_cells - 1 - gy) * cell
            if v > 0:
                rgb = COLORS[v - 1]
                c.setFillColorRGB((rgb >> 16 & 255) / 255,
                                  (rgb >> 8 & 255) / 255, (rgb & 255) / 255)
                c.rect(cx, cy, cell, cell, fill=1, stroke=0)
            else:
                c.setFillColorRGB(0.96, 0.96, 0.96)
                c.rect(cx, cy, cell, cell, fill=1, stroke=0)
            c.setStrokeColorRGB(0.4, 0.4, 0.4)
            c.setLineWidth(0.3)
            c.rect(cx, cy, cell, cell, fill=0, stroke=1)
            if v > 0:
                txt = CODES[v - 1]
                fs = max(4, min(9, cell * 0.42))
                c.setFont(font, fs)
                r, g, b = (rgb >> 16 & 255), (rgb >> 8 & 255), (rgb & 255)
                if (r * 0.299 + g * 0.587 + b * 0.114) > 128:
                    c.setFillColorRGB(0, 0, 0)
                else:
                    c.setFillColorRGB(1, 1, 1)
                c.drawCentredString(cx + cell / 2, cy + cell / 2 - fs * 0.35, txt)

    axis_fs = max(4, min(9, cell * 0.42))
    c.setFont(font, axis_fs)
    c.setFillColorRGB(0, 0, 0)
    for gx in range(pw_cells):
        abs_x = x_start + gx + 1
        cx = grid_x + gx * cell + cell / 2
        cy = grid_y + grid_h + 1
        c.drawCentredString(cx, cy, str(abs_x))
    for gy in range(ph_cells):
        abs_y = y_start + gy + 1
        cx = grid_x - 1
        cy = grid_y + (ph_cells - 1 - gy) * cell + cell / 2 - axis_fs * 0.35
        c.drawRightString(cx, cy, str(abs_y))

    tx = pw - MARGIN - table_w
    ty = ph - TOP
    for col in range(table_cols):
        col_x = tx + col * table_col_w
        c.setFillColorRGB(0.94, 0.94, 0.94)
        c.rect(col_x, ty - table_header_h, table_col_w, table_header_h, fill=1, stroke=0)
        c.setStrokeColorRGB(0.2, 0.2, 0.2)
        c.setLineWidth(0.5)
        c.rect(col_x, ty - table_header_h, table_col_w, table_header_h, fill=0, stroke=1)
        c.setFillColorRGB(0, 0, 0)
        c.setFont(font, 7)
        header_y = ty - table_header_h / 2 - 2
        c.drawString(col_x + 1.5 * MM, header_y, "色号")
        c.drawString(col_x + 11 * MM, header_y, "数量")
        c.drawString(col_x + 18 * MM, header_y, "已完成")

        for r in range(table_rows_per_col):
            i = col * table_rows_per_col + r
            if i >= len(items):
                break
            idx, cnt = items[i]
            row_y = ty - table_header_h - (r + 1) * table_row_h

            c.setStrokeColorRGB(0.7, 0.7, 0.7)
            c.setLineWidth(0.3)
            c.line(col_x, row_y, col_x + table_col_w, row_y)

            sw = 3 * MM
            c.setFillColorRGB((COLORS[idx] >> 16 & 255) / 255,
                              (COLORS[idx] >> 8 & 255) / 255,
                              (COLORS[idx] & 255) / 255)
            c.rect(col_x + 1 * MM, row_y + (table_row_h - sw) / 2, sw, sw, fill=1, stroke=0)
            c.setStrokeColorRGB(0.2, 0.2, 0.2)
            c.setLineWidth(0.3)
            c.rect(col_x + 1 * MM, row_y + (table_row_h - sw) / 2, sw, sw, fill=0, stroke=1)

            c.setFillColorRGB(0, 0, 0)
            c.setFont(font, 7)
            text_y = row_y + table_row_h / 2 - 2
            c.drawString(col_x + 5 * MM, text_y, CODES[idx])
            c.drawRightString(col_x + 17 * MM, text_y, str(cnt))

            c.setStrokeColorRGB(0.2, 0.2, 0.2)
            c.setLineWidth(0.4)
            c.rect(col_x + 18 * MM, row_y + (table_row_h - 3 * MM) / 2,
                   3 * MM, 3 * MM, fill=0, stroke=1)


# ==================== 可拖动区域 ====================

class RegionFrame(tk.Frame):
    """一个可拖动/可缩放的区域容器，用 place() 定位。"""

    EDGE = 5
    TITLE_H = 20

    def __init__(self, master, key, title, on_move, get_other_rects, app):
        super().__init__(master, bg="#888", bd=0, highlightthickness=0)
        self.key = key
        self.app = app
        self.on_move = on_move
        self.get_other_rects = get_other_rects

        self.title_bar = tk.Label(self, text=title, bg="#444", fg="#fff",
                                  font=("Arial", 9, "bold"), anchor="w",
                                  padx=6, pady=2)
        self.body = tk.Frame(self, bg="#2b2b2b")

        self.mask = tk.Frame(self.body, bg="#f0a000", bd=0)
        self.mask.bind("<Motion>", self._on_motion)
        self.mask.bind("<Button-1>", self._on_press)
        self.mask.bind("<B1-Motion>", self._on_drag)
        self.mask.bind("<ButtonRelease-1>", self._on_release)

        self.body.place(x=0, y=0, width=1, height=1)
        self.title_bar.place_forget()

        self.edit_mode = False
        self.drag_mode = None
        self.drag_start = None
        self.rect_start = None

        self.bind("<Configure>", self._on_region_configure)
        self.title_bar.bind("<Button-1>", self._on_press)
        self.title_bar.bind("<B1-Motion>", self._on_drag)
        self.title_bar.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Motion>", self._on_motion)
        self.title_bar.bind("<Motion>", self._on_motion)

    def _on_region_configure(self, e):
        w = self.winfo_width()
        h = self.winfo_height()
        if self.edit_mode:
            self.title_bar.place(x=0, y=0, width=w, height=self.TITLE_H)
            self.body.place(x=0, y=self.TITLE_H, width=w,
                            height=max(1, h - self.TITLE_H))
        else:
            self.title_bar.place_forget()
            self.body.place(x=0, y=0, width=w, height=h)

    def set_edit_mode(self, on):
        self.edit_mode = on
        if on:
            self.config(bg="#f0a000")
            self.title_bar.place(x=0, y=0, width=self.winfo_width(),
                                 height=self.TITLE_H)
            self.body.place(x=0, y=self.TITLE_H, width=self.winfo_width(),
                            height=max(1, self.winfo_height() - self.TITLE_H))
            self.mask.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.mask.lift()
        else:
            self.config(bg="#888")
            self.title_bar.place_forget()
            self.body.place(x=0, y=0, width=self.winfo_width(),
                            height=self.winfo_height())
            self.mask.place_forget()

    def _on_motion(self, e):
        if not self.edit_mode:
            self.configure(cursor="")
            return
        x = e.x
        y = e.y
        if e.widget is self.mask:
            y += self.TITLE_H
        w = self.winfo_width()
        h = self.winfo_height()
        left = x < self.EDGE
        right = x > w - self.EDGE
        top = y < self.EDGE
        bottom = y > h - self.EDGE
        if (left and top) or (right and bottom):
            self.configure(cursor="size_nw_se")
        elif (right and top) or (left and bottom):
            self.configure(cursor="size_ne_sw")
        elif left or right:
            self.configure(cursor="sb_h_double_arrow")
        elif top or bottom:
            self.configure(cursor="sb_v_double_arrow")
        else:
            self.configure(cursor="fleur")

    def _mode_from_xy(self, x, y):
        w = self.winfo_width()
        h = self.winfo_height()
        left = x < self.EDGE
        right = x > w - self.EDGE
        top = y < self.EDGE
        bottom = y > h - self.EDGE
        if left and top: return "tl"
        if right and top: return "tr"
        if left and bottom: return "bl"
        if right and bottom: return "br"
        if left: return "left"
        if right: return "right"
        if top: return "top"
        if bottom: return "bottom"
        return "move"

    def _on_press(self, e):
        if not self.edit_mode:
            return
        if e.widget is self.mask:
            x = e.x
            y = e.y + self.TITLE_H
        elif e.widget is self.title_bar:
            x = e.x
            y = e.y
        else:
            x, y = e.x, e.y
        mode = self._mode_from_xy(x, y)
        if e.widget is self.title_bar:
            mode = "move"
        self.drag_mode = mode
        self.drag_start = (e.x_root, e.y_root)
        self.rect_start = (self.winfo_x(), self.winfo_y(),
                           self.winfo_width(), self.winfo_height())

    def _on_drag(self, e):
        if not self.edit_mode or self.drag_mode is None:
            return
        dx = e.x_root - self.drag_start[0]
        dy = e.y_root - self.drag_start[1]
        x0, y0, w0, h0 = self.rect_start
        mode = self.drag_mode

        nx, ny, nw, nh = x0, y0, w0, h0
        if mode == "move":
            nx, ny = x0 + dx, y0 + dy
        else:
            if mode in ("left", "tl", "bl"):
                nx = x0 + dx
                nw = w0 - dx
            if mode in ("right", "tr", "br"):
                nw = w0 + dx
            if mode in ("top", "tl", "tr"):
                ny = y0 + dy
                nh = h0 - dy
            if mode in ("bottom", "bl", "br"):
                nh = h0 + dy

        nw = max(1, nw)
        nh = max(1, nh)

        if mode == "move":
            nx, ny = self._snap_move(nx, ny, nw, nh)
        else:
            nx, ny, nw, nh = self._snap_resize(nx, ny, nw, nh, mode)

        if self._overlaps_others(nx, ny, nw, nh):
            return

        self.place(x=nx, y=ny, width=nw, height=nh)
        self.on_move(self.key, nx, ny, nw, nh)

    def _snap_move(self, x, y, w, h):
        root_w = self.master.winfo_width()
        root_h = self.master.winfo_height()
        others = self.get_other_rects(self.key)
        xs = [0, root_w - w]
        ys = [0, root_h - h]
        for (ox, oy, ow, oh) in others:
            xs.extend([ox, ox + ow, ox - w, ox + ow - w])
            ys.extend([oy, oy + oh, oy - h, oy + oh - h])
        for tx in xs:
            if abs(x - tx) <= SNAP:
                x = tx
                break
        for ty in ys:
            if abs(y - ty) <= SNAP:
                y = ty
                break
        return x, y

    def _snap_resize(self, x, y, w, h, mode):
        root_w = self.master.winfo_width()
        root_h = self.master.winfo_height()
        others = self.get_other_rects(self.key)

        vlines = [0, root_w]
        hlines = [0, root_h]
        for (ox, oy, ow, oh) in others:
            vlines.extend([ox, ox + ow])
            hlines.extend([oy, oy + oh])

        if mode in ("left", "tl", "bl"):
            for vx in vlines:
                if abs(x - vx) <= SNAP:
                    w += x - vx
                    x = vx
                    break
        if mode in ("right", "tr", "br"):
            right = x + w
            for vx in vlines:
                if abs(right - vx) <= SNAP:
                    w = vx - x
                    break
        if mode in ("top", "tl", "tr"):
            for vy in hlines:
                if abs(y - vy) <= SNAP:
                    h += y - vy
                    y = vy
                    break
        if mode in ("bottom", "bl", "br"):
            bottom = y + h
            for vy in hlines:
                if abs(bottom - vy) <= SNAP:
                    h = vy - y
                    break

        w = max(1, w)
        h = max(1, h)
        return x, y, w, h

    def _on_release(self, e):
        if self.drag_mode is not None:
            self.app.save_layout()
        self.drag_mode = None
        self.drag_start = None
        self.rect_start = None

    def _overlaps_others(self, x, y, w, h):
        for (ox, oy, ow, oh) in self.get_other_rects(self.key):
            if not (x + w <= ox or x >= ox + ow or y + h <= oy or y >= oy + oh):
                return True
        return False


# ==================== 主程序 ====================

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("拼豆实验室 Bead Lab")
        try:
            icon = ensure_icon()
            if icon:
                self.iconbitmap(icon)
        except Exception:
            pass
        self.geometry("1400x860")
        self.minsize(600, 400)
        self.recent_files = []
        self.load_recent()

        self.board_size = 16
        self.completed = False
        self.ref_original = None
        self.mc_version = "1.20.5-"

        self.region_ratios = dict(DEFAULT_LAYOUT)
        self.region_visible = {k: tk.BooleanVar(value=True) for k in REGION_NAMES}
        self.regions = {}
        self.edit_mode = False

        self.load_layout()

        self._build_menu()
        self._build_toolbar()
        self._build_regions()

        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.bind("<Configure>", self._on_window_configure)

    # ---------- 工具 / 坐标 ----------

    def on_tool_change(self):
        self.canvas.set_tool(self.tool_var.get())

    def on_coords_toggle(self):
        self.canvas.set_show_coords(self.coords_var.get())

    def on_pick_color(self, idx):
        self.palette.select(idx)
        self.status_var.set(f"取色 {CODES[idx]}")

    # ---------- 撤销 / 重做 ----------

    def undo_cmd(self):
        if not self.canvas.undo():
            self.status_var.set("无可撤销")

    def redo_cmd(self):
        if not self.canvas.redo():
            self.status_var.set("无可重做")

    # ---------- 选区 ----------

    def delete_selection_cmd(self):
        if self.canvas.delete_selection():
            self.status_var.set("已删除选区内容")

    # ---------- 最近文件 ----------

    def load_recent(self):
        try:
            with open(RECENT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                self.recent_files = [p for p in data if isinstance(p, str)][:RECENT_LIMIT]
        except Exception:
            self.recent_files = []

    def save_recent(self):
        try:
            os.makedirs(os.path.dirname(RECENT_FILE), exist_ok=True)
            with open(RECENT_FILE, "w", encoding="utf-8") as f:
                json.dump(self.recent_files, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def add_recent(self, path):
        path = os.path.abspath(path)
        if path in self.recent_files:
            self.recent_files.remove(path)
        self.recent_files.insert(0, path)
        self.recent_files = self.recent_files[:RECENT_LIMIT]
        self.save_recent()
        self._rebuild_recent_menu()

    def _rebuild_recent_menu(self):
        self.recent_menu.delete(0, tk.END)
        if not self.recent_files:
            self.recent_menu.add_command(label="(空)", state="disabled")
            return
        for p in self.recent_files:
            self.recent_menu.add_command(
                label=os.path.basename(p),
                command=lambda path=p: self.open_recent(path))
        self.recent_menu.add_separator()
        self.recent_menu.add_command(label="清除列表", command=self.clear_recent)

    def clear_recent(self):
        self.recent_files = []
        self.save_recent()
        self._rebuild_recent_menu()

    def open_recent(self, path):
        if not os.path.exists(path):
            messagebox.showerror("文件不存在", path)
            self.recent_files.remove(path)
            self.save_recent()
            self._rebuild_recent_menu()
            return
        self._load_json_file(path)

    def clear_canvas(self):
        if self.completed:
            messagebox.showinfo("提示", "请先点击「修改设计」再编辑。")
            return
        if not messagebox.askyesno("确认", "清空整个拼豆板？"):
            return
        old = list(self.canvas.pixels)
        self.canvas.pixels = [0] * (self.board_size ** 2)
        self.canvas.push_undo_state(old)
        self.canvas.redraw()
        self._clear_command()
        self._update_stats()

    # ---------- 菜单 ----------

    def _build_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        board_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="画板", menu=board_menu)

        import_menu = tk.Menu(board_menu, tearoff=0)
        import_menu.add_command(label="导入拼豆文件 (json)", command=self.import_json)
        import_menu.add_command(label="导入图片", command=self.import_image)
        board_menu.add_cascade(label="导入", menu=import_menu)

        # 最近打开 → 放进画板菜单
        self.recent_menu = tk.Menu(board_menu, tearoff=0)
        board_menu.add_cascade(label="最近打开", menu=self.recent_menu)
        self._rebuild_recent_menu()

        board_menu.add_command(label="撤销  Ctrl+Z", command=self.undo_cmd)
        board_menu.add_command(label="重做  Ctrl+Y", command=self.redo_cmd)
        board_menu.add_separator()

        export_menu = tk.Menu(board_menu, tearoff=0)
        export_menu.add_command(label="导出拼豆文件 (json)", command=self.export_json)
        export_menu.add_command(label="导出拼豆图纸 (png)", command=self.export_png_cmd)
        export_menu.add_command(label="导出拼豆图纸 (pdf)", command=self.export_pdf_cmd)
        board_menu.add_cascade(label="导出", menu=export_menu)

        version_menu = tk.Menu(board_menu, tearoff=0)
        self.version_var = tk.StringVar(value=self.mc_version)
        version_menu.add_radiobutton(
            label="1.20.5- (NBT 格式)",
            variable=self.version_var, value="1.20.5-",
            command=self._on_version_change)
        version_menu.add_radiobutton(
            label="1.20.5+ (数据驱动格式)",
            variable=self.version_var, value="1.20.5+",
            command=self._on_version_change)
        board_menu.add_cascade(label="版本", menu=version_menu)

        ref_menu = tk.Menu(board_menu, tearoff=0)
        ref_menu.add_command(label="导入参考图", command=self.import_reference)
        ref_menu.add_command(label="清空参考图", command=self.clear_reference)
        board_menu.add_cascade(label="参考图", menu=ref_menu)

        board_menu.add_separator()
        board_menu.add_command(label="清空画板", command=self.clear_canvas)
        board_menu.add_separator()
        board_menu.add_command(label="退出", command=self._on_close)

        region_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="区域", menu=region_menu)
        for key, name in REGION_NAMES.items():
            region_menu.add_checkbutton(label=name, variable=self.region_visible[key],
                                        command=lambda k=key: self._toggle_region(k))
        region_menu.add_separator()
        self.edit_mode_var = tk.BooleanVar(value=False)
        region_menu.add_checkbutton(label="编辑模式", variable=self.edit_mode_var,
                                    command=self._toggle_edit_mode)
        region_menu.add_separator()
        region_menu.add_command(label="重置布局", command=self.reset_layout)

    def _toggle_region(self, key):
        visible = self.region_visible[key].get()
        region = self.regions.get(key)
        if region is None:
            return
        if visible:
            self._apply_region_ratios()
        else:
            region.place_forget()
        self.save_layout()

    def _toggle_edit_mode(self):
        on = self.edit_mode_var.get()
        self.edit_mode = on
        for region in self.regions.values():
            region.set_edit_mode(on)

    def reset_layout(self):
        if not messagebox.askyesno("确认", "恢复默认布局？"):
            return
        self.region_ratios = dict(DEFAULT_LAYOUT)
        for var in self.region_visible.values():
            var.set(True)
        self._apply_region_ratios()
        self.save_layout()

    # ---------- 工具栏 ----------

    def _build_toolbar(self):
        self.toolbar = ttk.Frame(self, padding=6)
        self.toolbar.place(x=0, y=0, width=1400, height=40)

        self.tool_var = tk.StringVar(value=TOOL_BRUSH)
        for tool in (TOOL_BRUSH, TOOL_ERASER, TOOL_FILL, TOOL_PICKER, TOOL_SELECT):
            ttk.Radiobutton(self.toolbar, text=TOOL_NAMES[tool],
                            value=tool, variable=self.tool_var,
                            command=self.on_tool_change).pack(side="left", padx=1, pady=2)
        ttk.Separator(self.toolbar, orient="vertical").pack(side="left", fill="y", padx=4)

        ttk.Label(self.toolbar, text="拼豆板:").pack(side="left", pady=2)
        self.size_var = tk.StringVar(value="16")
        self.size_combo = ttk.Combobox(self.toolbar, textvariable=self.size_var,
                                       width=5, state="readonly",
                                       values=[str(s) for s in BOARD_SIZES])
        self.size_combo.pack(side="left", padx=2, pady=2)
        self.size_combo.bind("<<ComboboxSelected>>", self.on_size_change)

        ttk.Label(self.toolbar, text="标题:").pack(side="left", padx=(12, 2), pady=2)
        self.title_var = tk.StringVar(value="拼豆图纸")
        ttk.Entry(self.toolbar, textvariable=self.title_var, width=12).pack(side="left", pady=2)

        self.crop_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.toolbar, text="裁剪空白", variable=self.crop_var,
                        command=self.refresh_command_if_any).pack(side="left", padx=(12, 4), pady=2)

        self.rescale_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.toolbar, text="游戏内缩放", variable=self.rescale_var,
                        command=self.refresh_command_if_any).pack(side="left", padx=4, pady=2)

        self.highlight_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.toolbar, text="高亮显示选择的层",
                        variable=self.highlight_var,
                        command=self.on_highlight_toggle).pack(side="left", padx=4, pady=2)

        self.coords_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.toolbar, text="坐标",
                        variable=self.coords_var,
                        command=self.on_coords_toggle).pack(side="left", padx=4, pady=2)

        self.design_btn = ttk.Button(self.toolbar, text="完成设计",
                                     command=self.toggle_design)
        self.design_btn.pack(side="left", padx=12, fill="y")

        self.codes_btn = ttk.Button(self.toolbar, text="显示色号",
                                    command=self.toggle_codes, state="disabled")
        self.codes_btn.pack(side="left", padx=4, fill="y")

        ttk.Button(self.toolbar, text="重置视图",
                   command=self.reset_view).pack(side="left", padx=4, fill="y")

        ttk.Label(self.toolbar, text="玩家:").pack(side="left", padx=(16, 2), pady=2)
        self.player_var = tk.StringVar(value="@s")
        entry = ttk.Entry(self.toolbar, textvariable=self.player_var, width=12)
        entry.pack(side="left", pady=2)
        entry.bind("<KeyRelease>", lambda e: self.refresh_command_if_any())

    # ---------- 区域 ----------

    def _build_regions(self):
        for key, name in REGION_NAMES.items():
            self.regions[key] = RegionFrame(
                self, key, name,
                self._on_region_move, self._get_other_rects, self)

        self.palette = ColorPalette(self.regions["palette"].body,
                                    on_select=self.on_color_select)
        self.palette.pack(fill="both", expand=True)

        self.canvas = PreviewCanvas(self.regions["canvas"].body,
                                    on_cell_change=self._on_cell_change,
                                    on_pick_color=self.on_pick_color)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.set_board_size(16)

        self.canvas.bind("<Control-z>", lambda e: (self.undo_cmd(), "break"))
        self.canvas.bind("<Control-y>", lambda e: (self.redo_cmd(), "break"))
        self.canvas.bind("<Delete>", lambda e: (self.delete_selection_cmd(), "break"))

        cmd_body = self.regions["command"].body
        cmd_hdr = ttk.Frame(cmd_body)
        cmd_hdr.pack(fill="x")
        self.cmd_len = tk.StringVar(value="长度 0")
        ttk.Label(cmd_hdr, textvariable=self.cmd_len).pack(side="left", padx=4)
        ttk.Button(cmd_hdr, text="一键复制", command=self.copy_cmd).pack(side="right", padx=4)
        self.cmd_text = tk.Text(cmd_body, wrap="word", font=("Consolas", 9))
        self.cmd_text.pack(fill="both", expand=True)

        stat_body = self.regions["stats"].body
        self.stat_tree = ttk.Treeview(stat_body, columns=("code", "count"), show="headings")
        self.stat_tree.heading("code", text="色号")
        self.stat_tree.heading("count", text="数量")
        self.stat_tree.column("code", width=80, anchor="w", stretch=False)
        self.stat_tree.column("count", width=80, anchor="e", stretch=False)
        stat_sb = ttk.Scrollbar(stat_body, orient="vertical", command=self.stat_tree.yview)
        self.stat_tree.configure(yscrollcommand=stat_sb.set)
        self.stat_tree.pack(side="left", fill="both", expand=True)
        stat_sb.pack(side="right", fill="y")

        self.status_var = tk.StringVar(value="就绪")
        self.status_bar = ttk.Label(self, textvariable=self.status_var,
                                    relief="sunken", anchor="w")
        self.status_bar.place(x=0, y=830, width=1400, height=22)

        self._apply_region_ratios()

    def _on_region_move(self, key, x, y, w, h):
        W = self.winfo_width()
        H = self.winfo_height()
        if W <= 0 or H <= 0:
            return
        toolbar_h = 40
        status_h = 22
        avail_h = H - toolbar_h - status_h
        if avail_h <= 0:
            avail_h = H
            toolbar_h = 0
        self.region_ratios[key] = (
            x / W,
            (y - toolbar_h) / avail_h,
            w / W,
            h / avail_h,
        )

    def _get_other_rects(self, exclude_key):
        rects = []
        for key, region in self.regions.items():
            if key == exclude_key:
                continue
            if not self.region_visible[key].get():
                continue
            if not region.winfo_ismapped():
                continue
            rects.append((region.winfo_x(), region.winfo_y(),
                          region.winfo_width(), region.winfo_height()))
        return rects

    def _apply_region_ratios(self):
        W = self.winfo_width()
        H = self.winfo_height()
        if W <= 1 or H <= 1:
            return
        toolbar_h = 40
        status_h = 22
        avail_y = toolbar_h
        avail_h = H - toolbar_h - status_h
        if avail_h <= 0:
            avail_h = H
            avail_y = 0
        for key, (rx, ry, rw, rh) in self.region_ratios.items():
            if key not in self.regions:
                continue
            if not self.region_visible[key].get():
                continue
            x = int(rx * W)
            y = int(avail_y + ry * avail_h)
            w = max(1, int(rw * W))
            h = max(1, int(rh * avail_h))
            region = self.regions[key]
            region.place(x=x, y=y, width=w, height=h)
            region.lift()

    def _on_window_configure(self, e):
        if e.widget is not self:
            return
        self._apply_region_ratios()
        self.status_bar.place(x=0, y=self.winfo_height() - 22,
                            width=self.winfo_width(), height=22)
        self.toolbar.place(x=0, y=0, width=self.winfo_width(), height=40)

    # ---------- 布局持久化 ----------

    def save_layout(self):
        data = {
            "regions": {k: list(v) for k, v in self.region_ratios.items()},
            "visible": {k: bool(v.get()) for k, v in self.region_visible.items()},
        }
        try:
            with open(LAYOUT_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception:
            pass

    def load_layout(self):
        if not os.path.exists(LAYOUT_FILE):
            return
        try:
            with open(LAYOUT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            return
        regions = data.get("regions") or {}
        for k, v in regions.items():
            if k in DEFAULT_LAYOUT and isinstance(v, list) and len(v) == 4:
                self.region_ratios[k] = tuple(v)
        visible = data.get("visible") or {}
        for k, v in visible.items():
            if k in self.region_visible:
                self.region_visible[k].set(bool(v))

    def _on_close(self):
        self.save_layout()
        self.quit()

    # ---------- 业务逻辑 ----------

    def _on_version_change(self):
        self.mc_version = self.version_var.get()
        self.refresh_command_if_any()

    def on_color_select(self, idx):
        self.canvas.set_current_color(idx)
        self.status_var.set(f"已选 {CODES[idx]}")

    def on_highlight_toggle(self):
        self.canvas.set_show_highlight(self.highlight_var.get())
        self.status_var.set("高亮显示选择的层: " +
                            ("开" if self.highlight_var.get() else "关"))

    def reset_view(self):
        self.canvas.reset_view()
        self.canvas.redraw()

    def on_size_change(self, e=None):
        new = int(self.size_var.get())
        if new == self.board_size:
            return
        if any(v > 0 for v in self.canvas.pixels):
            if not messagebox.askyesno("确认", "切换拼豆板大小会清空拼豆板，是否继续？"):
                self.size_var.set(str(self.board_size))
                return
        if new >= 64:
            if not messagebox.askyesno("确认", "拼豆板太大可能会影响性能并导致卡顿，是否继续？"):
                self.size_var.set(str(self.board_size))
                return
        self.board_size = new
        self.canvas.set_board_size(new)
        if self.ref_original:
            self._apply_reference()
        self._clear_command()
        self._update_stats()

    def import_image(self):
        if self.completed:
            messagebox.showinfo("提示", "请先点击「修改设计」再编辑。")
            return
        path = filedialog.askopenfilename(
            title="选择图片",
            filetypes=[("图片", "*.png *.jpg *.jpeg *.gif *.bmp *.webp"),
                       ("所有文件", "*.*")])
        if not path:
            return
        try:
            w, h, pixels = load_image_pixels(path)
        except Exception as e:
            messagebox.showerror("读取失败", str(e))
            return
        n = self.board_size
        nw, nh, ox, oy = fit_into(w, h, n, n)
        scaled = nearest_resize(w, h, pixels, nw, nh)
        old = list(self.canvas.pixels)
        new_pixels = [0] * (n * n)
        for yy in range(nh):
            for xx in range(nw):
                r, g, b, a = scaled[yy * nw + xx]
                if a < 128:
                    continue
                idx = nearest_index(r, g, b)
                new_pixels[(oy + yy) * n + (ox + xx)] = idx + 1
        self.canvas.pixels = new_pixels
        self.canvas.push_undo_state(old)
        self.canvas.redraw()
        self._clear_command()
        self._update_stats()
        self.status_var.set(f"已加载图片 {w}×{h} → {nw}×{nh}")

    def import_reference(self):
        path = filedialog.askopenfilename(
            title="选择参考图",
            filetypes=[("图片", "*.png *.jpg *.jpeg *.gif *.bmp *.webp"),
                       ("所有文件", "*.*")])
        if not path:
            return
        try:
            w, h, pixels = load_image_pixels(path)
        except Exception as e:
            messagebox.showerror("读取失败", str(e))
            return
        self.ref_original = (w, h, pixels)
        self._apply_reference()
        self.status_var.set(f"参考图 {w}×{h}")

    def _apply_reference(self):
        w, h, pixels = self.ref_original
        n = self.board_size
        nw, nh, ox, oy = fit_into(w, h, n, n)
        scaled = nearest_resize(w, h, pixels, nw, nh)
        arr = [None] * (n * n)
        for yy in range(nh):
            for xx in range(nw):
                arr[(oy + yy) * n + (ox + xx)] = scaled[yy * nw + xx]
        self.canvas.set_reference(arr)

    def clear_reference(self):
        if self.ref_original is None:
            self.status_var.set("没有参考图")
            return
        self.ref_original = None
        self.canvas.set_reference(None)
        self.status_var.set("已清空参考图")

    def export_json(self):
        filename = safe_filename(self.title_var.get()) + ".json"
        path = filedialog.asksaveasfilename(
            title="导出拼豆文件",
            defaultextension=".json",
            initialfile=filename,
            filetypes=[("拼豆 JSON", "*.json"), ("所有文件", "*.*")])
        if not path:
            return
        data = {
            "format": FILE_FORMAT,
            "version": FILE_VERSION,
            "boardSize": self.board_size,
            "pixels": list(self.canvas.pixels),
            "title": self.title_var.get(),
            "settings": {
                "player": self.player_var.get(),
                "mcVersion": self.mc_version,
                "cropEmpty": bool(self.crop_var.get()),
                "needRescale": bool(self.rescale_var.get()),
            },
        }
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
            self.status_var.set(f"已导出: {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("导出失败", str(e))

    def import_json(self):
        path = filedialog.askopenfilename(
            title="导入拼豆文件",
            filetypes=[("拼豆 JSON", "*.json"), ("所有文件", "*.*")])
        if not path:
            return
        self._load_json_file(path)

    def _load_json_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            messagebox.showerror("读取失败", str(e))
            return

        fmt = data.get("format")
        if fmt != FILE_FORMAT and fmt != FILE_FORMAT_LEGACY:
            messagebox.showerror("格式错误", "这不是拼豆文件。")
            return

        board = data.get("boardSize")
        pixels = data.get("pixels")
        if board not in BOARD_SIZES or not isinstance(pixels, list) or len(pixels) != board * board:
            messagebox.showerror("数据错误", "拼豆板尺寸或像素数量不对。")
            return

        for v in pixels:
            if not isinstance(v, int) or v < 0 or v > len(CODES):
                messagebox.showerror("数据错误", f"像素值非法: {v}")
                return

        if any(v > 0 for v in self.canvas.pixels):
            if not messagebox.askyesno("确认", "会覆盖当前画布，继续？"):
                return

        self.board_size = board
        self.size_var.set(str(board))
        self.canvas.set_board_size(board)
        self.canvas.pixels = [int(v) for v in pixels]
        self.canvas.redraw()

        if isinstance(data.get("title"), str):
            self.title_var.set(data["title"])

        s = data.get("settings") or {}
        if isinstance(s.get("player"), str):
            self.player_var.set(s["player"])
        if s.get("mcVersion") in ("1.20.5-", "1.20.5+"):
            self.mc_version = s["mcVersion"]
            self.version_var.set(self.mc_version)
        self.crop_var.set(bool(s.get("cropEmpty", False)))
        self.rescale_var.set(bool(s.get("needRescale", False)))

        self._clear_command()
        self._update_stats()
        self.add_recent(path)
        self.status_var.set(f"已导入: {os.path.basename(path)}")

    def export_png_cmd(self):
        if not HAS_PIL:
            messagebox.showerror("缺少依赖", "需要 Pillow：pip install pillow")
            return
        filename = safe_filename(self.title_var.get()) + ".png"
        path = filedialog.asksaveasfilename(
            title="导出拼豆图纸 PNG",
            defaultextension=".png",
            initialfile=filename,
            filetypes=[("PNG 图片", "*.png"), ("所有文件", "*.*")])
        if not path:
            return
        try:
            export_png(self.canvas.pixels, self.board_size,
                       self.title_var.get() or "拼豆图纸", path)
            self.status_var.set(f"已导出 PNG: {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("导出失败", str(e))

    def export_pdf_cmd(self):
        if not HAS_REPORTLAB:
            messagebox.showerror("缺少依赖", "需要 reportlab：pip install reportlab")
            return
        filename = safe_filename(self.title_var.get()) + ".pdf"
        path = filedialog.asksaveasfilename(
            title="导出拼豆图纸 PDF",
            defaultextension=".pdf",
            initialfile=filename,
            filetypes=[("PDF", "*.pdf"), ("所有文件", "*.*")])
        if not path:
            return
        try:
            export_pdf(self.canvas.pixels, self.board_size,
                       self.title_var.get() or "拼豆图纸", path)
            self.status_var.set(f"已导出 PDF: {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("导出失败", str(e))

    def toggle_design(self):
        self.completed = not self.completed
        self.canvas.set_locked(self.completed)
        self.palette.set_enabled(not self.completed)
        if self.completed:
            self.design_btn.config(text="修改设计")
            self.codes_btn.config(state="normal")
            self.generate_command()
        else:
            self.design_btn.config(text="完成设计")
            self.codes_btn.config(state="disabled")
            self.canvas.set_show_codes(False)
            self.codes_btn.config(text="显示色号")

    def toggle_codes(self):
        on = self.canvas.show_codes
        self.canvas.set_show_codes(not on)
        self.codes_btn.config(text="隐藏色号" if not on else "显示色号")

    def _on_cell_change(self):
        if not self.completed:
            self._clear_command()
        self._update_stats()

    def _clear_command(self):
        self.cmd_text.delete("1.0", tk.END)
        self.cmd_len.set("长度 0")

    def refresh_command_if_any(self):
        if self.cmd_text.get("1.0", tk.END).strip():
            self.generate_command(silent=True)

    def _update_stats(self):
        for row in self.stat_tree.get_children():
            self.stat_tree.delete(row)
        counts = {}
        for v in self.canvas.pixels:
            if v > 0:
                counts[v - 1] = counts.get(v - 1, 0) + 1
        items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        for idx, c in items:
            self.stat_tree.insert("", "end", values=(CODES[idx], c))
        total = sum(c for _, c in items)
        self.stat_tree.insert("", "end", values=("总计", total))
        self.stat_tree.insert("", "end", values=("色数", len(items)))

    def generate_command(self, silent=False):
        n = self.board_size
        px_all = self.canvas.pixels

        if self.crop_var.get():
            min_x, min_y = n, n
            max_x, max_y = -1, -1
            for y in range(n):
                for x in range(n):
                    if px_all[y * n + x] > 0:
                        if x < min_x: min_x = x
                        if x > max_x: max_x = x
                        if y < min_y: min_y = y
                        if y > max_y: max_y = y
            if max_x < 0:
                if not silent:
                    messagebox.showwarning("无数据", "画布为空。")
                return
            w = max_x - min_x + 1
            h = max_y - min_y + 1
            px = []
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    px.append(px_all[y * n + x])
        else:
            w = h = n
            px = list(px_all)

        player = self.player_var.get().strip() or "@s"
        size = max(w, h)
        px_str = ",".join(str(v) for v in px)
        rescale = "1b" if self.rescale_var.get() else "0b"
        inner = (f"Size:{size},Width:{w},Height:{h},"
                 f"BeadDataVersion:2,NeedRescale:{rescale},Pixels:[I;{px_str}]")
        if self.mc_version == "1.20.5+":
            cmd = f"/give {player} brainlayers:bead_artwork[custom_data={{{inner}}}]"
        else:
            cmd = f"/give {player} brainlayers:bead_artwork{{{inner}}}"
        self.cmd_text.delete("1.0", tk.END)
        self.cmd_text.insert("1.0", cmd)
        self.cmd_len.set(f"长度 {len(cmd)}")
        self.status_var.set(f"已生成命令，尺寸 {w}×{h}，长度 {len(cmd)} 字符")

    def copy_cmd(self):
        text = self.cmd_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showinfo("无内容", "没有可复制的命令。")
            return
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()
        self.status_var.set("已复制到剪贴板")


if __name__ == "__main__":
    App().mainloop()