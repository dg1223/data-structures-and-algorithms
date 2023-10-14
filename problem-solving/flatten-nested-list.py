def flatten(my_list):
#   print("\nStarting function flatten()...")
  result = []
  for item in my_list:

    # RECURSIVE STEP
    if isinstance(item, list):			
      flat_list = flatten(item)
    #   print("flat_list from return statement = {0}".format(flat_list))      
      result += flat_list
    #   print("result after concat = {0}".format(result))

    # BASE CASE
    else: 
    #   print("item = {0}".format(item))
      result.append(item)
    #   print("result after append = {0}".format(result))
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))