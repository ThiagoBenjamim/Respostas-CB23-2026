class Node:
    def __init__(self, data):
        '''Inicia a classe Node.'''
        self.data = data
        self.next = None

class PilhaEncadeada:
    def __init__(self):
        '''Inicia a classe Pilha Encadeada com o header node vazio e um contador de comprimento inicialmente vazio.'''

        self.header_node = None
        self.length_counter = 0

    def push(self, node_data):
        '''Insere um node no topo da pilha.
        Como o node simplesmente assume o valor do header node,
        que pode ser acessado intantaneamente, e o endereça depois, sua complexidade é:
        O(1)'''

        node = Node(node_data)

        if self.header_node == None:
            self.header_node = node

        else:
            node.next = self.header_node
            self.header_node = node

        self.length_counter += 1

    def pop(self):
        '''Escolhe o node endereçado pelo header atual como novo header e retorna o substituido,
        Pelos mesmos motivos do método anterior, sua complexidade é:
        O(1)'''

        if self.header_node == None:
            raise IndexError("Pilha Vazia")

        popped = self.header_node
        self.header_node = self.header_node.next
        self.length_counter -= 1
        return popped.data

    def topo(self):
        '''Simplemente retorna o header node, que pode ser acessado direto,
        A complexidade é:
        O(1)'''

        if self.header_node == None:
            raise IndexError("Pilha Vazia")
        
        return self.header_node.data

    def esta_vazia(self):
        '''Verifica o contador de comprimento e retorna se é maior que 0
        Sua complexidade é:
        O(1)'''

        if self.length_counter <= 0:
            return True
        else:
            return False

    def __len__(self):
        '''Simplemente retorna o contador de comprimento,
        sua complexidade é:
        O(1)'''

        return self.length_counter

    def repr(self):
        '''Como precisa percorrer a pilha inteira pelo menos uma vez,
        sua complexidade é:
        O(N)'''

        if self.esta_vazia():
            raise IndexError("Pilha vazia.")

        current = self.header_node
        text = ""
        while current.next != None:
            text += f"{current.data} - "
            current = current.next
        text += str(current.data)

        return text


pilha = PilhaEncadeada()
print(pilha.repr())