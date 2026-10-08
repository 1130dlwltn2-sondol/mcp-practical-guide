#!/usr/bin/env python3
"""MCP 실전 가이드 - 표지 및 설명용 이미지 생성 (PIL)."""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
os.makedirs(ASSETS, exist_ok=True)

def font(size, bold=True):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

NAVY = (15, 25, 55); TEAL = (0, 150, 135); LIGHT = (235, 245, 250)
WHITE = (255, 255, 255); GRAY = (90, 100, 115); ACCENT = (255, 140, 0)

def cover():
    img = Image.new("RGB", (1000, 1300), NAVY); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1000, 520], fill=TEAL)
    d.rectangle([0, 520, 1000, 528], fill=ACCENT)
    d.text((80, 140), "MODEL CONTEXT", font=font(72), fill=WHITE)
    d.text((80, 230), "PROTOCOL", font=font(72), fill=WHITE)
    d.text((80, 360), "MCP 실전 가이드", font=font(88), fill=WHITE)
    d.text((80, 470), "AI와 도구를 잇는 공개 표준", font=font(40, False), fill=WHITE)
    d.text((80, 620), "아키텍처부터 SDK 실습,", font=font(44, False), fill=LIGHT)
    d.text((80, 690), "원격 서버와 OAuth까지", font=font(44, False), fill=LIGHT)
    d.text((80, 820), "Host · Client · Server", font=font(40), fill=ACCENT)
    d.text((80, 890), "Tools · Resources · Prompts", font=font(40), fill=ACCENT)
    d.text((80, 1060), "저자 이준수", font=font(44, False), fill=GRAY)
    d.text((80, 1140), "기준일 2026-10-09", font=font(36, False), fill=GRAY)
    img.save(os.path.join(ASSETS, "cover.png"))

def diagram(name, title, boxes, arrows):
    img = Image.new("RGB", (1200, 700), WHITE); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1200, 110], fill=NAVY)
    d.text((60, 32), title, font=font(44), fill=WHITE)
    for (x, y, w, h, label, sub, color) in boxes:
        d.rectangle([x, y, x + w, y + h], fill=color, outline=NAVY, width=3)
        d.text((x + 20, y + 18), label, font=font(36), fill=NAVY)
        if sub: d.text((x + 20, y + 68), sub, font=font(28, False), fill=GRAY)
    for (x1, y1, x2, y2, label) in arrows:
        d.line([x1, y1, x2, y2], fill=ACCENT, width=5)
        d.polygon([(x2, y2), (x2 - 18, y2 - 10), (x2 - 18, y2 + 10)], fill=ACCENT)
        if label:
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2 - 34
            d.text((mx - 60, my), label, font=font(26, False), fill=GRAY)
    img.save(os.path.join(ASSETS, name))

B1 = TEAL; B2 = (255, 200, 120); B3 = (150, 200, 255)

diagram("fig-mcp-overview.png", "MCP: 연결의 표준화",
    [(60, 200, 320, 130, "M개 AI 도구", "각자 다른 연동 방식", B2),
     (820, 200, 320, 130, "N개 데이터·도구", "API, DB, 파일...", B3),
     (440, 430, 320, 130, "MCP", "하나의 표준 프로토콜", B1)],
    [(380, 265, 440, 495, ""), (820, 265, 760, 495, "")])

diagram("fig-arch.png", "MCP 아키텍처: Host, Client, Server",
    [(60, 200, 300, 140, "MCP Host", "Claude Desktop 등", B2),
     (450, 200, 300, 140, "MCP Client", "서버별 연결 담당", B3),
     (840, 200, 300, 140, "MCP Server", "도구·리소스 제공", B1)],
    [(360, 270, 450, 270, ""), (750, 270, 840, 270, "")])

diagram("fig-primitives.png", "세 가지 프리미티브",
    [(60, 200, 340, 150, "Tools", "실행 가능한 함수", B1),
     (430, 200, 340, 150, "Resources", "읽을 수 있는 데이터", B2),
     (800, 200, 340, 150, "Prompts", "재사용 템플릿", B3),
     (380, 470, 440, 110, "MCP Client", "tools/list → tools/call", LIGHT)],
    [(230, 350, 450, 470, ""), (600, 350, 600, 470, ""), (970, 350, 750, 470, "")])

diagram("fig-remote.png", "원격 MCP 서버와 OAuth",
    [(60, 180, 300, 130, "사용자", "Claude Code", B2),
     (450, 180, 300, 130, "원격 MCP 서버", "Streamable HTTP", B1),
     (840, 180, 300, 130, "인증 서버", "OAuth 토큰 발급", B3)],
    [(360, 245, 450, 245, "연결"), (750, 245, 840, 245, "토큰 검증")])

diagram("fig-project.png", "실전 프로젝트: 팀용 원격 MCP 서버",
    [(60, 170, 280, 120, "사내 API", "문서·배포 조회", B3),
     (400, 170, 280, 120, "MCP 서버", "도구로 감싸기", B1),
     (740, 170, 280, 120, "OAuth", "사용자별 권한", B2),
     (400, 430, 280, 120, "팀의 Claude Code", "공유 사용", LIGHT)],
    [(340, 230, 400, 230, ""), (680, 230, 740, 230, ""),
     (540, 290, 540, 430, "")])

cover()
print("done:", sorted(os.listdir(ASSETS)))
