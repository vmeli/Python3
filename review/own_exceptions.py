class Error(Exception):
    def __init__(self, x):
        print('Este fue el valor: ', x)

try:
    raise Error(20) #raise permite forzar a que ocurra una excepción específica
except Error:
    print('Error')


#http://docs.python.org.ar/tutorial/2/errors.html
#http://librosweb.es/libro/algoritmos_python/capitulo_12/excepciones.html