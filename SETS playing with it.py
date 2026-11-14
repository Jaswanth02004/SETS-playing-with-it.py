#ONE
'''
a = {1,2,2,3,4}
print(a)    #OUTPUT = {1,2,3,4} CUZ NO repeated values IN SETS

b = [1,2,3,4,4]
print("Beforeconversion:",b)    #[1,2,3,4,4]
print("After conversion:",set(b))   #[1,2,3,4]
'''

#METHODS ON SETS
#TWO
'''
a = {1,2,3,4}
a.add("d")
print(a)
'''

#UNION
a = {1,2,3,4,5}
b = {1,2,3,4,6}
print(a,b)
print("Union=",a.union(b))  #AKA " | " for UNION
print("intersection=",a.intersection(b))    #AKA " & " for INTERSECTION
print("difference", a.difference(b))
print(a<=b)
