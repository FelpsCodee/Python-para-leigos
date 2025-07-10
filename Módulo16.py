# ===================================================================
# MÓDULO 16: TRATAMENTO DE EXCEÇÕES (A Rede de Segurança do Circo)
# ===================================================================
#
# Pense no bloco `try...except` como a REDE DE SEGURANÇA de um trapezista.
# Sem a rede, se o trapezista errar, ele cai e o show acaba (o programa quebra).
# Com a rede, se ele errar, ele cai nela, se levanta e o show continua!
#
# O programa vai TENTAR (try) fazer a manobra arriscada.
# Se um erro específico acontecer, ele é "amparado" pelo EXCEPT correspondente.

# --- O Espetáculo: A Calculadora de Divisão Perigosa ---
# Vamos pedir dois números para o usuário. Isso pode dar vários erros!
# >> Teste o programa com estas combinações para ver cada "rede" funcionando:
#    1. Números: 10 e 2 (o sucesso)
#    2. Números: 10 e 0 (o erro de divisão por zero)
#    3. Números: 10 e "oi" (o erro de valor inválido)
print("--- Bem-vindo à Calculadora de Divisão Perigosa! ---")

try:
    # A manobra arriscada: pedir números e tentar a divisão.
    print("\nPor favor, digite os números para a divisão.")
    numero1 = float(input("Digite o dividendo (ex: 10): "))
    numero2 = float(input("Digite o divisor (ex: 2): "))

    resultado = numero1 / numero2

# A 'rede de segurança' ESPECÍFICA para o erro de divisão por zero.
except ZeroDivisionError:
    print("\nERRO: Caiu na rede 'ZeroDivisionError'!")
    print("Opa! Na matemática, não se pode dividir um número por zero.")

# A 'rede de segurança' ESPECÍFICA para quando o usuário digita texto em vez de número.
except ValueError:
    print("\nERRO: Caiu na rede 'ValueError'!")
    print("Opa! Você precisa digitar um número válido, não um texto.")

# O bloco 'else' é a COMEMORAÇÃO. Ele só acontece se a manobra no 'try' deu CERTO (sem erros).
else:
    print("\nSUCESSO! A manobra foi perfeita, o trapezista não caiu!")
    print(f"O resultado da divisão de {numero1} por {numero2} é {resultado:.2f}.")

# O bloco 'finally' é a LIMPEZA FINAL. Ele SEMPRE é executado, não importa se deu certo ou errado.
# É como as luzes do circo que se apagam no final do número, aconteça o que acontecer.
finally:
    print("\n-----------------------------------------------------")
    print("Fim do número! O trapezista agradece a presença.")