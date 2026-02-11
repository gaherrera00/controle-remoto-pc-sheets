################################################################################
# CONTROLE REMOTO VIA GOOGLE SHEETS
# Script que executa comandos no computador através de uma planilha do Google
# Requisitos: oauth2client, gspread, keyboard
# Instale com: pip install oauth2client gspread keyboard
################################################################################

# IMPORTAÇÕES NECESSÁRIAS
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
import time
import keyboard


# CONFIGURAÇÃO DE CREDENCIAIS DO GOOGLE SHEETS

# IMPORTANTE: VOCÊ PRECISA FAZER ISSO ANTES DE EXECUTAR O SCRIPT:
#
# 1. Criar um arquivo JSON com credenciais do Google:
#    - Acesse: https://console.cloud.google.com/
#    - Crie um projeto
#    - Ative a API do Google Sheets
#    - Crie uma "Service Account" e gere a chave JSON
#    - Salve como "credenciais.json" nesta pasta
#
# 2. Criar uma planilha Google chamada "comandos"
#    - Compartilhe com o email da Service Account (encontrado no JSON)
#    - A célula A1 será usada para ler os comandos
#    - A coluna B mostrará a lista de comandos disponíveis (/help)

# Escopo de acesso à API do Google (não altere)
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# CUSTOMIZE AQUI: Caminho para arquivo de credenciais JSON
# Altere para o caminho real do seu arquivo credenciais.json
CAMINHO_CREDENCIAIS = (
    r"C:\Users\Gabriel\Documents\GitHub\controle-remoto-pc-sheets\credenciais.json"
)

cred = ServiceAccountCredentials.from_json_keyfile_name(CAMINHO_CREDENCIAIS, scope)

client = gspread.authorize(cred)
sheet = client.open("comandos").sheet1


# FUNÇÕES DE INICIALIZAÇÃO (Abrir programas e sites)


def start_google():
    """Abre o navegador Chrome na página do Google"""
    os.system("start chrome https://google.com")


def start_google_youtube():
    """Abre o navegador Chrome no YouTube"""
    os.system("start chrome https://youtube.com")


def start_google_chat():
    """Abre o navegador Chrome no ChatGPT"""
    os.system("start chrome https://chatgpt.com/")


def start_google_asimov():
    """Abre o navegador Chrome na plataforma Asimov Academy"""
    os.system("start chrome https://hub.asimov.academy/?auth=direct")


def start_vscode():
    """Abre o VS Code (editor de código)"""
    os.system("start code")


# FUNÇÕES DE LAYOUT (Gerenciar disposição de janelas)


def win_left():
    """Posiciona a janela ativa na metade esquerda da tela (Win+Left)"""
    keyboard.press_and_release("win+left")


def win_right():
    """Posiciona a janela ativa na metade direita da tela (Win+Right)"""
    keyboard.press_and_release("win+right")


def win_full():
    """Maximiza a janela ativa em tela cheia (Win+Up)"""
    keyboard.press_and_release("win+up")


# FUNÇÕES DE FECHAMENTO (Encerrar programas)


def off_chrome():
    """Fecha o navegador Chrome e todos seus processos"""
    os.system("taskkill /IM chrome.exe /F")


def off_computer():
    """Desliga o computador imediatamente"""
    os.system("shutdown /s /t 0")


def off_vscode():
    """Fecha o VS Code e todos seus processos"""
    os.system("taskkill /IM code.exe /F")


# FUNÇÕES DE SISTEMA (Controle do computador)


def lock_pc():
    """Bloqueia o computador com a tela de login (Win+L)"""
    keyboard.press_and_release("win+l")


def restart_computer():
    """Reinicia o computador imediatamente"""
    os.system("shutdown /r /t 0")


def tab():
    """Pressiona a tecla Tab para navegar entre elementos"""
    keyboard.press_and_release("tab")


def pesquisar():
    """Ativa a barra de endereço no navegador (Ctrl+L)"""
    keyboard.press_and_release("ctrl+l")


def nova_guia():
    """Abre uma nova aba no navegador (Ctrl+T)"""
    keyboard.press_and_release("ctrl+t")


def enter():
    """Pressiona a tecla Enter/Return"""
    keyboard.press_and_release("enter")


def fechar_guia():
    """Fecha a aba/janela atual do navegador (Ctrl+W)"""
    keyboard.press_and_release("ctrl+w")


def voltar():
    """Volta para a página anterior no navegador (Alt+Left)"""
    keyboard.press_and_release("alt+left")


def avancar():
    """Avança para a próxima página no navegador (Alt+Right)"""
    keyboard.press_and_release("alt+right")


def atualizar():
    """Atualiza a página atual no navegador (F5)"""
    keyboard.press_and_release("f5")


def minimizar():
    """Minimiza a janela ativa (Win+Down)"""
    keyboard.press_and_release("win+down")


def trocar_janela():
    """Alterna entre as janelas abertas (Alt+Tab)"""
    keyboard.press_and_release("alt+tab")


# FUNÇÕES AUXILIARES


