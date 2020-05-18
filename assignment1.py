level = int(input("Enter a level number: "))
number = 1
space = level - 1
order = 1
current_order = order
while level > 0:
    line = " " * space + f"{number}" + " "
    number += 1
    current_order -= 1
    while current_order > 0:
        line += f"{number}" + " "
        number += 1
        current_order -= 1
    print(line)
    order += 1
    current_order = order
    level -= 1
    space = level - 1

#    01
#   02 03
#  04 05 06
# 07 08 09 10
#11 12 13 14 15
