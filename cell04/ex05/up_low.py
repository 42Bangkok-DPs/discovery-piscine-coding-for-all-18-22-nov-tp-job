#!/usr/bin/env python3

word = input("")

new_word = ""
for char in word:
    if char.isupper():
        new_word += char.lower()
    else:
        new_word += char.upper()

print(new_word)