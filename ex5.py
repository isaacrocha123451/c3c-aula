nomeProduto = input('Infome o nome do produto:\n')
dataValidade = input('Informe a data de validade do produto:\n')
dataFabricacao = input('Infome a data de fabricação do produto:\n')
fabricante = input('Informe o fabricante do produto:\n')
lote = int(input('Informe o lote do produto:\n'))

dadosProduto = [nomeProduto, dataValidade, dataFabricacao, fabricante, lote]

for produto in dadosProduto:
    print(produto)
