# task 7

list = []
while (True):
    x = int(input())
    if (x == 0):
        break
    list.append(x)
list.sort()
print("list was contain: {}".format(list))
