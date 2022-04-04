horasTrabalhadasMes = int(input('Informe quantas horas você trabalhou no mês: \n'))
salarioPorHora = int(input('Informe quanto você recebe por hora: \n'))

if horasTrabalhadasMes <= 160 and horasTrabalhadasMes > 0  : 
    salario = salarioPorHora*horasTrabalhadasMes
    print(salario)
elif horasTrabalhadasMes > 160: 
    horaExtra = horasTrabalhadasMes - 160
    salario = (salarioPorHora*(horasTrabalhadasMes-horaExtra)) + ((salarioPorHora/2) * horaExtra)
    print(salario)
else: 
    print('Ao que me consta você não trabalhou')