#MATPLOTLIB
#based on https://www.youtube.com/watch?v=OZOOLe2imFo&t=3s
#check him out
import matplotlib.pyplot as plt
import numpy as np

#scatter plots
"""

# a scatter plot is a plot of points in a coordinate system
#so you need X and y coordinates:

X_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

#create the plot
plt.scatter(x= X_data,y= y_data)

#show the plot
#plt.show()

#delete the last plot
plt.close()

#or close all of them
plt.close("all")

#color the dots
plt.scatter(X_data,y_data, c="red")
#plt.show()

#use hexadecimal and stuff
plt.close()
plt.scatter(X_data,y_data, c="#000")        # --> black color
#plt.show()

#change the marker
plt.close()
plt.scatter(X_data,y_data, c="red",marker="*")
#plt.show()

#you can put basically anything into the marker parameter

#change the opacity / alpha
plt.close()
plt.scatter(X_data,y_data, c="red",alpha = 0.3) # --> number between 0 and 1
#plt.show()

#change the size of the symbols with s=

plt.close()
plt.scatter(X_data,y_data, c="red", s= 40)
#plt.show()
"""

#line plots
"""

years = [2006 + x for x in range (16)]
weights = [80, 83 , 84, 85 ,86 ,82 ,81 ,79, 83, 80, 82, 82, 83, 81 ,80 ,79]

#years from 2006 to 2021

#note that years and weights have to have the same length

if len(years) == len(weights):  # --> len = 16
    print("its the same")
    
#plot the line with plt.plot
# #parameter 1 = x-axis, parameter 2 = y-axis

plt.plot(years,weights)
#plt.show()

#change color

plt.close()
plt.plot(years,weights, c="red")
#plt.show()

#change the linewidth with lw= 

plt.close()
plt.plot(years,weights, c="red", lw= 10)
#plt.show()

#make another linetype, fE dashed

plt.close()
plt.plot(years,weights, c="red", lw= 10, linestyle= "--")
#plt.show()

#also works with positional paramters for example the code above equals:

plt.close()
plt.plot(years,weights, "r--", lw= 10)
#plt.show()

"""

#bar plots
"""

#use barplots to visualize surveys for example

x = ["C++", "C#", "Python", "Java","Go"]
y = [20, 50, 140, 1, 45]

#create barchart

plt.bar(x,y)
#plt.show()

#shows categorical amounts
#change color

plt.close
plt.bar(x,y, color="red")
#note that color NEEDS to be spelled out here for whatever reason
#plt.show()

#change alignment 

plt.close
plt.bar(x,y, color="red", align="center")
#plt.show()

#change barwidth width = paramter * original width
#half the width

plt.close
plt.bar(x,y, color="red", align="center", width= 0.3)
#plt.show()

#different edge color

plt.close
plt.bar(x,y, color="red", align="center", edgecolor= "blue", lw= 10)
plt.show()
"""

#histogram plots
"""

ages = np.random.normal(20, 1.5, 1000)

#normal distribution of ages around 20 with std of 1.5, 1000 data points

#create the histogram 
plt.hist(ages)
#plt.show()

#you can clearly see around 20 being the mean and min and max values around 15/25

#change the color
plt.close()
plt.hist(ages, color="green")
#plt.show()

#customize the bins
#more bins means more accurate results
#less bins means the data is more clustered

plt.close()
plt.hist(ages, color="green", bins= 20) # --> high bins#
#plt.show()

#specify specific bins as a collection

plt.close()
plt.hist(ages,
         bins= [ages.min(), 18, 21, ages.max()]
         )
#plt.show()

#plot the cummulative distribution function
plt.close()
plt.hist(ages,cumulative= True
         )
#plt.show()
"""

#pie plots
"""
#create labels and data for each label
langaugaes =["C++", "C#", "Python", "Java","Go"]
votes = [24, 6, 50, 14, 17]

#create the pie plot

plt.pie(votes, labels=langaugaes)
#plt.show()

#very good to visualize when each person in a survey can only decide on 1 possibility
# --> if people could choose python and C#, the pie chart would not make a lot of sense
#but like this the distribution of the people can be visualized well

#highlight certain features

explodes= [0,0.2,0.3,0,0]
plt.close()
plt.pie(votes, labels=langaugaes, explode= explodes)
#plt.show()
"""

