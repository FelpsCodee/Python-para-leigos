# ========================================================================
# MÓDULO 22: LIST COMPREHENSION (O Atalho Mágico para Criar Listas)
# ========================================================================
#
# List Comprehension é um "super-poder" do Python. É uma forma elegante e
# super concisa de criar uma nova lista a partir de uma já existente.
#
# A Analogia: O Comando de Voz para um Exército
# - O jeito normal (com loop 'for'): É como dar uma ordem para cada soldado, um por um. (Lento e repetitivo).
# - Com List Comprehension: É como gritar um único comando para o exército inteiro de uma vez só. (Rápido e eficiente).

# A lista com a qual vamos trabalhar
numeros_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Nossa lista de números original: {numeros_base}")
print("-" * 55)


# --- Cenário 1: Criar uma nova lista com o DOBRO de cada número ---

# Jeito 1: O jeito tradicional, soldado por soldado
lista_dobro_tradicional = []
for numero in numeros_base:
    lista_dobro_tradicional.append(numero * 2)
print(f"Jeito Tradicional (com for): {lista_dobro_tradicional}")


# Jeito 2: Com List Comprehension (O Comando de Voz)
# A sintaxe parece um "inglês ao contrário". A ordem do comando de voz é:
# "O que fazer" -> "Para quem" -> "De onde"
# [faça_isso | para_cada_item | na_lista]
# [ numero * 2 |  for numero  | in numeros_base]
lista_dobro_pythonico = [numero * 2 for numero in numeros_base]
print(f"Com List Comprehension:      {lista_dobro_pythonico}")
print("-" * 55)


# --- Cenário 2: Criar uma lista APENAS com os números ímpares ---

# Jeito 1: O jeito tradicional com uma condição 'if'
impares_tradicional = []
for numero in numeros_base:
    if numero % 2 != 0:  # Se o número não for par (ou seja, for ímpar)...
        impares_tradicional.append(numero)
print(f"Tradicional com if: {impares_tradicional}")


# Jeito 2: List Comprehension com CONDIÇÃO (Comando de Voz Inteligente)
# Agora o comando é: "Pegue o número, para cada número na lista, SÓ SE ele for ímpar!"
# [faça_isso | para_cada_item | na_lista | se_a_condição_for_verdadeira]
# [  numero   |   for numero   |in numeros_base|    if numero % 2 != 0   ]
impares_pythonico = [numero for numero in numeros_base if numero % 2 != 0]
print(f"List Comprehension com if: {impares_pythonico}")

# List comprehensions são muito amadas na comunidade Python por serem limpas,
# legíveis (depois que você se acostuma com a ordem) e, muitas vezes, mais rápidas!