aluno = { 
    "nome":input("Informe o nome do aluno: "),
    "a1":float(input("Informe a nota a1 do aluno: ")),
    "a2":float(input("Informe a nota a2 do aluno: "))
}

media = (aluno["a1"] + aluno["a2"])/2

if media >= 7 :
    print(" A média do aluno " + aluno["nome"] + "foi " + str(media) + " e está aprovado")
else:
    print(" A média do aluno " + aluno["nome"] + "foi " + str(media) +  " e está reprovado")