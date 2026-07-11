class Filme():
    def __init__(self, titulo, ano, duracao, genero, sinopse, assistido):
        self.titulo = titulo
        self.ano = ano
        self.duracao = duracao
        self.genero = genero
        self.sinopse = sinopse
        self.assistido = False

    def exibir_filme(self):
        print(f"""
{self.titulo} ({self.ano}) - {self.genero}
Duração: {self.duracao} minutos
Sinopse: {self.sinopse}

Assistido: {"Sim" if self.assistido else "Não"}
""")
        

class Serie():
    def __init__(self, titulo, ano, temporadas, genero, sinopse, assistido):
        self.titulo = titulo
        self.ano = ano
        self.temporadas = temporadas
        self.genero = genero
        self.sinopse = sinopse
        self.assistido = False

    def exibir_serie(self):
        print(f"""
{self.titulo} ({self.ano}) - {self.genero}
Duração: {self.temporadas} temporadas
Sinopse: {self.sinopse}

Assistido: {"Sim" if self.assistido else "Não"}
""")