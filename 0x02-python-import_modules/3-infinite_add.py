#!/usr/bin/python3

import sys
from decimal import Decimal

if __name__ == "__main__":
    arguments = sys.argv[1:]  # Exclude the script name itself
    result = sum(Decimal(arg) for arg in arguments)

    print(result)
