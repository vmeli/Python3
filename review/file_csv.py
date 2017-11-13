import csv

data = [['Xiomara', 435678922],['Juliet', 945687344],['Sandor', 354356789]]

with open('data.csv', 'w') as archivo:
  lineas = [','.join(map(str, elemento)) for elemento in data]
  archivo.write('\n'.join(lineas))


input_csv = open('data.csv', 'r')
document = csv.reader(input_csv)

for(name , number) in document:
    print(name, number)

input_csv.close()