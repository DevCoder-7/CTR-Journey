#!/usr/bin/env python3
from py_ecc import bn128
from ast import literal_eval
import os
import random

q = 21888242871839275222246405745257275088696311157297823662689037894645226208583
r = 21888242871839275222246405745257275088548364400416034343698204186575808495617

def recv_G1():
    raw = input('> ')
    return tuple(bn128.FQ(val) for val in literal_eval(raw))

def recv_G2():
    raw = input('> ')
    (x0, x1), (y0, y1) = literal_eval(raw)
    return (bn128.FQ2([x0, x1]), bn128.FQ2([y0, y1]))


def main():
    print("=== Cryptography sanity check ===")
    s = random.randint(1, r - 1)

    A = recv_G1()
    C = recv_G2()

    sA = bn128.multiply(A, s)
    sC = bn128.multiply(C, s)

    lhs = bn128.pairing(C, sA)
    rhs = bn128.pairing(sC, A)

    if lhs == rhs:
        print("Good, you passed the check!")
    else:
        with open("flag.txt") as f:
            print(f.read().strip())

if __name__ == "__main__":
    main()