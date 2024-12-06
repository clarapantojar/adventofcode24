def avanzar(direccion, row, col):
    if direccion == 'up':
        row -= 1
    elif direccion == 'right':
        col += 1
    elif direccion == 'left':
        col -= 1
    elif direccion == 'down':
        row += 1
    return row, col

def cambio_direccion(direccion, row, col):
    direcciones = ['up', 'right', 'down', 'left']
    index = direcciones.index(direccion)
    try:
        dir =  direcciones[index+1]
    except IndexError:
        dir =  direcciones[0]

    if dir == 'up': # 'left':col -= 1
        row -= 1
        col += 1
    elif dir == 'right': # 'up':row -= 1
        col += 1
        row += 1
    elif dir == 'left': # 'down':row += 1
        col -= 1
        row -= 1
    elif dir == 'down': # 'right':col += 1 
        row += 1
        col -= 1
    
    return dir, row, col
    
# def siguiente(x, y):
    

with open("input6.txt") as file:
    my_map = []
    
    row_ini = 0
    col_ini = 0
    
    row = 0
    for line in file:
        l = []
        col = 0
        for s in line.strip():
            if(s == '^'):
                row_ini = row
                col_ini = col
            l.append(s)
            col += 1
        row += 1
        my_map.append(l)

    tall_rows = len(my_map)
    wide_cols = len(my_map[0])
    direccion = 'up'
    row_next, col_next = avanzar('up', row_ini, col_ini)
    movimientos = 0
    continua = True
    while(
        col_next >= 0 and col_next <= wide_cols and
        row_next >= 0 and row_next <= tall_rows 
        and continua
    ):
        row_ini = row_next
        col_ini = col_next
        siguiente = my_map[row_next][col_next]
        if siguiente != '#':
            # avanzar
            if siguiente != "X":
                movimientos += 1
            my_map[row_ini][col_ini]  = "X"
            row_next, col_next = avanzar(direccion, row_next, col_next)
            if(
                (row_next == tall_rows and direccion == 'down') or
                (row_next == -1 and direccion == 'up') or
                (col_next == wide_cols and direccion == 'right') or
                (row_next == -1 and direccion == 'left')
            ):
                continua = False
        else:
            # cambio_direccion
            direccion, row_next, col_next = cambio_direccion(direccion, row_next, col_next)
        
        

        
    
    print(f"part1: {movimientos}")
    
