from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_pickle("Dataframes/Wrist Dataframe.pkl")
new = pd.DataFrame(df.Acc[0].tolist())[0]
new = new.to_list()
type(new)

new2 = new[0:1190]
xaxis2 = []
xaxis = []
for i in range(4760):
    xaxis.append(i/238)

for i in range(1190):
    xaxis2.append(i/238)

plt.plot(xaxis, new, linewidth = 0.5)
plt.plot(xaxis2, new2, linewidth = 0.5)
plt.show()

df.Acc.mean()

with open('Accelerometer for 5 seconds.csv', 'w') as f:
    for line in xaxis2:
        f.write(f'{line},')


