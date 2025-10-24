class Usuario:
    def __init__(self, nome, email, permissao='comum'):
        self.nome = nome
        self.email = email
        self.permissao = permissao

    def editar_permissao(self, nova_permissao):
        self.permissao = nova_permissao

    def __str__(self):
        return f'Usuário: {self.nome}, Email: {self.email}, Permissão: {self.permissao}'

