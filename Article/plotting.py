import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FallAllD = pd.read_pickle(r'D:\teddy\Documents\UNIVALI\TCC III\TCC-iii\Dataframes\Dataframe1.pkl')
activity = FallAllD[FallAllD['ActivityID'] == 104]
accX = pd.DataFrame(activity.iloc[0].Acc.tolist())[0]
accY = pd.DataFrame(activity.iloc[0].Acc.tolist())[1]
accZ = pd.DataFrame(activity.iloc[0].Acc.tolist())[2]

gyrX = pd.DataFrame(activity.iloc[0].Gyr.tolist())[0]
gyrY = pd.DataFrame(activity.iloc[0].Gyr.tolist())[1]
gyrZ = pd.DataFrame(activity.iloc[0].Gyr.tolist())[2]


t_Acc = []
for i in range(len(accX)):
    t_Acc.append(i/238)


fig, ax1 = plt.subplots(2, sharex=True)
fig.suptitle('Forward fall while walking with recovery')

ax1[0].plot(t_Acc, accX, linewidth = 0.25, label = 'X')
ax1[0].plot(t_Acc, accY, linewidth = 0.25, label = 'Y')
ax1[0].plot(t_Acc, accZ, linewidth = 0.25, label = 'Z')
ax1[0].set_title('Accelerometer', {'fontsize': 8})
ax1[0].set_ylabel('g')
ax1[0].legend(loc = 'upper left', prop={'size': 6})

ax1[1].plot(t_Acc, gyrX, linewidth = 0.25, label = 'X')
ax1[1].plot(t_Acc, gyrY, linewidth = 0.25, label = 'Y')
ax1[1].plot(t_Acc, gyrZ, linewidth = 0.25, label = 'Z')
ax1[1].set_title('Gyroscope', {'fontsize': 8})
ax1[1].set_ylabel('°/s')

fig.supxlabel('Time (s)')
fig.dpi = 200
plt.legend(loc = 'upper left', prop={'size': 6})
plt.show()
#plt.savefig('./Forward fall while walking with recovery.jpeg', dpi=300)