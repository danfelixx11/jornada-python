def dobro(num=0, is_formatted=False):
    resultado = num * 2
    return moeda(resultado) if is_formatted else resultado


def metade(num=0, is_formatted=False):
    resultado = num / 2
    return moeda(resultado) if is_formatted else resultado


def aumentar(num=0, taxa=0, is_formatted=False):
    resultado = num + (taxa * num / 100)
    return moeda(resultado) if is_formatted else resultado


def diminuir(num=0, taxa=0, is_formatted=False):
    resultado = num - (taxa * num / 100)
    return moeda(resultado) if is_formatted else resultado


def moeda(num=0, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")


def resumo(num=0, aumento=0, diminuicao=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    resultado = f"""
Preço analisado: \t{moeda(num)}
Dobro do preço: \t{dobro(num, True)}
Metade do preço: \t{metade(num, True)}
{aumento}% de aumento: \t{aumentar(num, aumento, True)}
{diminuicao}% de redução: \t{diminuir(num, diminuicao, True)}
    """
    return resultado