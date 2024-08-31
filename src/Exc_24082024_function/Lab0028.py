#Types of user defined function
#1.Non_return - No return type and No parameter
"""def greet():
    print("Hello world\n")
result=greet()
print(result)"""

#2.No return type with argument
def greet(name):
    print("Hello,",name)

greet("Pramod")

#3. No return type with default argument - If you dont pass anythind default argument will taken
def say_hello_default_args(name="Prasad"):
    print("Hello,",name.upper())

say_hello_default_args("Amit")
say_hello_default_args()

#Multiple args
def multiple_args(name1="kinari",name2="Ravi",name3="Rina"):
    print("multiple args",name1,name2,name3)

multiple_args(name1="Sid", name3="Ira")
multiple_args()


#Argument+return type
def sum_of_two_number(num1, num2):
    return  num1 + num2

result = sum_of_two_number(10,34)
print(result)

#with default
def sum_of_two_number_with_Default(num1=100, num2=300):
        return num1+num2
result=sum_of_two_number_with_Default()
print(result)
    
