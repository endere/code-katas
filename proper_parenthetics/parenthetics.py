"""A simple code implementing a queue to tell if a line of parentheses is open, closed, or balanced."""
from _que import Queue


def parenthetics(string):
    """Return 0 if balanced, 1 if open, -1 if closed. Function does not care about other characters in the string."""
    Q = Queue(list(string))
    open_count = 0
    while Q.size() > 0:
        par = Q.dequeue().value
        if par == '(':
            open_count += 1
        elif par == ')':
            open_count -= 1
            if open_count < 0:
                return -1
    if open_count > 0:
        return 1
    return 0


if __name__ == '__main__':
    string = '('

    print(parenthetics(string))