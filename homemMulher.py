'''Escreva um código que receba as idades de 2 homens e de 2 mulheres 
(considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). 
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, 
e o produto das idades do homem mais novo com a mulher mais velha.'''

# h1 + m1 e h2 * m2 // h2 + m2 e h1 * m1 

h1 = int(input('Informe o a idade do homem 1: '))
h2 = int(input('Informe o a idade do homem 2: '))
m1 = int(input('Informe o a idade do mulher 1: '))
m2 = int(input('Informe o a idade do mulher 2: '))

if h1 > h2 and m1 > m2 :
    print("Soma: ")
    print(h1 + m2)
    print("Produto")
    print(h2 * m1 )
elif h1 > h2 and m1 < m2 :
    print("Soma: ")
    print(h1 + m1)
    print("Produto")
    print(h2 * m2 )
elif h2 > h1 and m1 > m2 :
    print("Soma: ")
    print(h2 + m2)
    print("Produto")
    print(h1 * m1 )
else : 
    print("Soma: ")
    print(h2 + m1)
    print("Produto")
    print(h1 * m2 )   


