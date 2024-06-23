from database import criar_tabelas
from views import menu_principal

if __name__ == '__main__':
    criar_tabelas()
    print("Bem-vindo ao Sistema de Gestão de Encomendas")
    menu_principal()