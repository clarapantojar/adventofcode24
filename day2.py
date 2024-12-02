def validar (a, b, increasing):
    if increasing:
        if b <= a:
            return False
        if (b - a) > 3:
            return False
    else:
        if b >= a:
            return False
        if (a - b) > 3:
            return False
        
    return True

def analyze(arr_element):
    x = 0
    y = 1
    increasing = True if arr_element[x] < arr_element[y] else False
    for i in range(1, len(arr_element)):
        if not validar(arr_element[i-1], arr_element[i], increasing):
            return False
    return True

safes = 0
safesDumper = 0
with open('input2.txt', 'r') as f:
    for line in f:
        # PART 1
        arr = line.split()
        arr = list(map(int, arr))
        if(analyze(arr)): #part1
            safes+=1
            safesDumper+=1
        else: #part2
            for i in range(len(arr)):
                new_arr = arr[:i]+arr[i+1:]
                if(analyze(new_arr)):
                    safesDumper+=1
                    break

print(f"seguras: {safes}")
print(f"seguras2: {safesDumper}")