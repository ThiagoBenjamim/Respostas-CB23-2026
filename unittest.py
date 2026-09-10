from pilha_encadeada import PilhaEncadeada
from fila_encadeada import FilaEncadeada

print("Teste Pilha:")
pilha_push_pop = PilhaEncadeada()
pilha_push_pop.push(10)
print(pilha_push_pop.pop())

print("======================================================")

pilha_vazia = PilhaEncadeada()
if input("Gostaria de testar o caso de Pilha Vazia 1?(Y/N)(Encerrará o programa):").lower() == "y":
    print(pilha_vazia.pop())
if input("Gostaria de testar o caso de Pilha Vazia 2?(Y/N)(Encerrará o programa):").lower() == "y":
    print(pilha_vazia.topo())

print("======================================================")

pilha_len = PilhaEncadeada()
print(len(pilha_len))
pilha_len.push(10)
print(len(pilha_len))
pilha_len.pop()
print(len(pilha_len))

print("======================================================")

pilha_alternancia = PilhaEncadeada()
print(pilha_alternancia.esta_vazia())
pilha_alternancia.push(10)
pilha_alternancia.push(30)
pilha_alternancia.push(20)
print(len(pilha_alternancia))
print(pilha_alternancia)
pilha_alternancia.pop()
print(len(pilha_alternancia))
print(pilha_alternancia)
pilha_alternancia.pop()
print(len(pilha_alternancia))
print(pilha_alternancia)
pilha_alternancia.push(50)
print(len(pilha_alternancia))
print(pilha_alternancia)
print(pilha_alternancia.esta_vazia())

print("======================================================")

pilha_diferentes = PilhaEncadeada()
pilha_diferentes.push("ABC")
pilha_diferentes.push(10)
pilha_diferentes.push(True)
pilha_diferentes.push(10.0)
print(pilha_diferentes)

print("======================================================")

print("Teste Fila:")

fila_inter = FilaEncadeada()
fila_inter.enfileirar(10)
print(fila_inter.desenfileirar())

print("======================================================")

fila_esva = FilaEncadeada()
fila_esva.enfileirar(10)
fila_esva.enfileirar(30)
fila_esva.enfileirar(20)
print(fila_esva.desenfileirar())
print(fila_esva.desenfileirar())
print(fila_esva.desenfileirar())
fila_esva.enfileirar("10")
print(fila_esva)

print("======================================================")

fila_vazia = FilaEncadeada()
if input("Gostaria de testar o caso de Fila Vazia 1?(Y/N)(Encerrará o programa):").lower() == "y":
    print(fila_vazia.desenfileirar())
if input("Gostaria de testar o caso de Fila Vazia 2?(Y/N)(Encerrará o programa):").lower() == "y":
    print(fila_vazia.frente())

print("======================================================")

fila_len = FilaEncadeada()
print(len(fila_len))
fila_len.enfileirar(10)
print(fila_len)
print(len(fila_len))
fila_len.enfileirar(30)
print(fila_len)
print(len(fila_len))
fila_len.enfileirar(20)
print(fila_len)
print(len(fila_len))
fila_len.desenfileirar()
print(fila_len)
print(len(fila_len))