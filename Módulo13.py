# ===================================================================
# MÓDULO 13: FUNÇÕES EM UM EXEMPLO SÓ (A Máquina de Fazer Coisas)
# ===================================================================
#
# Pense em uma Função como o projeto de uma MÁQUINA que faz uma tarefa.
# O processo tem duas partes muito claras:
# 1. O DESIGN DA MÁQUINA (é quando definimos a função com 'def').
# 2. USAR A MÁQUINA (é quando chamamos a função pelo nome para que ela trabalhe).

# -------------------------------------------------------------------
# Parte 1: O DESIGN DA MÁQUINA (A definição da função)
# -------------------------------------------------------------------
# Usamos 'def' para começar o design da nossa "Máquina de Saudações".
# 'saudacao_personalizada' é o nome da máquina.
# '(nome_da_pessoa)' é o "ingrediente" que a máquina espera receber. Chamamos isso de PARÂMETRO.
# 'return' é o que a máquina "entrega" no final, o produto pronto.

def saudacao_personalizada(nome_da_pessoa):
    # Este é o mecanismo interno da máquina:
    mensagem_pronta = f"Olá, {nome_da_pessoa}! Tenha um ótimo dia!"
    return mensagem_pronta

# Importante: Até este momento, a máquina está só no papel.
# Nenhuma saudação foi criada ainda. Apenas projetamos a máquina.
print("--- Design da 'Máquina de Saudações' criado com sucesso! ---")
print("-" * 60)


# -------------------------------------------------------------------
# Parte 2: USAR A MÁQUINA (A chamada da função)
# -------------------------------------------------------------------
# Agora vamos ligar a máquina e dar a ela ingredientes de verdade!
# "Maria" e "Carlos" são os ARGUMENTOS que passamos para a máquina.

print("--- Usando a máquina para criar saudações: ---")

# Usando a máquina com o nome "Maria"
# O que a máquina retorna (a mensagem pronta) é guardado na variável 'saudacao_para_maria'.
saudacao_para_maria = saudacao_personalizada("Maria")
print(f"Produto 1: {saudacao_para_maria}")

# Podemos usar a MESMA máquina com um ingrediente diferente.
saudacao_para_carlos = saudacao_personalizada("Carlos")
print(f"Produto 2: {saudacao_para_carlos}")
print("-" * 60)


# --- Outro exemplo: Uma máquina de calcular com DOIS ingredientes ---

def somar_numeros(numero1, numero2):
    print(f"-> A máquina está somando {numero1} + {numero2}...")
    resultado_da_soma = numero1 + numero2
    return resultado_da_soma

soma_final = somar_numeros(15, 10)
print(f"O resultado da máquina de somar é: {soma_final}")

# A grande vantagem das funções é: escreva o código UMA VEZ,
# e use-o quantas vezes quiser, com "ingredientes" diferentes!