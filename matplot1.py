# 2 modules - pyplot, pylab
# data visualization library
# line chart, bar chart, histogram, scatter plot,pi chart, 


#Axes - 


from cProfile import label
from tkinter import BOTTOM
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import random
x = np.arange(0,10,1)
print(x)

y = x**2

print(y)
plt.xlabel("Number")
plt.ylabel("Square of number")
plt.title("SIMPLE SQUARE FUNCTION")

plt.plot(x,y,marker = "o" , mec = "b", ms = "3",lw = "10", c = "b")
plt.show()
# #only 1 parameter to axis - it will consider it as y axis

# #multiple plot

# y1 = x**3
# y2 = x**1.5
# plt.plot(x,y,x,y2,x,y1)
# plt.show()

# #Grid
# #grid() -> to get grid

# #lw,c,ls

# plt.grid(axis="both")
# plt.show()


# #subplot

# plt.subplot(2,2,1)
# plt.plot(x,y)

# plt.subplot(2,2,3)
# plt.plot(x,y)
# plt.subplot(2,2,4)
# plt.plot(x,y)


# plt.show()


#legend() function, we will use lable parameter inside the plot, we will have to use legend()
plt.plot(x,y, label = "square")
plt.legend(shadow = True)
plt.show()


# #scatter Plot
# #alpha = transperancy
# z = [random.randint(1,10) for _ in range(0,10)]
# plt.scatter(x,z,marker="s",s=12)
# plt.show()


# #colorbar() use when we want color bar in side

# #barplot, bar - vertical bar

# x = ['a','b','c','d','f']
# y = [10,20,10,60,20]
# plt.bar(x,y)
# plt.xlabel("yoyo")
# plt.ylabel("honey")
# plt.show()


# #barh = horizontal bar

# #stacked bar plot - x is same and y is diffrent then we can avoid overlapping of the bar using bottom

x = ['a','b','c','d','f']
y = [10,20,10,60,20]
y1 = [21,34,45,12,34,]
y2 = [23,34,34,12,45]

# y2_start = [y1[i] + y[i] for i in range(0,5)]
# plt.bar(x_str,y,color = "yellow")
# plt.bar(x_str,y1,bottom = y,color = "black")
# plt.bar(x_str,y2,color = "pink", bottom=y2_start)
# plt.show()
w = 0.2


#groupped bar chart

#locatrion to plot
x_bar = np.arange(len(x))
y1_bar = [i+w for i in x_bar]
y2_bar = [i+w for i in y1_bar]

plt.bar(x_bar,y,label = "x_bar",width=0.2)
plt.bar(y1_bar,y1,label = "y1_bar",width=0.2)
plt.bar(y2_bar,y2,label = "y2_bar",width=0.2)
plt.xticks(y1_bar,x)
plt.show()


#fig size = plt.figure(figsize = (10,7))



#pie chart
#parameter for pie = startangle, explode(by default everthing is 0), autopct

student = ["excellent","good", "average","poor"]
num_student = [10,20,34,7]

plt.pie(num_student,labels=student,explode=[0.2,0,0,0],shadow=True,autopct='%.2f%%')
plt.show()


#histogram

marks = [90,98,60,34,100]
grade_interal = [30,40,50,60,70,80,100]
plt.xticks(grade_interal) 
plt.title("student grade")
plt.hist(marks,grade_interal)
plt.show()