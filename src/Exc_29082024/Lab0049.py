#SET
#Collection of unique elemet {}
list_of_uniq_item={1,2,3,4,3,5,4,1}
print(list_of_uniq_item)

#if you want to remove duplicate convert them into the set
list1=[45.2,33,33,45,21]
set1=set(list1)
print(set1)

#
t=("Thetestingacademy","For","Thetestingacademy")
print(t)
print(set(t))

#Set with uniun
set1={1,2,3}
set2={4,5,6}
my_set=set1.union(set2)
print(my_set)

#set with intersection
set1={1,2,3,4,5}
set2={4,5,6,7,8}
my_set=set1.intersection(set2)
print(my_set)

my_set=set1.difference(set2)
print(my_set)
