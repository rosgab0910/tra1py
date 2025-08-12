# Gerenciador de Tarefas

## Descrição
O Gerenciador de Tarefas é um programa interativo que permite ao usuário adicionar, visualizar e remover tarefas de uma lista. É uma ferramenta simples para ajudar na organização de atividades diárias.

## Como usar
1. Certifique-se de ter o Python instalado em seu sistema.
2. Salve o código acima em um arquivo chamado `gerenciador_tarefas.py`.
3. Abra o terminal e navegue até o diretório onde o arquivo está salvo.
4. Execute o programa com o comando: python gerenciador_tarefas.py
5. Siga as instruções exibidas no terminal para gerenciar suas tarefas.

## Estruturas utilizadas

- **Loop `while`**: O programa utiliza um loop `while` para permitir que o usuário interaja com o menu até que decida sair. Isso garante que o programa tenha um início, meio e fim definidos.

- **Estruturas de controle de fluxo**:
- **`break`**: Usado para sair do loop quando o usuário escolhe a opção de sair (opção 4).
- **`continue`**: Usado para reiniciar o loop quando o usuário tenta adicionar uma tarefa vazia, evitando que uma tarefa em branco seja adicionada à lista.

- **Validação de entradas**:
- O programa valida se a entrada da tarefa não está vazia. Se o usuário tentar adicionar uma tarefa vazia, uma mensagem de erro é exibida e o loop continua.
- Ao remover uma tarefa, o programa verifica se o índice fornecido pelo usuário é válido, garantindo que não ocorra um erro de índice fora do intervalo.

- **Condicionais (`if`, `elif`, `else`)**: Utilizadas para controlar o fluxo do programa, permitindo que diferentes ações sejam executadas com base na opção escolhida pelo usuário.

Este programa é uma maneira prática de gerenciar tarefas e pode ser expandido com mais funcionalidades, como salvar tarefas em um arquivo ou adicionar prazos.