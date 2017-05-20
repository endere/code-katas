
"""Kata: Roman Numerals Decoder
kyu 4
#1 Best Practices Solution by mgalang, frkntrn, pomps

def solution(roman):
    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total

#2 Best Practices Solution by c4po
def solution(roman):
    d={'I':1, 'V':5 ,'X':10, 'L':50 ,'C':100, 'D':500,'M':1000}

    return reduce(lambda x,y: x+y if x>=y else y-x , (d[c] for c in roman))
"""



def solution(roman):
    """code for parsing a roman numeral into a number"""
    final = 0;
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman) - 1):
        if values[roman[i]] < values[roman[i + 1]]:
            final -= values[roman[i]]
            continue
        final += values[roman[i]]
    final += values[roman[-1]]
    return final
