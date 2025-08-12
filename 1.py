def mostrar_tarefas(tarefas):
    # Função para exibir a lista de tarefas
    if not tarefas:  # Verifica se a lista de tarefas está vazia
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        # Itera sobre a lista de tarefas e imprime cada uma com seu índice
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def main():
    tarefas = []  # Inicializa uma lista vazia para armazenar as tarefas
    
    # Executa o laço de repetição infinitamente
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        # Solicita ao usuário que escolha uma opção
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':  # Se o usuário escolher adicionar uma tarefa
            tarefa = input("Digite a tarefa: ").strip()  # Solicita a tarefa e remove espaços em branco
            if not tarefa:  # Verifica se a tarefa está vazia
                print("A tarefa não pode ser vazia. Tente novamente.")
                continue  # Reinicia o loop se a tarefa for vazia
            tarefas.append(tarefa)  # Adiciona a tarefa à lista
            print("Tarefa adicionada com sucesso!")
        
        elif opcao == '2':  # Se o usuário escolher visualizar as tarefas
            mostrar_tarefas(tarefas)  # Chama a função para mostrar as tarefas
        
        elif opcao == '3':  # Se o usuário escolher remover uma tarefa
            mostrar_tarefas(tarefas)  # Mostra as tarefas antes de remover
            if tarefas:  # Verifica se há tarefas na lista
                try:
                    # Solicita o índice da tarefa a ser removida e converte para inteiro
                    indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                    # Verifica se o índice está dentro do intervalo válido
                    if 0 <= indice < len(tarefas):
                        tarefas.pop(indice)  # Remove a tarefa da lista
                        print("Tarefa removida com sucesso!")
                    else:
                        print("Índice inválido. Tente novamente.")
                except ValueError:  # Captura erro se a entrada não for um número
                    print("Por favor, digite um número válido.")
        
        elif opcao == '4':  # Se o usuário escolher sair
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break  # Sai do loop e encerra o programa
        
        else:  # Se a opção escolhida não for válida
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
