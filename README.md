# 🧹 Limpador de Sistema Windows

Um script simples e eficiente em Python para automatizar a limpeza de arquivos temporários e resíduos do sistema operacional Windows, ajudando a liberar espaço em disco de forma rápida.

---

## 📌 O que o script faz?

O script realiza a limpeza automatizada em três diretórios críticos do Windows onde costumam ser acumulados arquivos temporários:

* **Pasta Temp do Usuário (`%TEMP%`):** Arquivos temporários criados por aplicativos em execução no seu perfil de usuário.
* **Pasta Temp do Sistema (`C:\Windows\Temp`):** Arquivos temporários gerados pelo próprio sistema operacional e serviços do Windows.
* **Pasta Prefetch (`C:\Windows\Prefetch`):** Dados de cache do Windows utilizados para otimizar a inicialização de programas.

---

## ⚡ Principais Recursos

* **Elevação Automática de Privilégios (UAC):** Ao ser executado, o script verifica se já está rodando como **Administrador**. Se não estiver, ele solicita automaticamente a permissão do Windows para rodar com privilégios elevados (necessário para limpar diretórios como a *Prefetch* e a *Temp* do sistema).
* **Tratamento de Erros/Arquivos em Uso:** Se um arquivo estiver sendo utilizado no momento por outro programa ou pelo sistema, o script ignora o arquivo sem travar e contabiliza o erro no resumo final.
* **Resumo da Limpeza:** Exibe no terminal a quantidade de arquivos/pastas removidos com sucesso e a quantidade de itens mantidos por estarem em uso.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Bibliotecas nativas:** `os`, `shutil`, `ctypes`, `sys` (não requer nenhuma instalação externa via `pip`).

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python** instalado na sua máquina.
2. Baixe ou clone este repositório.
3. Execute o arquivo diretamente no seu terminal ou dando duplo clique nele:

```bash
python Limpador_sistema.py
