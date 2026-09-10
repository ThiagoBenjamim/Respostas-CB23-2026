class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PilhaEncadeada:
    def __init__(self):
        self.header_node = None
        self.length_counter = 0

    def push(self, node_data):

        node = Node(node_data)

        if self.header_node == None:
            self.header_node = node

        else:
            node.next = self.header_node
            self.header_node = node

        self.length_counter += 1

    def pop(self):

        if self.header_node == None:
            raise IndexError("Pilha Vazia")

        popped = self.header_node
        self.header_node = self.header_node.next
        self.length_counter -= 1
        return popped.data

    def topo(self):
        if self.header_node == None:
            raise IndexError("Pilha Vazia")
        
        return self.header_node.data

    def esta_vazia(self):

        if self.length_counter == 0:
            return True
        else:
            return False

    def __len__(self):

        return self.length_counter

    def repr(self):

        if self.esta_vazia():
            raise IndexError("Pilha vazia.")

        current = self.header_node
        text = ""
        while current.next != None:
            text += f"{current.data} - "
            current = current.next
        text += str(current.data)

        return text