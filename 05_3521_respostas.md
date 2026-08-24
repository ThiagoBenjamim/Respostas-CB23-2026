1\. Organização em hierarquia de herança:

* Pessoa é classe base de Funcionário, visto que funcionários são pessoas e necessitam dos atributos de uma pessoa(Nome e Idade) além dos próprios.  
* Gerente, Chefe de Cozinha e Garçom são todos subclasses de Funcionário, visto que são funcionários e necessitam dos atributos da classe(Nome, Idade, Salário e Carga Horária).  
* Restaurante é classe base de Pizzaria, visto que uma pizzaria é um tipo de restaurante e necessita dos atributos de um restaurante(Nome, Endereço e Telefone).  
* Pizza e Bolo são ambos subclasses de Iguaria(comida), visto que são ambos comidas e precisam dos atributos de uma comida de um restaurante(Nome e Preço).

2\. Essa relação poderia ser implementada criando uma lista de instâncias de Iguaria(comida), chamada menu, pertencente à Restaurante, com cada item sendo um prato diferente no restaurante.

3\. Tipos para os argumentos:

* Argumento1: O Argumento1 é uma lista representando o pedido feito, onde o primeiro item é uma instância de Iguiaria(comida) e o segundo item é um número int representando o número da mesa que fez o pedido.  
* Argumento2: O Argumento2 é uma instância de Iguaria(comida), visto que o Chefe de Cozinha apenas precisa preparar o pedido.  
* Argumento3: O Argumento3 é uma instância de Funcionário, visto que o Gerente precisa demitir um funcionário do restaurante.