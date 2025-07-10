# ===================================================================
# MÓDULO 9: ESTRUTURAS DE REPETIÇÃO (FOR, WHILE)
# ===================================================================
#
# Loops (ou laços) são ferramentas para repetir uma tarefa várias vezes
# sem ter que escrever o mesmo código de novo e de novo.
#
# A grande pergunta é: QUANDO USAR CADA UM?
#
# -> Use 'for' quando você tem uma LISTA de itens e quer fazer algo com CADA UM deles.
#    (Pense: Uma checklist de tarefas que você precisa cumprir uma a uma).
#
# -> Use 'while' quando você quer repetir algo ENQUANTO uma CONDIÇÃO for verdadeira.
#    (Pense: Jogar videogame ENQUANTO o chefão tiver vida).

# -------------------------------------------------------------------
# Exemplo 1: O loop `for` (O Especialista em Listas)
# -------------------------------------------------------------------
# Cenário: Temos uma lista de compras e vamos passar cada item no caixa do mercado.

lista_de_compras = ["Maçã", "Leite", "Pão", "Café"]

print("--- Passando as compras no caixa com o loop FOR: ---")

# O loop 'for' vai pegar cada item da lista, um de cada vez, e colocar na variável 'item'.
# Ele vai repetir exatamente o número de vezes do tamanho da lista (neste caso, 4 vezes).
for item in lista_de_compras:
    # Este bloco de código vai repetir para cada item da lista.
    print(f"Caixa registrando: {item}... bip!")

print("Pronto! Todos os itens da sua lista foram registrados.")


print("\n" + "="*55 + "\n") # Apenas para separar os exemplos


# -------------------------------------------------------------------
# Exemplo 2: O loop `while` (O Vigilante da Condição)
# -------------------------------------------------------------------
# Cenário: Estamos enchendo um balde de 10 litros com um copo de 2 litros.
# Não sabemos quantos copos vamos precisar, mas sabemos que devemos parar QUANDO o balde estiver cheio.

capacidade_total_balde = 10
agua_no_balde = 0
numero_de_copos = 0

print("--- Enchendo o balde com o loop WHILE: ---")
print(f"O balde está com {agua_no_balde} litros.")

# O loop 'while' vai continuar repetindo ENQUANTO a água no balde for MENOR que a capacidade total.
while agua_no_balde < capacidade_total_balde:
    print("Enchendo com mais um copo...")
    
    # A CADA REPETIÇÃO, PRECISAMOS ATUALIZAR A CONDIÇÃO!
    # Se esquecermos esta parte, o loop se torna infinito, pois a água nunca aumentaria.
    agua_no_balde += 2  # Adiciona 2 litros de água
    numero_de_copos += 1 # Conta quantos copos usamos
    
    print(f"Agora o balde está com {agua_no_balde} litros.")

print(f"\nO balde encheu! Usamos {numero_de_copos} copos de água.")