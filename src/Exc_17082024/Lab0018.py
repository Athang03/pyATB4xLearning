#Write a python program to calculate area of circle given its radius using formula
# Logic building formula
#step 1 figure out the input and output
#input->r->datatype->float
#pi->3.14 and power->**
#o/p->float-area ,print area

#step2
#rough logic= area= 3.14*(r,2)
#step3 - right logic

import math #math is python library
radius = float(input("Enter the radious of circle\n"))
print(radius)
print(math.pi)
area2=3.14*(radius**2)
area=math.pi*math.pow(radius,2)
print(f"area of circle, {area:.2f}")
print(f"area2 of circle, {area2:.2f}")


