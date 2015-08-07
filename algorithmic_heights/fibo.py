#!/usr/bin/env python

def fibo(filename):
    """
    Given a file with an integer, returns the fibonacci number for Fn
    """

    # Take the number:
    with open(filename) as fi:
        number = int(fi.read().strip())

    # Print the number
    fibonacci_sequence = []

    i = 0
    while i <= 25:
        if i == 0:
            fibonacci_sequence.append(i)
        elif i == 1:
            fibonacci_sequence.append(i)
        else:
            fibonacci_sequence.append(fibonacci_sequence[i-2]+fibonacci_sequence[i-1])

        i += 1

    print(fibonacci_sequence[number])

if __name__ == "__main__":
    fibo('files/rosalind_fibo.txt')

