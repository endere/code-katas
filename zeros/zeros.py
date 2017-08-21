def move_zeros(data):
    temp_list = [i for i in data if i != 0 or type(i) == bool]
    return temp_list + [0 for i in range(len(data) - len(temp_list))]
