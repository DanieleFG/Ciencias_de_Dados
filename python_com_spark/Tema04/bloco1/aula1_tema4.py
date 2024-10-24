import pandas as pd
# primeiro parametro o arquivo, segundo parametro qual tabela especifica
df = pd.read_excel("arquivo/internet.xlsx", "Tab 1.1.38")

#Definição dos nomes das colunas:
colNm = [
    "Regiao",
    "MediaTotal",
    "MediaUltilizam",
    "MediaNaoUtilizam",
    "MedianoTotal",
    "MedianoUltilizaram",
    "MedianoNaoUltilizaram",
]

df.columns = colNm

# descarto as linhas 
df = df.drop([0, 1, 2, 3, 46, 47])

#descarto as colunas
#df = df.drop(columns=["remov1", "remov2", "remov3", "remov4"])

#Ajuste do índice ,escreve o nome das linhas
df = df.set_index(df["Regiao"])
df = df.drop(columns=["Regiao"])

df = df.drop(["Brasil"])

df = df.sort_values("MediaTotal")

#Criação de um gráfico de linhas:
# gerar o grafico passando o ratação com o rot=  e o tamanhao do grafico no figsize
df.plot.line(rot=90)

df = df.apply(pd.to_numeric, errors="coerce")
matCorrer = df.corr()

#Criação de histogramas:
df.hist("ultilizam")
df.hist("napUltilizam")