#É usado para manipulação dos registros a biblioteca pandas.
import pandas as pd

data = pd.read_csv('arquivo.csv',sep = ';') #Aqui nós usamos a funçãoo read_csv para ler o csv que foi criado, em forma de separação em ponto e vírgula.

data = data.sort_values(by=['nome']) #Aqui nós organizamos tudo em função dos nomes, ou seja, em forma alfabética.

print(data) #printamos os registros ordenado pelo nome, com o índice informando a posição.

'''
#No texto da segunda questão não fica claro se quer o retorno da lista ou do registro por inteiro.
#Caso seja pedido somente a lista, podemos usar o seguinte código comentado:

#É usado para manipulação dos registros a biblioteca pandas.
import pandas as pd

data = pd.read_csv('arquivo.csv',sep = ';') #Aqui nós usamos a funçãoo read_csv para ler o csv que foi criado, em forma de separação em ponto e vírgula.
data = data.sort_values(by=['nome']) #Aqui nós organizamos tudo em função dos nomes, ou seja, em forma alfabética.

data = data['nome'].tolist() #isso transformará o csv em uma lista, onde ela estará ordenada em ordem alfabética.
print(data) #printamos a lista, ordenado pelo nome, com o índice informando a posição.

#De acordo com o texto, existem essas duas possibilidades, para testar essa basta descomentar.
'''

