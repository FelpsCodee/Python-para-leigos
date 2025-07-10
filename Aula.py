# Python para Leigos: Do Zero ao Avançado

# Bem-vindo ao seu guia de referência de Python! Este documento foi feito para ser um lugar de consulta rápida sempre que você precisar relembrar um conceito, seja ele básico ou avançado.

#  Módulo 1: O Básico do Básico

# O que é Python?

 # Pense no Python como uma linguagem de comunicação entre você e o computador. A vantagem é que o python foi criado para ser fácil de ler e escrever, quase como se estivéssemos lendo uma frase em inglês. É extremamente versátil, usado para tudo, desde scripts simples até inteligência artificial complexa.
 
 
 # O "Olá, Mundo!" é o primeiro programa que todos escrevem. Ele simplesmente mostra uma mensagem na tela.

#Este código imprime a mensagem "Olá, Mundo!" na tela.
print("Olá, Mundo!") # a sintaxe print() é usada para exibir informações na tela. para escrever uma mensagem, você deve colocar o texto entre aspas. As aspas podem ser simples ou duplas, mas devem ser consistentes. e se for numeros ou variaveis, não precisa de aspas.

#VARIAVEIS E TIPOS DE DADOS 

# Variáveis são como caixas onde você pode guardar informações. Você pode nomear essas caixas e colocar diferentes tipos de dados dentro delas, como números, texto ou listas.
# Aqui estão alguns exemplos de variáveis e tipos de dados:
 
# Para textos sempre usaremos aspas, simples ou duplas.
# Para numeros, não usamos aspas.
# Para numeros com virgula(decimal), usamos float.
# Para valor boolean, usamos True ou False.
# Para listas, usamos colchetes [] e podemos colocar varios tipos de dados dentro dela.
# Para dicionarios, usamos chaves {} e podemos colocar varios tipos de dados dentro dela, mas com chaves e valores.
# Para tuplas, usamos parenteses () e podemos colocar varios tipos de dados dentro dela, mas não podemos alterar os valores depois de criadas.

# Exemplo de variáveis
nome = "João"  # String (texto)
idade = 30  # Inteiro (número inteiro)
altura = 1.75  # Float (número com ponto decimal)
ativo = True  # Booleano (verdadeiro ou falso)
lista = [1, 2, 3, "quatro", True]  # Lista (coleção de itens)
dicionario = {"nome": "Maria", "idade": 25}  # Dicionário (pares chave-valor)
tupla = (1, 2, 3)  # Tupla (coleção imutável de itens)

# Para ver o tipo de dado de uma variável, use a função type()
print(type(nome))
print(type(idade))


# Módulo 2: Operadores Matemáticos e Lógicos
# Operadores Matemáticos
# Os operadores matemáticos são usados para realizar cálculos. Aqui estão alguns exemplos:
# Adição
soma = 5 + 3  # Soma
# Subtração
subtracao = 10 - 4  # Subtração
# Multiplicação
multiplicacao = 2 * 3  # Multiplicação
# Divisão
divisao = 10 / 2  # Divisão
# Módulo 2: Operadores Matemáticos e Lógicos
# Exponenciação
exponenciacao = 2 ** 3  # Exponenciação (2 elevado a 3)
# Divisão inteira
divisao_inteira = 10 // 3  # Divisão inteira (resultado sem a parte decimal)
modulo = 10 % 3  # Módulo (resto da divisão)
# Operadores Lógicos
# Os operadores lógicos são usados para combinar condições. Aqui estão alguns exemplos:
# E lógico (and)
condicao1 = True
condicao2 = False
resultado_and = condicao1 and condicao2  # Retorna True se ambas as condições forem verdadeiras
# Ou lógico (or)
resultado_or = condicao1 or condicao2  # Retorna True se pelo menos uma das condições for verdadeira
# Não lógico (not)
resultado_not = not condicao1  # Inverte o valor da condição (True se condicao1 for False, e vice-versa)
# Exemplo de uso de operadores
numero1 = 10
numero2 = 5
soma = numero1 + numero2  # Soma
subtracao = numero1 - numero2  # Subtração
multiplicacao = numero1 * numero2  # Multiplicação
divisao = numero1 / numero2  # Divisão
print("Soma:", soma)


