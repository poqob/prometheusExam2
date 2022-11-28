# task 5

print("be ready you gonna enter X numbers manually :D\nthe X:  ")

sumOfNumbers = 0
howManyTimesYouWillAcceptNumber = int(input())
for i in range(0, howManyTimesYouWillAcceptNumber):
    sumOfNumbers += (float(input()))
print(sumOfNumbers/howManyTimesYouWillAcceptNumber)
