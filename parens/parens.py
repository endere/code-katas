

def parens(num, the_str='()'):
    the_set = set()
    if num == 1:
        return [the_str]
    else:
        for i in range(len(the_str) + 1):
            the_set.add(the_str[:i] + '()' + the_str[i:])
        for i in the_set:
            temp_list = parens(num - 1, i)
            if type(temp_list) == set:
                the_set = the_set | temp_list
    return the_set


def workaround(num):
    output = list(parens(num))
    to_return = []
    for i in output:
        if len(i) == num * 2:
            to_return.append(i)
    return to_return


if __name__ == '__main__':
    print(workaround(8))
