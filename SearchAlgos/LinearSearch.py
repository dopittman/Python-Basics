# Basic Linear Search

def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        print(search_list[idx])
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} not in list".format(target_value))


# uncomment the lines below to test...
values = [54, 22, 46, 99]
print(linear_search(values, 22))


# Linear Search with catch if the target is not in the data
number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33

def linear_search_w_catch(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))



try:
  # Call the function below...
  result = linear_search(number_list, 100)
  print(result)

except ValueError as error_message:
  print("{0}".format(error_message))


#  Linear search with multiple targets
# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

#Linear Search Algorithm
def linear_search_w_multiple_hits(search_list, target_value):
  #   Create empty list to hold indexes of hits
  matches = []
  # Loops through search_list looking for the target
  for idx in range(len(search_list)):
    #   checks if the current index equals target value
    if search_list[idx] == target_value:
      #   appends the index to the matches list
      matches.append(idx)
  #  If matches == true, ie. Not Empty
  if matches:
    # then return the matches list containing the indexes that matched target
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)


# Linear Search that returns highest value's index
# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
def linear_search_w_highest_value(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)

