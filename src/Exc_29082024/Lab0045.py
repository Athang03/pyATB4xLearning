#
squares=[1,4,9,16,25]
squares.sort(reverse=type)
print(squares)

#POP-working like stack
print("-----pop-----")
squares =[1,4,9,16,25]
print(squares.pop())
print(squares)

#List- is mutable in nature- i.e can change
squares[3]= 64
print(squares)

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

