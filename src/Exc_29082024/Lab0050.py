 #issubset - test wheter every element in the set is present in other subset
 # i.e if all the element are present in another set then it is true or its false

set1={1,2,3,4,5}
set2={2,3,8}
subset=set2.issubset(set1)
print(subset)

#Set is also list..just unique list
set1=set(["Thetestingacademy","For","Thetestingacademy."])
print(len(set1))

for i in set1:
    print(i)

set1.add("Rihan")#add element this has no effect if element is already present
print(set1)
