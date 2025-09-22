# Anhanguera exercícios

### Exercício 1

Você foi contratado para desenvolver um sistema simples de gestão de notas de alunos. O sistema
deve permitir que o usuário adicione notas, calcule a média das notas, determine a situação do
aluno (aprovado ou reprovado), e exiba um relatório final. Utilize estruturas condicionais, de
repetição e funções.

Cadastro de Notas:

- O sistema deve permitir que o usuário insira as notas dos alunos.
- As notas devem ser armazenadas em uma lista.
Cálculo da Média:
- O sistema deve calcular a média das notas inseridas.
Determinação da Situação:
- Se a média for maior ou igual a 7, o aluno está aprovado.
- Se a média for menor que 7, o aluno está reprovado.
Relatório Final:
3
- Exibir as notas inseridas, a média e a situação do aluno.

### Exercício 2

Você foi contratado para desenvolver um sistema simples de gerenciamento de livros em uma
biblioteca. O sistema deve permitir cadastrar novos livros, listar todos os livros disponíveis, buscar
um livro pelo título, e gerar um gráfico com a quantidade de livros por gênero.

Passo 1: Definir a classe Livro

- Comece definindo a estrutura básica de um livro usando uma classe em Python. Cada livro
terá atributos como título, autor, gênero e quantidade disponível.

Passo 2: Criar a lista de livros

- Inicialize uma lista vazia para armazenar os livros que serão cadastrados.

Passo 3: Implementar funções para gerenciar os livros

- Função para cadastrar um novo livro
- Função para listar todos os livros
3
- Função para buscar um livro pelo título

Passo 4: Utilizar a biblioteca Matplotlib para gerar um gráfico

- Instalação da Matplotlib
- Gerar o gráfico de quantidade de livros por gênero

Passo 5: Testar o sistema

### Exercício 3

Você trabalha em uma empresa de varejo e precisa analisar os dados de vendas do último ano
para identificar padrões e insights para melhorar o desempenho. Os dados estão armazenados
em um banco de dados SQLite, e você utilizará a biblioteca Pandas para manipular e analisar
esses dados, além de gerar visualizações utilizando Matplotlib e Seaborn.

Passo 1: Conectar ao banco de dados SQLite e criar uma tabela

- Primeiro, você precisa estabelecer uma conexão com o banco de dados SQLite e carregar
os dados relevantes para análise.
import sqlite3

Passo 1.1: Conectar ao banco de dados (ou criar, se não existir)

    conexao = sqlite3.connect('dados_vendas.db')

Passo 1.2: Criar um cursor

    cursor = conexao.cursor()

Passo 1.3: Criar uma tabela (se não existir)
    
    cursor.execute('''
    CREATE TABLE vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
    )
    ''')

 Passo 1.4: Inserir alguns dados

    cursor.execute('''
    INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
    ''')

Passo 1.5: Confirmar as mudanças

    conexao.commit()

Passo 2: Explorar e preparar os dados

- Agora que os dados estão carregados em um DataFrame do Pandas (df_vendas), você
pode explorá-los e prepará-los para análise.
4

Passo 3: Análise dos dados

- Realize análises específicas para extrair insights sobre as vendas.

Passo 4: Visualização dos dados

- Utilize Matplotlib e Seaborn para criar visualizações que ajudem na interpretação dos
resultados.

Passo 5: Conclusão e análise de insights

- Finalize o exercício com uma breve análise dos insights obtidos e sugestões para a
empresa com base nos dados analisados.

### Exercício 4

Você foi contratado para criar um modelo de Machine Learning que classifica espécies de flores Iris
com base em características como comprimento e largura das sépalas e pétalas. Você usará o
TensorFlow para construir, treinar e avaliar o modelo.

Passo 1: Importar Bibliotecas e Carregar Dados

- Usar bibliotecas como tensorflow, pandas e scikit-learn.
- Carregar o conjunto de dados Iris disponível no scikit-learn.

Importar bibliotecas

    import tensorflow as tf
    import pandas as pd
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    Carregar conjunto de dados Iris
    3
    iris = load_iris()
    X = iris.data
    y = iris.target

Passo 2: Pré-processamento dos Dados

- Dividir o conjunto de dados em treinamento e teste.
- Normalizar os dados.

Passo 3: Construir o Modelo

- Usar TensorFlow para construir um modelo de rede neural simples.

Passo 4: Treinar o Modelo

- Treinar o modelo com os dados de treinamento

Passo 5: Avaliar o Modelo

- Avaliar a precisão do modelo usando os dados de teste.

Passo 6: Fazer Previsões

- Fazer previsões com o modelo treinado
PROCEDIMENTOS PARA A REALIZAÇÃO DA ATIVIDADE:
- Acesse o Google Colab e crie um novo notebook.
- Implemente as funcionalidades solicitadas usando as instruções e dicas fornecidas.
- Teste o código com diferentes entradas para garantir que ele está funcionando
corretamente.
- Comente o código para explicar cada parte da lógica implementada.
CHECKLIST:
- Acessar o Google Colab e criar um novo notebook.
- Copiar e colar o código inicial no notebook.
- Implementar as funcionalidades de adicionar notas, calcular média, determinar situação e
exibir relatório final.
- Testar o código com diferentes entradas.
- Comentar o código para explicar a lógica implementada.
- Tire um print do código executado pelo menos uma vez.
