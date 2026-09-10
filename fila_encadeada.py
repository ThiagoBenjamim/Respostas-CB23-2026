from pilha_encadeada import PilhaEncadeada

class FilaEncadeada:
    def __init__(self):
        '''Inicializa a classe Fila Encadeada contendo uma pilha para a entrada de nodes e uma para a extração'''

        self.pilha_entrada = PilhaEncadeada()
        self.pilha_saida = PilhaEncadeada()

    def enfileirar(self, data):
        '''Insere o item na pilha de entrada com o método push de complexidade O(1)'''
        self.pilha_entrada.push(data)

    def desenfileirar(self):
        '''Remove o item mais antido da pilha de extração,
        caso ela esteja vazia, retira os elementos da pilha de entrada e os insere em si mesmo em ordem contrária,
        (Explicação mais detalhada no documento md)'''

        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

        if self.pilha_saida.esta_vazia():
            raise IndexError("Fila está vazia.")
        
        return self.pilha_saida.pop()

    def frente(self):
        '''Retorna o documento mais antigo da pilha de extração,
        caso ela esteja vazia, faz o mesmo que o método desenfileirar para preenchela,
        (Explicação mais detalhada no documento md)'''

        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

        if self.pilha_saida.esta_vazia():
            raise IndexError("Fila está vazia.")

        return self.pilha_saida.topo()

    def esta_vazia(self):
        '''Retorna True se os dois métodos esta_vazia() forem True também,
        como são dois métodos O(1),
        a complexidade é O(1)'''

        return (self.pilha_entrada.esta_vazia() and self.pilha_saida.esta_vazia())

    def __len__(self):
        '''Retorna a soma do comprimento das duas pilhas, assim,
        tem complexidade O(1) ao chamar dois métodos O(1)'''

        return (len(self.pilha_entrada) + len(self.pilha_saida))

    def repr(self):
        '''Primeiro passa todos os itens da pilha de entrada para a pilha de extração, que é uma ação O(N),
        após isso, '''

        while not self.pilha_entrada.esta_vazia():
            self.pilha_saida.push(self.pilha_entrada.pop())

        if self.pilha_saida.esta_vazia():
            raise IndexError("Fila está vazia.")

        sub_pilha_saida = self.pilha_saida
        text = f"{sub_pilha_saida.pop()}"
        while not sub_pilha_saida.esta_vazia():
            text += f" - {sub_pilha_saida.pop()}"
        
        return text

fila = FilaEncadeada()

print(fila.repr())