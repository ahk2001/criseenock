# Casamento Cris & Enock — 09 de Janeiro de 2027 💍✨

Site interativo e convite digital oficial do casamento de **Cris & Enock**, projetado com uma experiência editorial cinematográfica de luxo, integração com Google Sheets em tempo real e animações fluidas a 60/120 FPS.

---

## 🌟 Principais Recursos

- **Envelope Interativo 3D:** Animação de abertura da carta de convite por *scroll scrubbing* via Canvas HTML5 (200 quadros) com renderização final em Ultra HD (8K) e opção de download.
- **Confirmação de Presença (RSVP):**
  - Validação estrita de WhatsApp/Telefone brasileiro (DDD + 9 dígitos) com formatação em tempo real.
  - Sistema de acompanhantes e familiares dinâmico.
  - Sincronização sigilosa em tempo real com a planilha dos noivos via **Google Apps Script Webhook**.
  - Barra de Totais consolidada no topo da planilha com cálculo automático para o Buffet (Adultos, Crianças e Total Geral).
- **Trilha Sonora Solene:** Player de áudio de fundo com inicialização contínua e equalizador visual animado por aceleração GPU.
- **Mural Colaborativo & Galeria 3D:** Galeria de memórias dos convidados com visualização tridimensional via WebGL / Three.js e suporte a upload de fotos da celebração.
- **Localização & Rotas:** Botões com traçado de rotas direto para **Google Maps** e **Waze** até o *Salão Petry's* em Jaraguá do Sul — SC.
- **Dúvidas Frequentes (FAQ):** Accordion interativo com informações sobre trajes, horários, bebidas e estacionamento.
- **Performance de Elite:** Rolagem ultra-suave com *Lenis Smooth Scroll*, aceleração por hardware e zero queda de quadros em dispositivos móveis.

---

## 📁 Estrutura do Projeto

```text
cris&enock/
├── .github/
│   └── workflows/
│       └── deploy.yml              # Pipeline de deploy automático no GitHub Pages
├── assets/
│   ├── audio/                      # Trilha sonora do casamento (.mp3, .m4a, .mp4)
│   ├── envelope-frames/            # 200 quadros para a animação do envelope interativo
│   ├── images/                     # Fotos dos noivos, convite 8K, QR Codes e fundo botânico
│   │   ├── qrcode-mural.png        # QR Code Ultra HD (300 DPI) para impressão
│   │   ├── qrcode-mural.svg        # QR Code Vetorial escalável sem perda de resolução
│   │   └── qrcode-mural-monograma.png # QR Code com iniciais C & E no centro
│   └── videos/                     # Vídeos do Hero inicial e fundo do formulário RSVP
├── docs/
│   └── especificacao_projeto.md    # Especificação detalhada da arquitetura e design
├── scripts/
│   ├── generate_qrcode.py          # Script gerador dos QR Codes oficiais com 30% tolerância
│   └── google_sheets_script.js     # Script oficial do Google Apps Script (RSVP / Webhook)
├── .gitignore                      # Arquivos e diretórios ignorados pelo Git
├── display-mesa-mural.html         # Plaquinha de mesa oficial para impressão (10x15cm, tenda, A4)
├── index.html                      # Aplicação web completa e estruturada
└── README.md                       # Documentação oficial do repositório
```

---

## 🚀 Como Executar Localmente

Como o projeto é construído em HTML5, CSS moderno e Vanilla JavaScript, ele não necessita de etapas de compilação (*build*):

1. Clone o repositório:
   ```bash
   git clone https://github.com/ahk2001/criseenock.git
   ```
2. Abra o arquivo `index.html` diretamente em qualquer navegador moderno (Chrome, Safari, Edge, Firefox), ou use uma extensão de servidor local como *Live Server* ou `npx serve .`.

---

## 🌐 Hospedagem & Deploy

Este projeto está pronto para publicação via **GitHub Pages**, **Vercel** ou **Netlify**:
- **GitHub Pages:** Ativado automaticamente através do GitHub Actions configurado em `.github/workflows/deploy.yml`.
- Todos os caminhos de assets utilizam referências relativas, permitindo execução tanto na raiz de domínios personalizados quanto em subdiretórios (`https://usuario.github.io/repositorio/`).

---

## 👰🤵 Noivos

**Cris & Enock**  
*09 de Janeiro de 2027 • Jaraguá do Sul — SC*  
*"O amor é paciente, o amor é bondoso. Tudo sofre, tudo crê, tudo espera, tudo suporta." (1 Coríntios 13:4, 7)*
