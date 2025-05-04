class Cliente:

    lista_clientes = []

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

        Cliente.lista_clientes.append(
            {"nome": self.nome, "cpf": self.cpf, "email": self.email}
        )
