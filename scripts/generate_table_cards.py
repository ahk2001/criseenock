"""
Gerador de Plaquinhas de Mesa em Alta Definição (300 DPI)
Casamento Cris & Enock — 09 de Janeiro de 2027

Gera 6 arquivos prontos para impressão:
1. plaquinha-10x15-monograma.png (1200x1800 px)
2. plaquinha-10x15-classica.png (1200x1800 px)
3. plaquinha-tenda-monograma.png (1400x2000 px)
4. plaquinha-tenda-classica.png (1400x2000 px)
5. plaquinha-folha-a4-monograma.png (2480x3508 px - 2 cartões em folha A4 com guias de corte)
6. plaquinha-folha-a4-classica.png (2480x3508 px - 2 cartões em folha A4 com guias de corte)
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, "..")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets", "images")
OUTPUT_DIR = os.path.join(ASSETS_DIR, "plaquinhas")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Cores oficiais da identidade visual
COLOR_BG_LIGHT = (253, 251, 247, 255)     # #FDFBF7
COLOR_BG_DARK = (247, 242, 233, 255)      # #F7F2E9
COLOR_GOLD = (212, 175, 55, 255)          # #D4AF37
COLOR_GOLD_DARK = (184, 134, 11, 255)     # #B8860B
COLOR_GOLD_LIGHT = (239, 229, 213, 255)   # #EFE5D5
COLOR_CHARCOAL = (34, 30, 28, 255)        # #221E1C
COLOR_WARMGRAY = (107, 98, 91, 255)       # #6B625B

def get_font(name="georgia.ttf", size=32):
    try:
        return ImageFont.truetype(name, size)
    except Exception:
        try:
            return ImageFont.truetype("times.ttf", size)
        except Exception:
            return ImageFont.load_default()

def draw_gradient_background(img, c1, c2):
    w, h = img.size
    base = Image.new("RGBA", (w, h), c1)
    draw = ImageDraw.Draw(base)
    for y in range(h):
        r = int(c1[0] + (c2[0] - c1[0]) * (y / h))
        g = int(c1[1] + (c2[1] - c1[1]) * (y / h))
        b = int(c1[2] + (c2[2] - c1[2]) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
    return base

def draw_single_card(w=1200, h=1800, qr_type="monograma"):
    """Renderiza uma plaquinha individual de 10x15cm (1200x1800 px)"""
    card = draw_gradient_background(Image.new("RGBA", (w, h)), COLOR_BG_LIGHT, COLOR_BG_DARK)
    draw = ImageDraw.Draw(card)
    
    # Molduras douradas duplas elegantes
    margin1 = int(w * 0.04)
    margin2 = int(w * 0.055)
    draw.rounded_rectangle([margin1, margin1, w - margin1, h - margin1], radius=24, outline=COLOR_GOLD_DARK, width=4)
    draw.rounded_rectangle([margin2, margin2, w - margin2, h - margin2], radius=16, outline=COLOR_GOLD, width=2)
    
    # Detalhes ornamentais nos 4 cantos
    corner_font = get_font("georgia.ttf", 26)
    draw.text((margin2 + 15, margin2 + 10), "✦", fill=COLOR_GOLD_DARK, font=corner_font)
    draw.text((w - margin2 - 35, margin2 + 10), "✦", fill=COLOR_GOLD_DARK, font=corner_font)
    draw.text((margin2 + 15, h - margin2 - 40), "✦", fill=COLOR_GOLD_DARK, font=corner_font)
    draw.text((w - margin2 - 35, h - margin2 - 40), "✦", fill=COLOR_GOLD_DARK, font=corner_font)
    
    # 1. Monograma circular no topo
    cx = w // 2
    circle_y = int(h * 0.09)
    circle_r = int(w * 0.055)
    draw.ellipse([cx - circle_r, circle_y - circle_r, cx + circle_r, circle_y + circle_r], fill=(255, 255, 255, 255), outline=COLOR_GOLD_DARK, width=3)
    draw.ellipse([cx - circle_r + 4, circle_y - circle_r + 4, cx + circle_r - 4, circle_y + circle_r - 4], outline=COLOR_GOLD, width=1)
    
    mono_font = get_font("georgia.ttf", 36)
    draw.text((cx, circle_y), "C & E", fill=COLOR_GOLD_DARK, font=mono_font, anchor="mm")
    
    # 2. Nomes dos Noivos
    names_font = get_font("georgia.ttf", 34)
    draw.text((cx, circle_y + circle_r + 35), "C R I S   &   E N O C K", fill=COLOR_GOLD_DARK, font=names_font, anchor="mm")
    
    date_font = get_font("times.ttf", 26)
    draw.text((cx, circle_y + circle_r + 75), "09 de Janeiro de 2027 • Jaraguá do Sul — SC", fill=COLOR_WARMGRAY, font=date_font, anchor="mm")
    
    # Divisor dourado sutil
    div_y = circle_y + circle_r + 115
    draw.line([(cx - 150, div_y), (cx + 150, div_y)], fill=COLOR_GOLD, width=2)
    draw.polygon([(cx, div_y - 4), (cx + 6, div_y), (cx, div_y + 4), (cx - 6, div_y)], fill=COLOR_GOLD_DARK)
    
    # 3. Chamada Principal
    title_font = get_font("georgia.ttf", 46)
    draw.text((cx, div_y + 55), "Compartilhe seus cliques da festa!", fill=COLOR_CHARCOAL, font=title_font, anchor="mm")
    
    sub_font = get_font("times.ttf", 28)
    draw.text((cx, div_y + 110), "Aponte a câmera do seu celular para o QR Code abaixo", fill=COLOR_WARMGRAY, font=sub_font, anchor="mm")
    draw.text((cx, div_y + 145), "e envie suas fotos direto para o nosso Mural ao Vivo!", fill=COLOR_WARMGRAY, font=sub_font, anchor="mm")
    
    # 4. QR Code oficial em Alta Resolução
    qr_filename = "qrcode-mural-monograma.png" if qr_type == "monograma" else "qrcode-mural.png"
    qr_path = os.path.join(ASSETS_DIR, qr_filename)
    if os.path.exists(qr_path):
        qr_img = Image.open(qr_path).convert("RGBA")
        qr_size = int(w * 0.44)  # ~530x530 px
        qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
        
        # Fundo branco e borda para o QR Code
        qr_box_pad = 20
        qr_box_x1 = cx - (qr_size // 2) - qr_box_pad
        qr_box_y1 = div_y + 200
        qr_box_x2 = cx + (qr_size // 2) + qr_box_pad
        qr_box_y2 = qr_box_y1 + qr_size + (qr_box_pad * 2)
        
        draw.rounded_rectangle([qr_box_x1, qr_box_y1, qr_box_x2, qr_box_y2], radius=24, fill=(255, 255, 255, 255), outline=COLOR_GOLD, width=3)
        card.paste(qr_img, (cx - (qr_size // 2), qr_box_y1 + qr_box_pad), qr_img)
        bottom_flow_y = qr_box_y2
    else:
        bottom_flow_y = div_y + 700

    # 5. Passos simples numerados (1, 2, 3)
    step_y = bottom_flow_y + 65
    step_num_font = get_font("georgia.ttf", 22)
    step_txt_font = get_font("arial.ttf", 22)
    
    steps = [
        ("1", "Abra a câmera"),
        ("2", "Aponte para o QR"),
        ("3", "Suba suas fotos!")
    ]
    spacing = w // 3
    for i, (num, txt) in enumerate(steps):
        sx = int((i + 0.5) * spacing)
        draw.ellipse([sx - 20, step_y - 20, sx + 20, step_y + 20], fill=(239, 229, 213, 255), outline=COLOR_GOLD, width=1)
        draw.text((sx, step_y), num, fill=COLOR_GOLD_DARK, font=step_num_font, anchor="mm")
        draw.text((sx, step_y + 36), txt, fill=COLOR_WARMGRAY, font=step_txt_font, anchor="mm")
        
    # 6. Assinatura do casal
    sig_font = get_font("times.ttf", 40)
    draw.text((cx, h - margin2 - 55), "Com amor, Cris & Enock", fill=COLOR_GOLD_DARK, font=sig_font, anchor="mm")
    
    return card

def generate_all_cards():
    # 1. Porta-Retrato 10x15 cm (Monograma e Clássico)
    for q_type in ["monograma", "classica"]:
        print(f"Gerando Porta-Retrato 10x15 ({q_type})...")
        card = draw_single_card(w=1200, h=1800, qr_type=q_type)
        filename = f"plaquinha-10x15-{q_type}.png"
        out_path = os.path.join(OUTPUT_DIR, filename)
        card.save(out_path, "PNG", dpi=(300, 300))
        print(f" -> Salvo em {out_path} ({card.size[0]}x{card.size[1]} px, 300 DPI)")
        
    # 2. Tenda Dobrável (1400x2000 px)
    for q_type in ["monograma", "classica"]:
        print(f"Gerando Tenda Dobrável ({q_type})...")
        tent = Image.new("RGBA", (1400, 2000), (255, 255, 255, 255))
        
        # Cada lado tem 1300 x 940 px
        side1 = draw_single_card(w=1300, h=940, qr_type=q_type)
        # Lado 1 (superior) fica invertido em 180° para que o cume fique na dobra central
        side1_rot = side1.rotate(180)
        
        side2 = draw_single_card(w=1300, h=940, qr_type=q_type)
        # Lado 2 (inferior) fica na orientação padrão
        
        tent.paste(side1_rot, (50, 40), side1_rot)
        tent.paste(side2, (50, 1020), side2)
        
        # Linha de vinco central tracejada
        draw = ImageDraw.Draw(tent)
        mid_y = 1000
        for x in range(60, 1340, 30):
            draw.line([(x, mid_y), (x + 18, mid_y)], fill=COLOR_GOLD_DARK, width=3)
            
        badge_font = get_font("georgia.ttf", 22)
        badge_txt = "✂ LINHA DE DOBRA AO MEIO (VINCO PARA FICAR EM PÉ) ✂"
        draw.rounded_rectangle([350, mid_y - 20, 1050, mid_y + 20], radius=15, fill=(255, 255, 255, 255), outline=COLOR_GOLD, width=2)
        draw.text((700, mid_y), badge_txt, fill=COLOR_GOLD_DARK, font=badge_font, anchor="mm")
        
        filename = f"plaquinha-tenda-{q_type}.png"
        out_path = os.path.join(OUTPUT_DIR, filename)
        tent.save(out_path, "PNG", dpi=(300, 300))
        print(f" -> Salvo em {out_path} ({tent.size[0]}x{tent.size[1]} px, 300 DPI)")

    # 3. Folha A4 Econômica (2480x3508 px - 2 cartões por folha)
    for q_type in ["monograma", "classica"]:
        print(f"Gerando Folha A4 Econômica ({q_type})...")
        a4 = Image.new("RGBA", (2480, 3508), (255, 255, 255, 255))
        draw = ImageDraw.Draw(a4)
        
        # 2 cartões de 1160 x 1700 px colocados lado a lado ou empilhados
        # Empilhados: Cartão 1 no topo, Cartão 2 na base
        card_w = 2100
        card_h = 1580
        
        c1 = draw_single_card(w=card_w, h=card_h, qr_type=q_type)
        c2 = draw_single_card(w=card_w, h=card_h, qr_type=q_type)
        
        pos_x = (2480 - card_w) // 2
        a4.paste(c1, (pos_x, 100), c1)
        a4.paste(c2, (pos_x, 1780), c2)
        
        # Linha de corte central
        cut_y = 1730
        for x in range(100, 2380, 40):
            draw.line([(x, cut_y), (x + 24, cut_y)], fill=(180, 180, 180, 255), width=2)
            
        cut_font = get_font("arial.ttf", 26)
        draw.text((1240, cut_y - 25), "✂ LINHA DE CORTE (SEPARE OS 2 CARTÕES) ✂", fill=(120, 120, 120, 255), font=cut_font, anchor="mm")
        
        filename = f"plaquinha-folha-a4-{q_type}.png"
        out_path = os.path.join(OUTPUT_DIR, filename)
        a4.save(out_path, "PNG", dpi=(300, 300))
        print(f" -> Salvo em {out_path} ({a4.size[0]}x{a4.size[1]} px, 300 DPI)")

if __name__ == "__main__":
    generate_all_cards()
    print("\n[SUCESSO] Todas as 6 plaquinhas foram geradas com perfeição a 300 DPI!")
