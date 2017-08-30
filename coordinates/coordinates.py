def is_valid_coordinates(coordinates):
    try:
        two_nums = coordinates.split()
        if len(two_nums) != 2:
            return False
        if any(c.isalpha() for c in two_nums[0][:-1]):
            return False
        if any(c.isalpha() for c in two_nums[1]):
            return False
        num_one = float(two_nums[0][:-1])
        num_two = float(two_nums[1])
        if abs(num_one) <= 90 and abs(num_two) <= 180:
            return True
        return False
    except ValueError:
        return False


if __name__ == '__main__':
    print(is_valid_coordinates('28, -12'))