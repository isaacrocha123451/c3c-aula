horaInicio = int(input('Hora de inicio do jogo de xadrez: '))
horaTermino = int(input('Hora do termino do jogo de xadrez: '))

tempoJogo = horaTermino - horaInicio

if horaInicio >= horaTermino:
    tempoJogo =  (24 + horaTermino) - horaInicio
    print('O jogo teve ' + str(tempoJogo) + ' horas de duração ')
else: 
     print('O jogo teve ' + str(tempoJogo) + ' horas de duração ')