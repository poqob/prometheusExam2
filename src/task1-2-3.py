# task one-two-three
#string, list, number
import random as rand

text = "i am an string hello to group prometheus !"
adj = "hehe boi {sign}"
text = text+" "+adj.format(sign='&')
print(text.upper())
######################################################


listexample = []
alphabeth = "A B C D E F G H I K L M N O P Q R S T V X Y Z"
alphabeth = alphabeth.replace(" ", "")

generatedText = "{head}"
for i in range(1, 15):
    generatedText += rand.choice(alphabeth)
    if (i % 4 == 0):
        listexample.append(generatedText[i-4:i])

print(generatedText.format(head='generated clause is: '))
print("parts of generated clause: "+listexample.__str__())

# number and len()-apply for task two- example
lenghtOfAlphabeth = len(alphabeth)
print("all letters are in alphabeth: {alphabethCount}".format(
    alphabethCount=lenghtOfAlphabeth))

print("lenght of alphabet numer is positive") if (  # apply for task three
    lenghtOfAlphabeth > 0) else print("number is negative")
