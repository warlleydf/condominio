from models import Encomenda

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Registrar Encomenda")
        print("2. Dar Baixa na Encomenda")
        print("3. Listar Encomendas")
        print("4. Listar Encomendas Baixadas")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_encomenda()
        elif opcao == '2':
            listar_encomendas()
            dar_baixa_encomenda()
        elif opcao == '3':
            listar_encomendas()
        elif opcao == '4':
            listar_encomendas_entregues()

        elif opcao == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")

def registrar_encomenda():
    unidade = input("Digite a unidade de destino da encomenda: ")
    descricao = input("Digite a descrição da encomenda: ")
    porteiro = input("Digite o nome do porteiro que recebeu a encomenda: ")    
    data_recebimento = input("Digite a data de recebimento (AAAA-MM-DD): ")
    Encomenda.registrar_encomenda(unidade, descricao, porteiro, data_recebimento)
    print("Encomenda registrada com sucesso.")

def listar_encomendas():
    encomendas = Encomenda.listar_encomendas()
    if encomendas:
        for encomenda in encomendas:
            print(f"ID: {encomenda[0]}, Unidade: {encomenda[1]}, Descrição: {encomenda[2]}, Porteiro: {encomenda[3]}, Recebida em: {encomenda[4]}")
    else:
        print("Nenhuma encomenda pendente.")

def dar_baixa_encomenda():
    id_encomenda = int(input("Digite o ID da encomenda para dar baixa: "))
    if Encomenda.encomenda_existe(id_encomenda):
         if Encomenda.encomenda_existe_entrega(id_encomenda):
           print("Encomenda não disponivel para baixa.")            
         else: 
              Encomenda.dar_baixa_encomenda(id_encomenda)
              print(f"Encomenda {id_encomenda} marcada como entregue.")              
    else:
        print("Encomenda não encontrada.")
    
def listar_encomendas_entregues():
    encomendas = Encomenda.listar_encomendas_entregues()
    if encomendas:
        for encomenda in encomendas:
            print(f"ID: {encomenda[0]}, Unidade: {encomenda[1]}, Descrição: {encomenda[2]}, Porteiro: {encomenda[3]}, Entregue em: {encomenda[5]}")
    else:
        print("Nenhuma encomenda entregue.")