import importlib
from mylib import myfunc

character = input("please input character: ")  # รับตัวอักษรจากผู้ใช้
rounds = int(input("How many turns you want to run: "))  # รับจำนวนรอบ

for i in range(1, rounds + 1):
    print(myfunc(character, i))
