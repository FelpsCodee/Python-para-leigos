# ========================================================================
# MÓDULO FINAL: GIT & GITHUB (O Super Sistema de Save de Videogame)
# ========================================================================
#
# Este módulo ensina a usar Git e GitHub, as ferramentas mais importantes
# para salvar e compartilhar seu código de forma profissional.
#
# A Analogia:
# -> Git: É o PROGRAMA DE SAVE que roda no seu PC (sua máquina do tempo pessoal).
# -> GitHub: É o SITE na nuvem onde você guarda uma cópia online dos seus saves.
#
# Siga este passo a passo DENTRO DA PASTA do seu projeto, usando o terminal.

# ------------------------------------------------------------------------
# PASSO 1: `git init` (Começando um Novo "Jogo")
# ------------------------------------------------------------------------
# Este comando é usado apenas UMA VEZ no início de um projeto.
print("git init")
# >> O que faz? Cria uma "pasta de save" oculta (.git) no seu projeto.
#    Sua "máquina do tempo" está oficialmente ligada para esta pasta!


# ------------------------------------------------------------------------
# PASSO 2: `git add .` (Selecionando os Itens para o "Save Point")
# ------------------------------------------------------------------------
# Antes de salvar, você precisa dizer ao Git QUAIS arquivos ou alterações
# você quer incluir neste "save". O ponto "." é um atalho para "tudo nesta pasta".
print("git add .")
# >> O que faz? Prepara todas as suas alterações para serem salvas no próximo passo.
#    (Pense nisso como escolher os itens que entram na foto do seu save).


# ------------------------------------------------------------------------
# PASSO 3: `git commit` (Criando o "Save Point" com uma Mensagem)
# ------------------------------------------------------------------------
# Este é o ato de salvar de verdade. A mensagem é o "nome do seu save".
# Seja sempre claro e descritivo na sua mensagem!
print("git commit -m \"Meu primeiro commit! Criei a estrutura inicial do projeto.\"")
# >> O que faz? Tira uma "foto" (snapshot) do seu projeto e a guarda no
#    seu histórico LOCAL (no seu PC) com a sua mensagem.


# ------------------------------------------------------------------------
# PASSO 4: Conectando com o GitHub (O "Cofre na Nuvem")
# ------------------------------------------------------------------------
# Agora, vamos para a internet para criar o lugar onde seus saves ficarão guardados.
#
# 1. Vá para o site github.com e faça login.
# 2. Clique em "New" (Novo Repositório).
# 3. Dê um nome ao seu repositório (ex: "meu-guia-python").
# 4. Deixe como "Public" para mostrar seu trabalho ao mundo (ótimo para portfólio!).
# 5. >> NÃO << marque nenhuma caixinha (README, .gitignore, license).
# 6. Clique em "Create repository".
# 7. Na próxima página, COPIE a URL do seu repositório. Será algo como:
#    https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
#
# O comando abaixo conecta seu projeto local com o repositório online. SÓ PRECISA FAZER UMA VEZ.
# !! TROQUE A URL DE EXEMPLO PELA SUA URL REAL !!
print("git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git")
# >> O que faz? Cria uma "ponte" chamada 'origin' para o seu cofre na nuvem.


# ------------------------------------------------------------------------
# PASSO 5: `git push` (Enviando seus "Saves" para a Nuvem)
# ------------------------------------------------------------------------
# Finalmente, vamos "empurrar" (push) os saves que você criou no seu PC para o GitHub.
# O comando '-u origin main' é um pouco mais longo na primeira vez para estabelecer a conexão principal.
print("git push -u origin main")
# >> O que faz? Envia todos os seus commits para o GitHub.
#    Recarregue a página do GitHub e seu código estará lá!
#
#    NAS PRÓXIMAS VEZES, depois de fazer 'git add' e 'git commit',
#    você só precisará digitar o comando simples: git push


# --- COMANDOS BÔNUS PARA O DIA A DIA ---
# `git status`: Seu melhor amigo. Mostra o que foi modificado. Use o tempo todo!
# `git pull`: Se outra pessoa (ou você em outro PC) atualizou o código no GitHub,
#             este comando "puxa" (pull) as novidades para o seu PC.
# `git log`: Mostra todo o histórico de "save points" (commits) que você já fez.
# `git clone [URL]`: Baixa um projeto inteiro de outra pessoa do GitHub para o seu computador.