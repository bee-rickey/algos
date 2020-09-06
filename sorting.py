
def main():
  input_array = [1, 8, 3, 2, 9, 6, 71]
  basic_insertion_sort(input_array)
  input_array = [1, 8, 3, 2, 9, 6, 71]
  binary_insertion_sort(input_array)
  input_array = [1, 8, 3, 2, 9, 6, 71]
  merge_sort(input_array)


def basic_insertion_sort(input_array):
  for index, data in enumerate(input_array):
    if index == 0:
      continue

    j = index
    
    while j > 0 :
      if int(input_array[j]) < int(input_array[j - 1]):
        temp = input_array[j-1]
        input_array[j - 1] = input_array[j]
        input_array[j] = temp
      else:
        break;
      
      j = j-1

  print("Using basic insertion sort: {}".format(input_array))

def binary_search(i, j, input_array, search_element):

  if i == j:
    if input_array[i] > search_element:
      return i;
    else:
      return i + 1

  if i > j:
    return i

  middle = int((i + j)/2)  

  if search_element < input_array[middle]:
    return binary_search(i, middle - 1, input_array, search_element)
  elif search_element > input_array[middle]:
    return binary_search(middle + 1, j, input_array, search_element)
  else:
    return middle

def binary_insertion_sort(input_array):
  length_of_array = len(input_array)
  for index in range(1, length_of_array):
    value = input_array[index]
    index_to_insert = binary_search(0, index - 1, input_array, value)
    input_array = input_array[:index_to_insert] + [value] + input_array[index_to_insert:index] + input_array[index+1:]
  print(input_array)

def merge_sort(input_array):
  merge(input_array)
  print("Merge: {}".format(input_array))


def merge(input_array):
  if len(input_array) > 1:
    
    i = j = k = 0
    middle = int(len(input_array)/2)
    
    left_array = input_array[:middle]
    right_array = input_array[middle:]

    merge(left_array)
    merge(right_array)

    while i < len(left_array) and j < len(right_array):
      
      if left_array[i] < right_array[j]:
        input_array[k] = left_array[i]
        k += 1
        i += 1
      else:
        input_array[k] = right_array[j]
        k += 1
        j += 1
    
    while i < len(left_array):
      input_array[k] = left_array[i]
      k += 1
      i += 1
    
    while j < len(right_array):
      input_array[k] = right_array[j]
      k += 1
      j += 1


main()