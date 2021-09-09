#!/usr/bin/python3
from calculator_1 import (
        add,
        sub,
        mul,
        div
        )

if __name__ == '__main__':
    a = 10
    b = 5
    print("{0} + {1} = {2}\n{0} - {1} = {3}\n{0} * {1} = {4}\n{0} / {1} = {5}"
          .format(
                a,
                b,
                add(a, b),
                sub(a, b),
                mul(a, b),
                div(a, b),
                ))
