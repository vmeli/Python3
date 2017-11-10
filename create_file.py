import json

#import ---> trae un pedazo de code(librería)
#from math import  sqrt ---> trae solo la función sqrt de la librería math
def create_file(name):
    file = open(name, 'w')
    file.close()

def write_file(name):
    file = open(name,'a') #antes de reescribir se considera append
    file.write('Londres\n')
    file.write('EE.UU')

def read_file(name):
    file = open(name,'r')
    line = file.readline()
    while line != '':
        print(line)
        line = file.readline()
    file.close()

create_file('data.txt')
write_file('data.txt')
read_file('data.txt')

#work with json
with open('data.json') as d:
    data = json.load(d)

print(data)
print(data['country'][0]['country_1'])