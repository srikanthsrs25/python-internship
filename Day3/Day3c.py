# set and its operations

my_set = {1, 2, 3, 4, 5 , 1, 2 ,3 , 1 , 4 , 5, 2, 1} 
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([7, 8, 9])
print(my_set)
my_set.remove(3)
print(my_set)
my_set.discard(10) 
print(my_set)
my_set.pop()  
print(my_set)
my_set.clear()
print(my_set)
print(type(my_set))
#my_set [1] = 10  # This will raise an error because sets are unordered and do not support indexing
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))
print(my_set1.difference(my_set2))
print(my_set1.symmetric_difference(my_set2))
