import matplotlib.pyplot as plt

xpoints = [0, 6, 7 ,8 , 9]
ypoints = [0, 25 , 35, 45, 55]

plt.plot(xpoints , ypoints , marker = '*', ms = 50)
plt.show()


plt.plot(xpoints , ypoints ,linestyle = 'dotted' )
plt.show()



plt.plot(xpoints , ypoints ,'o:r' )
plt.show()
