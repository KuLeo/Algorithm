from random import random
from time import perf_counter
from math import sqrt
import re


def monte_carlo(point: int):
    start = perf_counter()
    counter = 0

    print("Counting, wait a minute...")
    for i in range(point):
        x, y = random(), random()
        dis = sqrt(x ** 2 + y ** 2)
        if dis <= 1.0:
            counter += 1

    # pi : 4 = counter : point => 4 * counter = pi * point
    pi = 4 * counter/point
    print("{:.6f}".format(pi))
    print("Run time: {:.6f} seconds".format(perf_counter() - start))


if __name__ == '__main__':
    user_input = input("Please input integer number...\n")
    pattern = "^[0-9]+$"
    result = re.match(pattern, user_input)
    if result:
        monte_carlo(int(user_input))
    else:
        print("Your input not a integer number.\n")
