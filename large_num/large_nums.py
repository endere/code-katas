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

def last_multi(nums):
    power = 0
    for i in range(len(nums)):
        if i == 0:
            power = nums[-1 - i]
        elif i == len(nums) - 1:
            return last_digit(nums[0], power)
        else:
            power = nums[-1 - i] ** power


def find_mod(n1, n2):
    return n1 ** n2

if __name__ == '__main__':
    # print(last_digit(3, 6))
    # print(find_mod(3, 6))
    print(last_multi([3, 4, 2]))