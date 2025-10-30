class Compromisso:
    def __init__(self, data, descricao, tipo, status='pendente'):
        self.data = data
        self.descricao = descricao
        self.tipo = tipo
        self.status = status

    def editar(self, nova_data=None, nova_descricao=None, novo_status=None):
        if nova_data:
            self.data = nova_data
        if nova_descricao:
            self.descricao = nova_descricao
        if novo_status:
            self.status = novo_status

    def __str__(self):
        return f'{self.tipo} em {self.data}: {self.descricao} - Status: {self.status}'
