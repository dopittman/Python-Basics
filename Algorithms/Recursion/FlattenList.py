# define flatten() below...

def flatten(my_list):
  # Create an empty list to hold the flattened list
  result = []

  # Loop through non-empty list
  for i in my_list:
    # Checks if the element 'i' is a list within my_list
    if isinstance(i, list):
      print("List Found!")
      # If the element is a list, then we call flatten on list 'i'
      flat_list = flatten(i)
      # Add the recusive variable to the total result
      result += flat_list
    else:
      #   Append any non-list elements to the result list
      result.append(i)

  return result



### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))
