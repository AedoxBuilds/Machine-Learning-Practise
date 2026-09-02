
import matplotlib.pyplot as plt

# create x and y values
x = (80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
y = (240, 250, 260, 270, 280, 290, 300, 310, 320, 330)



# create font styling
font1 = {'family':'serif','color':'Green','size':30}
font2 = {'family':'serif','color':'darkblue','size':15}


# set labels with positioning and styles
plt.title("Sports Watch Data", fontdict = font1 , loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2 , loc = 'left')
plt.ylabel("Calorie Burnage", fontdict = font2 , loc = 'bottom')



# ploting
plt.plot(x, y)

# create grids with styling
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()


