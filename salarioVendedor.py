# Receber o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. 
# Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, 
#calcular e escrever o seu salário total.

salario = float(input('Informe o salário do vendedor: '));
valorVendas = float(input('Informe o valor de vendas feitas pelo vendedor: '));

if valorVendas <= 1500 :
    salario += (valorVendas * (3/100 ))
    print(salario)
else:
    salario += (1500 * (3/100 )) + ((valorVendas - 1500) * (5/100) )
    print(salario)