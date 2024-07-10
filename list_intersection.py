def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1,2,3,4,5,5,5,5,5,5,5]
list2 = [4,5,6,7,8,8,8,8,8,8,8]
intersection = list_intersection(list1, list2)
print(set(list1))
print(intersection)
