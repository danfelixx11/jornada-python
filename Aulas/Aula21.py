# Docstrings
def soma(a, b):
    """
    Função que retorna a soma de a e b.
    :param a: primeiro valor
    :param b: segundo valor
    :return: soma de a + b
    """
    return a + b

# Parâmetros opcionais

def saudacao(nome="usuário"):
    print(f"Olá, {nome}!")


# Se chamar saudacao("Maria"), imprime “Olá, Maria!”
# Se chamar apenas saudacao(), usa o valor padrão e imprime “Olá, usuário!”
# Outro exemplo mais prático

def exponencial(base, expoente=2):
    return base ** expoente

# exponencial(3) retorna 3 ** 2 = 9
# exponencial(2, 3) retorna 2 ** 3 = 8
# esse recurso dá mais flexibilidade às funções.

# Escopo de variáveis: local e global

# Variáveis definidas dentro de uma função são locais e só existem dentro dessa função.

# Variáveis definidas fora (no escopo global) são acessíveis “lá fora” mas não “dentro” de uma função para alterações diretas (a menos que se use global).

#Exemplo:

x = 10  # variável global

def func():
    y = 5  # local
    print(x)  # consegue ler global


