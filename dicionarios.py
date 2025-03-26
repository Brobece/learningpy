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
print("altura" in aluno)

#A função “ get()” é muito útil para evitar erros de chave inexistente.
print(aluno.get("Idade"))
print(aluno.get("Peso"))

#A função “items()” retorna uma lista de tuplas com os pares “chave” : valor.
print(aluno.items())
#A função “keys()” retorna uma lista apenas com as chaves do dicionário.
print(aluno.keys())
#A função “values()” retorna uma lista apenas com os valores dos itens do dicionário:
print(aluno.values())

#atualizando o dicionario
aluno = {"Nome": "João GUilherme", "Idade": 18, "Nota": 9.9}
aluno_update = {"Peso": 70, "Nota": 8.5
aluno.update(aluno_update)
print(aluno_update)

#sets: Os sets são listas ou coleções não ordenadas de itens únicos.                
