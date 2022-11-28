# task 8
import random as rand
list = []
times = 10
for i in range(0, times):
    list.append(rand.random()*100)
print("list is: {}".format(list))
print("avarage of list: {}".format(sum(list)/times))
