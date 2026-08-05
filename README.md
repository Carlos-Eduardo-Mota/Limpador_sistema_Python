# 🧹 Limpador de Arquivos Temporários do Windows (Python)

Este é um script em Python desenvolvido para automatizar a limpeza de arquivos temporários e caches do Windows (`%TEMP%`, `C:\Windows\Temp` e `C:\Windows\Prefetch`), liberando espaço em disco e otimizando o sistema.

---

## 🚀 Funcionalidades

- **Elevação Automática de Privilégios**: Solicita permissão de Administrador ao Windows para conseguir acessar e limpar a pasta protegida `Prefetch`.
- **Limpeza Abrangente**: Remove arquivos soltos e pastas inteiras contidos nos diretórios temporários.
- **Tratamento de Exceções**: Ignora arquivos que estão sendo usados pelo sistema no momento da execução sem interromper o script.
- **Cálculo de Espaço Liberado**: Mede o espaço livre no disco antes e depois da execução para exibir exatamente quantos **MB** ou **GB** foram recuperados.

---

## 🛠️ Tecnologias e Módulos Utilizados

O projeto utiliza exclusivamente bibliotecas nativas do Python, sem necessidade de instalar pacotes externos:

- `os`: Manipulação de caminhos (`os.path.join`), verificação de arquivos/pastas (`os.path.isfile`, `os.path.isdir`) e exclusão de arquivos (`os.remove`).
- `shutil`: Remoção de diretórios completos (`shutil.rmtree`) e medição de uso do disco (`shutil.disk_usage`).
- `ctypes`: Comunicação com a API do Windows para verificar e solicitar privilégios de Administrador (`IsUserAnAdmin`, `ShellExecuteW`).
- `sys`: Manipulação dos argumentos do script e controle de execução (`sys.exit`).

---

## ⚙️ Como Funciona o Código

1. **Checagem de Admin (`solicitar_admin`)**: 
   Verifica se o programa possui privilégios elevados. Caso não possua, o script reabre a si mesmo solicitando permissão ao Windows.

2. **Cálculo de Disco Inicial**:
   Converte a leitura em bytes de `shutil.disk_usage("C:").free` para Gigabytes (GB) dividindo por $1024^3$.

3. **Loop de Limpeza**:
   Percorre a lista de caminhos, diferencia arquivos de diretórios e aplica o método de remoção adequado (`os.remove` para arquivos e `shutil.rmtree` para pastas).

4. **Resultado Final**:
   Calcula a diferença de espaço livre e exibe o total liberado na tela em MB.

---

## 📋 Como Baixar e Executar

Você pode rodar este projeto de duas formas: baixando o executável pronto ou rodando direto pelo código fonte em Python.

---

### Opção 1: Baixando o Executável (.exe) — Recomendado

1. Acesse a aba **Releases** aqui no repositório do GitHub.
2. Baixe o arquivo `Limpador.exe`.

---

### 🛡️ Avisos de Segurança (O que fazer se for bloqueado?)

Como este é um projeto independente e não possui um certificado digital pago, tanto o **navegador** quanto o **Windows** podem emitir alertas de segurança. 

> **🔒 O arquivo é seguro?** > Sim! O código fonte é totalmente **aberto (Open Source)** e transparente aqui no GitHub. Qualquer pessoa pode inspecionar o código Python utilizado para gerar o `.exe`.

#### 1. Se o NAVEGADOR bloquear o download:
Alguns navegadores (como Chrome ou Edge) podem exibir a mensagem *"Este arquivo pode ser perigoso"* ou *"Download bloqueado"*.
- **No Google Chrome**: Clique nos três pontos ao lado do download cancelado (ou pressione `Ctrl + J`), encontre o arquivo e clique em **Manter mesmo assim**.
- **No Microsoft Edge**: Passe o mouse sobre o aviso do download, clique nos três pontinhos (`...`), selecione **Manter** e depois **Manter mesmo assim**.

#### 2. Se o WINDOWS (SmartScreen) bloquear ao abrir:
Ao dar duplo clique no `.exe`, o Windows pode exibir a tela azul do SmartScreen (*"O Windows protegeu o seu computador"*).
- Clique no texto **"Mais informações"**.
- Em seguida, clique no botão **"Executar mesmo assim"**.
- Confirme a permissão de Administrador clicando em **Sim**.

---

### Opção 2: Executando via Código Fonte (Python)

Se preferir rodar o script diretamente:
1. Certifique-se de ter o **Python 3.x** instalado.
2. Baixe o arquivo `.py` deste repositório.
3. Abra o terminal na pasta e execute:
   ```bash
   python nome_do_seu_script.py**
