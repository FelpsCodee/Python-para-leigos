# ========================================================================
# MÓDULO 23: FUNÇÕES LAMBDA (O "Post-it" das Funções)
# ========================================================================
#
# O que é uma função lambda? É uma função pequena, anônima (sem nome) e de uma linha só.
#
# A Analogia: A Receita Formal vs. O Post-it
# -> Uma função 'def' é como uma RECEITA FORMAL: você dá um nome, escreve
#    os passos e a guarda em um caderno para usar várias vezes.
#
# -> Uma função 'lambda' é como um POST-IT: você escreve uma instrução rápida
#    e anônima para uma tarefa imediata e depois pode "jogar fora".

# --- Exemplo: Dobrar um número ---

# Jeito 1: A Receita Formal (o jeito tradicional com 'def')
def calcular_dobro(numero):
    return numero * 2
print(f"Usando a função 'def': O dobro de 10 é {calcular_dobro(10)}")
print("-" * 55)


# Jeito 2: O Post-it (o jeito com 'lambda')
# A sintaxe é:  lambda <parâmetros>: <a única expressão/ação a ser feita>
# O resultado da expressão é retornado automaticamente, sem precisar de 'return'.
dobro_com_lambda = lambda numero: numero * 2
print(f"Usando a função 'lambda': O dobro de 10 é {dobro_com_lambda(10)}")
print("-" * 55)


# "Ok, mas por que usar lambda se 'def' parece mais claro?"
# Porque o verdadeiro poder do 'Post-it' aparece quando o usamos como
# um argumento rápido para outras funções, como a de ordenar listas.


# --- ONDE O LAMBDA REALMENTE BRILHA: Dando instruções rápidas ---

# Cenário: Temos uma lista de alunos (dicionários) e queremos ordená-la pela NOTA.
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 7.0},
    {"nome": "Bia", "nota": 9.2}
]
print(f"Lista de alunos original: {alunos}")

# O problema: Como a função 'sorted()' vai saber que é para usar a 'nota' como critério?
# A solução: Nós passamos um "Post-it" (lambda) para ela como instrução!

# A 'chave' (key) da ordenação será o resultado da nossa função lambda.
# Leia-se: "Ordene a lista 'alunos', usando como chave de comparação, para cada 'aluno', a sua 'nota'".
alunos_ordenados_por_nota = sorted(alunos, key=lambda aluno: aluno["nota"])

print(f"Lista ordenada pela nota: {alunos_ordenados_por_nota}")


# Viu? Não precisamos criar uma função 'def' inteira só para dar essa instrução rápida
# de ordenação. O lambda foi o "Post-it" perfeito para a tarefa!
# Esse é o principal uso de lambdas: funções pequenas e descartáveis para tarefas imediatas.
# Lembre-se: Lambdas são ótimas para tarefas simples e rápidas, mas se a lógica for complexa,
# é melhor usar uma função 'def' normal para manter o código claro e legível.