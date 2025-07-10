# ===================================================================
# MÓDULO 17: JUNTANDO TUDO - UM PROGRAMA INTERATIVO COMPLETO
# ===================================================================
#
# Chegamos à nossa "formatura"! Vamos usar quase TUDO o que aprendemos
# (loops, condicionais, input, tratamento de erros, etc.) para criar
# um programa de verdade: um mini jogo de adivinhação!

# --- 1. O Setup do Jogo ---
# Primeiro, importamos a "caixa de ferramentas" do Python para gerar números aleatórios.
import random

# O computador vai "pensar" em um número secreto entre 1 e 100.
numero_secreto = random.randint(1, 100)
palpite_do_usuario = 0      # Variável para guardar o palpite do jogador.
contador_de_tentativas = 0  # Variável para contar os palpites.

print("--- BEM-VINDO AO JOGO DE ADIVINHAÇÃO! ---")
print("Eu pensei em um número entre 1 e 100. Será que você consegue adivinhar?")
print("-" * 65)


# --- 2. O Loop Principal do Jogo ---
# Usamos 'while True' para criar um loop que roda "para sempre",
# até que nós mesmos o mandemos parar com a palavra 'break'.
# Isso mantém o jogo ativo enquanto o jogador não acertar o número.
while True:
    # --- 3. Pegando o palpite do jogador com segurança ---
    try:
        # Pedimos para o jogador digitar um número.
        palpite_str = input("Qual é o seu palpite? ")
        # Tentamos converter o texto digitado para um número inteiro.
        palpite_do_usuario = int(palpite_str)
    except ValueError:
        # Se o jogador digitar algo que não é um número (como "oi"),
        # a "rede de segurança" do except é acionada.
        print("Opa! Isso não parece um número. Por favor, digite apenas números.")
        continue  # A palavra 'continue' pula para a próxima rodada do loop, ignorando o código abaixo.

    # --- 4. A Lógica Principal: Comparações ---
    # A cada palpite válido, adicionamos 1 ao nosso contador.
    contador_de_tentativas += 1

    if palpite_do_usuario < numero_secreto:
        print("-> Muito baixo! Tente um número maior.")
    elif palpite_do_usuario > numero_secreto:
        print("-> Muito alto! Tente um número menor.")
    else:
        # Se não é maior nem menor, só pode ser igual! O jogador acertou!
        print("\n==============================================")
        print(f"BOA! Você acertou! O número secreto era {numero_secreto}!")
        print(f"Você precisou de {contador_de_tentativas} tentativas para conseguir.")
        print("==============================================")
        break  # A palavra 'break' é a "saída de emergência" que quebra o loop e encerra o jogo.


# --- 5. O Fim do Jogo ---
# Este código só é executado depois que o 'break' acontece dentro do loop.
print("\nFim de jogo. Obrigado por jogar!")
