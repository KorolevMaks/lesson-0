my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
b = 0
while my_list[-1]:
    if b < 12:
        if my_list [b] > 0 or my_list [b] == 0:
            if my_list [b] == 0:
                b = b + 1
            print(my_list[b])
            b = b + 1
        else:
            continue
    else:
        break
print("end")
