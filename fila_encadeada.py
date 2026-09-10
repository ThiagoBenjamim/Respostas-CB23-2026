from pilha_encadeada import PilhaEncadeada

class FilaEncadeada:
    def __init__(self):

        self.pilha_entrada = PilhaEncadeada()
        self.pilha_saida = PilhaEncadeada()

    def enfileirar(self, data):

        self.pilha_entrada.push(data)

    def desenfileirar(self):
    #Pode ser O(1) quando a pilha de saída tiver elementos,
    #mas quando ela estiver vazia, será necessário a reordenação da pilha de entrada, o que custa O(n)

        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

        if self.pilha_saida.esta_vazia():
            raise IndexError("Fila está vazia.")
        
        return self.pilha_saida.pop()

    def frente(self):
    #Pode ser O(1) quando a pilha de saída tiver elementos,
    #mas quando ela estiver vazia, será necessário a reordenação da pilha de entrada, o que custa O(n)

        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

        if self.pilha_saida.esta_vazia():
            raise IndexError("Fila está vazia.")

        return self.pilha_saida.topo()

    def esta_vazia(self):

        return (self.pilha_entrada.esta_vazia() and self.pilha_saida.esta_vazia())

    def __len__(self):

        return (len(self.pilha_entrada) + len(self.pilha_saida))

    def repr(self):

        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

        if self.pilha_saida.esta_vazia():
            raise IndexError("Fila está vazia.")

        current = self.pilha_saida.header_node
        text = ""
        while current.next != None:
            text += f"{current.data} - "
            current = current.next
        text += str(current.data)
        
        return text