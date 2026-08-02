import os
import shutil
import ctypes
import sys

# 1. Função que força o script a abrir como Administrador
def solicitar_admin():
    try:
        # Checa se o script JÁ é Administrador
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        is_admin = False

    if not is_admin:
        print("🔑 Solicitando permissão de Administrador ao Windows...")
        # Reabre o próprio script pedindo privilégios elevados (janela com o escudo)
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        # Fecha a versão normal sem permissão
        sys.exit()

# O programa COMEÇA aqui pedindo a permissão
solicitar_admin()

# 2. Definição das pastas do sistema
pastas_para_limpar = [
    os.environ.get("TEMP"),
    os.path.join(os.environ.get("SystemRoot"), "Temp"),
    os.path.join(os.environ.get("SystemRoot"), "Prefetch")
]

print("Iniciando limpeza do sistema como Administrador...\n")

for pasta in pastas_para_limpar:
    if not pasta or not os.path.exists(pasta):
        continue

    print(f"Limpando: {pasta}")
    arquivos_removidos = 0
    erros = 0

    # Agora o os.listdir vai conseguir ler a Prefetch sem travar!
    try:
        itens = os.listdir(pasta)
    except Exception as e:
        print(f"Não foi possível acessar {pasta}: {e}\n")
        continue

    for item in itens:
        caminho_completo = os.path.join(pasta, item)
        
        try:
            if os.path.isfile(caminho_completo) or os.path.islink(caminho_completo):
                os.remove(caminho_completo)
                arquivos_removidos += 1
            elif os.path.isdir(caminho_completo):
                shutil.rmtree(caminho_completo)
                arquivos_removidos += 1

        except Exception:
            # Arquivos do Windows que estão abertos/em uso no momento não podem ser apagados
            erros += 1

    print(f"Removidos: {arquivos_removidos} | Em uso (ignorados): {erros}\n")

print("✨ Limpeza concluída com sucesso!")
input("\nPressione ENTER para fechar...")