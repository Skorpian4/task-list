import os

os.system('cls')
lista_tarefas = [] #serve para guardar as tarefas

def mostrar_tarefas():
    if not lista_tarefas:
        os.system('cls') 
        print('Não existe nenhuma tarefa ativa.')
    else:
        os.system('cls') 
        print('Lista Tarefas:')
        for i, tarefa in enumerate(lista_tarefas, 1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa():
    os.system('cls') 
    tarefa = input('Digite a nova tarefa: ')
    lista_tarefas.append(tarefa)
    os.system('cls')
    print('Tarefa feita com sucesso')

def remover_tarefa():
   os.system('cls') 
   mostrar_tarefas()
   if lista_tarefas:
        numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
        
        if 1 <= numero_tarefa <= len(lista_tarefas):
            os.system('cls')
            tarefa_removida = lista_tarefas.pop(numero_tarefa - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            os.system('cls')
            print("Número de tarefa inválido. Tente novamente.")

def alterar_tarefa():
    os.system('cls') 
    mostrar_tarefas()
    if lista_tarefas:
        numero_tarefa = int(input("Digite o número da tarefa que deseja atualizar o nome: "))
        if 1 <= numero_tarefa <= len(lista_tarefas):
            os.system('cls')
            novo_nome = str(input('Indique o novo nome que deseja: '))
            lista_tarefas[numero_tarefa] = novo_nome    
            print(f"Tarefa '{novo_nome}' com novo nome!")
        else:
            os.system('cls')
            print("Número de tarefa inválido. Tente novamente.")
            
while True:
    print('Opções: ')
    print('1. Mostrar Tarefas')
    print('2. Adicionar Tarefa')
    print('3. Remover Tarefa')
    print('4. Alterar nome de tarefa')
    print('0. Sair')

    e = input("Escolha uma opção (0-4): ")

    if e == "1":
        mostrar_tarefas()
    elif e == "2":
        adicionar_tarefa()
    elif e == "3":
        remover_tarefa()
    elif e == "4":
        alterar_tarefa()
    elif e == "0":
        print("Saindo do programa. Adeus!")
        break
    else:
        print("Opção inválida. Tente novamente.")