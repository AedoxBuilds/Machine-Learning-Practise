import matplotlib.pyplot as plt

xpoints = [0, 6, 7 ,8 , 9]
ypoints = [0, 25 , 35, 45, 55]

plt.plot(xpoints , ypoints , marker = '*', ms = 50)
plt.show()


plt.plot(xpoints , ypoints , marker = 'o', ms = 20, mec = 'r' , mfc = '#123019')
plt.show()
