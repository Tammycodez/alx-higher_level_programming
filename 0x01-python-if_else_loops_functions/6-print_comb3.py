#!/usr/bin/python3
for i in range(100):
    for int(i / 10) != 1 % 10 and int(i / 10) < i % 10:
        print("{}{}".format(int(i / 10), i % 10), end="")
        if (i != 89):
            print(", ", end="")
