''' Faça um código que receba: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. 
Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). 
Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'Não efetuar compra', 
senão escrever mensagem 'Efetuar compra'. '''

estoqueAtual = int(input('Estoque atual do produto: '))
estoqueMaximo = int(input('Estoque maximo do produto: '))
estoqueMinimo = int(input('Estoque mininmo do produto: '))

qntdMedia = (estoqueMaximo + estoqueMinimo)/2

if estoqueAtual >= qntdMedia :
    print('Não efetuar compra')
else:
    print('Efetuar compra')
