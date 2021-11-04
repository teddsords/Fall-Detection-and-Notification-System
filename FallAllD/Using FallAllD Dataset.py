import pandas as pd
import numpy as np
from matplotlib import pyplot

# to import data use:
FallAllD = pd.read_pickle('FallAllD.pkl')
#FallAllD = pd.read_hdf('FallAllD.h5', 'df')
print(FallAllD.info())
indexToPlot = 1
sensor = 3  # Use 1 for Acc, 2 for Gyr and 3 for Mag
print(FallAllD.loc[indexToPlot])

if sensor == 1:
    toPlotX = pd.DataFrame(FallAllD.loc[indexToPlot].Acc.tolist())[0]
    toPlotY = pd.DataFrame(FallAllD.loc[indexToPlot].Acc.tolist())[1]
    toPlotZ = pd.DataFrame(FallAllD.loc[indexToPlot].Acc.tolist())[2]
    fsAcc = 238
    accSen = 0.000244
    toPlotX = toPlotX * accSen
    toPlotY = toPlotY * accSen
    toPlotZ = toPlotZ * accSen
    xAxis = []

    for i in range(toPlotX.size):
        xAxis.append(i/fsAcc)
    
    fig, (ax1, ax2, ax3) = pyplot.subplots(3, sharex=True)
    fig.suptitle('Accelerometer')
    fig.text(0.5, 0.04, 'Time (s)', ha = 'center')
    fig.text(0.04, 0.5, 'G', va = 'center', rotation = 'vertical')
    ax1.plot(xAxis, toPlotX, linewidth = 0.5)
    ax2.plot(xAxis, toPlotY, linewidth = 0.5)
    ax3.plot(xAxis, toPlotZ, linewidth = 0.5)
    pyplot.show()
    
elif sensor == 2:
    toPlotX = pd.DataFrame(FallAllD.loc[indexToPlot].Gyr.tolist())[0]
    toPlotY = pd.DataFrame(FallAllD.loc[indexToPlot].Gyr.tolist())[1]
    toPlotZ = pd.DataFrame(FallAllD.loc[indexToPlot].Gyr.tolist())[2]
    fsGyr = 238
    gyrSen = 0.07
    toPlotX = toPlotX * gyrSen
    toPlotY = toPlotY * gyrSen
    toPlotZ = toPlotZ * gyrSen
    xAxis = []
    for i in range(toPlotX.size):
        xAxis.append(i/fsGyr)
    
    fig, (ax1, ax2, ax3) = pyplot.subplots(3, sharex=True)
    fig.suptitle('Gyroscope')
    fig.text(0.5, 0.04, 'Time (s)', ha = 'center')
    fig.text(0.04, 0.5, '°/s', va = 'center', rotation = 'vertical')
    ax1.plot(xAxis, toPlotX, linewidth = 0.5)
    ax2.plot(xAxis, toPlotY, linewidth = 0.5)
    ax3.plot(xAxis, toPlotZ, linewidth = 0.5)
    pyplot.show()
else:
    toPlotX = pd.DataFrame(FallAllD.loc[indexToPlot].Mag.tolist())[0]
    toPlotY = pd.DataFrame(FallAllD.loc[indexToPlot].Mag.tolist())[1]
    toPlotZ = pd.DataFrame(FallAllD.loc[indexToPlot].Mag.tolist())[2]
    fsMag = 80
    magSen = 0.00014
    toPlotX = toPlotX * magSen
    toPlotY = toPlotY * magSen
    toPlotZ = toPlotZ * magSen
    xAxis = []
    for i in range(toPlotX.size):
        xAxis.append(i/fsMag)
    
    fig, (ax1, ax2, ax3) = pyplot.subplots(3, sharex=True)
    fig.suptitle('Magnetometer')
    fig.text(0.5, 0.04, 'Time (s)', ha = 'center')
    fig.text(0.04, 0.5, 'Gauss', va = 'center', rotation = 'vertical')
    ax1.plot(xAxis, toPlotX, linewidth = 0.5)
    ax2.plot(xAxis, toPlotY, linewidth = 0.5)
    ax3.plot(xAxis, toPlotZ, linewidth = 0.5)
    pyplot.show()


