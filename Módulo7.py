# =================================================================
# MÓDULO 7: OPERADORES LÓGICOS (AND, OR, NOT)
# =================================================================
#
# Pense nos operadores lógicos como uma forma de o seu programa
# tomar uma decisão baseada em várias condições, como nós fazemos na vida real.
#
# Vamos usar um cenário: "O que vou fazer no meu sábado?".
# Para decidir, temos alguns fatos (nossas variáveis True ou False).

# --- Nossos Fatos para o Sábado ---
esta_chovendo = False
terminei_minhas_tarefas = True
tenho_filme_novo_para_ver = True
tenho_jogo_novo_no_pc = False

print("--- ANÁLISE DO MEU SÁBADO ---")

# -------------------------------------------------
# 1. Operador 'not' (NÃO) - O Inversor
# Ele simplesmente inverte um valor: True vira False e False vira True.
# -------------------------------------------------
o_tempo_esta_bom = not esta_chovendo # Se NÃO está chovendo, o tempo está bom.
print(f"O tempo está bom para sair? {o_tempo_esta_bom}") # 'not False' resulta em True.


# -------------------------------------------------
# 2. Operador 'and' (E) - O Exigente
# Só considera o resultado True se TODAS as condições forem verdadeiras.
# -------------------------------------------------
# Cenário: "Posso ir ao parque?". Para isso, o tempo precisa estar bom E eu preciso ter terminado minhas tarefas.
posso_ir_ao_parque = o_tempo_esta_bom and terminei_minhas_tarefas
print(f"Posso ir ao parque? {posso_ir_ao_parque}") # 'True and True' resulta em True.


# -------------------------------------------------
# 3. Operador 'or' (OU) - O Flexível
# Já fica feliz e considera o resultado True se PELO MENOS UMA condição for verdadeira.
# -------------------------------------------------
# Cenário: "Tenho alguma opção de lazer em casa?". Basta eu ter um filme novo OU um jogo novo.
tenho_lazer_em_casa = tenho_filme_novo_para_ver or tenho_jogo_novo_no_pc
print(f"Tenho alguma opção de lazer em casa? {tenho_lazer_em_casa}") # 'True or False' resulta em True.


# =================================================================
# A DECISÃO FINAL: Juntando tudo com `if`
# =================================================================
# Agora, vamos usar os resultados acima para tomar uma decisão final.

print("\n--- Então, o que vou fazer hoje? ---")

if posso_ir_ao_parque:
    print("Decidido! O tempo está ótimo e já fiz minhas obrigações. Vou ao parque!")
elif tenho_lazer_em_casa:
    print("Não vou sair, mas tenho um filme ou jogo novo para me divertir em casa.")
else:
    print("Hoje o dia está meio parado... sem opções de lazer definidas. Vou relaxar.")
