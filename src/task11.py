# task 11
import re

# fields
majors = {
    "0101": "electrical enginering",
    "0102": "civil engineering",
    "0103": "machine engineering",
    "0104": "mechatronics engineering"
}
ogrenimT = ""
girisyili = ""
bolum = ""
siralama = ""


def writer():
    print("lerning type: {}".format(ogrenimT))
    print("enroll year : {}".format("20"+girisyili))
    print("major : {}".format(bolum))
    print("rank : {}".format(siralama))


while (True):
    x = input("\nquerry a collage number: ")
    # x = "g210104016"
    if (x == 'q'):
        break
    if (not (re.search("[BGbg][0-9]", x) and len(x) == 10)):
        print("please enter valid collage number")
        continue

    if (x[0] == "b" or x[0] == "B"):
        ogrenimT = "session one"
    elif (x[0] == "g" or x[0] == "G"):
        ogrenimT = "session two"

    girisyili = x[1:3]
    bolum = majors[x[3:7]]
    siralama = x[7:]

    writer()
