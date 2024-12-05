import math
def find(lista, valor):
    try:
        return lista.index(valor)
    except ValueError:
        return -1

def middle_page(pages):
        long = len(pages)
        center_index = int(math.ceil((long-1)/2))
        middle = int(pages[center_index])
        return middle

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
    corrections_nules = []
    for i, updates in enumerate(input_order):
        rules_broke = 0
        for rule in input_rules:
            index_a = find(updates, rule[0])
            index_b = find(updates, rule[1])
            if index_a >= 0 and index_b >= 0:
                if index_a > index_b:
                    nulas.append(i)
                    rules_broke += 1
                    # break
        if rules_broke > 0:
            corrections_nules.append(rules_broke)
    
    valid_updates = [element for i, element in enumerate(input_order) if i not in nulas]
    invalid_updates = [element for i, element in enumerate(input_order) if i in nulas]


    #part1
    sum_middle = 0
    for v_update in valid_updates:
        sum_middle += middle_page(v_update)

    #part2
    for j, invalid_up in enumerate(invalid_updates):
        for k in range(corrections_nules[j]):
            for rule in input_rules:
                index_a = find(invalid_up, rule[0])
                index_b = find(invalid_up, rule[1])
                if index_a >= 0 and index_b >= 0:
                    if index_a > index_b:
                        temp = invalid_up[index_a]
                        invalid_up[index_a] = invalid_up[index_b]
                        invalid_up[index_b] = temp
                        break
    
    sum_middle_invalid = 0
    for in_update in invalid_updates:
        middle = middle_page(in_update)
        sum_middle_invalid += middle

    print(f"part1: {sum_middle}")
    print(f"part2: {sum_middle_invalid}")


