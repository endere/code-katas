
def compute_sum(number):
    print(number)
    if len(str(number)) == 1:
        print('here')
        return compute_digit(number)
    sum = 0
    for i in range(int(str(number)[0]), 0, -1):
        sum += 1 + compute_sum(int('9' + ('0' * (len(str(number)) - 2))))
    sum += compute_sum(int(str(number)[1:]))
    return sum

def compute_digit(number):
    if number == 1 or number == 0:
        return number
    else:
        return number + compute_digit(number - 1)


if __name__ == '__main__':
    print(compute_sum(11))