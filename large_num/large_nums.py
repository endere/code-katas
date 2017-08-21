references = {
    0: 0,
    1: 1,
    2: [6, 2, 4, 8],
    3: [1, 3, 9, 7],
    4: [6, 4],
    5: 5,
    6: 6,
    7: [1, 7, 9, 3],
    8: [6, 8, 4, 2],
    9: [1, 9]
}

def last_digit(n1, n2):
    if n2 == 0:
        return 1
    num = references[n1 % 10] if type(references[n1 % 10]) == int else references[n1 % 10][n2 % 4] if len(references[n1 % 10]) == 4 else references[n1 % 10][n2 % 2]
    return num


    
if __name__ == '__main__':
    print(last_digit(2454, 2335))
    print(2454 ** 2335 )