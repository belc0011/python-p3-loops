#!/usr/bin/env python3

def happy_new_year():
    for i in range(11, 0, -1):
        if i != 1:
            print(i - 1)
            i -= 1
        else:
            print("Happy New Year!")
            i -= 1


def square_integers(int_list):
    squared_integers = [int * int for int in int_list]
    return squared_integers

def fizzbuzz():
    for i in range(1, 101, 1):
        if i == 1:
            print(i)
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
           

