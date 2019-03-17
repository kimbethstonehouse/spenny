import numpy as np
import matplotlib.pyplot as plt

#OECD SOURCE DATA for UK Real Interest Rates
source = np.array([[2014,2.569083333], [2015,1.901033333], [2016,1.305208333],[2017,1.235808333],[2018, 1.463758333],[2019, 1.654658333],[2020, 1.8075]])

x= source[:,0]
y= source[:,1]/100

ys= np.array([2021, 2022, 2023, 2024])
   
xplus = np.concatenate((x,ys))

p4 = np.polyfit(x, y, 3)

def savings_function(t, goal, assets):
    for t in range (0,t+1):
        assets += assets*(np.polyval(p4, t+2019))
    amount_to_save = (goal - assets)/(52*t)
    return amount_to_save

#print(savings_function(4, 2400, 1000))

#print(savings_function(t, goal, assets))
#plt.plot(xplus, (np.polyval(p4, xplus)))
#plt.plot(xplus, np.polyval(p4, xplus))
#plt.xlim([x.min(), xplus.max()+1])
#plt.ylim([0, .03])
#plt.show()