import random as rand
store=[]
values_of_x=[]
sumvalues_of_y=0
iteration=1000
for i in range(iteration):
    x=rand.uniform(0,1)
    values_of_x.append(x)

for j in values_of_x:
    sumvalues_of_y +=j**2
    
area=sumvalues_of_y/iteration
print("area using monte carlo approach-",area)
print("area using normal integration=",1/3)

