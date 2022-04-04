impar = []
par = {"numeroPar":[]}

for u in range(5):
    numero = int(input("infome um numero\n"))
    if numero%2 == 0:
        par["numeroPar"].append(numero)
    else:
        impar.append(numero)    


print(par)
print(impar)        

