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