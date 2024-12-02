lista1 = list()
lista2 = list()

with open('input1.txt', 'r') as f:
    line = f.readline()
    while line:
        tab = line.find('   ')
        lista1.append(int(line[:tab]))
        lista2.append(int(line[tab:]))
        line = f.readline()

lista1.sort()
lista2.sort()

distancia = 0
for i in range(len(lista1)):
    d = lista2[i] - lista1[i]
    distancia +=abs(d)

print(distancia)