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

#TUPLAS(tuple) son inmutables
tupla = (1,'string',True,4.5)
print(tupla[2])

user = ('Sandor','sandor@gmail.com',7,'Lima')
print(user[1])

for item in user:
    print(item)

#example-tuplas
def post_data():
    name = 'Fulano'
    email = 'fulano@gmail.com'
    age = 20
    city = 'Lima'
    return (name, email, age, city)

def get_data(data):
    print(data[0],data[1])

person1 = post_data()
get_data(person1)

#LISTAS se pueden modificar
list = [1, 2, 3, 4, 5, 6, 7]

for item in list:
    print(item)

list.append(20)
print(list)

list[3] = 'added element'
print(list)

list.pop()
print(list)

list_A = [4, 5, 6, 7]
list_B = [1, 2, 3, 4]

list_A.extend(list_B)
print(list_A)

#eliminar un elemento por posición
del list_A[2]
print(list_A)

#eliminar un elemento por su valor
list_A.remove(3)
print(list_A)

#contar elementos repetidos
list_C = [7, 3, 3, 3, 5, 3]
print(list_C.count(3))

#ordenar elementos
list_C.sort()
print(list_C)

list_C.sort(reverse=True)
print(list_C)

#indice negativo
list_D = [4, 2, 8, 9]
print(list_D[-2])

#DICCIONARIOS key - value ---> para almacenar
users = {'Sandor': 20, 'Kika': 17, 'Xiomara': 23}
for name in users:
     print(name)

print(users['Xiomara'])
print(users.keys())
print(users.values())

''' limpiar diccionarios
users.clear() 
'''

users_students = users.copy()
print(users_students)
print(users_students.get('Sandor'))

#actualizar diccionarios
new_age = {'Sandor': 25}
users_students.update(new_age)
print(users_students)