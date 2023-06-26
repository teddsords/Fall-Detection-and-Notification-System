import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FallAllD = pd.read_pickle('Dataframes/Wrist Dataframe.pkl')
stopWalking = FallAllD.loc[FallAllD['ActivityID'] == 12]


accX = pd.DataFrame(stopWalking.iloc[0].Acc.tolist())[0]
accY = pd.DataFrame(stopWalking.iloc[0].Acc.tolist())[1]
accZ = pd.DataFrame(stopWalking.iloc[0].Acc.tolist())[2]

Fs_Acc = 238
Acc_Sen = 0.000244
accX = accX * Acc_Sen
accY = accY * Acc_Sen
accZ = accZ * Acc_Sen
t_Acc = []
for i in range(len(accX)):
    t_Acc.append(i/Fs_Acc)

fig, ax1 = plt.subplots(3, sharex=True)
fig.suptitle('Sitting in a moving bus/metro')
ax1[0].plot(t_Acc, accX, linewidth = 0.25)
ax1[1].plot(t_Acc, accY, linewidth = 0.25)
ax1[2].plot(t_Acc, accZ, linewidth = 0.25)
plt.show()