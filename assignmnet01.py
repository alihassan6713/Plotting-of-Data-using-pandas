import pandas as pd
import matplotlib.pyplot as plt



#Reading file

file3 = pd.read_excel('Rainfall.xlsx')

#Printing Data
 
print(file3)

#Defining Funcition for Regular plot to limit the number of years 

def limit_plot(x,y,z, xlim = None, ylim = None, zlim = None):
    plt.plot(x, y, scalex = True, data = None, label = 'January rainfall')
    plt.plot(x, z, scalex = True, data = None, label = "Feburary Rainfall")
    
#Labeling the Plot
 
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Rainfall")
   
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    if zlim:
        plt.ylim(zlim)
    plt.show()
     
#Plotting Regular plot

x = file3['year']
y = file3['jan']
z = file3['feb']
plt.figure()

#Calling the funcition
 
limit_plot(x, y, z, xlim = (2000,2023), ylim = None, zlim = None)

# Defining Funcition to Categorize the bar plot according to values given

def Catorizeing_the_plot(x_axis, y_axis):
    z = []
   
    for j in y_axis:
        if j > 1000:
            z.append("r")
        if j <= 1000:
            z.append("g")
    plt.figure()
    plt.barh(x_axis, y_axis, color = z, height = 0.5, label = "Amount of rainfall if less than 1000 green color and greater than 1000 red color")

#Labeling the plot
 
    plt.title('Annual Rainfall')
    plt.xlabel('Rainfall')
    plt.ylabel('Year')
    plt.legend()
    plt.show()  
  
#For Bar Plot

x_axis = file3["year"]
y_axis = file3["ann"]
Catorizeing_the_plot(x_axis, y_axis)


#For Scatter Plot

#Defining Function to add the data
def plot_function(ann, year):
    return ann + year

z = plot_function(file3['ann'], file3['year'])

#Ploting the data

plt.scatter(file3['ann'], file3['year'], c = z)

#Adding Details for Labelling

plt.xlabel('x')
plt.ylabel('y')
plt.title('Function plot')
plt.colorbar()
plt.show()


