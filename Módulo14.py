# ===================================================================
# MÓDULO 14: MANIPULAÇÃO DE STRINGS (O Editor de Texto Mágico)
# ===================================================================
#
# Pense em uma string (texto) como um documento. O Python te dá um
# "canivete suíço" de ferramentas (métodos) para editar e transformar esse texto.
#
# IMPORTANTE: As strings são "imutáveis" em Python. Isso significa que
# as ferramentas NUNCA mudam o texto original. Elas sempre criam uma
# CÓPIA nova e modificada, deixando o original intacto.

# --- Nosso "documento" original (com letras maiúsculas e minúsculas) ---
frase_original = "o Dia está Lindo e Ensolarado para aprender Python!"
print(f"Frase Original: '{frase_original}'")
print("-" * 55)


# --- Ferramenta 1: Mudar para MAIÚSCULO ou minúsculo ---
# .upper() -> Deixa o texto todo em caixa alta, como se estivesse GRITANDO.
# .lower() -> Deixa o texto todo em caixa baixa, como se estivesse sussurrando.
frase_em_maiusculo = frase_original.upper()
frase_em_minusculo = frase_original.lower()
print(f"Com .upper(): {frase_em_maiusculo}")
print(f"Com .lower(): {frase_em_minusculo}")
print("-" * 55)


# --- Ferramenta 2: Localizar e Substituir ---
# .replace('texto antigo', 'texto novo') -> Procura uma palavra e a troca por outra na cópia.
frase_substituida = frase_original.replace("Lindo", "ótimo")
print(f"Com .replace(): '{frase_substituida}'")
print("-" * 55)


# --- Ferramenta 3: Quebrar o texto em uma lista de palavras ---
# .split() -> Recorta a string em vários pedaços, usando o espaço como "tesoura".
#            O resultado é uma LISTA com cada palavra separada.
lista_de_palavras = frase_original.split()
print(f"Com .split(), a frase vira uma lista: {lista_de_palavras}")
# Agora que é uma lista, podemos pegar uma palavra específica pelo índice!
print(f"A terceira palavra da lista é: '{lista_de_palavras[2]}'")
print("-" * 55)


# --- Ferramenta 4: Juntar uma lista de palavras em um texto só ---
# 'cola'.join(lista) -> Essa é a ferramenta mais "estranha", mas é muito poderosa.
# Analogia: Pense no texto antes do .join() como uma "COLA MÁGICA".
# Você diz para a cola: "Passe você mesma entre cada palavra da lista e junte tudo!"

cola_de_espaco = " "
frase_remontada = cola_de_espaco.join(lista_de_palavras)
print(f"Usando ' '.join() para remontar a frase: '{frase_remontada}'")

cola_de_seta = " -> "
frase_com_setas = cola_de_seta.join(lista_de_palavras)
print(f"Usando ' -> '.join(): '{frase_com_setas}'")
print("-" * 55)


# --- PROVA FINAL: O original NUNCA muda! ---
# Note que, depois de todas as operações, nossa frase original continua a mesma.
print("E a frase original? Continua intacta:")
print(f"Frase Original no final de tudo: '{frase_original}'")
