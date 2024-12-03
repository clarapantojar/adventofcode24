import re
#mul({},{})
def mul(a,b):
    return a*b

with open('input3.txt', 'r') as f:
    content = f.read()
    resultado = 0
    regrex1 = '(mul\([0-9]{1,3}\,[0-9]{1,3}\))'
    regrex2 = '(mul\([0-9]{1,3}\,[0-9]{1,3}\))|(do\(\))|(don\'t\(\))'
    multiplicaciones = re.findall(regrex2, content)
    flag_enable = True
    for multiplicacion in multiplicaciones:
        #resultado += eval(multiplicacion) #part1
        #parte 2
        operacion = ",".join(string for string in multiplicacion if (len(string) > 0))
        if(flag_enable and "mul" in operacion ):
            resultado += eval(operacion)
        elif "don't" in operacion:
            flag_enable = False
        elif "do()" in operacion:
            flag_enable = True
        #fin parte 2

print(f"resultado: {resultado}")