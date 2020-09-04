'''
Peak finder is a simple algorithm that finds a local/global maxima in a list. 
This can be used for identifying specific pixes that are darker/lighter in an image. 
'''

def main():
  input_array = [3, 2, 21, 25, 5, 7, 1]

  brute_force(input_array)
  global_maxima(input_array)
  print("Using Divide and conquer")
  divide_and_conquer(input_array, 0, len(input_array))
  twoD_peak()

def brute_force(input_array):
  print("Using brute force")
  for index, element in enumerate(input_array):
    if index > 0 and index < len(input_array) - 1:
      if element > input_array[index - 1] and element > input_array[index + 1]:
        print(f"Local maxima: {element}")
        #break


def global_maxima(input_array):
  print("Using global maxima")
  index_of_maxima = 0
  maxima = input_array[0]
  for index, element in enumerate(input_array):
    if element > maxima:
      maxima = element
      index_of_maxima = index

  print(f"Local maxima using global maxima: {maxima}")
  return [maxima, index_of_maxima]

def divide_and_conquer(input_array, i, j):
  m = int((i + j)/2)
  if input_array[m] > input_array[m + 1] and input_array[m] > input_array[m - 1]:
    print(f"Local maxima {input_array[m]}") 
    return
  elif input_array[m + 1] > input_array[m]:
    divide_and_conquer(input_array, m, j)
  else: # input_array[m - 1] > input_array[m]:
    divide_and_conquer(input_array, i, m - 1)


def twoD_peak():
  input_array = []
  input_array.append([5, 6, 7, 0, 2, 1])
  input_array.append([5, 6, 7, 0, 3, 1])
  input_array.append([5, 6, 0, 4, 2, 1])
  input_array.append([5, 7, 7, 0, 2, 1])
  input_array.append([5, 6, 7, 2, 9, 1])
  input_array.append([5, 6, 7, 1, 2, 1])

  ''' Divide and conquer based on columns and then find global maxima for each column '''
  compute_2d_maxima(input_array, 0, len(input_array[0]))

def compute_2d_maxima(input_array, i, j):

  middle_column = int((i + j)/2)
  middle_column_values = []

  for row in input_array:
    middle_column_values.append(row[middle_column])

  return_values = global_maxima(middle_column_values)
  column_maxima = return_values[0]
  index_of_column_maxima = return_values[1]

  #print("{}, {}, {}".format(middle_column_values, column_maxima, index_of_column_maxima))

  if input_array[index_of_column_maxima][middle_column - 1] < column_maxima > input_array[index_of_column_maxima][middle_column + 1]:
    print("2D Maxima: i: {}, j: {}, v: {}".format(index_of_column_maxima, middle_column, column_maxima))
    return
  elif input_array[index_of_column_maxima][middle_column - 1] > column_maxima:
    compute_2d_maxima(input_array, i, middle_column - 1)
  else: # input_array[index_of_column_maxima][middle_column + 1] > column_maxima:
    compute_2d_maxima(input_array, middle_column + 1, j)

main()