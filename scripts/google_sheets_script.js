/**
 * =========================================================================
 * CASAMENTO CRIS & ENOCK 2027 — INTEGRAÇÃO GOOGLE SHEETS / RSVP
 * =========================================================================
 * - Validação de dados e quebra automática de texto (Wrap) para nunca cortar
 *   nomes de acompanhantes e familiares.
 * - Linha de Totais consolidada no topo (Linha 2 congelada), somando
 *   automaticamente Adultos, Crianças e Total de Convidados para o Buffet.
 */

// ID Oficial da Planilha dos Noivos
var SPREADSHEET_ID = "1jdnLftjJZgq5HRVjkaXQSIuz14N0HYbKA6SBp8tJVtM";

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    var ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    var sheet = ss.getActiveSheet();

    // Garante que o cabeçalho e a linha de totais no topo existam
    configurarCabecalhoETotais(sheet);

    var data = {};
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (err) {
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    var dataHora = data.dataHora || Utilities.formatDate(new Date(), "America/Sao_Paulo", "dd/MM/yyyy HH:mm:ss");
    var titular = data.titularNome || "Não informado";
    var whatsapp = data.whatsapp || "Não informado";
    var status = data.presenca || "Confirmado";
    var acompanhantes = data.acompanhantes || "Nenhum";
    var adultos = Number(data.totalAdultos) || 1;
    var criancas = Number(data.totalCriancas) || 0;
    var total = Number(data.totalGeral) || (adultos + criancas);

    // Insere a nova confirmação na próxima linha disponível (a partir da linha 3)
    var nextRow = Math.max(sheet.getLastRow() + 1, 3);

    sheet.getRange(nextRow, 1, 1, 8).setValues([[
      dataHora,
      titular,
      whatsapp,
      status,
      acompanhantes,
      adultos,
      criancas,
      total
    ]]);

    // Formatação e alinhamento elegante dos dados com QUEBRA AUTOMÁTICA (NUNCA CORTA)
    var rowRange = sheet.getRange(nextRow, 1, 1, 8);
    rowRange.setFontFamily("Arial").setFontSize(10);
    rowRange.setWrap(true);
    rowRange.setVerticalAlignment("middle");
    sheet.getRange(nextRow, 4, 1, 1).setHorizontalAlignment("center");
    sheet.getRange(nextRow, 6, 1, 3).setHorizontalAlignment("center");

    // Garante que a coluna E tenha largura ampla e quebra ativada para toda a planilha
    sheet.getRange("E:E").setWrap(true);
    sheet.setColumnWidth(5, 380);

    return ContentService.createTextOutput(JSON.stringify({ result: "success", row: nextRow }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ result: "error", error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

function configurarCabecalhoETotais(sheet) {
  // Se a planilha estiver vazia ou com formato anterior (menos de 2 linhas):
  if (sheet.getLastRow() < 2) {
    sheet.clear();

    // 1. Linha 1: Cabeçalhos Principais
    sheet.appendRow([
      "Data / Hora",
      "Convidado Titular",
      "WhatsApp",
      "Status",
      "Acompanhantes & Familiares",
      "Adultos",
      "Crianças",
      "Total Pessoas"
    ]);

    var headerRange = sheet.getRange(1, 1, 1, 8);
    headerRange.setFontWeight("bold");
    headerRange.setBackground("#D4AF37"); // Dourado solene
    headerRange.setFontColor("#1A1715");
    headerRange.setHorizontalAlignment("center");

    // 2. Linha 2: Barra de Totais / Resumo do Buffet (Sempre visível no topo)
    sheet.appendRow([
      "📊 TOTAIS",
      "=IF(COUNTA(B3:B)=0; \"Aguardando respostas\"; COUNTA(B3:B) & \" respostas\")",
      "—",
      "Confirmados",
      "Soma para o Buffet ➔",
      "=SUM(F3:F)",
      "=SUM(G3:G)",
      "=SUM(H3:H)"
    ]);

    var totalRange = sheet.getRange(2, 1, 1, 8);
    totalRange.setFontWeight("bold");
    totalRange.setBackground("#221E1C"); // Carvão editorial de luxo
    totalRange.setFontColor("#F5E6D3"); // Champagne dourado
    totalRange.setFontSize(11);
    totalRange.setHorizontalAlignment("center");
    sheet.getRange(2, 5).setHorizontalAlignment("right");

    // Congela as 2 primeiras linhas (ficam sempre fixas no topo da tela)
    sheet.setFrozenRows(2);

    // Ativa quebra de texto em todas as colunas
    sheet.getRange("A:H").setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
    sheet.getRange("A:H").setVerticalAlignment("middle");

    // Largura ideal para leitura no computador e celular
    sheet.setColumnWidth(1, 150); // Data/Hora
    sheet.setColumnWidth(2, 220); // Titular
    sheet.setColumnWidth(3, 160); // WhatsApp
    sheet.setColumnWidth(4, 110); // Status
    sheet.setColumnWidth(5, 380); // Acompanhantes (amplo para famílias inteiras)
    sheet.setColumnWidth(6, 100); // Adultos
    sheet.setColumnWidth(7, 100); // Crianças
    sheet.setColumnWidth(8, 120); // Total Pessoas
  }
}

function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({ status: "online", message: "Webhook Ativo" }))
    .setMimeType(ContentService.MimeType.JSON);
}

// Execute esta função no editor do Apps Script para formatar as linhas existentes agora mesmo
function ajustarQuebraDeTexto() {
  var ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  var sheet = ss.getActiveSheet();
  sheet.getRange("A:H").setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
  sheet.getRange("A:H").setVerticalAlignment("middle");
  sheet.setColumnWidth(5, 380);
}

// Se quiser resetar a planilha do zero com tudo formatado
function resetarComTotais() {
  var ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  var sheet = ss.getActiveSheet();
  sheet.clear();
  configurarCabecalhoETotais(sheet);
}
