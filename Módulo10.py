# ===================================================================
# MÓDULO 10: LISTAS EM UM EXEMPLO SÓ (O Carrinho de Compras)
# ===================================================================
#
# Pense em uma Lista como um carrinho de supermercado: você pode colocar
# itens, tirar itens, e os itens ficam na ORDEM em que você os colocou.
# Uma lista é sempre definida por colchetes [].

# --- 1. Começando as compras ---
# Nosso carrinho já começa com alguns itens que pegamos na entrada.
carrinho_de_compras = ["Maçã", "Pão", "Leite", "Ovos"]
print(f"Comecei as compras. No carrinho tem: {carrinho_de_compras}")
print("-" * 50)


# --- 2. Acessando um item (O famoso 'índice 0') ---
# Por que o primeiro item é o 0 e não o 1?
# Pense no índice como "quantos passos dar a partir do início do carrinho".
# -> Para pegar o PRIMEIRO item ("Maçã"), você não dá nenhum passo. Fica parado no começo (passo 0).
# -> Para pegar o SEGUNDO item ("Pão"), você dá 1 passo à frente (passo 1).
primeiro_item = carrinho_de_compras[0]
terceiro_item = carrinho_de_compras[2]
print(f"O primeiro item do carrinho é o '{primeiro_item}' (no índice 0).")
print(f"O terceiro item do carrinho é o '{terceiro_item}' (no índice 2).")
print("-" * 50)


# --- 3. Adicionando um item com .append() ---
# No meio do corredor, lembrei que preciso de café!
# O .append() SEMPRE adiciona o novo item no FINAL da lista (do carrinho).
print("Lembrei! Preciso de café...")
carrinho_de_compras.append("Café")
print(f"Agora o carrinho tem: {carrinho_de_compras}")
print("-" * 50)


# --- 4. Removendo um item com .remove() ---
# Olhando para o carrinho, acho melhor não levar pão hoje. Vou devolver na prateleira.
# O .remove() procura pelo item com aquele NOME (valor) e o tira da lista.
print("Mudei de ideia sobre o pão...")
carrinho_de_compras.remove("Pão")
print(f"Carrinho atualizado: {carrinho_de_compras}")
print("-" * 50)


# --- 5. Contando quantos itens temos com len() ---
# Antes de ir para o caixa, quero saber quantos produtos estou levando.
# A função len() (de 'length', comprimento em inglês) nos diz o tamanho da lista.
quantidade_de_itens = len(carrinho_de_compras)
print(f"No total, estou levando {quantidade_de_itens} itens para o caixa.")