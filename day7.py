from itertools import product
import operator
def concat(a, b):
    return int(str(a) + str(b))

operators_p1 = {operator.add, operator.mul}
operators_p2 = {operator.add, operator.mul, concat}
total_part1 = 0
total_part2 = 0

def calibrate(elements, result, operators):
    operations = len(elements)-1    
    op_order_variations = list(product(operators, repeat = operations))

    for op_order in op_order_variations:
        res = elements[0]
        for i, op in enumerate(op_order):
            res = op(res, elements[i+1])
        if res == result:
            return result
    
    return 0

with open("input7.txt") as file:
    for line in file:
        pos_dots = line.index(':')
        result = int(line[:pos_dots])
        elements = [int(e) for e in line[pos_dots+1:].rsplit()]

        total_part1 += calibrate(elements, result, operators_p1)
        total_part2 += calibrate(elements, result, operators_p2)

    print(f"part 1: {total_part1}")
    print(f"part 1: {total_part2}")