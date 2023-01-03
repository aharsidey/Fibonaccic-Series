
list1 = [1, 1]

# 1 1 2 3 5 8 13 21 34 55 89

for i in range(11):
    new_num = (list1[-1]) + (list1[-2])

    list1.append(new_num)

for j in list1:
    print(str(j), end=" ")
