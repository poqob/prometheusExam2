# task 4

print("please enter number to calculate wanted percent: ")
g = input()
g = float(g)

print("please enter a number in range 0-100 to calculate percent of last entered number: ")
y = input()
y = float(y)
while (True):
    if (y < 0):
        print("please enter valid number which must be positive")
        y = input()
        y = float(y)
    break
print("the result: {}".format((g*y/100)))
