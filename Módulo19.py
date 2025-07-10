# ===================================================================
# MÓDULO 19: BIBLIOTECA MATH (A Calculadora Científica do Python)
# ===================================================================
#
# Pense no Python básico como uma calculadora de bolso: ela faz as quatro
# operações (+, -, *, /).
#
# Mas e se você precisar de operações complexas como raiz quadrada, ou o valor de Pi (π)?
# Para isso, você precisa pegar uma "caixa de ferramentas" extra, uma CALCULADORA CIENTÍFICA.
# Em Python, a principal calculadora científica se chama 'math'.

# --- 1. Pegando a Calculadora Científica da Prateleira ---
# A linha 'import math' diz ao nosso programa: "Ok, vou precisar
# das ferramentas avançadas de matemática. Deixa a caixa 'math' aqui do meu lado."
import math

print("--- Calculadora Científica 'math' importada e pronta para uso! ---")
print("-" * 65)


# --- 2. Usando as "Teclas" (Funções) da Calculadora ---
# Para usar uma ferramenta, sempre dizemos o nome da caixa, um ponto, e o nome da ferramenta.
# Formato:  math.nome_da_ferramenta()

# Ferramenta de Raiz Quadrada: math.sqrt() (de "square root")
numero = 81
raiz_quadrada = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
print("-" * 65)


# Ferramentas de Arredondamento: math.ceil() e math.floor()
# 'ceil' vem de ceiling (TETO). Sempre arredonda o número PARA CIMA.
# 'floor' vem de floor (CHÃO). Sempre arredonda o número PARA BAIXO.
preco_quebrado = 29.35
preco_arredondado_para_cima = math.ceil(preco_quebrado)
preco_arredondado_para_baixo = math.floor(preco_quebrado)
print(f"O preço R$ {preco_quebrado} arredondado para CIMA (teto) é: R$ {preco_arredondado_para_cima}")
print(f"O preço R$ {preco_quebrado} arredondado para BAIXO (chão) é: R$ {preco_arredondado_para_baixo}")
print("-" * 65)


# A Calculadora também tem constantes famosas, como o PI (π)
# 'math.pi' não é uma função (não tem ()), é um valor já guardado na memória da calculadora.
print(f"O valor de PI (π) que a calculadora 'math' conhece é: {math.pi}")

# Exemplo prático: Calcular a área de um círculo (Fórmula: Área = π * raio²)
raio_do_circulo = 10
# Usamos math.pi para o valor de π e math.pow(base, expoente) para calcular a potência.
area_do_circulo = math.pi * math.pow(raio_do_circulo, 2)
print(f"A área de um círculo com raio {raio_do_circulo} é: {area_do_circulo:.2f}") # :.2f formata para 2 casas decimais


# A biblioteca 'math' tem muitas outras ferramentas (seno, cosseno, logaritmo, etc.).
# O importante é saber como IMPORTAR a caixa de ferramentas e como USAR uma ferramenta de dentro dela!
