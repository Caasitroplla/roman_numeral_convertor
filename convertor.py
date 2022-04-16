import math

def convert_to_integer(roman_numeral: str) -> int:
    romans_dict = \
        {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'G': 5000,
            'H': 10000
        }
    roman_numeral.upper()
    res = 0
    n = len(roman_numeral)
    for (idx, c) in enumerate(roman_numeral):
        if idx < n - 1 and romans_dict[c] < romans_dict[roman_numeral[idx+1]]:
            res -= romans_dict[c]
        else:
            res += romans_dict[c]

    return res

def convert_to_roman(integer: int) -> str:
    romans_dict = \
        {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            5000: 'G',
            10000: 'H'
        }

    div = 1
    while integer >= div:
        div *= 10

    div /= 10

    res = ''

    while integer:
        # main significant digit extracted into lastNum
        lastNum = int(integer / div)

        if lastNum <= 3:
            res += (romans_dict[div] * lastNum)
        elif lastNum == 4:
            res += (romans_dict[div] + romans_dict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romans_dict[div * 5] + (romans_dict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romans_dict[div] + romans_dict[div * 10])

        integer = math.floor(integer % div)
        div /= 10

    return res