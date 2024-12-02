listaIzq = list()
listaDcha = list()

# listaIzq = [3,4,2,1,3,3]
# listaDcha = [4,3,5,3,9,3]

with open('input1.txt', 'r') as f:
    line = f.readline()
    while line:
        tab = line.find('   ')
        listaIzq.append(int(line[:tab]))
        listaDcha.append(int(line[tab:]))
        line = f.readline()

listaIzq.sort()
listaDcha.sort()

distancia = 0
for i in range(len(listaIzq)):
    d = listaDcha[i] - listaIzq[i]
    distancia +=abs(d)

print("distancia: ", distancia)

similaridad = 0
for x in listaIzq:
    contador = listaDcha.count(x)
    similaridad += abs(x * contador)

print("similarity: ", similaridad)