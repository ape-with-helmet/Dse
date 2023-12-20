#python program to display multiple types of charts using matplotlib
import matplotlib.pyplot as plt
import numpy as np

#line chart
x=np.linspace(0,10,100)#from 0,10 there are 100 points to be plotted... defined the smoothness of the curve
y=np.sin(x)
plt.figure()
plt.plot(x,y)
plt.title("Line CHart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#Bar CHart
categories=['A','B','C','D']
values=[20,35,30,25]
plt.figure()
plt.bar(categories,values)
plt.title("Bar CHart")
plt.xlabel("Categories")
plt.ylabel("Values")

#Scatter plot
x=np.random.randn(100)
y=np.random.randn(100)
colors=np.random.randn(100)
sizes=100*np.random.randn(100)
plt.figure()
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5)#alpha is the opacity
plt.title("Scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#pie chart
sizes=[30,20,25,15,10]
label=['A','B','C','D','E']
plt.figure()
plt.pie(sizes,labels=label,autopct='%1.1f%%')
plt.title("Pie chart")

#SHowing all outputs
plt.show()
