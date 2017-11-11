from xml.etree.ElementTree import parse
import json
import csv

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

#work with XML
file_xml = parse('data.xml')
for item in file_xml.findall('nombre'):
    print(item.text)

#work with JSON
with open('data.json') as d:
    data = json.load(d)

print(data)
print(data['country'][0]['country_1'])

#work with CSV
file_csv = open('data.csv', 'w')
csv_data = csv.writer(file_csv) #write in the file
contacts = [['Xiomara', 435678922] ,['Juliet', 945687344] ,['Sandor', 354356789]]
print(contacts)
for item in contacts:
    csv_data.writerow(item)
file_csv.close()

doc_csv = open('data.csv', 'r')
document = csv.reader(doc_csv)
''' print(document)
    print(list(document)) --->debugger'''
for(name , number) in document:
    print(name, number)
doc_csv.close()