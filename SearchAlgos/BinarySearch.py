
# Unoptimized Binary search that copies the array each time
# define binary_search()
def binary_search(sorted_list, target):
  #   if list is empty, return 'value not found'
  if not sorted_list:
    return 'value not found'
  # vars for middle index and middle index value
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]

  # if middle index is target, return mid_index
  if mid_val == target:
    return mid_idx
  # if middle index value is > target, recursively call binary search again on the left half of the arrray
  if mid_val > target:
    #   sorted_list[:mid_idx] will return everything before mid_idx
    #   [:index] returns everything before index
    left_half = sorted_list[:mid_idx]
    # recursively calls binary_search on the left_half array
    return binary_search(left_half, target)
  if mid_val < target:
    # [mid_idx+1:] will return everything higher than the mid_idx
    # [index:] will return everything from index and higher, including index, hence the +1 to remove index from the
    # right_half array
    right_half = sorted_list[mid_idx+1:]
    # recursively calls binary_search on the right_half array
    result = binary_search(right_half, target)
    # if value is not found at all then return 'value not found'
    if result == "value not found":
      return result
    else:
      return result + mid_idx + 1

# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))



# Optimized Binary Search with Pointers

def binary_search(sorted_list, left_pointer, right_pointer, target):
  # this condition indicates we've reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return "value not found"

  # We calculate the middle index from the pointers now
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]

  if mid_val == target:
    return mid_idx
  if mid_val > target:
    # we reduce the sub-list by passing in a new right_pointer
    # the middle index now becomes the right pointer
    return binary_search(sorted_list, left_pointer, mid_idx, target)
  if mid_val < target:
    # we reduce the sub-list by passing in a new left_pointer
    # the middle index now becomes the left pointer
    return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))