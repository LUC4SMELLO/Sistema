class Venda:

    lista_de_vendas = []

    def __init__(self, cliente, produtos, quantidade):
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
