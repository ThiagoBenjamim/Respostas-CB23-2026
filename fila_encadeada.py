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

    def __repr__(self):
        '''Primeiro, se a pilha de extração estiver vazia, passa todos os itens para ela, se não,
        esvazia essa pilha no output antes de passar os elementos da fila de entrada,
        após isso, finalmente extrai no output, e por fim, tudo volta para a pilha de saida,
        como todas as ações são O(N),
        a complexidade total desse método é O(N).'''

        pilha_aux = PilhaEncadeada()

        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

        if self.pilha_saida.esta_vazia():
            raise IndexError("Fila está vazia.")

        pop = self.pilha_saida.pop()
        pilha_aux.push(pop)
        texto = f"{pop}"
        while not self.pilha_saida.esta_vazia():
            pop = self.pilha_saida.pop()
            pilha_aux.push(pop)
            texto += f" - {pop}"

        if not self.pilha_entrada.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

            while not self.pilha_saida.esta_vazia():
                pop = self.pilha_saida.pop()
                pilha_aux.push(pop)
                texto += f" - {pop}"

        while not pilha_aux.esta_vazia():
            self.pilha_saida.push(pilha_aux.pop())

        return texto