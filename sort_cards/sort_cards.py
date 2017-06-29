"""A function for sorting cards!"""


def sort_cards(arr):
    print(arr)
    """Use merge sort to sort the input of cards given."""
    reference_dict = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13
    }
    if len(arr) > 1:
        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]
        sort_cards(left_side)
        sort_cards(right_side)
        i = 0
        j = 0
        k = 0
        while i < len(left_side) and j < len(right_side):
            if reference_dict[left_side[i]] < reference_dict[right_side[j]]:
                arr[k]=left_side[i]
                i += 1
            else:
                arr[k]=right_side[j]
                j += 1
            k += 1
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1
        while j < len(right_side):
            arr[k]=right_side[j]
            j += 1
            k += 1
    return arr
