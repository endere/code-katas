def move_zeros(data):
    temp_list = []
    for i in data:
        if i == 0:
            temp_list.append(i)
            data.remove(i)
    for i in temp_list:
        data.append(i)
    print(data)


if __name__ == '__main__':
    move_zeros([1, 2, 3, 0, 4, 0, 5, 6])