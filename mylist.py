@@ -0,0 +1,24 @@
My_List = [10,5,20,15]
print("Original List:",My_List)

#Access list elements
print("Frist element:",My_List[0])
print("Last element:",My_List[-1])

#Add elements to the list 
My_List.append(25)
print("After append:",My_List)

#Remove element from the list 
My_List.remove(5)
print("After removing 5:", My_List)

#Sort the list 
My_List.sort()
print("Sort List:",My_List)

#Reverse the list  
print("Reversed List:", My_List)
