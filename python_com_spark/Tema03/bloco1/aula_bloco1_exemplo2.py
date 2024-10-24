import random as rd
import pandas as pd


nCol = 3
nRow = 10

df = pd.read_csv("arquivo/arq.csv")
# df = pd.DataFrame()

# for i in range(1, nCol):
    # colRd = [rd.random() * 100 for i in range(0, nRow)]
   #  df["col" + str(i)] = colRd


df.hist("width", "length")
df.plot.line()
df.plot.bar()
df.plot.area()
df.plot.pie(y = "width", x="length")