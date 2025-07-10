# ===================================================================
# MÓDULO 15: MANIPULAÇÃO DE ARQUIVOS (O Diário Mágico)
# ===================================================================
#
# Pense em um arquivo .txt como um "Diário Mágico" que seu programa pode ler e escrever.
# Assim, as informações (como uma lista de tarefas ou um ranking de jogo)
# não se perdem quando o programa fecha.
#
# A forma mais segura de fazer isso é com o "feitiço": with open(...) as ...
# Ele garante que, aconteça o que acontecer, o diário será fechado corretamente no final.

# O nome do nosso arquivo de diário. Ele será criado na mesma pasta do seu script.
nome_do_arquivo = "minha_lista_de_compras.txt"

# -------------------------------------------------------------------
# 1. Escrevendo no Diário (Modo "w" - Write / Escrever do Zero)
# -------------------------------------------------------------------
# O modo "w" é como abrir o diário em uma PÁGINA EM BRANCO.
# >> ATENÇÃO: Se já havia algo escrito no diário, o modo "w" APAGA TUDO! <<
print("--- 1. Escrevendo a lista de compras do zero... ---")
with open(nome_do_arquivo, "w") as arquivo:
    arquivo.write("- Arroz\n")  # O \n é como apertar "Enter" para pular para a próxima linha.
    arquivo.write("- Feijão\n")
    arquivo.write("- Batata\n")
print(f"Arquivo '{nome_do_arquivo}' criado/sobrescrito com sucesso!")
print("-" * 55)


# -------------------------------------------------------------------
# 2. Adicionando ao Diário (Modo "a" - Append / Anexar)
# -------------------------------------------------------------------
# O modo "a" é como abrir o diário no FINAL da última anotação para continuar escrevendo.
# Ele NÃO apaga o conteúdo anterior. É o mais seguro para adicionar novas informações.
print("--- 2. Lembrei de mais um item! Adicionando ao final... ---")
with open(nome_do_arquivo, "a") as arquivo:
    arquivo.write("- Macarrão\n")
print("Item adicionado ao final do arquivo!")
print("-" * 55)


# -------------------------------------------------------------------
# 3. Lendo o conteúdo do Diário (Modo "r" - Read / Ler)
# -------------------------------------------------------------------
# O modo "r" é como abrir o diário apenas para LER o que está escrito, sem poder alterar.
print("--- 3. Lendo a lista de compras completa que está salva: ---")
try:
    with open(nome_do_arquivo, "r") as arquivo:
        # .read() lê todo o conteúdo do arquivo e o guarda em uma única string.
        conteudo_completo = arquivo.read()
        print("\n=== CONTEÚDO DO ARQUIVO ===\n" + conteudo_completo)
except FileNotFoundError:
    print(f"ERRO: O arquivo '{nome_do_arquivo}' não foi encontrado para leitura.")

#
# RESUMO DOS MODOS:
# "w" (Write)   -> PÁGINA EM BRANCO. Cuidado, apaga tudo! Use para começar um arquivo novo.
# "a" (Append)  -> CONTINUAÇÃO. Adiciona informações no final. O mais seguro para atualizar.
# "r" (Read)    -> APENAS LEITURA. Usa-se para ler o que já está salvo.
