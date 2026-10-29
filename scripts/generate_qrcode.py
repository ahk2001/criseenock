"""
Script de Geração Oficial dos QR Codes de Mesa - Casamento Cris & Enock
Gera QR Codes em altíssima resolução (PNG e SVG) com correção de erro de 30% (Nível H),
permitindo leitura instantânea por qualquer câmera de smartphone, mesmo à distância ou com iluminação suave de buffet.
Destino direto: Seção de Fotos dos Convidados (Mural do Casamento #mural-section).
"""

import os
import qrcode
from qrcode.image.svg import SvgPathImage
from PIL import Image, ImageDraw, ImageFont

TARGET_URL = "https://criseenock.vercel.app/#mural-section"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_qr_svg():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=3,
        image_factory=SvgPathImage
    )
    qr.add_data(TARGET_URL)
    qr.make(fit=True)
    svg_img = qr.make_image(attrib={'class': 'wedding-table-qr'})
    
    svg_path = os.path.join(OUTPUT_DIR, "qrcode-mural.svg")
    with open(svg_path, "wb") as f:
        svg_img.save(f)
    print(f"[OK] QR Code SVG salvo em: {svg_path}")

def generate_qr_png_standard():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=40,  # ~1600x1600 px Ultra HD
        border=3,
    )
    qr.add_data(TARGET_URL)
    qr.make(fit=True)
    
    # Cores harmonizadas com a paleta do casamento:
    # charcoal: #221E1C sobre fundo branco #FFFFFF
    img = qr.make_image(fill_color="#221E1C", back_color="#FFFFFF").convert("RGBA")
    
    png_path = os.path.join(OUTPUT_DIR, "qrcode-mural.png")
    img.save(png_path, "PNG", dpi=(300, 300))
    print(f"[OK] QR Code PNG Padrão salvo em: {png_path} ({img.size[0]}x{img.size[1]} px, 300 DPI)")

def generate_qr_png_monogram():
    # Versão de luxo com Monograma central "C & E"
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% de tolerância
        box_size=40,
        border=3,
    )
    qr.add_data(TARGET_URL)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#221E1C", back_color="#FFFFFF").convert("RGBA")
    w, h = img.size
    
    # Cria distintivo central para as iniciais C & E
    badge_size = int(w * 0.22)
    badge = Image.new("RGBA", (badge_size, badge_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(badge)
    
    # Desenha círculo de fundo branco com borda dourada (#D4AF37)
    draw.ellipse([2, 2, badge_size - 2, badge_size - 2], fill="#FAF7F2", outline="#B8860B", width=6)
    draw.ellipse([8, 8, badge_size - 8, badge_size - 8], outline="#D4AF37", width=2)
    
    # Tenta usar fonte padrão ou desenha texto
    try:
        font = ImageFont.truetype("georgia.ttf", int(badge_size * 0.32))
    except Exception:
        try:
            font = ImageFont.truetype("times.ttf", int(badge_size * 0.32))
        except Exception:
            font = ImageFont.load_default()
            
    text = "C & E"
    # Centralização
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = (badge_size - text_w) / 2
    text_y = (badge_size - text_h) / 2 - (bbox[1] / 2)
    
    draw.text((text_x, text_y), text, fill="#5C4427", font=font)
    
    # Cola o badge no centro exato do QR Code
    paste_pos = ((w - badge_size) // 2, (h - badge_size) // 2)
    img.paste(badge, paste_pos, badge)
    
    mono_path = os.path.join(OUTPUT_DIR, "qrcode-mural-monograma.png")
    img.save(mono_path, "PNG", dpi=(300, 300))
    print(f"[OK] QR Code com Monograma salvo em: {mono_path}")

if __name__ == "__main__":
    generate_qr_svg()
    generate_qr_png_standard()
    generate_qr_png_monogram()
    print("[Concluído] Todos os QR Codes foram gerados com sucesso para o URL:", TARGET_URL)
