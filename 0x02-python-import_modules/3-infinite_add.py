#!/usr/bin/python3
import sys
if __name__ == "__main__":
    usr_input = sys.argv[1:]
    total = 0
    for arg in usr_input:
        total += int(arg)
    print("{}".format(total))
