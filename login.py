''' Faça um código para receber um número que é um código de usuário. 
Caso este código seja diferente de um código armazenado internamente no algoritmo (código de 6 números de sua escolha) 
deve ser apresentada a mensagem ‘Usuário inválido!’. 
Caso o Código seja correto, deve ser lido outro valor que é a senha. 
Se esta senha estiver incorreta (a certa é C3c@9999#) deve ser mostrada a mensagem ‘senha incorreta’. 
Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.''' 

codigo = 123456
codigoUsuario = int(input('Informe o seu codigo de acesso: '))
senha = 'C3c@9999#'


if codigoUsuario == codigo :
    senhaUsuario = input('Informe a senha de acesso: ')
    if senhaUsuario == senha:
        print('Acesso permitido')
    else:
        print('Acesso negado')
else :
    print('Usuário invalido')
