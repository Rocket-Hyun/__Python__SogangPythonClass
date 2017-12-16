import operator

dict = {1:1, 2:2, 3:5, 4:4}

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
print(sorted_dict)
