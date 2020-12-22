from Node import Node
#Lista Duplamente encadeada, com diversos métodos. Todos estão explicados na main, no final do programa.
class DoubleList:

    def __init__(self):
        self.head = None
        self.end = None
        self._size = 0 #não mexer

    def append(self, item): #Adiciona um elemento ao fim da lista
        if self.head:
            pointer = self.end
            pointer.next = Node(item)
            pointer.next.prev = self.end
            self.end = pointer.next
            self.end.prev = pointer
            self.head.prev = Node(None)
            self.end.next = Node(None)
        else:
            self.end = Node(item)
            self.head = self.end

        self._size += 1

    def _getnode(self, index): #não mexer
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def _getitem(self, index):   ##Não mexer
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else: raise IndexError("list index out of range")

    def __getitem__(self, index):   #Para manipular dados nesse formato >>>>lista[n]<<<<<, retornando o valor da posição n
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else: raise IndexError("list index out of range")

    def __setitem__(self, index, value):    #Para atribuir valor a algum lugar da lista desde que já haja algum valor
        pointer = self._getnode(index)      ###IMPORTANTE, essa função não irá adicionar elementos na lista
        if pointer:
            pointer.data = value
        else: raise IndexError("list index out of range")

    def index(self, item):      #dado um valor, essa função irá procura-lo dentro da lista retornando o indice que se encontra tal favor que foi passado como parâmetro.
        pointer = self.head
        cont = 0
        while pointer:
            if pointer.data == item:
                return cont
            pointer = pointer.next
            cont += 1
        raise ValueError("{} is not in list".format(item))

    def searchantecessor(self, index):    #a partir de um indice, a função irá retornar o antecessor dado um indice
        pointer = self._getnode(index)      ###IMPORTANTE, caso seja passado a posição head, seu antecessor será retornado como >>>>>> None <<<<<<
        return pointer.prev.data

    def searchsucessor(self, index):    #a partir de um indice, a função irá retornar o sucessor dado um indice
        pointer = self._getnode(index)  ###IMPORTANTE, caso seja passado a posição end, seu sucessor será retornado como >>>>>> None <<<<<<
        return pointer.next.data

    def __len__(self):  #len padrão do python>>>> || len(lista) || retornando o tamanho do mesmo
        return self._size

    def insert(self, index, item):
        node = Node(item)

        if index == 0:
            node.next = self.head
            self.head = node
            node.prev = Node(None)
            self._size = self._size + 1
        elif index <= self._size:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            node.prev = pointer.prev
            pointer.next = node
            pointer.prev = pointer
            self._size = self._size + 1
        else:
            raise IndexError("list index out of range")

    def removeitem(self, item):
        if self.head == None:
            return False
        elif self.head.data == item:
            self.head = self.head.next
            self.head.prev = None
            self._size = self._size - 1
            return True

        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == item:
                    ancestor.next = pointer.next
                    ancestor.next.prev = ancestor
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
            return False

    def removeindex(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = Node(None)
            self._size = self._size - 1
        elif index>= 0 and index <= self._size:
            pointer = self._getnode(index)
            pointer.next.prev = pointer.prev
            pointer.prev.next = pointer.next
        self._size = self._size - 1

'''
lista = DoubleList()
a = 5

lista.append(4) #adicionando elemento ao final
lista.append(22)
lista.append(3)
lista.append(7)
lista.append(9)
lista.append(32)
lista.append(2)
lista.append(24)

print(+lista[3])  #procurando elemento a partir do índice
print("||||||||||")
lista[3] = a   #alterando valor da lista a partir de um dado
print(lista[3])
print("||||||||||")
print(lista.index(32))  #printando o valor do indice do 32
print("||||||||||")
print(lista.searchantecessor(5)) #acessando o valor anterior do indice que está como parâmetro
print(lista.searchantecessor(5)) #acessando o proximo valor do indice que está como parâmetro
print("||||||||||")
print(len(lista)) #tamanho da lista
print("||||||||||")
lista.insert(2, 5) #adiciona o valor 5 no indice 2
print(lista[2])
print("||||||||||")
print(lista.removeitem(23)) #remove o node do valor passado da lista, caso exista retornará True, caso não, False
print("||||||||||")
lista.removeindex(3) #remove o node do indice passado

for i in range(len(lista) - 1): #printando a lista
    print("{}->{}<-{}".format(lista.searchantecessor(i), lista[i], lista.searchsucessor(i)))
'''