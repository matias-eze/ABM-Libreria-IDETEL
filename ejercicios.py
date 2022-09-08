#monto = int(input('ingrese un monto:'))
#total = 0
#banderaDescuento = 1000
#descuento = 10
#while (monto != 0):
#    if monto > 0 :
#        total = total + monto
#    else:
#        print('el monto debe ser positivo')
#    monto = int(input('ingrese un monto:'))
#if total > banderaDescuento:
#    total = total - (total/descuento)
#print(int(total))

#---------------------------------------------

#canti = int(input('ingrese cantidad de valores a ingresar: '))
#total = 0
#for x in range (canti):
#    valor = int(input('ingrese un calor: '))
#    total = total + valor
#print('el promedio es: {}'.format(total//canti)) #la '//' es el operador logico para division entera, excluye los float del resultado.

#---------------------------------------------

#hora = int(input('ingrese una hora de inicio del evento:'))
#minuto = int(input('ingrese un minuto de inicio del evento:'))
#duracionHora = int(input('ingrese una cantidad de horas de duracion del evento:'))
#duracionMinutos = int(input('ingrese una cantidad de minutos de duracion del evento:'))
#horaFinal = 0
#minutoFinal = 0
#horaFinal = hora + duracionHora
#minutoFinal= minuto + duracionMinutos
#while minutoFinal >= 60:
#    minutoFinal = minutoFinal - 60
#    horaFinal += 1
#    if hora >= 24:
#        hora = 0
#if minutoFinal == 0:
#    print('la hora de finalizacion del evento sera: {}:{}0 hs.'.format(horaFinal, minutoFinal))
#else:
#    print('la hora de finalizacion del evento sera: {}:{} hs.'.format(horaFinal, minutoFinal))

#-------------------------------------------

#hora = int(input('ingrese una hora de inicio del evento:'))
#minuto = int(input('ingrese un minuto de inicio del evento:'))
#duracion = int(input('ingrese la cantidad de minutos de duracion del evento:'))
#minutoFinal = minuto + duracion
#while minutoFinal >= 60:
#    minutoFinal = minutoFinal - 60
#    hora += 1
#    if hora >= 24:
#        hora = 0
#    
#if minutoFinal == 0:
#    print('la hora de finalizacion del evento sera: {}:{}0 hs.'.format(hora, minutoFinal))
#else:
#    print('la hora de finalizacion del evento sera: {}:{} hs.'.format(hora, minutoFinal))

#-------------------------------------------

