# 🖥️ Controle Remoto via Google Sheets

Sistema que permite controlar seu computador remotamente através de uma planilha do Google Sheets. Digite comandos na planilha e veja-os serem executados automaticamente no seu PC!

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Requisitos](#-requisitos)
- [Instalação e Configuração](#-instalação-e-configuração)
  - [Passo 1: Ativar APIs do Google](#passo-1-ativar-apis-do-google)
  - [Passo 2: Criar Service Account e Credenciais](#passo-2-criar-service-account-e-credenciais)
  - [Passo 3: Criar e Configurar a Planilha](#passo-3-criar-e-configurar-a-planilha)
  - [Passo 4: Instalar Dependências Python](#passo-4-instalar-dependências-python)
  - [Passo 5: Configurar o Script](#passo-5-configurar-o-script)
- [Como Usar](#-como-usar)
- [Lista de Comandos](#-lista-de-comandos)
- [Exemplos Práticos](#-exemplos-práticos)
- [Solução de Problemas](#-solução-de-problemas)
- [Avisos Importantes](#-avisos-importantes)

---

## 🎯 Funcionalidades

- ✅ Abrir programas e sites automaticamente
- ✅ Controlar janelas (maximizar, minimizar, posicionar)
- ✅ Executar atalhos de teclado personalizados
- ✅ Digitar texto remotamente
- ✅ Navegar na web (abrir abas, fechar, atualizar)
- ✅ Desligar, reiniciar ou bloquear o PC
- ✅ Feedback visual de sucesso/erro na planilha
- ✅ Lista de comandos integrada no Google Sheets

---

## 💻 Requisitos

### Sistema Operacional
- **Windows 10/11** (o script usa comandos específicos do Windows)

### Software
- **Python 3.7 ou superior** → [Download aqui](https://www.python.org/downloads/)
- **Google Chrome** (para os comandos de navegação)
- **Conexão com a Internet** (para acessar a API do Google Sheets)

---

## 🚀 Instalação e Configuração

### Passo 1: Ativar APIs do Google

#### 1.1 - Acesse o Google Cloud Console
1. Abra seu navegador e acesse: [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. Faça login com sua conta Google

#### 1.2 - Criar um Novo Projeto
1. No canto superior esquerdo, clique no **seletor de projetos**
2. Clique em **"NOVO PROJETO"**
3. Digite um nome para o projeto (ex: `Controle-Remoto-Sheets`)
4. Clique em **"CRIAR"**
5. Aguarde alguns segundos e selecione o projeto criado

#### 1.3 - Ativar Google Sheets API
1. No menu lateral, vá em: **APIs e serviços** → **Biblioteca**
2. Na barra de pesquisa, digite: `Google Sheets API`
3. Clique no resultado **Google Sheets API**
4. Clique no botão **"ATIVAR"**
5. Aguarde a ativação (alguns segundos)

#### 1.4 - Ativar Google Drive API
1. Volte para a **Biblioteca** de APIs
2. Digite: `Google Drive API`
3. Clique no resultado **Google Drive API**
4. Clique no botão **"ATIVAR"**

---

### Passo 2: Criar Service Account e Credenciais

#### 2.1 - Acessar Credenciais
1. No menu lateral, vá em: **APIs e serviços** → **Credenciais**
2. Clique no botão **"+ CRIAR CREDENCIAIS"** (topo da página)
3. Selecione **"Conta de serviço"**

#### 2.2 - Configurar a Conta de Serviço
1. **Nome da conta de serviço**: Digite `sheet-bot` (ou outro nome de sua preferência)
2. **ID da conta de serviço**: Será gerado automaticamente
3. **Descrição**: (opcional) Digite "Bot para controle remoto via Sheets"
4. Clique em **"CRIAR E CONTINUAR"**

#### 2.3 - Conceder Permissões (Opcional)
1. Na seção "Conceder acesso a este projeto", você pode pular esta etapa
2. Clique em **"CONTINUAR"**
3. Clique em **"CONCLUÍDO"**

#### 2.4 - Gerar a Chave JSON
1. Na página de **Credenciais**, role até a seção **"Contas de serviço"**
2. Clique no **email da conta de serviço** que você acabou de criar
   - Formato: `sheet-bot@seu-projeto.iam.gserviceaccount.com`
3. Vá na aba **"CHAVES"** (no topo)
4. Clique em **"ADICIONAR CHAVE"** → **"Criar nova chave"**
5. Selecione o formato **JSON**
6. Clique em **"CRIAR"**

**⚠️ IMPORTANTE:** Um arquivo JSON será baixado automaticamente. Este é o arquivo `credenciais.json`. Guarde-o com segurança!

#### 2.5 - Copiar o Email da Service Account
1. Volte para a página de **Credenciais**
2. Na seção **Contas de serviço**, copie o email completo
   - Exemplo: `sheet-bot@controle-remoto-sheets.iam.gserviceaccount.com`
3. **Guarde este email** - você vai usá-lo no próximo passo!

---

### Passo 3: Criar e Configurar a Planilha

#### 3.1 - Criar Nova Planilha
1. Acesse: [https://sheets.google.com/](https://sheets.google.com/)
2. Clique em **"+"** para criar uma nova planilha em branco
3. Renomeie a planilha para: **`comandos`** (exatamente este nome, sem espaços extras)

#### 3.2 - Compartilhar com a Service Account
1. Clique no botão **"Compartilhar"** (canto superior direito)
2. No campo de email, cole o **email da service account** que você copiou anteriormente
   - Exemplo: `sheet-bot@controle-remoto-sheets.iam.gserviceaccount.com`
3. Mude a permissão para **"Editor"** (não pode ser "Visualizador")
4. **DESMARQUE** a opção "Notificar pessoas"
5. Clique em **"Compartilhar"**

#### 3.3 - Entender a Estrutura da Planilha
- **Célula A1**: Onde você vai digitar os comandos
- **Coluna B**: Exibirá a lista de comandos disponíveis quando você usar `/help`
- **Cor da célula A1**: 
  - 🟢 **Verde** = Comando executado com sucesso
  - 🔴 **Vermelho** = Erro no comando
  - ⚪ **Branco** = Estado padrão

---

### Passo 4: Instalar Dependências Python

#### 4.1 - Verificar se o Python está instalado
1. Abra o **Prompt de Comando** (Windows + R, digite `cmd`, Enter)
2. Digite:
```bash
python --version
```
3. Se aparecer a versão (ex: `Python 3.11.5`), está instalado!
4. Se não, baixe em: [https://www.python.org/downloads/](https://www.python.org/downloads/)

#### 4.2 - Instalar as Bibliotecas Necessárias
No Prompt de Comando, navegue até a pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

Isso instalará automaticamente todas as dependências necessárias:
- `oauth2client` - Autenticação com Google
- `gspread` - Integração com Google Sheets
- `keyboard` - Controle de teclado

**Observação:** Se aparecer "pip não é reconhecido", tente usar:
```bash
python -m pip install -r requirements.txt
```

---

### Passo 5: Configurar o Script

#### 5.1 - Organizar os Arquivos
1. Crie uma pasta no seu computador (ex: `C:\ControleRemoto\`)
2. Coloque nesta pasta:
   - O arquivo `app.pyw` (o script Python)
   - O arquivo `credenciais.json` (que você baixou do Google Cloud)

#### 5.2 - Editar o Caminho das Credenciais
1. Abra o arquivo `app.pyw` em um editor de texto (Bloco de Notas, VS Code, etc.)
2. Localize a linha 40-42:
```python
CAMINHO_CREDENCIAIS = (
    r"C:\Users\Gabriel\Documents\projetosTeste\controleRemoto\credenciais.json"
)
```
3. Altere para o caminho **real** onde você salvou o arquivo `credenciais.json`
   - Exemplo: `r"C:\ControleRemoto\credenciais.json"`
4. **Mantenha o `r` antes das aspas!** (indica raw string)
5. Salve o arquivo

#### 5.3 - Executar o Script
No Prompt de Comando, navegue até a pasta do projeto:
```bash
cd C:\ControleRemoto
```

Execute o script:
```bash
python app.pyw
```

**✅ Se tudo estiver correto:**
- O script iniciará sem erros
- Abrirá uma janela do Python em segundo plano
- Já está pronto para receber comandos!

---

## 📖 Como Usar

### Uso Básico

1. **Abra a planilha Google Sheets** chamada "comandos"
2. **Digite um comando na célula A1**
3. **Pressione Enter**
4. **Aguarde 3 segundos** (tempo de processamento)
5. **Observe o feedback:**
   - Célula A1 ficará **verde** se o comando foi executado
   - Célula A1 ficará **vermelha** se houve erro

### Ver Lista de Comandos

1. Na célula A1, digite: `/help`
2. Pressione Enter
3. A **coluna B** será preenchida com todos os comandos disponíveis

### Limpar a Lista de Comandos

1. Na célula A1, digite: `/help off`
2. A coluna B será limpa

---

## 📝 Lista de Comandos

### 🌐 Abrir Sites e Programas

| Comando | Descrição |
|---------|-----------|
| `start google` | Abre o Google no Chrome |
| `start google youtube` | Abre o YouTube |
| `start google chat` | Abre o ChatGPT |
| `start google asimov` | Abre a Asimov Academy |
| `start vscode` | Abre o Visual Studio Code |

### 🪟 Gerenciar Janelas

| Comando | Descrição |
|---------|-----------|
| `window half left` | Posiciona a janela ativa na metade esquerda (Win+Left) |
| `window half right` | Posiciona a janela ativa na metade direita (Win+Right) |
| `window full` | Maximiza a janela (Win+Up) |
| `minimizar` | Minimiza a janela ativa (Win+Down) |
| `trocar_janela` | Alterna entre janelas abertas (Alt+Tab) |

### 🌐 Navegação Web

| Comando | Descrição |
|---------|-----------|
| `nova_guia` | Abre uma nova aba (Ctrl+T) |
| `fechar_guia` | Fecha a aba atual (Ctrl+W) |
| `pesquisar` | Ativa a barra de endereço (Ctrl+L) |
| `voltar` | Volta para a página anterior (Alt+Left) |
| `avancar` | Avança para a próxima página (Alt+Right) |
| `atualizar` | Atualiza a página (F5) |
| `tab` | Pressiona a tecla Tab |
| `enter` | Pressiona Enter |

### ❌ Fechar Programas

| Comando | Descrição |
|---------|-----------|
| `off google` | Fecha o Chrome completamente |
| `off vscode` | Fecha o VS Code |
| `off pc` | **Desliga o computador imediatamente** |

### 🔧 Sistema

| Comando | Descrição |
|---------|-----------|
| `lock` | Bloqueia o computador (Win+L) |
| `restart` | **Reinicia o computador imediatamente** |

### ✍️ Comandos Especiais

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `write:texto` | Digita o texto especificado | `write:Olá, mundo!` |
| `atalho:teclas` | Executa um atalho de teclado | `atalho:ctrl+c` |
| `/help` | Mostra a lista de comandos na coluna B | `/help` |
| `/help off` | Limpa a lista de comandos | `/help off` |

### ⌨️ Atalhos Válidos para `atalho:`

Você pode combinar qualquer uma destas teclas:

**Modificadores:** `ctrl`, `shift`, `alt`, `win`

**Teclas de função:** `f1`, `f2`, `f3`, ... `f12`

**Navegação:** `up`, `down`, `left`, `right`, `home`, `end`, `pageup`, `pagedown`

**Especiais:** `enter`, `esc`, `tab`, `backspace`, `delete`, `space`

**Letras:** `a` até `z`

**Números:** `0` até `9`

**Exemplos:**
- `atalho:ctrl+c` → Copiar
- `atalho:ctrl+v` → Colar
- `atalho:ctrl+z` → Desfazer
- `atalho:alt+f4` → Fechar janela
- `atalho:win+d` → Mostrar área de trabalho

---

## 💡 Exemplos Práticos

### Exemplo 1: Abrir YouTube e Maximizar
```
1. Digite na A1: start google youtube
2. Aguarde a janela abrir
3. Digite na A1: window full
```

### Exemplo 2: Pesquisar Algo no Google
```
1. Digite na A1: start google
2. Digite na A1: pesquisar
3. Digite na A1: write:receita de bolo
4. Digite na A1: enter
```

### Exemplo 3: Copiar Texto
```
1. Digite na A1: atalho:ctrl+a
2. Digite na A1: atalho:ctrl+c
```

### Exemplo 4: Workflow Completo
```
1. start google youtube          ← Abre YouTube
2. window half left              ← Posiciona à esquerda
3. start vscode                  ← Abre VS Code
4. window half right             ← Posiciona à direita
```

---

## 🔧 Solução de Problemas

### ❌ Erro: "No module named 'oauth2client'"
**Solução:** Instale a biblioteca:
```bash
pip install oauth2client
```

### ❌ Erro: "gspread.exceptions.APIError: PERMISSION_DENIED"
**Solução:** 
1. Verifique se você compartilhou a planilha com o email da service account
2. Confirme que a permissão é "Editor", não "Visualizador"

### ❌ Erro: "FileNotFoundError: credenciais.json"
**Solução:**
1. Verifique se o caminho em `CAMINHO_CREDENCIAIS` está correto
2. Use barras duplas `\\` ou barra simples `/` ou `r"caminho"`
3. Exemplo correto: `r"C:\ControleRemoto\credenciais.json"`

### ❌ Comandos não são executados
**Solução:**
1. Verifique se a célula A1 está sendo usada
2. Aguarde 3 segundos após digitar o comando
3. Confira se o nome da planilha é exatamente `comandos`
4. Veja se o script Python está em execução

### ❌ Célula fica vermelha constantemente
**Solução:**
1. Digite `/help` para ver a lista de comandos válidos
2. Verifique a ortografia do comando
3. Comandos são sensíveis a espaços extras

### ❌ O Chrome não abre
**Solução:**
1. Verifique se o Google Chrome está instalado
2. Se estiver usando outro navegador, edite as funções no código:
   - Troque `start chrome` por `start firefox` ou `start msedge`

---

## ⚠️ Avisos Importantes

### Segurança
- 🔒 **Nunca compartilhe o arquivo `credenciais.json`** com ninguém
- 🔒 **Não suba este arquivo para repositórios públicos** (GitHub, etc.)
- 🔒 Adicione `credenciais.json` ao `.gitignore` se usar Git

### Uso Responsável
- ⚠️ **Cuidado com os comandos de desligar/reiniciar** - eles são executados imediatamente
- ⚠️ Teste primeiro em um ambiente seguro antes de usar em produção
- ⚠️ Mantenha a planilha privada ou compartilhada apenas com pessoas de confiança

### Limitações
- 📌 Funciona apenas em **Windows**
- 📌 Requer **conexão com a internet** constante
- 📌 Delay de ~3 segundos entre comandos (configurável no código)
- 📌 Chrome deve estar no PATH do sistema para os comandos `start google` funcionarem

### .gitignore Recomendado
Se você usar Git, crie um arquivo `.gitignore` com:
```
credenciais.json
*.pyc
__pycache__/
```

---

## 🎓 Personalização

### Adicionar Novos Sites
Edite o arquivo `app.pyw` e adicione novas funções:

```python
def start_netflix():
    """Abre Netflix"""
    os.system("start chrome https://netflix.com")

# Adicione ao dicionário COMMANDS:
COMMANDS = {
    "start": {
        "google": { ... },
        "netflix": start_netflix,  # NOVO
        ...
    },
    ...
}
```

Agora você pode usar: `start netflix`

### Alterar Tempo de Verificação
Na linha 551, altere o valor:
```python
time.sleep(3)  # Mude para 1, 2, 5, etc.
```

---

## 📜 Licença

Este projeto é de código aberto. Use e modifique como desejar!

---

## 🤝 Contribuindo

Sugestões e melhorias são bem-vindas! 

---

## 📞 Suporte

Se você encontrar problemas:
1. Verifique a seção **Solução de Problemas**
2. Confira se seguiu todos os passos corretamente
3. Revise as permissões da planilha e das APIs

---

**Desenvolvido com ❤️ para automação e produtividade**

🎉 **Agora você pode controlar seu PC de qualquer lugar do mundo, apenas editando uma planilha!**