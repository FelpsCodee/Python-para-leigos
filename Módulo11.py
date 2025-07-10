# ===================================================================
# MÓDULO 11: TUPLAS (A Caixa-Forte de Dados)
# ===================================================================
#
# Se a Lista era um "Carrinho de Compras" que você podia alterar,
# pense na Tupla como uma "Caixa-Forte" ou algo "Escrito em Pedra".
#
# O seu propósito é guardar dados em ordem que NÃO DEVEM ser alterados por engano.
# Uma tupla é sempre definida por parênteses ().

# --- Guardando dados importantes na nossa Caixa-Forte ---
# Exemplo: Os dias da semana. A ordem deles é fixa e não muda.
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

print(f"Dados guardados na tupla: {dias_da_semana}")
print("-" * 55)


# --- O que você PODE fazer: LER os dados ---
# Você pode acessar e ler qualquer item da tupla, assim como fazia na lista.
# Lembre-se que a contagem sempre começa no índice 0.
print("Vamos ver qual é o dia no índice 4...")
quinto_dia = dias_da_semana[4] # Índice 4 é o quinto item.
print(f"O dia no índice 4 é: '{quinto_dia}'")
print("-" * 55)


# --- O que você NÃO PODE fazer: ALTERAR os dados ---
# É aqui que a "Caixa-Forte" mostra seu valor. Qualquer tentativa de alteração vai dar ERRO!
print("Agora, vamos tentar modificar a tupla (o que vai dar erro):")

# TENTATIVA 1: Adicionar um novo dia.
# dias_da_semana.append("Oitavodia")
# >> ERRO! O cofre está lacrado, não é possível adicionar novos itens.

# TENTATIVA 2: Alterar um item existente.
# dias_da_semana[0] = "Dia-Novo"
# >> ERRO! Você não pode reescrever algo que já foi gravado na pedra.

# TENTATIVA 3: Remover um item.
# del dias_da_semana[2]
# >> ERRO! A estrutura da caixa-forte é permanente.

print("O Python nos protege e gera um erro se tentarmos alterar a tupla.")
print("-" * 55)


# --- Então, por que usar uma Tupla? ---
# 1. SEGURANÇA: Garante que dados importantes, como configurações, coordenadas
#    ou uma sequência fixa, não sejam modificados por acidente no seu código.
#
# 2. CLAREZA: Quando outro programador (ou você mesmo no futuro) vê uma tupla,
#    ele já sabe que aqueles dados são constantes e não devem ser alterados.

# Exemplo de uso prático: Coordenadas de um local.
coordenadas_cristo_redentor = (-22.9519, -43.2105) # Latitude e Longitude não devem mudar!
print(f"Coordenadas do Cristo Redentor (Latitude, Longitude): {coordenadas_cristo_redentor}")