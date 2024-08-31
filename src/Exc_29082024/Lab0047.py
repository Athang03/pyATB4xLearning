a,b,c=(10,11,12)
print(a,b,c)

#Search in tuple
cities=("London","Paris","Los Angeles","Mumbai","Tokyo")
print("Paris" in cities)
print("mumbai" in cities)#will give false cause case sensitive
print("Mumbai" in cities)

t=(12,34,56)
#t.append(12)#'tuple' object has no attribute 'append'
print(t)
my_list=list(t)
my_list.append(4)
t=tuple(my_list)
print(t)

