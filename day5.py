import math
def find(lista, valor):
    try:
        return lista.index(valor)
    except ValueError:
        return -1


with open("input5.txt") as file:
    input_rules = []
    input_order = []
    for line in file:
        if "|" in line.rstrip():
            r = line.rstrip()
            input_rules.append((r[:2], r[3:]))
        elif "," in line.rstrip():
            r = line.rstrip()
            input_order.append(r.split(","))

    nulas = []
    for i, updates in enumerate(input_order):
        for rule in input_rules:
            index_a = find(updates, rule[0])
            index_b = find(updates, rule[1])
            if index_a >= 0 and index_b >= 0:
                if index_a > index_b:
                    nulas.append(i)
                    break

    valid_updates = [element for i, element in enumerate(input_order) if i not in nulas]
    #find middle page
    sum_middle = 0
    for v_update in valid_updates:
        long = len(v_update)
        center_index = int(math.ceil((long-1)/2))
        # print(f"long: {len(v_update)} -- medio: {center_index} -- valor medio: {v_update[center_index]}")
        # print(f"v_update: {v_update}")
        
        # print(f"medio:{int(v_update[center_index])}")
        sum_middle += int(v_update[center_index])


    print(f"part1: {sum_middle}")        
    # print(f"input_order: {input_order}")
    # print(f"nulas: {nulas}")
    # print(f"validas: {valid_updates}")


