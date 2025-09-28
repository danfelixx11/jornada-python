while True:
    numeros = []
    for i in range(3):
        num = int(input("Número " + str(i+1) + ": "))
        numeros.append(num)
    soma = sum(numeros)
    media = soma / len(numeros)
    print(f"A soma é {soma} e a média é {media}")
    #assert soma == 12  # Se soma não for 12 (ex.: [2,4,6]), dá erro
    if input("Continuar? (s/n): ").lower() !='s':
        break