def write(text, delay=0.05):
    """
    Digita um texto caractere por caractere no aplicativo ativo.

    Args:
        text (str): O texto a ser digitado
        delay (float): Intervalo em segundos entre cada caractere (padrão: 0.05s)
    """
    for char in text:
        keyboard.write(char)
        time.sleep(delay)


def atalho(keys):
    """
    Executa um atalho de teclado customizado.

    Args:
        keys (str): Combinação de teclas (ex: 'ctrl+c', 'alt+f4')

    Returns:
        bool: True se o atalho foi executado com sucesso, False caso contrário
    """
    parts = keys.split("+")
    for p in parts:
        if p not in VALID_KEYS:
            return False
    keyboard.press_and_release(keys)
    return True


def mostrar_help():
    """
    Gera e exibe uma lista completa de comandos disponíveis na coluna B da planilha.
    Útil para referência rápida dos comandos que o sistema reconhece.
    """
    # Acumula lista de help
    comandos_lista = []

    # Cabeçalho principais
    comandos_lista.append(["=== COMANDOS DISPONÍVEIS ==="])
    comandos_lista.append([""])

    # Seção: Comandos especiais (sintaxe personalizada)
    comandos_lista.append(["COMANDOS ESPECIAIS:"])
    comandos_lista.append(["write:texto - Digita o texto"])
    comandos_lista.append(["atalho:ctrl+c - Executa atalho de teclado"])
    comandos_lista.append(["/help - Mostra esta lista"])
    comandos_lista.append(["/help off - Limpa esta lista"])
    comandos_lista.append([""])

    # Seção: Abrir programas
    comandos_lista.append(["ABRIR PROGRAMAS:"])
    comandos_lista.append(["start google - Abre Google"])
    comandos_lista.append(["start google youtube - Abre YouTube"])
    comandos_lista.append(["start google chat - Abre ChatGPT"])
    comandos_lista.append(["start google asimov - Abre Asimov Academy"])
    comandos_lista.append(["start vscode - Abre VS Code"])
    comandos_lista.append([""])

    # Seção: Gerenciar janelas
    comandos_lista.append(["GERENCIAR JANELAS:"])
    comandos_lista.append(["window half left - Janela metade esquerda"])
    comandos_lista.append(["window half right - Janela metade direita"])
    comandos_lista.append(["window full - Maximizar janela"])
    comandos_lista.append(["minimizar - Minimizar janela"])
    comandos_lista.append(["trocar_janela - Alt+Tab"])
    comandos_lista.append([""])

    # Seção: Navegação
    comandos_lista.append(["NAVEGAÇÃO:"])
    comandos_lista.append(["nova_guia - Ctrl+T"])
    comandos_lista.append(["fechar_guia - Ctrl+W"])
    comandos_lista.append(["pesquisar - Ctrl+L (barra endereço)"])
    comandos_lista.append(["voltar - Alt+Left"])
    comandos_lista.append(["avancar - Alt+Right"])
    comandos_lista.append(["atualizar - F5"])
    comandos_lista.append(["tab - Pressiona Tab"])
    comandos_lista.append(["enter - Pressiona Enter"])
    comandos_lista.append([""])

    # Seção: Fechar/Desligar
    comandos_lista.append(["FECHAR/DESLIGAR:"])
    comandos_lista.append(["off google - Fecha Chrome"])
    comandos_lista.append(["off vscode - Fecha VS Code"])
    comandos_lista.append(["off pc - Desliga computador"])
    comandos_lista.append([""])

    # Seção: Sistema
    comandos_lista.append(["SISTEMA:"])
    comandos_lista.append(["lock - Bloqueia PC"])
    comandos_lista.append(["restart - Reinicia computador"])
    comandos_lista.append([""])

    # Seção: Exemplos de atalhos customizados
    comandos_lista.append(["EXEMPLOS DE ATALHOS:"])
    comandos_lista.append(["atalho:ctrl+c - Copiar"])
    comandos_lista.append(["atalho:ctrl+v - Colar"])
    comandos_lista.append(["atalho:ctrl+z - Desfazer"])
    comandos_lista.append(["atalho:alt+f4 - Fechar janela"])

    # Atualiza a planilha com os comandos
    try:
        sheet.update(range_name="B1", values=comandos_lista)
        return True
    except:
        return False


def limpar_help():
    """
    Limpa a lista de comandos da planilha (remove o conteúdo da coluna B).
    Chamada quando o usuário executa '/help off'.
    """
    try:
        # Limpa as células de B1 até B50 (espaço suficiente para a lista de ajuda)
        valores_vazios = [[""] for _ in range(50)]
        sheet.update(range_name="B1:B50", values=valores_vazios)
        return True
    except:
        return False


# VALIDAÇÃO E ESTRUTURA DE COMANDOS


# Conjunto de teclas válidas para atalhos customizados
# Se o usuário tentar usar uma tecla fora desta lista, o atalho será rejeitado
VALID_KEYS = {
    "enter",
    "esc",
    "tab",
    "backspace",
    "delete",
    "up",
    "down",
    "left",
    "right",
    "home",
    "end",
    "pagedown",
    "pageup",
    "ctrl",
    "shift",
    "alt",
    "win",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "f1",
    "f2",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "f10",
    "f11",
    "f12",
    "space",
}


