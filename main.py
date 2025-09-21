import importlib
from mylib import myfunc

if __name__ == "__main__":
    character = input("please input character: ")  # รับตัวอักษรจากผู้ใช้
    round = int(input(" How many turns you want to run: "))  # รับจำนวนรอบ

    for i in range(1, round + 1):
        print(myfunc(character, i))