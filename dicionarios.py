aluno = {"Nome": "João GUilherme", "Idade": 18, "Nota": 9.9}
print(aluno)
print(aluno["Nome"])
print(aluno["Idade"])
print(aluno["Nota"])

#modificando/adicionando um item novo ao dicionario
aluno["Nota"] = 8.5
aluno["Peso"] = 70
print(aluno)

#para remover uma chave e o seu valor, usamos a função "del" e para apagar todas as chaves, usamos o ".clear()"
del aluno["Peso"]
print(aluno)
aluno.clear()
print(aluno)

#para contar a quantidade de pares de chaves que o dic tem
aluno = {"Nome": "João GUilherme", "Idade": 18, "Nota": 9.9}
print(len(aluno))

#verificar a existencia de um par de chave1
print("idade" in aluno)
print("alutra" in aluno)
