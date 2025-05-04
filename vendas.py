class Venda:

    lista_de_vendas = []
    id_venda = 1

    def __init__(self, cliente, produtos, quantidade):
        self.id_venda = Venda.id_venda
        Venda.id_venda += 1

        self.cliente = cliente
        self.produtos = produtos
        self.quantidade = quantidade

        Venda.lista_de_vendas.append(
            {
                "cliente": self.cliente,
                "produtos": self.produtos,
                "quantidade": self.quantidade,
            }
        )

    def __str__(self):
        return f"ID_VENDA: {self.id_venda}\nCLIENTE: {str.upper(self.cliente)}\nPRODUTOS: {str.upper(self.produtos)}\nQUANTIDADE: {self.quantidade}"
