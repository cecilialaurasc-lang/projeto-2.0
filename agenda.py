from compromisso import Compromisso

class Agenda:
    def __init__(self):
        self.compromissos = []

    def adicionar_compromisso(self, compromisso):
        self.compromissos.append(compromisso)

    def listar_compromissos(self):
        if not self.compromissos:
            print("Nenhum compromisso agendado.")
            return
        for compromisso in self.compromissos:
            print(compromisso)

    def buscar_compromisso(self, descricao):
        for compromisso in self.compromissos:
            if descricao.lower() in compromisso.descricao.lower():
                return compromisso
        return None

    def excluir_compromisso(self, descricao):
        compromisso_a_excluir = self.buscar_compromisso(descricao)
        if compromisso_a_excluir:
            self.compromissos.remove(compromisso_a_excluir)
            print(f"Compromisso '{descricao}' excluído com sucesso.")
        else:
            print("Compromisso não encontrado.")