#box plot
"""

#statistical plot showing all kinds of interesting data

height = np.random.normal(172, 8 , 300)

#create a box plot

plt.boxplot(height)
plt.show()
"""

#plot customization
"""

years = [2006 + x for x in range (16)]
weights = [80, 83 , 84, 85 ,86 ,82 ,81 ,79, 83, 80, 82, 82, 83, 81 ,80 ,79]

plt.plot(years, weights)

#add a title to explain whats happening
plt.title("weight of person in specific years", fontsize= 25, fontname="Cursive")
plt.xlabel("years")
plt.ylabel("weight in kg")
#plt.show()

#add a ticker to the y axis
weight_ticker = range(75,90)
plt.yticks(weight_ticker, [f"{x} kg" for x in weight_ticker])
#plt.show()

#add a legend to the plot
#this is useful when you have multiple plots i none 

plt.close()
data_a = [100,102,99,101,101,100,102]
data_b = [90,95,102,104,105,103,109]
data_c = [110,115,100,105,100,98,95]

#if we only pass one list, the x axis is enumration by default

plt.plot(data_a, label="Company1")
plt.plot(data_b, label="Company2")
plt.plot(data_c, label="Company3")
#plt.show()

#now we have 3 lines and dont really now whats going on
#fortunately we added labels to all our lines and can now just call the legend function
plt.legend()
#plt.show()

#change position of legend
plt.legend(loc= "lower center")
plt.show()

#do that with a pie chart
plt.close()
votes = [10,2,5,16,22]
people=["A","B","C","D","E"]

plt.pie(votes, labels= None)
plt.legend(labels= people)
plt.show()
"""

#style the charts
"""

from matplotlib import style

style.use("dark_background")
#for a list of all styles visit the matplotlib website

votes = [10,2,5,16,22]
people=["A","B","C","D","E"]

plt.pie(votes, labels= None)
plt.legend(labels= people)
plt.show()

#you can also customize your own stylesheets on hte matplotlib website
"""

#multiple plots dsiplayed at once
"""
x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(x1, y1)

plt.figure(2)
plt.plot(x2, y2)

plt.show()

#for displaying both in one window we use subplots

x = np.arange(100)

#2 x 2 grid
fig, axs = plt.subplots(2, 2)

#coordinates 0,0 --> top left
axs[0,0].plot(x, np.sin(x)) 
axs[0,0].set_title("Sine Wave")


#coordinates 0,1 --> top right
axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title("Cosine Wave")

#coordinates 1,0 --> bottom left
axs[1,0].plot(x, np.random.random(100)) 
axs[1,0].set_title("random", loc= "left")


#coordinates 1,1 --> bottom right
axs[1,1].plot(x, np.log(x))
axs[1,1].set_title("log")

#now we have 4 subplots in a single figure

#add title to figure
fig.suptitle("Four plots", fontsize= 20)
#plt.show()

#make the overlay not overlap
plt.tight_overlay()
plt.show()
"""

#exporting plots
"""
data= [80,90,105,120,150]
plt.plot(data)
plt.title("MYPLOT")

#export the plot
#NOTICE THAT AFTER YOU SHOW THE PLOT IT IS DELETED, SO ALWAYS SAVE IT FIRST
plt.savefig("MYPLOT.png")
#plt.show()

#you cna also change the resultion by using dpi
plt.savefig("MYPLOT.png", dpi= 300)

#or make it transparent
plt.savefig("MYPLOT.png", dpi= 300, transparent=True)
"""

#3d plots
"""
axis = plt.axes(projection="3d")

x= np.arange(100)
y= np.sin(x)
z= np.cos(x)

plt.figure(1)
axis.scatter(x,y,z)
axis.set_title("3dplot")
#plt.show()

plt.figure(2)
axis_2 = plt.axes(projection="3d")
axis_2.plot(x,y,z)
plt.show()

#create a more intersting 3d grid plot

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)

X, Y = np.meshgrid(x,y)
Z = np.sin(X) * np.cos(Y)

axis_3 = plt.axes(projection="3d")
axis_3.plot_surface(X, Y, Z, cmap= "Spectral")
plt.show()
"""

#animate a plot
"""

#flip a coin

import random
heads_tails = [0,0]

for x in range(100000):
    heads_tails[random.randint(0, 1)] += 1
    
#every iteration randomly flips the coin

plt.bar(["Heads", "Tails"], heads_tails, color=["red","blue"])
plt.pause(0.001)    # --> like show() but it created an animation
"""