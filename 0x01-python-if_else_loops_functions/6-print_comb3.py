#!/usr/bin/python3

for y in range(10):
    for z in range(y + 1, 10):
        print("{:d}{:d}".format(y, z), end=", " if y != 8 or z != 9 else "")
print()
