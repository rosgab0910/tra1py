def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def main():
    tarefas = []
    
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            tarefa = input("Digite a tarefa: ").strip()
            if not tarefa:
                print("A tarefa não pode ser vazia. Tente novamente.")
                continue
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
        
        elif opcao == '2':
            mostrar_tarefas(tarefas)
        
        elif opcao == '3':
            mostrar_tarefas(tarefas)
            if tarefas:
                try:
                    indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                    if 0 <= indice < len(tarefas):
                        tarefas.pop(indice)
                        print("Tarefa removida com sucesso!")
                    else:
                        print("Índice inválido. Tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
        
        elif opcao == '4':
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
