import json
from usuario import Usuario
from compromisso import Compromisso
from agenda import Agenda

def exibir_menu():
    print("\n1. Adicionar compromisso")
    print("2. Listar compromissos")
    print("3. Buscar compromisso")
    print("4. Excluir compromisso")
    print("5. Sair")

def salvar_dados(agenda, usuario):
    with open('dados.json', 'w') as f:
        dados = {
            'usuario': {
                'nome': usuario.nome,
                'email': usuario.email,
                'permissao': usuario.permissao
            },
            'compromissos': [{'data': c.data, 'descricao': c.descricao, 'tipo': c.tipo, 'status': c.status} for c in agenda.compromissos]
        }
        json.dump(dados, f, indent=4)

def carregar_dados():
    try:
        with open('dados.json', 'r') as f:
            dados = json.load(f)
            usuario = Usuario(dados['usuario']['nome'], dados['usuario']['email'], dados['usuario']['permissao'])
            agenda = Agenda()
            for c in dados['compromissos']:
                compromisso = Compromisso(c['data'], c['descricao'], c['tipo'], c['status'])
                agenda.adicionar_compromisso(compromisso)
            return agenda, usuario
    except FileNotFoundError:
        return Agenda(), Usuario('Novo Usuário', 'email@dominio.com')

def main():
    agenda, usuario = carregar_dados()
    print(f"Bem-vindo, {usuario.nome}!")

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            descricao = input("Descrição do compromisso: ")
            tipo = input("Tipo de compromisso (reunião, evento, tarefa): ")
            data = input("Data do compromisso (dd/mm/yyyy): ")
            compromisso = Compromisso(data, descricao, tipo)
            agenda.adicionar_compromisso(compromisso)
        
        elif escolha == "2":
            agenda.listar_compromissos()
        
        elif escolha == "3":
            descricao = input("Digite a descrição do compromisso: ")
            compromisso = agenda.buscar_compromisso(descricao)
            if compromisso:
                print(compromisso)
            else:
                print("Compromisso não encontrado.")
        
        elif escolha == "4":
            descricao = input("Digite a descrição do compromisso a ser excluído: ")
            agenda.excluir_compromisso(descricao)
        
        elif escolha == "5":
            print("Saindo...")
            salvar_dados(agenda, usuario)
            break

if __name__ == "__main__":
    main()

