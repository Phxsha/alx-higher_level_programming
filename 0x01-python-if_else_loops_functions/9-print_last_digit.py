#!/usr/bin/python3
def print_last_digit(number):
    for n in number:
        n = abs(number) % 10
        if number < 0:
            n = -n
            print(n)
        else:
            print(n)
    return(n)
