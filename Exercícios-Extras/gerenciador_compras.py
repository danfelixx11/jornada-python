# 1. Começamos com uma lista vazia. Ela vai guardar nossos dicionários de produtos.
lista_de_compras = []

# 2. O loop 'while True' cria um menu que se repete infinitamente
#    até que a gente decida sair dele (com o comando 'break').
while True:
    print("\n--- GERENCIADOR DE COMPRAS ---")
    print("1: Adicionar item")
    print("2: Ver lista")
    print("3: Remover item")
    print("4: Sair")

    # 3. Pedimos ao usuário para escolher uma opção.
    opcao = input("Escolha uma opção: ")

    # Agora, vamos criar a lógica para cada opção
    if opcao == '1':
        print("Você escolheu Adicionar Item.")
        if opcao == '1':
        # Pedimos o nome e a quantidade do produto
            nome_item = input("Digite o nome do item: ")
            
            # Um pequeno loop para garantir que a quantidade seja um número
            while True:
                try:
                    quantidade_item = int(input(f"Digite a quantidade de {nome_item}: "))
                    break # Sai do loop se a conversão para inteiro der certo
                except ValueError:
                    print("Quantidade inválida. Por favor, digite apenas números.")

            # Criamos o dicionário que representa nosso item
            novo_item = {
                'nome': nome_item,
                'quantidade': quantidade_item
            }

        # Adicionamos o dicionário à nossa lista principal
        lista_de_compras.append(novo_item)
        print(f"'{nome_item}' foi adicionado à lista!")
    elif opcao == '2':
        print("Você escolheu Ver a Lista.")
        print("\n--- SUA LISTA DE COMPRAS ---")
        
        # Primeiro, verificamos se a lista não está vazia
        if not lista_de_compras:
            print("Sua lista está vazia.")
        else:
            # Agora usamos o 'for' para percorrer cada item (que é um dicionário) na lista
            for item in lista_de_compras:
                # Acessamos os valores do dicionário usando as chaves 'nome' e 'quantidade'
                print(f"- {item['nome']}: {item['quantidade']} unidade(s)")
    elif opcao == '3':
        print("Você escolheu Remover Item.")
        print("\n--- REMOVER ITEM ---")
        if not lista_de_compras:
            print("Sua lista já está vazia. Nada para remover.")
        else:
            # Mostramos a lista numerada para o usuário
            for i, item in enumerate(lista_de_compras):
                print(f"{i}: {item['nome']} - {item['quantidade']}")
            
            try:
                indice_para_remover = int(input("Digite o número do item que deseja remover: "))
                
                # Verificamos se o número digitado é válido
                if 0 <= indice_para_remover < len(lista_de_compras):
                    item_removido = lista_de_compras.pop(indice_para_remover)
                    print(f"O item '{item_removido['nome']}' foi removido com sucesso!")
                else:
                    print("Número inválido. Nenhum item foi removido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    elif opcao == '4':
        print("Saindo do programa. Boas compras!")
        break # Este comando quebra o loop 'while True' e encerra o programa.
    else:
        print("Opção inválida! Por favor, escolha um número de 1 a 4.")
