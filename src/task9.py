# task 9
from enum import Enum


class Months(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class Seasons(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


def season(x):
    if (x < 6 and x > 2):
        return Seasons(1).name
    elif (x < 9 and x > 5):
        return Seasons(2).name
    elif (x < 12 and x > 8):
        return Seasons(3).name
    else:
        return Seasons(4).name


while (True):
    x = int(input())
    print("the month : {}".format(Months(x).name))
    print("season of the month : {}".format(season(x)))
