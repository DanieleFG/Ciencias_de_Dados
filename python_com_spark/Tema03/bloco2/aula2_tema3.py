import pandas as pd
# primeiro parametro o arquivo, segundo parametro qual tabela especifica
df = pd.read_excel("arquivo/internet.xlsx", "Tab 1.1.38")

#Definição dos nomes das colunas:
colNm = [
    "Regiao",
    "remov1",
    "ultilizam",
    "napUltilizam",
    "remov2",
    "remov3",
    "remov4",
]

df.columns = colNm

# descarto as linhas 
df = df.drop([0, 1, 2, 3, 46, 47])

#descarto as colunas
df = df.drop(columns=["remov1", "remov2", "remov3", "remov4"])

#Ajuste do índice ,escreve o nome das linhas
df = df.set_index(df["Regiao"])
df = df.drop(columns=["Regiao"])

#Cálculo da média:
df["ultilizam"].mean()
df["napUltilizam"].mean()

#Criação de um gráfico de linhas:
# gerar o grafico passando o ratação com o rot=  e o tamanhao do grafico no figsize
df.plot.line(rot=90, figsize=(10, 3))

#Conversão de colunas para valores numéricos:
df["ultilizam"] = pd.to_numeric(df["ultilizam"])
df["napUltilizam"] = pd.to_numeric(df["napUltilizam"])

#Criação de histogramas:
df.hist("ultilizam")
df.hist("napUltilizam")