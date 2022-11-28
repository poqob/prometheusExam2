# task 12
n = 3
t = 0
for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            t = t+i+j*k
        j += 1
    t = t+i**2
print(t)
