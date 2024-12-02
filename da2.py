safes = 0
totalL = 0
with open('input2.txt', 'r') as f:
    line = f.readline()
    while line:
        totalL = totalL + 1
        arr = line.split()
        print(arr)
        segura = True
        i = 1
        creciente = int(arr[0])-int(arr[1]) < 0
        print(f"creciente:{creciente}")
        while segura and i <len(arr):
            if(creciente):
                diff = int(arr[i]) - int(arr[i-1])
            else:
                diff = int(arr[i-1]) - int(arr[i])
            
            segura = (diff != 0 and diff > 0 and diff < 4)
            i = i + 1
            print(f"Diferencia: {diff} - Segura:{segura}")

        
        if(segura):
            print("linea segura")
            safes = safes + 1
        
        line = f.readline()

print(f"seguras: {safes}")
print(f"total lineas: {totalL}")