# Módulo 3: Estruturas de Controle
# Estruturas de controle são como sinais de trânsito para o computador. Elas dizem ao computador o que fazer em diferentes situações.
# Condicionais
# As condicionais permitem que o programa tome decisões com base em condições. Por exemplo, se a idade for maior que 18, o usuário é considerado adulto.
# Exemplo de estrutura condicional
idade_usuario = 20
if idade_usuario >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
#Módulo 4: Estruturas de Repetição
# Estruturas de repetição permitem que o programa execute um bloco de código várias vezes. Por exemplo, um loop pode imprimir números de 1 a 5.
# Exemplo de loop for
for i in range(1, 6):  # O range(1, 6) gera números de 1 a 5
    print(i)
# Exemplo de loop while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Incrementa o contador em 1 a cada iteração
# Módulo 5: Funções
# Funções são como pequenas máquinas que realizam uma tarefa específica. Elas podem receber entradas (argumentos) e retornar saídas (resultados).
# Exemplo de função simples
def saudacao(nome): # Define uma função chamada saudacao que recebe um parâmetro nome
    return f"Olá, {nome}!"  # Retorna uma saudação personalizada
# Chamada da função
resultado = saudacao("Maria")  # Chama a função saudacao com o argumento "Maria"
print(resultado)  # Imprime o resultado da função

# Módulo 6: Manipulação de Strings
# Strings são sequências de caracteres, como palavras ou frases. Você pode manipulá-las de várias maneiras, como concatenar (juntar) ou dividir.
# Exemplo de manipulação de strings
texto = "Python é incrível!"
# Concatenar strings
texto2 = " Eu amo programar."
texto_completo = texto + texto2  # Junta as duas strings
print(texto_completo)  # Imprime o texto completo
# Dividir uma string
palavras = texto.split()  # Divide a string em uma lista de palavras
print(palavras)  # Imprime a lista de palavras
# Módulo 7: Manipulação de Listas
# Listas são coleções de itens que podem ser de diferentes tipos. Você pode adicionar, remover ou acessar itens em uma lista.
# Exemplo de manipulação de listas
lista_numeros = [1, 2, 3, 4, 5]
# Adicionar um item à lista
lista_numeros.append(6)  # Adiciona o número 6 ao final da lista
print(lista_numeros)  # Imprime a lista atualizada
# Remover um item da lista
lista_numeros.remove(3)  # Remove o número 3 da lista
print(lista_numeros)  # Imprime a lista atualizada
# Acessar um item da lista
print(lista_numeros[0])  # Imprime o primeiro item da lista (índice 0)
# Módulo 8: Manipulação de Dicionários
# Dicionários são coleções de pares chave-valor. Eles permitem armazenar dados de forma estruturada, onde cada chave é única.
# Exemplo de manipulação de dicionários
dicionario_pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}
# Acessar um valor pelo nome da chave
print(dicionario_pessoa["nome"])  # Imprime o valor associado à chave "nome"
# Adicionar um novo par chave-valor
dicionario_pessoa["profissao"] = "Engenheiro"  # Adiciona a chave "profissao" com o valor "Engenheiro"
print(dicionario_pessoa)  # Imprime o dicionário atualizado
# Remover um par chave-valor
del dicionario_pessoa["idade"]  # Remove a chave "idade" e seu valor associado
print(dicionario_pessoa)  # Imprime o dicionário atualizado
# Módulo 9: Manipulação de Arquivos
# Manipular arquivos é essencial para ler e escrever dados em Python. Você pode abrir, ler
# e escrever arquivos de texto ou binários.
# Exemplo de manipulação de arquivos
# Abrir um arquivo para escrita
with open("exemplo.txt", "w") as arquivo:  # Abre o arquivo exemplo.txt em modo de escrita
    arquivo.write("Olá, mundo!")  # Escreve a string no arquivo
# Abrir um arquivo para leitura
with open("exemplo.txt", "r") as arquivo:  # Abre o arquivo exemplo.txt em modo de leitura
    conteudo = arquivo.read()  # Lê o conteúdo do arquivo
    print(conteudo)  # Imprime o conteúdo lido do arquivo
