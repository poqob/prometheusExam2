# task 10
import re
import os


def controll():
    os.system("cls")
    isvalid = True
    sifre = input("sifre: ")

    if (len(sifre) < 7):
        print("the password lenght must be bigger than {} at least 7".format(len(sifre)))
        isvalid = False

    if (not (re.search("[a-z]", sifre))):
        print("the input must be contains at least one lower letter")
        isvalid = False

    if (not (re.search("[A-Z]", sifre))):
        print("the input must be contains at least one upper letter")
        isvalid = False

    if (re.search(" ", sifre)):
        print("the password can't contain any spaces")
        isvalid = False

    if (not (re.search("[$_@]", sifre))):
        print("the password must be contains any of them @:_:$ ")
        isvalid = False
    return isvalid


while (True):
    result = controll()
    print("\npassword is valid") if (
        result) else print("\npassword is not valid")
    x = input("\nenter to controll another password, q to exit.\n")
    if (x == 'q'):
        break
