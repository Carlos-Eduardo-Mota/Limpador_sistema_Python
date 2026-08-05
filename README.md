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
   Calcula a diferença de espaço livre e exibe o total liberado na tela em MB ou GB.

---

## 📋 Como Executar

### Pré-requisitos
- Python 3.x instalado no Windows.

### Passos
1. Clone este repositório ou baixe o arquivo `.py`.
2. Abra o terminal ou dê um duplo clique no arquivo `.py`.
3. Quando o Windows exibir a solicitação de controle de conta de usuário (UAC), clique em **Sim**.
4. Aguarde a execução e pressione **Enter** ao final para fechar a janela.
