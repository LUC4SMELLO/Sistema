class Produto:

    lista_de_produtos = []

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade = estoque

        Produto.lista_de_produtos.append(
            {"nome": self.nome, "preco": self.preco, "quantidade": self.quantidade}
        )

    def atualizar_estoque(self, quantidade):
        self.estoque = quantidade
        