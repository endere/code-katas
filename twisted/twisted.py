
def compute_sum(number):
    pass

def compute_digit(number):
    if number == 1:
        return number
    else:
        return number + compute_digit(number - 1)


if __name__ == '__main__':
    print(compute_sum(10))