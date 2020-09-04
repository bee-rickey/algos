
def main():
  first_dict = {}
  second_dict = {}
  total_document_length = 0

  with open("document1.txt") as d:
    for line in d:
      for word in line.split(' '):
        if word.strip() not in first_dict.keys():
          first_dict[word.strip()] = 0
        total_document_length += 1
        first_dict[word.strip()] += 1

  with open("document2.txt") as d:
    for line in d:
      for word in line.split(' '):
        if word.strip() not in second_dict.keys():
          second_dict[word.strip()] = 0
        total_document_length += 1
        second_dict[word.strip()] += 1


  dot_product = 0
  for key, value in first_dict.items():
    if key in second_dict.keys():
      dot_product = dot_product + value * second_dict[key]

  similarity = float(dot_product)/float(total_document_length) if total_document_length != 0 else dot_product

  print("{}, {}, {}".format(dot_product, similarity, total_document_length))

main()