#.....................................IMPORTING REQUIRED LIBRARIES...................................................................
import matplotlib.pyplot as plt    #ploting graph 
import numpy as np 			 #for taking axises
import math    				 #for using pi, sin and cos value
#..................................................................................................................................

#assigning values l=89in h=49in b1=11.5deg 
l=89 	#l is lengh of vehicle in inchs
h=49    
b1=math.radians(11.5) #converting in radian because math function taking angles in radian

#assigning values to x-axis
D=np.arange(30,110,10) #creating a list {30,40,50...100}

#............................................Defining given Function..................................................................
def F(D,a):
	A=l*math.sin(b1)
	B=l*math.cos(b1)
	C=(h+0.5*D)*math.sin(b1)-0.5*D*math.tan(b1)
	E=(h+0.5*D)*math.cos(b1)-0.5*D
	
	fx=A*math.sin(a)*math.cos(a)+B*math.sin(a)*math.sin(a)-C*math.cos(a)-E*math.sin(a)
	return fx


alpha=[]  #empty list that going to store all the values of alpha (y-axis of the graph)

#.............................................. Using Bisection Method ................................................................

#hit and trial
print(F(55,math.radians(30))) #we are getting negative value for 30deg for all element in list D
print(F(55,math.radians(34))) #we are getting positive value for 34deg for all element in list D

#finding alpha for all the element of list D
for d in D:

	eps=0.0001 #tolerance
	a=30   #value of alpha we get negative value
	b=34   #value of alpha we get positive value
	p=a
	while abs(F(d,math.radians(p)))>eps:
		p=a+(b-a)/2
		if F(d,math.radians(a))*F(d,math.radians(p))>0:
			a=p
		else:
			b=p
	
	alpha.append(p)

#...................................................................................................................................

print(alpha)  #printing all the values of alpha we got

#..............................................Ploting graph.........................................................................
plt.plot(D,alpha,'-ro')
plt.title("nose in failure (Alpha vs D)")
plt.xlabel("Diameter of vehicle's wheels (inch)")
plt.ylabel("Alpha (Deg)")
plt.grid(color='g', ls='-.', lw=0.5)            #this will create grid
plt.show()
#...............................................The End...............................................................................









