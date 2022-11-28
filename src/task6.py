# task 6

print("enter a number to obtain its price with VAT")
fee = float(input())
print("enter VAT tax rate:")
VAT = float(input())

price = fee*(100+VAT)/100
print("price: {}$".format(price))