# Módulo 10: Tratamento de Exceções
# O tratamento de exceções é importante para lidar com erros que podem ocorrer durante a execução do programa. Você pode usar blocos try-except para capturar e tratar erros de forma controlada.
# Exemplo de tratamento de exceções
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Tenta dividir por zero
except ZeroDivisionError:
    # Tratamento da exceção
    print("Erro: Divisão por zero não é permitida.") # Imprime uma mensagem de erro específica
# Módulo 11: Programação Orientada a Objetos (POO)
# A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em objetos, que são instâncias de classes. As classes definem atributos e métodos que os objetos podem ter.
# Exemplo de POO
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}, Ano: {self.ano}")

# Criando um objeto da classe Carro
meu_carro = Carro("Fusca", 1970)
meu_carro.exibir_informacoes()  # Chama o método para exibir informações do carro
# Módulo 12: Bibliotecas e Módulos
# Bibliotecas e módulos são coleções de código reutilizável que você pode importar para o
# seu programa. Eles fornecem funcionalidades adicionais, como manipulação de dados, gráficos e muito mais.
# Exemplo de importação de biblioteca
import math  # Importa a biblioteca math para realizar operações matemáticas avançadas
# Usando uma função da biblioteca math
raiz_quadrada = math.sqrt(16)  # Calcula a raiz quadrada
print(raiz_quadrada)  # Imprime o resultado da raiz quadrada
# Módulo 13: Trabalhando com Dados
# Trabalhar com dados é uma parte importante da programação. Você pode usar bibliotecas como pandas e NumPy para manipular e analisar dados de forma eficiente.
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
# Exemplo de criação de um DataFrame com pandas
dados = {
    "nome": ["João", "Maria", "Pedro"],
    "idade": [28, 34, 23],
    "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}
df = pd.DataFrame(dados)
print(df)
# Módulo 14: Trabalhando com APIs
# APIs (Interfaces de Programação de Aplicações) permitem que você se conecte a serviços externos e obtenha dados ou execute ações. Você pode usar bibliotecas como requests para fazer requisições HTTP.
import requests  # Importa a biblioteca requests para fazer requisições HTTP
# Exemplo de requisição a uma API
response = requests.get("https://api.github.com")  # Faz uma requisição GET para a API do GitHub
if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
    dados_api = response.json()  # Converte a resposta em formato JSON
    print(dados_api)  # Imprime os dados da API

#Aula Bônus: como criar um repsotirio no GitHub e subir o seu projeto e dar commits
# 1. Crie um repositório no GitHub
# - Acesse o GitHub e faça login na sua conta.
# - Clique no botão "New" para criar um novo repositório.
# - Dê um nome ao repositório, adicione uma descrição e escolha se ele será público ou privado.
# - Clique em "Create repository" para criar o repositório.

# 2. Clone o repositório para o seu computador
# - Abra o terminal ou prompt de comando.
# - Navegue até o diretório onde você deseja clonar o repositório.
# - Use o comando `git clone` seguido do URL do repositório. Por exemplo:
# git clone https://github.com/usuario/repo.git # Substitua "usuario" e "repo" pelo seu nome de usuário e nome do repositório.

# 3. Adicione seus arquivos ao repositório
# - Navegue até o diretório do repositório clonado.
# - Copie seus arquivos para esse diretório.
# - Use os comandos `git add` para adicionar os arquivos e `git commit` para salvar as alterações.
# Exemplo de comandos para adicionar e fazer commit
# git add .  # Adiciona todos os arquivos do diretório atual
# git commit -m "Mensagem do commit"  # Faz o commit das alterações com uma mensagem

# 4. Envie as alterações para o GitHub
# - Use o comando `git push` para enviar as alterações para o repositório remoto
# Exemplo de comando para enviar as alterações
# git push origin main  # Envia as alterações para o branch principal (main) do repositório remoto

# 5. Verifique se as alterações foram enviadas
# - Acesse o repositório no GitHub e verifique se os arquivos foram atualizados.

# Parabéns! Você criou um repositório no GitHub, clonou-o para o seu computador, adicionou seus arquivos e enviou as alterações de volta para o GitHub. Agora você pode continuar desenvolvendo seu projeto e fazendo commits regularmente para manter o controle das alterações.
