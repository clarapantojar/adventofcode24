import re

input = open("input9.txt")
line = input.read()
input.close()
line = line.replace('\n', '')

out_temp = ""
cont_id = 0
for i, char in enumerate(line):
    if i % 2 == 0:
        #id
        if cont_id == 0:
            out_temp += (f"0" * int(char))
        else:
            out_temp += (f"{cont_id}" * int(char))
        cont_id += 1
    else:
        #space
        out_temp += ("." * int(char))

pos_dot = [i for i, val in enumerate(out_temp) if val == "."]
pos_content = [i for i, val in enumerate(out_temp) if val != "."]
len_content = len(pos_content)
# print(out_temp)
# print(type(out_temp))
out = list(out_temp.strip())
# print(out)

# print(pos_dot)
# print(pos_content)

pos_dot.sort(reverse = True)
flag_changes = True
disk = "".join(out)
while flag_changes:
    pos_last_content = pos_content.pop()
    pos_first_dot = pos_dot.pop()
    if pos_first_dot > pos_last_content:
        order_disk = disk[:len_content]
        order_out = out[:len_content]
        break
    # print(f"pos_last_content:{pos_last_content}")
    # print(f"pos_first_dot:{pos_first_dot}")
    change = out_temp[pos_last_content]
    # print(f"change:{change}")
    out[pos_first_dot] = change
    out[pos_last_content] = "."
    disk = "".join(out)
    # print(f"{i} - {disk}")

# print(f"order_disk: {order_disk}")
# print(f"disk: {disk}")
# print(f"out: {out}")
# print(f"order_out: {order_out}")

checksum = 0
for i, val in enumerate(order_out):
    checksum += int(val) * i

print(checksum)

    