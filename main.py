"""get execution time"""
import time
start_time=time.time()

"""import pandas as pd"""
#import pandas as pd
from pandas_ods_reader import read_ods
import pandas as pd


"""import created scripts:"""
from task import *

"""load for ods files"""
mydata=read_ods("actdata.ods","Feuille1")


"""for xlsx files:"""
#mydata = pd.read_excel(io='data.xlsx', sheet_name='Feuil1')

"""compute for thecritical path"""
mydata=computeCPM(mydata)
printTask(mydata)
print("\n")


"""number of tasks"""
ntask=mydata.shape[0]

"""the critical path"""
cp=[]
for i in range (ntask):
    if(mydata['SLACK'][i]==0):
        cp.append(mydata['CODE'][i])
print('the critical path is : '+'-'.join(cp))
print("\n")


"""computiong total project duration"""
tdur=0
for i in range(ntask):
    if(mydata['SLACK'][i]==0):
        tdur=tdur+mydata['DAYS'][i]

print('Total project duration is : '+str(tdur)+' unit time')
print("\n")

"""executation time """
print("executation time: %s milliseconds"%((time.time()-start_time)*1000)+"\n")
