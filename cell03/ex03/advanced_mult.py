#!/usr/bin/env python3

number = 0
while number <= 10:
    print(f"Table de {number}:", end=" ")
    result = 0
    while result <= 10:
        print(f"{number * result:3}", end=" ")
        result += 1
    print()
    number += 1