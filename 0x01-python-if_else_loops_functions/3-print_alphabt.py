#!/usr/bin/python3

"""Print the ASCII alphabet in lowercase, excluding 'q' and 'e', not followed by a new line."""
for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        print("{}".format(chr(letter)), end="")
