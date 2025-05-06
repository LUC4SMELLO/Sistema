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

    @staticmethod
    def exibir_lista_de_clientes():
        for cliente in Cliente.lista_de_clientes:
            print(f"NOME: {str.upper(cliente['nome'].ljust(25))} CPF: {cliente['cpf'].ljust(15)} E-MAIL: {cliente['email']}")


# CLIENTES FAKES PARA TESTES

cliente1 = Cliente("Lucas", "111.222.333-44", "lucas@gmail.com")
cliente2 = Cliente("Mariana", "222.333.444-55", "mariana@gmail.com")
cliente3 = Cliente("João", "333.444.555-66", "joao@gmail.com")
cliente4 = Cliente("Ana", "444.555.666-77", "ana@gmail.com")
cliente5 = Cliente("Pedro", "555.666.777-88", "pedro@gmail.com")
cliente6 = Cliente("Beatriz", "666.777.888-99", "beatriz@gmail.com")
cliente7 = Cliente("Carlos", "777.888.999-00", "carlos@gmail.com")
cliente8 = Cliente("Fernanda", "888.999.000-11", "fernanda@gmail.com")
cliente9 = Cliente("Rafael", "999.000.111-22", "rafael@gmail.com")
cliente10 = Cliente("Juliana", "000.111.222-33", "juliana@gmail.com")
cliente11 = Cliente("Mateus", "123.456.789-00", "mateus@gmail.com")
cliente12 = Cliente("Larissa", "234.567.890-11", "larissa@gmail.com")
cliente13 = Cliente("Gustavo", "345.678.901-22", "gustavo@gmail.com")
cliente14 = Cliente("Camila", "456.789.012-33", "camila@gmail.com")
cliente15 = Cliente("Thiago", "567.890.123-44", "thiago@gmail.com")
cliente16 = Cliente("Bruna", "678.901.234-55", "bruna@gmail.com")
cliente17 = Cliente("André", "789.012.345-66", "andre@gmail.com")
cliente18 = Cliente("Isabela", "890.123.456-77", "isabela@gmail.com")
cliente19 = Cliente("Eduardo", "901.234.567-88", "eduardo@gmail.com")
cliente20 = Cliente("Aline", "012.345.678-99", "aline@gmail.com")
cliente21 = Cliente("Henrique", "101.112.131-41", "henrique@gmail.com")
cliente22 = Cliente("Tatiane", "121.314.151-61", "tatiane@gmail.com")
cliente23 = Cliente("Leandro", "141.516.171-81", "leandro@gmail.com")
cliente24 = Cliente("Paula", "161.718.191-01", "paula@gmail.com")
cliente25 = Cliente("Vinícius", "181.920.212-21", "vinicius@gmail.com")
cliente26 = Cliente("Débora", "202.122.232-41", "debora@gmail.com")
cliente27 = Cliente("Ricardo", "222.324.252-61", "ricardo@gmail.com")
cliente28 = Cliente("Luana", "242.526.272-81", "luana@gmail.com")
cliente29 = Cliente("Felipe", "262.728.292-01", "felipe@gmail.com")
cliente30 = Cliente("Sandra", "282.930.313-21", "sandra@gmail.com")
cliente31 = Cliente("Roberto", "303.132.333-41", "roberto@gmail.com")
cliente32 = Cliente("Patrícia", "323.334.353-61", "patricia@gmail.com")
cliente33 = Cliente("Bruno", "343.536.373-81", "bruno@gmail.com")
cliente34 = Cliente("Luciana", "363.738.393-01", "luciana@gmail.com")
cliente35 = Cliente("Daniel", "383.940.414-21", "daniel@gmail.com")
cliente36 = Cliente("Vanessa", "404.142.434-41", "vanessa@gmail.com")
cliente37 = Cliente("Diego", "424.344.454-61", "diego@gmail.com")
cliente38 = Cliente("Mônica", "444.546.474-81", "monica@gmail.com")
cliente39 = Cliente("Marcelo", "464.748.494-01", "marcelo@gmail.com")
cliente40 = Cliente("Simone", "484.950.515-21", "simone@gmail.com")
cliente41 = Cliente("Alex", "505.152.535-41", "alex@gmail.com")
cliente42 = Cliente("Carla", "525.354.555-61", "carla@gmail.com")
cliente43 = Cliente("Renato", "545.556.575-81", "renato@gmail.com")
cliente44 = Cliente("Cintia", "565.758.595-01", "cintia@gmail.com")
cliente45 = Cliente("Fábio", "585.960.616-21", "fabio@gmail.com")
cliente46 = Cliente("Elaine", "606.162.636-41", "elaine@gmail.com")
cliente47 = Cliente("Sérgio", "626.364.656-61", "sergio@gmail.com")
cliente48 = Cliente("Jéssica", "646.566.676-81", "jessica@gmail.com")
cliente49 = Cliente("Vitor", "666.768.696-01", "vitor@gmail.com")
cliente50 = Cliente("Silvia", "686.970.717-21", "silvia@gmail.com")