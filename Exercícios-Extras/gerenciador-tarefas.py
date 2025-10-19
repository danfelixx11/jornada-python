tarefas = []

proximo_id = 1

def mostrar_menu():
    print('-=' * 20)
    print('\n --- GERNCIADOR DE TAREFAS ---')
    print('1. Adicionar Tarefas')
    print('2. Listar Tarefas')
    print('3. Marcar Tarefa como Concluída')
    print('4. Remover Tarefa')
    print('5. Sair')
    print('-=' * 20)
    return input('Escolha uma opção (1-5): ')

def listar_tarefas():
    print("\n--- LISTA DE TAREFAS ---")

    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return
    
    for tarefa in tarefas:
        status = "Concluída" if tarefa['status'] == 'concluida' else "Pendente"
        print(f'[{tarefa['id']}] {tarefa['descricao']} ({status})')

def adicionar_tarefa():
    global proximo_id

    descricao = input('Digite a descrição da nova tarefa: ')

    nova_tarefa = {
        'id': proximo_id,
        'descricao': descricao,
        'status': 'pendente'
    }

    tarefas.append(nova_tarefa)

    proximo_id += 1

    print(f"Tarefa '{descricao}' adicionada com sucesso! (ID: {nova_tarefa['id']})")

def atualizar_status():
    """Muda o status de uma tarefa para 'concluida'."""
    listar_tarefas() # Mostra a lista primeiro
    
    if not tarefas: # Se não houver tarefas, não faz nada
        return

    try:
        id_tarefa = int(input("Digite o ID da tarefa para marcar como concluída: "))
    except ValueError:
        print("Erro: Você deve digitar um número.")
        return

    tarefa_encontrada = False
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa['status'] = 'concluida'
            tarefa_encontrada = True
            print(f"Tarefa '{tarefa['descricao']}' marcada como concluída!")
            break # Para o loop assim que encontrar a tarefa
            
    if not tarefa_encontrada:
        print(f"Erro: Tarefa com ID {id_tarefa} não encontrada.")

def remover_tarefa():
    """Remove uma tarefa da lista."""
    listar_tarefas() # Mostra a lista
    
    if not tarefas: # Se não houver tarefas, não faz nada
        return

    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja REMOVER: "))
    except ValueError:
        print("Erro: Você deve digitar um número.")
        return

    tarefa_para_remover = None
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa_para_remover = tarefa
            break
            
    if tarefa_para_remover:
        tarefas.remove(tarefa_para_remover)
        print(f"Tarefa '{tarefa_para_remover['descricao']}' removida com sucesso!")
    else:
        print(f"Erro: Tarefa com ID {id_tarefa} não encontrada.")

def main():
    while True:
        opcao = mostrar_menu()

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            atualizar_status()
        elif opcao == '4':
            remover_tarefa()
        elif opcao == '5':
            print("Até logo! Encerrando o programa.")
            break
        else:
            print('Opção inválida! Por favor, escolha um número de 1 a 5.')

if __name__ == "__main__":
    main()