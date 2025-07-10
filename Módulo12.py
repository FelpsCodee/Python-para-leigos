# ===================================================================
# MÓDULO 12: DICIONÁRIOS (A Ficha de Personagem)
# ===================================================================
#
# Se a Lista é um "carrinho de compras" com itens em ordem (0, 1, 2...),
# o Dicionário é uma "Ficha Cadastral" onde cada informação tem uma ETIQUETA (a "chave").
#
# Você não pede pelo "item na posição 2", você pede pela etiqueta "nome" ou "idade".
# Um dicionário é sempre definido por chaves {}.
# Você não pede pelo "item na posição 2", você pede pela etiqueta "nome" ou "idade".
# Um dicionário é sempre definido por chaves {}.

# --- 1. Criando a Ficha de um Personagem de Jogo ---
# Cada informação (o valor) é associada a uma etiqueta única (a chave).
# Chave -> "nome", Valor -> "Gandalf"
personagem = {
    "nome": "Gandalf, o Cinzento",
    "classe": "Mago",
    "hp": 80,  # Pontos de Vida (Health Points)
    "inventario": ["Cajado Mágico", "Cachimbo"]
}
print(f"Ficha inicial do personagem: {personagem}")
print("-" * 55)


# --- 2. Acessando uma informação pela ETIQUETA (Chave) ---
# Quero saber a classe do meu personagem. Eu uso a etiqueta "classe".
classe_do_personagem = personagem["classe"]
print(f"A classe do personagem é: '{classe_do_personagem}'")
print("-" * 55)


# --- 3. Adicionando uma nova informação ---
# O personagem aprendeu uma nova magia! Adicionamos uma nova etiqueta "magia_principal".
print("O personagem aprendeu uma nova magia!")
personagem["magia_principal"] = "Bola de Fogo"
print(f"Ficha atualizada: {personagem}")
print("-" * 55)


# --- 4. Atualizando uma informação existente ---
# O personagem tomou dano em uma batalha. Vamos atualizar o HP.
# Basta acessar a etiqueta e atribuir um novo valor.
print("O personagem tomou 10 de dano...")
personagem["hp"] = 70  # O valor antigo (80) é substituído.
print(f"HP atual: {personagem['hp']}")
print("-" * 55)


# --- 5. Removendo uma informação com 'del' ---
# Imagine que o personagem tinha um status temporário (ex: "envenenado") que foi curado.
personagem["status"] = "Normal"
print(f"Personagem com status: {personagem}")

# A palavra 'del' (de delete) remove completamente a etiqueta e a informação associada.
del personagem["status"]
print(f"Após a cura, o status é removido da ficha: {personagem}")

# A grande vantagem do dicionário é poder pegar e guardar dados
# usando nomes que fazem sentido, em vez de posições numéricas!