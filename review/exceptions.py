#Execptions - son errores detectados durante la ejecución del programa (manejo de errores)
#try - intentar
courses = ['JavaScript', 'Python']
try:
    courses[20]
except IndexError:
    print('Error en el índice, no existe courses[20]')
else:
    print('Sin errores')
finally:
    print('Pase lo que pase, siempre me ejecuto')