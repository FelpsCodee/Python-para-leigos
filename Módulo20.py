# ===================================================================
# MÓDULO 20: PANDAS (A Super Tabela de Excel do Python)
# ===================================================================
#
# Pense na biblioteca 'pandas' como uma forma de ter uma SUPER TABELA DE EXCEL
# diretamente dentro do seu código Python. A principal ferramenta do pandas
# é o "DataFrame", que é essa super tabela.
#
# Com ela, podemos organizar, filtrar, calcular e manipular dados de forma muito poderosa.

# --- 1. Importando o "Excel" para o Python ---
# 'import pandas as pd' -> "Python, por favor, importe a caixa de ferramentas 'pandas',
# e para facilitar, vamos chamá-la pelo apelido (alias) 'pd'." Este é um apelido universal!
import pandas as pd

# --- 2. Nossos dados iniciais (O rascunho em um dicionário) ---
# Geralmente, os dados vêm de um arquivo (como um .csv ou Excel), mas podemos
# começar com um dicionário para entender o conceito.
dados_iniciais = {
    "Nome": ["João Silva", "Maria Garcia", "Pedro Martins", "Ana Costa"],
    "Idade": [28, 34, 22, 45],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "São Paulo"]
}
print("--- Dados iniciais em formato de dicionário Python ---")
print(dados_iniciais)
print("-" * 55)


# --- 3. Criando a "Super Tabela" (o DataFrame) ---
# Usamos o comando do pandas para transformar nosso dicionário em um DataFrame.
# Note como ele organiza tudo em colunas e linhas numeradas (o índice).
df = pd.DataFrame(dados_iniciais)

print("--- Nossos dados organizados em uma Super Tabela (DataFrame)! ---")
print(df)
print("-" * 55)


# --- 4. O Poder do Pandas: Explorando e Manipulando a Tabela ---
# Agora que temos um DataFrame, podemos fazer "mágicas" de Excel com poucas linhas de código.

# a) Ver apenas uma coluna (como clicar no cabeçalho "Idade" no Excel)
print("--- Vendo apenas a coluna 'Idade': ---")
print(df["Idade"])
print("-" * 55)

# b) Filtrar a tabela (como usar o "Filtro" do Excel)
# Quero ver apenas as pessoas com mais de 30 anos.
print("--- Filtrando para ver apenas quem tem mais de 30 anos: ---")
pessoas_mais_de_30 = df[df["Idade"] > 30]
print(pessoas_mais_de_30)
print("-" * 55)

# c) Criar uma nova coluna (como criar uma coluna com fórmula no Excel)
# Vamos criar uma coluna que diz se a pessoa pode se aposentar (vamos supor > 40 anos).
print("--- Criando uma nova coluna 'Pode_Aposentar': ---")
df["Pode_Aposentar"] = df["Idade"] > 40
print(df)
print("-" * 55)

# d) Fazer cálculos simples (como usar a função MÉDIA no Excel)
media_de_idade = df["Idade"].mean()
print(f"A média de idade da tabela é: {media_de_idade:.1f} anos.")

# Pandas é uma ferramenta gigante para análise de dados, capaz de ler arquivos
# de Excel, conectar a bancos de dados e muito mais, transformando tarefas
# que levariam horas em poucas linhas de código!
