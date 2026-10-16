# Especificação de Projeto — Site & Convite Interativo de Casamento

**Experiência Cinematográfica, Scroll-Driven Storytelling & Confirmação Direta em Planilha Excel/Google Sheets**

---

## 1. Visão Geral & Conceito de Interação

O site foi concebido como uma **jornada imersiva e cinematográfica**. Em vez de uma página tradicional estática, o convidado vivencia uma história conduzida por vídeo contínuo, áudio ambiente, paradas de leitura com tela travada (*scroll pinning*), fotos em estilo polaroid desordenadas que se alinham na interação, e a revelação do convite com envelope e carta solene.

Para a confirmação de presença (RSVP), adota-se um **modelo limpo e 100% sigiloso**: o convidado apenas confirma seus dados e de seus acompanhantes, visualiza uma notificação carinhosa de presença garantida, e os dados alimentam em segundo plano, em tempo real, uma **Planilha na Nuvem (Google Sheets / Excel)** acessível exclusivamente pelos noivos.

---

## 2. Fluxo Passo a Passo por Dobras (Sections)

```
[ Gate de Entrada ] ──► Vídeo Autoplay + Trilha Sonora de Abertura
         │
         ▼ (Vídeo finaliza / Desbloqueio da Página)
[ 1ª Dobra: Hero ] ──► Nomes dos noivos, data, local e micro-informações essenciais
         │
         ▼
[ 2ª Dobra: Storytelling Pin ] ──► Tela trava (Sticky Pin); texto do casal se revela pelo scroll
         │
         ▼
[ 3ª Dobra: Galeria Desalinhada ] ──► Carrossel infinito de fotos inclinadas/irregulares (hover endireita/amplia)
         │
         ▼
[ 4ª Dobra: O Convite & Envelope ] ──► Vídeo que acompanha o scroll + Envelope 3D com carta
         │
         ▼
[ 5ª Dobra: Cerimônia & Rotas ] ──► Horários, orientações e botões diretos Waze / Google Maps
         │
         ▼
[ 6ª Dobra: RSVP Multi-Convidado ] ──► Formulário titular + acompanhantes
         │                                   │
         ▼ (Ao clicar "Confirmar")           ▼ (Disparo invisível em background)
[ Notificação de Sucesso ]            [ Planilha Excel / Google Sheets dos Noivos ]
(Apenas toast/modal carinhoso)        (Nova linha automática com contagem para o buffet)
         │
         ▼
[ 7ª Dobra: Mural do Casamento ] ──► QR Code para mesas + upload na hora e após o evento
```

---

## 3. Detalhamento de Cada Dobra

### 3.1. Gate de Abertura & 1ª Dobra: Hero Cinematográfico
* **Comportamento Inicial:**
  * A tela inicial é preenchida por um vídeo em tela cheia com autoplay (iniciando o movimento contínuo da perspectiva superior para o enquadramento frontal do casal).
  * A trilha sonora do site se inicia suavemente com transição de fade-in.
  * O scroll do restante da página fica bloqueado até o término do vídeo de abertura (ou mediante toque no botão sutil *"Pular para o convite"* para garantir acessibilidade).
* **Desbloqueio & Informações da Hero:**
  * Ao término do vídeo, a página se destrava suavemente com transição de opacidade.
  * Aparecem as informações mínimas essenciais: Monograma do casal, nomes em tipografia editorial, data do casamento e a cidade/local.

---

### 3.2. 2ª Dobra: Texto do Casal com Leitura Travada (*Scroll Pinning*)
* **Mecânica de Trava:**
  * Ao atingir esta seção, a janela congela o container principal na tela (`position: sticky` / Pin de scroll).
  * O movimento de rolagem para baixo não move a página, mas sim **revela progressivamente a leitura do texto** (efeito de preenchimento de cor das palavras ou desfile de estrofes de uma carta aberta).
  * Apenas após a conclusão da leitura integral do texto do casal, a página se destrava e segue naturalmente para a próxima dobra.

---

### 3.3. 3ª Dobra: Galeria Pré-Wedding Irregular & Carrossel Infinito
* **Estética Desalinhada / Polaroids Orgânicas:**
  * As fotos do casal não ficam alinhadas em uma grade retangular comum.
  * Cada imagem possui uma leve rotação orgânica aleatória (ex: $-4^\circ$, $+3^\circ$, $-6^\circ$), margens brancas e sombras suaves, simulando fotografias reais sobre uma mesa.
* **Comportamento Interativo:**
  * **Fluxo Contínuo:** Deslizam em carrossel horizontal infinito.
  * **Hover / Toque:** Ao passar o mouse ou tocar na foto, ela **se endireita para $0^\circ$**, ganha escala ampliada (zoom suave), eleva-se na camada visual (`z-index`) e revela a legenda do momento.
  * Ao clicar, abre o modo *Lightbox* em tela cheia de altíssima resolução.

---

