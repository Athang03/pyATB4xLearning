#Tuple - Collection of the item
my_tuple=(1,4,9,16,25)
#my_tuple[3]=64 #Immutable in nature
print(my_tuple)#tuple object does not support item assignment
#If your list is not changing then you have to use tuple if list is changing use list

my_tuple=("tta.com","sdet.live")
my_api_list=list(my_tuple)#conversion
print(my_api_list)
#list to tuple
my_api_list=tuple(my_api_list)
print(my_api_list)
#to save the memory we use tuple

t=tuple()
print(t)
#Tuple within tuple
hero1 =("batmat","Superman")
hero2 =("Wonder women","Spice girls")
new_tuple=(hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][0])
print(new_tuple[1][1])