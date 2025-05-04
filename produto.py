class Produto:

    lista_de_produtos = []

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

        Produto.lista_de_produtos.append(
            {"nome": self.nome, "preco": self.preco, "estoque": self.estoque}
        )

    def atualizar_estoque(self, quantidade):
        self.estoque = quantidade
