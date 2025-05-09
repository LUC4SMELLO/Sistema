class Produto:

    lista_de_produtos = []
    id_produto = 1

    def __init__(self, nome, preco, estoque):
        self.id_produto = Produto.id_produto
        Produto.id_produto += 1

        self.nome = nome
        self.preco = preco
        self.estoque = estoque

        Produto.lista_de_produtos.append(
            {"id_produto": self.id_produto, "nome": self.nome, "preco": self.preco, "estoque": self.estoque}
        )

    def atualizar_estoque(self, quantidade):
        self.estoque = quantidade

    @staticmethod
    def exibir_lista_de_produtos():
        for produto in Produto.lista_de_produtos:
            print(f"ID_PRODUTO: {produto['id_produto']} NOME: {str.upper(produto['nome'].ljust(15))} PREÇO: {produto['preco']} ESTOQUE: {produto['estoque']}")
