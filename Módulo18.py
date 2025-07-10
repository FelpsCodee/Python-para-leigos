# ========================================================================
# MÓDULO 18: PROGRAMAÇÃO ORIENTADA A OBJETOS (A Fábrica de Heróis)
# ========================================================================
#
# Esqueça tudo por um instante e imagine uma FÁBRICA para criar heróis de um jogo.
#
# 1. A CLASSE (A Planta da Fábrica):
#    É o "molde", a "planta baixa", o "formulário de criação".
#    A classe `Heroi` vai definir QUAIS INFORMAÇÕES todo herói deve ter (nome, hp, etc.)
#    e QUAIS AÇÕES todo herói pode fazer (atacar, ganhar xp, etc.).
#
# 2. O OBJETO (O Herói Criado):
#    É o produto final que sai da fábrica. Cada herói (Aragorn, Legolas) é um
#    objeto único, criado a partir do mesmo molde (a classe `Heroi`).
#    Eles têm as mesmas características, mas com valores diferentes.

# ------------------------------------------------------------------------
# A PLANTA DA FÁBRICA: Definindo a classe `Heroi`
# ------------------------------------------------------------------------
class Heroi:
    # --- O RITUAL DE CRIAÇÃO (O Construtor: __init__) ---
    # Este método especial com dois "_" é o CONSTRUTOR. Ele é chamado
    # AUTOMATICAMENTE no momento exato em que um novo herói é criado.
    # Sua missão é definir os atributos iniciais do nosso herói.
    #
    # >> O MISTÉRIO DO 'self' <<
    # 'self' é a palavra mais importante aqui. É como o herói se refere a SI MESMO.
    # Pense no 'self' como o herói falando "eu" ou "meu".
    def __init__(self, nome_inicial, classe_inicial):
        print(f"-> A FÁBRICA está criando um novo herói chamado {nome_inicial}...")
        # "O MEU nome será o nome_inicial que você me deu."
        self.nome = nome_inicial
        # "A MINHA classe será a classe_inicial que você me deu."
        self.classe = classe_inicial
        # "Todo herói começa no nível 1 e com 100 de vida (HP)."
        self.nivel = 1
        self.hp = 100

    # --- AS AÇÕES (Os Métodos) ---
    # Métodos são as FUNÇÕES que pertencem à classe. São as ações que o herói pode fazer.
    # Note que eles também usam 'self' para acessar seus próprios atributos.
    def atacar(self):
        # Para atacar, o herói precisa saber o SEU PRÓPRIO nome. Ele o acessa com 'self.nome'.
        print(f"{self.nome} ({self.classe}) avança e ataca com sua arma!")

    def ganhar_xp(self, quantidade_xp):
        print(f"{self.nome} ganhou {quantidade_xp} pontos de experiência!")
        # A lógica para subir de nível poderia ser adicionada aqui.
        # Por exemplo: if self.xp > 1000: self.nivel += 1

    def exibir_status(self):
        print(f"--- STATUS DE {self.nome} ---")
        print(f"   Classe: {self.classe}")
        print(f"   Nível: {self.nivel}")
        print(f"   HP: {self.hp}")
        print("------------------------")

# ========================================================================
# A FÁBRICA EM AÇÃO: Criando e Usando nossos Heróis (os Objetos)
# ========================================================================

print("\n--- A produção de heróis vai começar! ---\n")

# Criando nosso primeiro herói. Estamos usando o molde (a classe Heroi)
# para criar um OBJETO. O método __init__ é chamado automaticamente aqui.
heroi_1 = Heroi("Aragorn", "Guerreiro")

# Criando um segundo herói. É um objeto COMPLETAMENTE INDEPENDENTE do primeiro.
heroi_2 = Heroi("Legolas", "Arqueiro")

print("\n--- Heróis criados com sucesso! Hora de interagir com eles. ---\n")

# Usando as ações (métodos) de cada herói
heroi_1.atacar()
heroi_2.atacar()

print("-" * 25)

# Exibindo os status individuais
heroi_1.exibir_status()
heroi_2.exibir_status()

# Vamos modificar um atributo de APENAS UM herói.
# Legolas caiu numa armadilha e perdeu vida.
print(f"\nLegolas sofreu 20 de dano!")
heroi_2.hp = 80 # Modificamos o atributo diretamente

# Note que o status de Aragorn continua o mesmo, pois eles são objetos separados.
print("Verificando status após o dano:")
heroi_1.exibir_status() # O HP de Aragorn continua 100.
heroi_2.exibir_status() # O HP de Legolas agora é 80.

# A POO nos ajuda a criar "componentes" organizados (nossos heróis),
# onde os dados (atributos) e as ações (métodos) estão juntos no mesmo lugar,
# tornando o código muito mais limpo e fácil de gerenciar em projetos grandes.
