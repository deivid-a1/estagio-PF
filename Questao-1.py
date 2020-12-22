#O problema envolve uma manipulação simples de listas e dicionários, porém adaptando ele a vida real, foi utilizado orientação a objetos e estruturas de dados.
#A orientação a objetos vem com o objetivo de organizar melhor e diminuir a quantidade de linhas para um código robusto e a estrutura de dados para o processamento
#de grandes quantidade de dados, no caso, se o nosso dicionário fosse enorme, teríamos um grande benefício em utilizar as estrutura de dados,
# pois se considerarmos um cenário real, estamos armazenando esses dados para manipula-lo posteriormente e entre a lista encadeada e a lista
#normal, a duplamente encadeada ou simplesmete encadeada possui um uso de processamento (O(n)) menor dependendo do cénario do que a lista que já existe.

#Importando a lista duplamente encadeada, simulando um problema que envolve complixidade.
from DoubleLinked import DoubleList

#Utilização de uma classe, para caso no futuro possa dar mais métodos e objetivos para o dicionário.
class Dict: #Criado a classe dicionário.

    #Aqui é inicializada a classe, criando o dicionário que será usadado para manipulação dos dados, caso queira adicionar ou retirar dados
    #basta alterar o dicionário abaixo.
    def __init__(self):
        self.dictionary = { 'João': 21,
                            'Maria': 30,
                            'Matheus': 15,
                            'Ana': 15,
                            'pera': 50,
                            'uva': 2,
                            'maçã': 55,
                            'abacaxi': 25,
                            'laranja': 0,
                            }

    '''Este método procura se a entrada do usuário está no dicionário criado acima, retornando False caso não esteja presente a chave e retornando o valor que está ligado
    a chave caso a chave exista.'''
    def searcyKey(self, key):
        if key not in self.dictionary: #Verificando se a chave não está no dicionário, se não estiver retorna False.
            return False
        else: #Se estiver
            return self.dictionary.get(key) #Retorna o valor da que está ligado a tal chave. A variavel key é a que está responsavel pela chave.

#Aqui estamos na main, onde acontecerá a instância das estruturas de dados e da nossa classe que acabou de ser criada.

dicionario = Dict() #Instancia do dicionário.
lista = DoubleList() #Instância da lista duplamente encadeada

#É utilizado uma repetição que verifica todos as chaves que o usuário deseja verificar, retornando se ela está ou não está no nosso dicionário.
exit = False
while exit == False: #Enquanto exit for False, continuará pedindo inputs pro usuário
    key = str(input("Digite uma chave em string, caso queira sair digite 0")) #Aqui é onde o looping pode acabar, basta que seja digitado zero.
    if key == '0': #Se key for 0 em string, o looping finaliza aqui.
        break
    saida = dicionario.searcyKey(key) #Se o programa não finalizou significa que a saida possui uma saida, sendo ela False ou um número inteiro.
    if saida == False: #Se for False, um boolean, o programa avisará ao usuário que a chave digitada não se encontra no dicionário.
        print("Chave não encontrada")
    else: #Mas se não for False, saida é um número inteiro que será adicionada a uma lista.
        if saida not in lista: #Se o valor inteiro saida estiver dentro da lista, não será feito nada. Mas se não houver tal valor, será adicionado a nossa lista.
            lista.append(saida)

#Aqui é o retorno da lista para o usuário, utilizando um for simples.
for i in range(len(lista)):
    print(lista[i])

'''Tentei simular um programa mais complexo, que utiliza vários dados dentro do dicionário. Para isso implementei uma lista duplamente encadeada, juntamente com
orientação a objeto visando um problema mais complexo que use menos dos nossos processadores. Existem diversas estruturas de dados que podem ser usada, como filas,
pilhas, arvores, listas encadeadas, etc. Cada cenário irá utilizar alguma delas. Utilizei uma lista encadeada como ilustração, mas poderia ser usada até mesmo uma
lista simples. Mas simulei um cenário mais real.
'''