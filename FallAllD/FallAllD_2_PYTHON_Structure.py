# FallAllD files to Python struct
# By By Majd SALEH 08-April-2020.
import os
from numpy import genfromtxt
import numpy as np
import pandas as pd 

oldDir=os.getcwd()
print(oldDir)
ParentDir=os.getcwd()
print(ParentDir)
FP= ParentDir+"\\FallAllD\\"
os.chdir(FP)

FileNamesAll=os.listdir(FP)
FileNames=[]
for f_name in FileNamesAll:
    if f_name.endswith('_A.dat'):
        FileNames.append(f_name)
LL=len(FileNames)

l_SubjectID=[]
l_Device=[]
l_ActivityID=[]
l_TrialNo=[]
l_Acc=[]
l_Gyr=[]
l_Mag=[]

for i in range(LL):
    f_name=FileNames[i]
    SubjectID=int(f_name[1:3])    
    l_SubjectID.append(np.uint8(SubjectID))
    ActivityID=int(f_name[8:11])    
    l_ActivityID.append(np.uint16(ActivityID))
    TrialNo=int(f_name[13:15])    
    l_TrialNo.append(np.uint8(TrialNo))
    Device=''
    if(int(f_name[5])==3):
        Device='Waist'
    l_Device.append(Device)
    
    l_Acc.append(np.int16(genfromtxt(f_name, delimiter=',')))
    chArr=list(f_name)
    chArr[16]='G'
    f_name="".join(chArr)    
    l_Gyr.append(np.int16(genfromtxt(f_name, delimiter=',')))
    chArr=list(f_name)
    chArr[16]='M'
    f_name="".join(chArr)    
    l_Mag.append(np.int16(genfromtxt(f_name, delimiter=',')))
    print(f'File  {i+1}  out of {len(FileNames)}')
os.chdir(oldDir)


FallAllD = pd.DataFrame(list(zip(l_SubjectID,l_Device,l_ActivityID,l_TrialNo,l_Acc,l_Gyr,l_Mag)), 
               columns =['SubjectID', 'Device','ActivityID','TrialNo','Acc','Gyr','Mag']) 

FallAllD.to_pickle('FallAllD.pkl')
FallAllD.to_csv('FallAllD.csv')
#FallAllD.to_hdf('FallAllD.h5', key='df', mode='w')

# to import data use:
#FallAllD = pd.read_pickle('FallAllD.pkl')
#FallAllD = pd.read_hdf('FallAllD.h5', 'df')
#print(FallAllD.info())
