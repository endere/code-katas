"""Four methods outlining a pyramid made from a string."""


def watch_pyramid_from_the_side(characters):
    """Return a string that shows the pyramid from the side."""
    try:
        if not isinstance(characters, str):
            return characters
        odds = []
        for i in range(1, len(characters) * 2, 2):
            odds.append(i)
        to_return = ''
        spacing = int((odds[-1] - 1) / 2)
        for i in range(len(characters)):
            to_return += ' ' * spacing + (characters[-1 - i] * odds[i]) + ' ' * spacing + '\n'
            spacing -= 1
        return to_return[:-1]
    except IndexError:
        return ''


def watch_pyramid_from_above(characters):
    """Return a string that shows the pyramid from above."""
    try:
        if not isinstance(characters, str):
            return characters
        odds = []
        for i in range(1, len(characters) * 2, 2):
            odds.append(i)
        to_return = ''
        cap = 0
        characters = 'X' + characters
        cap_flag = True
        for i in range(odds[-1]):
            temp = ''
            if cap < int(odds[-1] / 2 + 1) and cap_flag is True:
                cap += 1
            else:
                cap -= 1
                cap_flag = False
            flag = True
            count = 0
            for x in range(odds[-1]):
                if count < cap and flag is True:
                        count += 1
                elif count < int(odds[-1] / 2 + 1) and flag is True:
                    if x >= int(odds[-1] / 2 + 1):
                        flag = False
                else:
                    if odds[-1] - x >= cap:
                        pass
                    else:
                        count -= 1
                        flag = False
                if count < 1:
                    count = 1
                temp += characters[count]
            to_return += temp + '\n'
        return to_return[:-1]
    except IndexError:
        return ''


def count_visible_characters_of_the_pyramid(characters):
    """Return the amount of visible stones in the pyramid."""
    if not isinstance(characters, str):
        return -1
    total = 0
    for i in range(1, len(characters) * 2, 2):
        if i == 1:
            total += 1
        else:
            total += (i - 2) * 4 + 4
    if total == 0:
        return -1
    return total


def count_all_characters_of_the_pyramid(characters):
    """Return total number of stones in pyramid."""
    if not isinstance(characters, str):
        return -1
    total = 0
    for i in range(1, len(characters) * 2, 2):
        total += i * i
    if total == 0:
        return -1
    return total

if __name__ == '__main__':
  print(watch_pyramid_from_the_side(45))