### 3.4. 4ª Dobra: Apresentação da Carta-Convite & Vídeo Guiado por Scroll (*Scroll Scrubbing*)
* **Mecânica de Vídeo Acompanhando o Scroll:**
  * Conforme o usuário rola a tela para baixo, o vídeo avança quadro a quadro na proporção direta da descida, apresentando a transição até o envelope.
* **Envelope Interativo 3D:**
  * Envelope com textura premium e lacre de cera gravado com as iniciais do casal.
  * Ao clicar no selo de cera:
    1. O selo se rompe suavemente;
    2. A aba triangular do envelope rotaciona em 3D para trás;
    3. A **carta de convite formal desliza para fora e para cima**, contendo a convocação solene, nomes dos pais, horários e endereço.

---

### 3.5. 5ª Dobra: Informações do Evento & Rotas
* **Cards Integrados:**
  * **Cerimônia:** Local exato, horário de início e orientação de antecedência.
  * **Recepção:** Detalhes da comemoração, cardápio, estacionamento e traje.
* **Botões Inteligentes com Deep-Link:**
  * Botão **Waze**: Abre diretamente o aplicativo com o endereço setado como destino;
  * Botão **Google Maps**: Traça a rota pelo app do Google Maps.

---

### 3.6. 6ª Dobra: Confirmação de Presença (RSVP) & Integração Direta com a Planilha

#### A Experiência do Convidado (Simples, Elegante e Discreta)
* **Campos do Formulário:**
  * Nome completo do convidado principal (titular);
  * WhatsApp / Telefone de contato;
  * Confirmação (*Sim, estarei presente!* ou *Infelizmente não poderei comparecer*);
  * Botão `+ Adicionar Acompanhante / Familiar`: Permite incluir múltiplos nomes no mesmo envio (especificando se é Adulto ou Criança);
  * Campo de restrições alimentares ou alergias (glúten, lactose, vegetariano, etc.);
  * Mensagem carinhosa aos noivos.
* **O que o Convidado Vê ao Clicar em "Confirmar":**
  * Ele **não vê nenhuma lista de confirmados, nem números de convidados**.
  * Apenas recebe um aviso modal elegante com chuva de confetes:
    > *"Presença confirmada com sucesso! Muito obrigado pelo carinho. Mal podemos esperar para celebrar esse dia inesquecível com você!"*
  * O formulário é limpo e a experiência é encerrada com sofisticação.

---

## 4. Arquitetura da Lista dos Noivos: Google Sheets & Excel Automático

Para eliminar completamente a necessidade de painéis e logins no site, a lista é alimentada por meio de um **Webhook silencioso em segundo plano**.

```
[ Convidado clica em "Confirmar" ]
             │
             ├── (1) Mostra na tela do convidado: "Presença Confirmada!"
             │
             └── (2) Envia silenciosamente via HTTP POST (Webhook)
                          │
                          ▼
            [ Google Apps Script / API ]
                          │
                          ▼
            [ Google Sheets Privado dos Noivos ]
            • Nova linha inserida instantaneamente
            • Fórmula somatória calcula o total para o buffet
            • Permite download em .XLSX (Excel) a qualquer momento
```

### 4.1. Estrutura das Colunas na Planilha dos Noivos

A planilha criada no Google Drive do casal receberá os dados formatados nas seguintes colunas:

| Coluna A | Coluna B | Coluna C | Coluna D | Coluna E | Coluna F | Coluna G | Coluna H |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Data/Hora** | **Convidado Principal** | **WhatsApp** | **Status** | **Acompanhantes** | **Total Adultos** | **Total Crianças** | **Restrições / Mensagem** |
| 14/11 16:20 | Carlos Eduardo Silva | (11) 98888-7777 | Confirmado | Marina Silva (Esposa), Theo (Filho) | 2 | 1 | Sem lactose (Theo) / Parabéns ao casal! |

### 4.2. Vantagens Desta Abordagem
* **Sigilo Absoluto:** Ninguém além dos noivos tem acesso à lista, pois ela não existe no código público do site.
* **Zero Manutenção:** Não é necessário criar contas, lembrar senhas de admin no site ou gerenciar bancos de dados.
* **Pronto para o Buffet:** A planilha calcula automaticamente o total acumulado de convidados adultos e infantis, permitindo enviar o arquivo Excel para o buffet ou cerimonial com um clique.

---

## 5. 7ª Dobra: Mural Colaborativo do Casamento (QR Code das Mesas & Pós-Evento)

* **Plaquinhas com QR Code nas Mesas:**
  * Placas decorativas com QR Code nas mesas dos convidados e no bar: *"Aponte a câmera e compartilhe seus cliques da festa no nosso mural ao vivo!"*.
  * O QR Code rola a tela direto para esta seção.
* **Envio Rápido:**
  * O convidado pode tirar foto na hora pela câmera ou escolher da galeria do celular.
  * Campo de nome e legenda rápida.
  * Visualizador em alta definição com curtidas.
* **Pós-Evento:** Permanece aberto nos dias seguintes para amigos e familiares continuarem subindo fotos e vídeos do casamento.