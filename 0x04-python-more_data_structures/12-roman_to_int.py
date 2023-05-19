#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_numb = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    number = 0

    for x in range(len(roman_string)):
        if roman_numb.get(roman_string[x], 0) == 0:
            return (0)

        if (x != (len(roman_string) - 1) and
                roman_numb[roman_string[x]] < roman_numb[roman_string[x + 1]]):
            number += roman_numb[roman_string[x]] * -1

        else:
            number += roman_numb[roman_string[x]]
    return (number)
