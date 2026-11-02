"""
Gerador da Plaquinha Oficial de Mesa 10x15 cm — Casamento Cris & Enock
Dimensões exatas: 1200 x 1800 px (10 x 15 cm a 300 DPI)
Destino do QR Code: https://criseenock.vercel.app/#mural-section
"""

import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, "..")

W, H = 1200, 1800  # 10x15 cm a 300 DPI

# Cores oficiais da identidade visual
C_BG_TOP = (254, 252, 248, 255)       # Creme marfim muito suave
C_BG_BOT = (246, 240, 230, 255)       # Champanhe elegante
C_GOLD_DARK = (184, 134, 11, 255)     # #B8860B Ouro nobre
C_GOLD_LIGHT = (212, 175, 55, 255)    # #D4AF37 Ouro brilhante
C_CHARCOAL = (34, 30, 28, 255)        # #221E1C Carvão nobre para leitura
C_WARMGRAY = (115, 105, 98, 255)      # #736962 Cinza quente sofisticado

def get_font(family="georgia.ttf", size=32):
    try:
        return ImageFont.truetype(family, size)
    except Exception:
        try:
            return ImageFont.truetype("times.ttf", size)
        except Exception:
            return ImageFont.load_default()

def create_card_10x15():
    # 1. Fundo com degradê vertical acetinado
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        ratio = y / H
        r = int(C_BG_TOP[0] + (C_BG_BOT[0] - C_BG_TOP[0]) * ratio)
        g = int(C_BG_TOP[1] + (C_BG_BOT[1] - C_BG_TOP[1]) * ratio)
        b = int(C_BG_TOP[2] + (C_BG_BOT[2] - C_BG_TOP[2]) * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    cx = W // 2

    # 2. Moldura dupla decorativa
    pad1 = 50
    pad2 = 68
    draw.rounded_rectangle([pad1, pad1, W - pad1, H - pad1], radius=30, outline=C_GOLD_DARK, width=4)
    draw.rounded_rectangle([pad2, pad2, W - pad2, H - pad2], radius=20, outline=C_GOLD_LIGHT, width=2)

    # Detalhes ornamentais nos 4 cantos
    corner_font = get_font("georgia.ttf", 28)
    draw.text((pad2 + 18, pad2 + 12), "✦", fill=C_GOLD_DARK, font=corner_font)
    draw.text((W - pad2 - 40, pad2 + 12), "✦", fill=C_GOLD_DARK, font=corner_font)
    draw.text((pad2 + 18, H - pad2 - 45), "✦", fill=C_GOLD_DARK, font=corner_font)
    draw.text((W - pad2 - 40, H - pad2 - 45), "✦", fill=C_GOLD_DARK, font=corner_font)

    # 3. Selo de Monograma C & E no topo
    seal_y = 175
    seal_r = 65
    draw.ellipse([cx - seal_r, seal_y - seal_r, cx + seal_r, seal_y + seal_r], fill=(255, 255, 255, 255), outline=C_GOLD_DARK, width=3)
    draw.ellipse([cx - seal_r + 5, seal_y - seal_r + 5, cx + seal_r - 5, seal_y + seal_r - 5], outline=C_GOLD_LIGHT, width=1)
    mono_font = get_font("georgia.ttf", 40)
    draw.text((cx, seal_y), "C & E", fill=C_GOLD_DARK, font=mono_font, anchor="mm")

    # 4. Nomes dos Noivos e Data
    names_font = get_font("georgia.ttf", 36)
    draw.text((cx, 280), "C R I S   &   E N O C K", fill=C_GOLD_DARK, font=names_font, anchor="mm")
    
    date_font = get_font("times.ttf", 26)
    draw.text((cx, 325), "09 de Janeiro de 2027 • Jaraguá do Sul — SC", fill=C_WARMGRAY, font=date_font, anchor="mm")

    # Linha divisória dourada
    div_y = 370
    draw.line([(cx - 180, div_y), (cx + 180, div_y)], fill=C_GOLD_LIGHT, width=2)
    draw.polygon([(cx, div_y - 5), (cx + 7, div_y), (cx, div_y + 5), (cx - 7, div_y)], fill=C_GOLD_DARK)

    # 5. Título de Destaque
    title_font = get_font("georgia.ttf", 50)
    draw.text((cx, 440), "Compartilhe seus cliques!", fill=C_CHARCOAL, font=title_font, anchor="mm")

    sub_font = get_font("times.ttf", 30)
    draw.text((cx, 500), "Aponte a câmera do seu celular para o QR Code abaixo", fill=C_WARMGRAY, font=sub_font, anchor="mm")
    draw.text((cx, 540), "e envie suas fotos direto para o nosso Mural ao Vivo!", fill=C_WARMGRAY, font=sub_font, anchor="mm")

    # 6. QR Code Oficial com Monograma Central
    qr_path = os.path.join(PROJECT_ROOT, "assets", "images", "qrcode-mural-monograma.png")
    if os.path.exists(qr_path):
        qr = Image.open(qr_path).convert("RGBA")
    else:
        # Fallback gerando na hora
        qr_gen = qrcode.QRCode(box_size=16, border=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr_gen.add_data("https://criseenock.vercel.app/#mural-section")
        qr_gen.make(fit=True)
        qr = qr_gen.make_image(fill_color="#221E1C", back_color="#FFFFFF").convert("RGBA")

    qr_size = 560
    qr = qr.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

    box_pad = 22
    box_x1 = cx - (qr_size // 2) - box_pad
    box_y1 = 605
    box_x2 = cx + (qr_size // 2) + box_pad
    box_y2 = box_y1 + qr_size + (box_pad * 2)

    # Caixa branca com sombra e borda dourada para o QR Code
    draw.rounded_rectangle([box_x1, box_y1, box_x2, box_y2], radius=24, fill=(255, 255, 255, 255), outline=C_GOLD_LIGHT, width=3)
    img.paste(qr, (cx - (qr_size // 2), box_y1 + box_pad), qr)

    # 7. Instruções em 3 passos numerados
    steps_y = box_y2 + 80
    step_num_font = get_font("georgia.ttf", 24)
    step_txt_font = get_font("arial.ttf", 22)

    steps = [
        ("1", "Abra a câmera"),
        ("2", "Aponte para o QR"),
        ("3", "Suba suas fotos!")
    ]
    step_spacing = W // 3
    for i, (num, txt) in enumerate(steps):
        sx = int((i + 0.5) * step_spacing)
        draw.ellipse([sx - 22, steps_y - 22, sx + 22, steps_y + 22], fill=(240, 232, 218, 255), outline=C_GOLD_DARK, width=2)
        draw.text((sx, steps_y), num, fill=C_GOLD_DARK, font=step_num_font, anchor="mm")
        draw.text((sx, steps_y + 40), txt, fill=C_WARMGRAY, font=step_txt_font, anchor="mm")

    # 8. Assinatura solene dos noivos
    sig_font = get_font("times.ttf", 44)
    draw.text((cx, H - pad2 - 60), "Com amor, Cris & Enock", fill=C_GOLD_DARK, font=sig_font, anchor="mm")

    # Salva na raiz e em assets/images para fácil acesso
    dest1 = os.path.join(PROJECT_ROOT, "plaquinha_mesa_10x15_cris_e_enock.png")
    dest2 = os.path.join(PROJECT_ROOT, "assets", "images", "plaquinha_mesa_10x15_cris_e_enock.png")

    img.save(dest1, "PNG", dpi=(300, 300))
    img.save(dest2, "PNG", dpi=(300, 300))

    print(f"[OK] Imagem 10x15 gerada com sucesso:")
    print(f" -> {dest1} (1200x1800 px, 300 DPI)")

if __name__ == "__main__":
    create_card_10x15()
