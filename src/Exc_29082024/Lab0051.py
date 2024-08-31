#Dict=Dictionary: Key-value pair

student_info={"name":"pramod",
              "age":65,
              "age":67,# if we change the value it will give o/p of latest value
              "address":{"home_address": "KA","office_address":"ND"}
                 }#Dictionary within dictionory
print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["address"])#keys are always unique
#change the value
student_info["age"]=100
print(student_info)

