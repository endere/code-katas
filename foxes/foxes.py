"""Kata: Tribonacci Sequence
kyu 6
#1 Best Practices Solution by Blind4Basics

NO_BOX          = r'[^\[\]]'
FOX_OUT_PATTERN = re.compile(r'(.*\])?{0}*F{0}*(.*\[)?'.format(NO_BOX))    # do you find some pattern like "(...])?xxxFxxx([...)?", "x" being any character except "[" or "]"
CARNAGE_PATTERN = re.compile(r'\[{0}*\]|{0}*'.format(NO_BOX))              # matches the boxes with borders or the free space between boxes

def hungry_foxes(farm):
    isFoxOut = bool(FOX_OUT_PATTERN.match(farm))
    
    def eatTheCocotte(m):
        s = m.group(0)
        return re.sub(r'[^F\[\]]', '.', s) if (s and s[0] != "[" and isFoxOut) or "F" in s else re.sub(r'[^C\[\]]', '.', s)
    
    return CARNAGE_PATTERN.sub(eatTheCocotte, farm)

#2 Best practices Solution by siebenschlaefer

import re

def hungry_foxes(farm):
    eat_chicken = lambda match: match.group(0).replace('C', '.')
    farm = re.sub(r'\[[.CF]*F[.CF]*\]', eat_chicken, farm)
    if re.search(r'F[.C]*(?=\[|$)', farm):
        farm = re.sub(r'[.CF]*(?=\[|$)', eat_chicken, farm)
    return farm


Note from Erik: At first I was ashamed of this code for being far from
optimal... which it is. But looking at the best practice codes, I cannot
even begin to understand what's going on there...
"""



def hungry_foxes(farm):
    night_farm = list(farm)
    danger = True  
    foxes_outside = False
    if "F" not in farm:
        return farm
    for x in range(len(night_farm)):
        if night_farm[x] == "[":
            danger = False
            last_fence = x
        elif night_farm[x] == "]":
            danger = True
        elif night_farm[x] == "F" and danger == True:
            foxes_outside = True
    if foxes_outside == False:
        danger = False
    for x in range(len(night_farm)):
        if night_farm[x] == "C" and danger == True:
            night_farm[x] = "."
        elif night_farm[x] == "[":
                danger = False
                last_fence = x
        elif night_farm[x] == "]":
            if foxes_outside == True:
                danger = True
            else:
                danger = False
        elif night_farm[x] == "F" and danger == False:
            danger = True
            for i in range(last_fence, x):
                if night_farm[i] =="C":
                    night_farm[i] = "."
    return ''.join(night_farm)
  
  