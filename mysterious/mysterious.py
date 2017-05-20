"""Kata: Mysterious function
kyu 6
#1 Best Practices Solution by Unnamed

def get_num(n):
    return sum({'0': 1, '6': 1, '9': 1, '8': 2}.get(d, 0) for d in str(n))
"""



def get_num(n):
    """Return the number of holes in n."""
    count = 0
    list_from_n = [x for x in str(n)]
    for i in list_from_n:
        if i in ['0', '6','9']:
            count += 1
        elif i == '8':
            count += 2
    return count

    