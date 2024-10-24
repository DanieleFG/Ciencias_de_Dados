import numpy as np

arquivo = "arquivos/aula_bloco2_1.csv"
dados = np.genfromtxt(arquivo, delimiter=",", names=True)


from matplotlib import pyplot as plt
plt.scatter(dados["width"], dados["length"])
plt.bar(dados["width"], dados["length"])