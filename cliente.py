class Cliente:

    lista_de_clientes = []

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

        Cliente.lista_de_clientes.append(
            {"nome": self.nome, "cpf": self.cpf, "email": self.email}
        )

    def __str__(self):
        return f"NOME: {str.upper(self.nome)}\nE-MAIL: {self.email}"