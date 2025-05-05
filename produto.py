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

    @staticmethod
    def exibir_lista_de_produtos():
        for produto in Produto.lista_de_produtos:
            print(f"NOME: {str.upper(produto['nome'].ljust(15))} PREÇO: {produto['preco'].ljust(10)} ESTOQUE: {produto['estoque']}")
