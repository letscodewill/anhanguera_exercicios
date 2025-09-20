import matplotlib.pyplot as plt
import numpy as np

class Livro:
  def __init__ (self, titulo, autor, genero):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.quantidade = 1

class Biblioteca:
  def __init__ (self):
    self.livros_cadastrados = []
  
  def adiciona_livro(self, livro):
    self.livros_cadastrados.append(livro)

  def exibir_livros(self):
    for livro in self.livros_cadastrados:
      print(livro.titulo)

  def buscar_livro(self,titulo_do_livro):
    encontrado = False
    for livro in self.livros_cadastrados:
        if livro.titulo == titulo_do_livro:
            print(f"O livro '{titulo_do_livro}' foi encontrado.")
            encontrado = True
            break
    if not encontrado:
        print(f"O livro '{titulo_do_livro}' não foi encontrado.")

  def gerar_grafico(self):
    contagem_generos = {}
    for livro in self.livros_cadastrados:
        genero = livro.genero
        if genero in contagem_generos:
            contagem_generos[genero] += 1
        else:
            contagem_generos[genero] = 1

    # 2. Preparar os dados para o gráfico
    generos = list(contagem_generos.keys())
    quantidades = list(contagem_generos.values())

    # 3. Criar o gráfico
    plt.figure(figsize=(12, 7)) # Aumenta o tamanho do gráfico
    plt.bar(generos, quantidades, color='skyblue')

    # Adicionar títulos e rótulos
    plt.title('Distribuição de Livros por Gênero', fontsize=16)
    plt.xlabel('Gênero', fontsize=12)
    plt.ylabel('Quantidade de Livros', fontsize=12)

    # Rotacionar os rótulos do eixo X para melhor visualização
    plt.xticks(rotation=45, ha='right')

    # Adicionar a quantidade exata em cima de cada barra
    for i, quantidade in enumerate(quantidades):
        plt.text(i, quantidade + 0.1, str(quantidade), ha='center', va='bottom', fontsize=10)

    plt.tight_layout() # Ajusta o layout para evitar sobreposição de rótulos
    plt.show()


livros = [
    Livro('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 'Fantasia'),
    Livro('1984', 'George Orwell', 'Ficção Científica'),
    Livro('Cem Anos de Solidão', 'Gabriel García Márquez', 'Realismo Mágico'),
    Livro('Orgulho e Preconceito', 'Jane Austen', 'Romance'),
    Livro('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Fantasia'),
    Livro('O Guia do Mochileiro das Galáxias', 'Douglas Adams', 'Ficção Científica'),
    Livro('Dom Quixote', 'Miguel de Cervantes', 'Clássico'),
    Livro('O Ladrão de Raios', 'Rick Riordan', 'Fantasia'),
    Livro('Crime e Castigo', 'Fiódor Dostoiévski', 'Romance Psicológico'),
    Livro('O Retrato de Dorian Gray', 'Oscar Wilde', 'Gótico'),
    Livro('Admirável Mundo Novo', 'Aldous Huxley', 'Ficção Científica'),
    Livro('A Menina que Roubava Livros', 'Markus Zusak', 'Histórico'),
    Livro('Ulisses', 'James Joyce', 'Modernista'),
    Livro('Anna Karenina', 'Liev Tolstói', 'Romance'),
    Livro('O Sol é Para Todos', 'Harper Lee', 'Drama'),
    Livro('O Grande Gatsby', 'F. Scott Fitzgerald', 'Romance'),
    Livro('A Revolução dos Bichos', 'George Orwell', 'Sátira Política'),
    Livro('Frankenstein', 'Mary Shelley', 'Gótico'),
    Livro('O Código Da Vinci', 'Dan Brown', 'Suspense'),
    Livro('O Alquimista', 'Paulo Coelho', 'Autoajuda'),
    Livro('Ensaio sobre a Cegueira', 'José Saramago', 'Ficção Filosófica'),
    Livro('A Metamorfose', 'Franz Kafka', 'Clássico'),
    Livro('As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa', 'C.S. Lewis', 'Fantasia'),
    Livro('Duna', 'Frank Herbert', 'Ficção Científica'),
    Livro('E Não Sobrou Nenhum', 'Agatha Christie', 'Suspense'),
    Livro('Sapiens: Uma Breve História da Humanidade', 'Yuval Noah Harari', 'Não Ficção'),
    Livro('O Hobbit', 'J.R.R. Tolkien', 'Fantasia')
]

nova_biblioteca = Biblioteca()

for livro in livros:
  nova_biblioteca.adiciona_livro(livro)


nova_biblioteca.exibir_livros()

nova_biblioteca.buscar_livro('Anna Karenina')

nova_biblioteca.gerar_grafico()