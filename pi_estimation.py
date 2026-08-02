import random as rand
interval=1000
circle_point=0
square_point=0
outside=0
y_min=15
y_max=25
x_min=5
x_max=15
h=25
k=20
r=10
a=0
for i in range(interval):
    x= rand.uniform(5,35)
    y= rand.uniform(10,30)
   

    if (x_min <= x <= x_max) and (y_min<= y <= y_max):
        square_point+=1 
    elif ((x - h)**2 + (y - k)**2 <= r**2):
        circle_point +=1
    else:
        outside+=1
print("circle_point", circle_point)
print("square_point", square_point)
print("outside", outside)
print("value of pie=",circle_point/square_point)
    
