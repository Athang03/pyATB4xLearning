#No return type with argument
def print_argument(*args):
#to print all args
 #print(args[0])
 for i in args:
  print(i)

print_argument("anit","reva","Sunit")
print_argument("reva")
print_argument("anit","Sunit")
print_argument("Luky",10,True,False)