set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}

print("set 1:",set1)
print("set2:",set2)

#Access the elemnets 
print("/nElement of the set 1:")
for  element in set1:
 print(element)

print("/nElemnet of the set2:")
for element in set2:
 print(element) 

#Union of set 
union_set = set1.union(set2)
print("/nUnion of the set 1 and set 2:",union_set)

#Intersection of sets 
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Difference of sets
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 - Set1):", difference_set2)
