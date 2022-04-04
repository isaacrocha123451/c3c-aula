v1 = int(input('Digite um valor qualquer:'))
v2 = int(input('Digite um valor qualquer:'))
v3 = int(input('Digite um valor qualquer:'))

valores = []

if v1 < v2 and v1 < v3 and v2 < v3:
    valores = [v1,v2,v3]
    print(valores)
elif v1 > v2 and v1 < v3 :
    valores = [v2,v1,v3]
    print(valores)
elif v1 > v2 and v1 > v3 and v2 > v3:
    valores = [v3,v2,v1]
    print(valores)
elif v3 > v2 and v3 < v1:
    valores = [v2,v3,v1]
    print(valores)
elif v2 > v1 and v2 > v3 and v1 > v3:
    valores = [v3,v1,v2]
    print(valores)
else: 
    valores = [v1,v3,v2]
