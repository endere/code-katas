"""Kata: divisible by 6
kyu 6
#1 Best Practices Solution by TheSoulReaper

def is_divisible_by_6(s):
    return [str(int(b)) for b in [s.replace('*',i) for i in '0123456789'] if int(b)%6==0 and int(b) !=0]
"""





def is_divisible_by_6(s):
    """Replace the * with 0-9. For each new created number, if it is divisible by 6, return it as part of a list"""
    final = []
    for i in range(10):
        temp_list = list(s)
        temp_list[list(s).index('*')] = '%s' % i
        if int(''.join(temp_list)) % 6 == 0 and int(''.join(temp_list)) is not 0:
            final.append(''.join(temp_list))
            if final[-1][0] == '0':
                final[-1] = final[-1][1:]
    return final
    