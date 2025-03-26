frutas = ["Pera", "Maçã", "Uva"]

#Para adicionar algo na lista:
frutas.append('Banana')

#Para adicionar algo em uma posição especifica:
frutas.insert(2, 'Laranja')

#para adicionar varias coisas de uma vez so:
novas_frutas = ["Caju", "Limao", "Cacau"]
frutas.extend(novas_frutas)

#Para colocar uma lista na outra
frutas1 = ["Pera", "Maçã", "Uva"]
frutas2 = ["Caju", "Limao", "Cacau"]
print(frutas2 + frutas1)

#para remover algo da lista
fruta.remove('Pera')

#para usar uma parte em especifico da lista
print(frutas)
print(frutas[0,2])
print(frutas[1,2])
print(frutas[0])

#Funções para ajudar em problemas:

#contar a quantidade de itens na lista
print(len(frutas))
#falar qual o valor maximo e minimo da lista
notas = [9.9, 10, 8.1, 4.3]
print(notas)
print(min(notas))
print(max(notas))
#copiar uma lista da maneira correta
frutas_gostosas = frutas.copy()
#apagar todos os itens de uma lista
frutas.clear()
