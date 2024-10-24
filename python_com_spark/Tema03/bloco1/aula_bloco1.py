import random
import matplotlib.pyplot as plt


x = range(1, 50)
y = [random.random() * 100 for i in x]

plt.plot(x,y, color="red", linestyle="dashed")

plt.grid(True)

plt.legend("Dadios Aleatorios")
plt.title("Meu Primeiro Gráfico em Python")
plt.xlabel("Série de dados")
plt.ylabel("Valores aleatorios")