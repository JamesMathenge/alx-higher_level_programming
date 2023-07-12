#!/usr/bin/python3
"""Reads from standard input and computes metrics"""

import sys

lines_count = 0
total_file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
    }

try:
    for line in sys.stdin:
        lines_count += 1

        try:
            _, _, _, status_code, file_size = line.split(" ")
            status_code = int(status_code)
            file_size = int(file_size)
            total_file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
        except ValueError:
            pass

        if lines_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))
