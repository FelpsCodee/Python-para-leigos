# =================================================================
# MÓDULO 8: CONDICIONAIS (IF, ELIF, ELSE)
# =================================================================
#
# Pense na estrutura if/elif/else como uma recepcionista de evento
# que precisa dar uma pulseira para cada convidado.
#
# A recepcionista é eficiente: ela faz as perguntas em ordem e,
# na PRIMEIRA resposta "sim", ela entrega a pulseira e PARA de perguntar.

# ---- Altere o valor da idade aqui para ver o resultado mudar! ----
# ---- Teste com os valores 25, 17, e 10. ----
idade_do_convidado = 17

print(f"--- Verificando um convidado com {idade_do_convidado} anos ---")

# 1. A recepcionista faz a PRIMEIRA pergunta: "A idade é 18 ou mais?"
if idade_do_convidado >= 18:
    # Se a resposta for "sim" (True), ela entrega a pulseira e o trabalho dela ACABA AQUI.
    print("Resultado: Você recebe a pulseira VIP Dourada (Adulto).")

# 2. Se a primeira resposta foi "não" (False), E SOMENTE NESSE CASO, ela faz a segunda pergunta:
#    "Ok, então a idade é 12 ou mais?"
elif idade_do_convidado >= 12:
    # Se a resposta for "sim", ela entrega a pulseira e o trabalho dela ACABA AQUI.
    print("Resultado: Você recebe a pulseira Prata (Adolescente).")

# 3. Se NENHUMA das respostas acima foi "sim", ela nem pergunta mais nada e usa o último recurso:
else:
    # Este bloco só roda se todos os 'if' e 'elif' acima deram False.
    print("Resultado: Você recebe a pulseira Colorida (Criança).")


# Lembre-se da regra de ouro: Apenas UM dos blocos de código (o do if,
# de um dos elifs, ou o do else) será executado por vez!
print("-" * 55)