# Dicionário hierárquico que mapeia os comandos para suas funções correspondentes
# Estrutura: comando -> subcmando -> função
# Exemplo: COMMANDS["start"]["google"]["_"] chama start_google()
COMMANDS = {
    "start": {
        "google": {
            "_": start_google,  # Comando padrão se nenhum subcomando for fornecido
            "youtube": start_google_youtube,
            "chat": start_google_chat,
            "asimov": start_google_asimov,
        },
        "vscode": start_vscode,
    },
    "window": {
        "half": {
            "left": win_left,
            "right": win_right,
        },
        "full": win_full,
    },
    "off": {
        "google": off_chrome,
        "pc": off_computer,
        "vscode": off_vscode,
    },
    "lock": lock_pc,
    "restart": restart_computer,
    "tab": tab,
    "pesquisar": pesquisar,
    "nova_guia": nova_guia,
    "enter": enter,
    "fechar_guia": fechar_guia,
    "voltar": voltar,
    "avancar": avancar,
    "atualizar": atualizar,
    "minimizar": minimizar,
    "trocar_janela": trocar_janela,
}


def executar(comando: str):
    """
    Processa e executa um comando recebido da planilha.

    Suporta os seguintes formatos:
    - Comandos simples: 'lock', 'restart', etc.
    - Comandos com subcomandos: 'start google', 'window half left'
    - Comando especial de escrita: 'write:seu texto aqui'
    - Comando especial de atalho: 'atalho:ctrl+c'
    - Comando de ajuda: '/help', '/help off'

    Args:
        comando (str): O comando a ser executado (lido da célula A1 da planilha)

    Returns:
        bool: True se o comando foi executado com sucesso, False caso contrário
    """
    comando = comando.strip()

    if not comando:
        return False

    # Comando para mostrar lista de ajuda
    if comando.lower() == "/help":
        return mostrar_help()

    # Comando para limpar a lista de ajuda
    if comando.lower() == "/help off":
        return limpar_help()

    # Comando especial para digitar texto
    # Formato: write:seu texto aqui
    if comando.startswith("write:"):
        texto = comando.split(":", 1)[1]
        write(texto)
        return True

    # Comando especial para executar atalhos de teclado
    # Formato: atalho:ctrl+c (use underline no lugar de +: atalho:ctrl_c)
    if comando.startswith("atalho:"):
        keys = comando.split(":", 1)[1].lower()
        keys = keys.replace("_", "+")  # Converte underline em + para atalhos
        return atalho(keys)

    # Comandos estruturados (hierárquicos)
    # Exemplo: "start google youtube" navega por COMMANDS["start"]["google"]["youtube"]
    comando_parts = comando.lower().split()
    current = COMMANDS

    for part in comando_parts:
        if isinstance(current, dict):
            if part in current:
                current = current[part]
            elif "_" in current:
                # Se a parte não encontrada, usa o comando padrão "_" se disponível
                current = current["_"]
                break
            else:
                return False
        else:
            break

    # Executa a função encontrada
    if callable(current):
        try:
            current()
            return True
        except:
            return False

    return False


# FEEDBACK VISUAL (Cores na planilha indicam sucesso/falha)


# Verde: comando executado com sucesso
GREEN = {"red": 0.0, "green": 1.0, "blue": 0.0}
# Vermelho: erro na execução do comando
RED = {"red": 1.0, "green": 0.0, "blue": 0.0}
# Branco: cor padrão (comando processado)
WHITE = {"red": 1.0, "green": 1.0, "blue": 1.0}


def set_color(color):
    """
    Muda a cor da célula A1 da planilha como feedback visual.

    Args:
        color (dict): Dicionário com as chaves 'red', 'green', 'blue'
                     com valores entre 0.0 e 1.0
    """
    try:
        sheet.format("A1", {"backgroundColor": color})
    except:
        pass


def clear_cell():
    """Limpa o conteúdo da célula A1 após processar o comando"""
    try:
        sheet.update(range_name="A1", values=[[""]])
    except:
        pass


# LOOP PRINCIPAL

# O script fica continuamente lendo a célula A1 da planilha.
# Quando um comando é digitado lá, ele é executado imediatamente.
# A célula muda de cor para indicar sucesso (verde) ou falha (vermelho).
# Após 2 segundos, a cor volta ao branco (padrão).

while True:
    try:
        # Lê o comando da célula A1 da planilha
        comando = sheet.acell("A1").value

        if comando:
            # Tenta executar o comando
            ok = executar(comando)

            # Feedback visual: verde se sucesso, vermelho se falha
            if ok:
                set_color(GREEN)  # Comando executado com sucesso
                time.sleep(2)
                set_color(WHITE)
            else:
                set_color(RED)  # Erro ao executar comando
                time.sleep(2)
                set_color(WHITE)

        # Aguarda 3 segundos antes de checar novamente por novos comandos
        time.sleep(3)
    except:
        # Em caso de erro (ex: perda de conexão), aguarda 5 segundos antes de tentar novamente
        time.sleep(5)
