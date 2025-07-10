# ===================================================================
# MÓDULO 21: TRABALHANDO COM APIS (O Garçom da Internet)
# ===================================================================
#
# O que é uma API? Pense nela como um GARÇOM ou um ATENDENTE DE DELIVERY.
#
# Seu programa (o cliente) não pode simplesmente entrar na "cozinha" de outro
# site (como o GitHub, Twitter ou um app de previsão do tempo) para pegar dados.
# Em vez disso, você chama o "garçom" (a API) e faz um PEDIDO (em inglês, "request").
# O garçom vai até a cozinha e te traz uma RESPOSTA (em inglês, "response").

# --- 1. Contratando o "Garçom" (A biblioteca `requests`) ---
# A biblioteca 'requests' é a ferramenta mais popular em Python para atuar como nosso garçom.
# Se você não a tiver, abra o terminal e digite: pip install requests
import requests

# --- 2. Escolhendo o Prato e Fazendo o Pedido (O `GET` request) ---
# O "endereço" (URL) é como o item que escolhemos do cardápio da API.
# Vamos pedir as informações públicas do próprio GitHub.
url = "https://api.github.com"

print(f"--- Fazendo um pedido para o garçom no endereço: {url} ---")
# 'requests.get(url)' é o ato de chamar o garçom e fazer o pedido.
resposta = requests.get(url)


# --- 3. Verificando a Resposta do Garçom (O `status_code`) ---
# Antes de "comer", verificamos se o garçom trouxe o prato certo.
# Código 200 significa "OK, seu pedido foi um sucesso e aqui está!".
# (Um código famoso que indica erro é o 404, que significa "Prato não encontrado").
print(f"O garçom respondeu com o código de status: {resposta.status_code}")

if resposta.status_code == 200:
    print("Sucesso! O pedido veio correto. Hora de ver os dados!")
    
    # --- 4. Abrindo o "Prato" (O método `.json()`) ---
    # Os dados vêm "embrulhados" em um formato de texto para web chamado JSON.
    # O método .json() é a mágica que transforma esse texto em um DICIONÁRIO Python,
    # que nós já sabemos como usar!
    dados_da_api = resposta.json()
    
    # --- 5. Usando os Dados ---
    # Agora que os dados são um dicionário, podemos acessar as informações com as chaves.
    # Vamos pegar o link que a própria API nos diz onde encontrar informações sobre usuários.
    url_dos_usuarios = dados_da_api['current_user_url']
    
    print("-" * 55)
    print("A API do GitHub nos informou que a URL para pesquisar usuários é:")
    print(url_dos_usuarios)
    print("\nIsso mostra como uma API pode guiar a outra!")
    
else:
    # Se o código não for 200, algo deu errado com nosso pedido.
    print("Opa! Algo deu errado. O garçom não conseguiu trazer nosso pedido.")
    print(f"Motivo (Status Code): {resposta.status_code}")