#List- It is collection of item(Duplicates are allowed)
my_list =[1,2,3]
my_list2 =[1,True,"Pramod",12.34]#Same type and different type of data are allowed
print(my_list)
print(len(my_list))#lenght always start from 1

print(my_list[0])#index always start from 0
print(my_list[2])
#print(my_list[10])#list index out of range-exception

my_list[0]="Pramod" #changed the value of my_list
my_list[1]="Dutta"
#indexing
print("Element at index 0-",my_list[0])
print("element of index 1-",my_list[1])
print(my_list)
#To print in for loop
for element in my_list:
    print(my_list)
#range itself provide list

#append
my_list.append(4)#append object at end of the list
my_list.append(5 )#cant append element in bunch like(5,6,7,) it should only append one by one
my_list.append(4)#Duplicate can allowed
print(my_list)

#Extend- if you dont want to write function multiple time then use extend
my_list.extend([7,8,9])
print(my_list)
my_list.extend([10])#can add different datatype
print(my_list)
print(len(my_list))
#insert()- insert in the middle of the list
my_list.insert(5,"Umesh")
print(my_list )
print(len(my_list))
#we dont have replace funtion if you want to replace then ressign the value
my_list[1]="Amit"
print(my_list)#replaced "Dutta" by "Amit"
#
my_list.insert(-1,"Romi")
print(my_list)


#Remove
my_list.remove(my_list[1])
print(my_list)

print("____________________")
print("____________________")
#Copy of list
my_copy_list=my_list.copy()
print(my_copy_list)
print(my_list)
#clear
my_copy_list.clear()
print(my_list)
print(my_copy_list)
#sort
#
#my_list.sort()#the my_list is combination of sting and int so it will give error so remove the str or int
my_list.remove("Pramod")
my_list.remove("Umesh")
my_list.remove("Romi")
my_list.sort()
my_list.sort(reverse=False)
print(my_list)

print("-----Reverse-------")
#reverse
my_list.reverse()
print(my_list)

print("-----Concat-------")
#upper() and lower() only use with string
#List concatenation
l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)
