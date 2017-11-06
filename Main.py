# VARIABLES
a = 'Sandor'
b = 'Negro'
c = 'Yesenia'
print('{} tiene dos perros llamados: {} y {}'.format(c,a,b))

r = 'a'
r = 10.2
print(r)
print(int(r))

t = True
f = False

# COMENTARIOS
# se puede comentar con #, para comentar por bloque con '''   ''''
#if else anidados
#if elif
datoA = int(input('Ingresa un número 1: '))
datoB = int(input('Ingresa un número 2: '))
print(datoA,datoB)

if (datoA > datoB) :
    print('El número mayor es:',datoA)
else:
    print('El número mayor es:', datoB)

datoA1 = int(input('Ingresa un número 1: '))
datoA2 = int(input('Ingresa un número 2: '))
datoA3 = int(input('Ingresa un número 3: '))

if (datoA1 == datoA2 == datoA3):
    print('Todos los números son iguales')

# CICLO WHILE
x = 1
while (x < 10):
    print(x)
    x += 1

y = 10
while (y > 0):
    print(y)
    y -=1

#CICLO FOR
x1 = 1
for x1 in range(1,10):
    print(x1)

for x2 in range(0,10,2):
    print(x2)

for x3 in range(10,0,-1):
    print(x3)

name = 'Sandor'
for letter in name:
    print(letter)

datos = ['dato1',['dato2']],['dato3']
for item in datos:
    print(item)

#FUNCIONES
def saludo():
    print('Bienvenido a Python')

saludo()

def cuadrado(n):
    print(n*n)

cuadrado(20)

def suma(a,b):
    return a + b
print(suma(3,2))

#TUPLAS