def running_median(the_list):
    total = the_list[0]
    running_list = []
    for i in range(1, len(the_list)):
        running_list.append(the_list[i])
        yield find_median(running_list)

def find_median(median_list):
    # print(median_list)
    median_list = sorted(median_list)
    if len(median_list) % 2 == 0:
        # print(median_list[int((len(median_list) / 2) - .5)] + median_list[int((len(median_list) / 2) + .5)])
        return (median_list[int((len(median_list) / 2) - .5)] + median_list[int((len(median_list) / 2) + .5)]) / 2
    else:
        return float(median_list[int(len(median_list) / 2)])


if __name__ == '__main__':
    data = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print([i for i in running_median(data)])
    gen = running_median(data)
    for i in range(len(data) - 1):
        print(next(gen))

    # print(array)





  #    def in_order(self):
  #       """Generator function that yields values from tree in order."""
  #       """Get our bst back in order."""
  #       current = self.root
  #       the_list = []
  #       seen_parents = []
  #       while current:
  #           if current.left is None and current.right is None or current in seen_parents:
  #               yield current.value
  #           else:
  #               seen_parents.append(current)
  #               the_list = [current.left, current, current.right] + the_list
  #               the_list[:3] = [x for x in the_list[:3] if x is not None]
  #           try:
  #               current = the_list.pop(0)
  #           except IndexError:
  #               current = None


  # data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  #   test_tree = BinarySearchTree(data)
  #   # print('depth:', test_tree.depth())
  #   array = [i for i in test_tree.post_order()]
  #   print(array)
  #   # tree_two = BinarySearchTree(i for i in test_tree.in_order())
  #   # thing = test_tree.in_order()
  #   # print(next(thing))
  #   # print(i for i in test_tree.in_order())

  #   test_array = []
  #   test_generator = test_tree.post_order()
  #   while len(test_array) < test_tree.size():
  #       test_array.append(next(test_generator))
  #       print(test_array)