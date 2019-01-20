# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:06:23 2019

@author: elopsuc
"""

import pandas as pd
import numpy as np
import math
import os
def powerFreq(f1,f2,dataset):
    dataset1=dataset.query('Frequency> %f ' % f1 )
    dataset1=dataset1.query('Frequency< %f ' % f2) 
    dataset1["Power"]=dataset1["Power"].map(lambda x: 10**(x/10)/6)
    dataset1["Power"]=dataset1["Power"].map(lambda x: 10*math.log(x,10))
    tables=pd.pivot_table(dataset1,index=["Latitude","Longitude"],values=["Power"],aggfunc=(np.mean))
    f1M=int(f1/1000000)
    f2M=int(f2/1000000)
    newname=str(f1M)+"-"+str(f2M)+"Mhz_Power"
    if f2==2615000000 and f1==2515000000 :
        tables.rename(columns={"Power":"NR Frq range(2515~2615Mhz) avg power"},inplace = True)
        #tables["NR Frq range(2515~2615Mhz) avg power"]=tables["NR Frq range(2515~2615Mhz) avg power"].map(lambda x: 10*math.log(x,10))
    elif f1 !=0:
        tables.rename(columns={"Power":newname},inplace = True)
        #tables[newname]=tables[newname].map(lambda x: 10*math.log(x,10))  
    elif f1==0:
        tables.rename(columns={"Power":"total avg power"},inplace = True)
        #tables["total avg power"]=tables["total avg power"].map(lambda x: 10*math.log(x,10))
    return tables
    
dirs=input("pls input path：")  
dirs1=input("pls input newfiles of path:")
f1_1=2500000000 #2.5G_1频段起点
f2_1=2515000000 #2.5G_1频段终点
f1_D4=2515000000 #D4频段起点
f2_D4=2535000000 #D4频段终点
f1_D5=2535000000 #D5频段起点
f2_D5=2555000000 #D5频段终点
f1_U=2555000000 #联通频段起点
f2_U=2575000000 #联通频段终点
f1_D1=2575000000 #D1频段起点
f2_D1=2595000000 #D1频段终点
f1_D2=2595000000 #D2频段起点
f2_D2=2615000000 #D2频段终点
f1_D3=2615000000 #D3频段起点
f2_D3=2635000000 #D3频段终点
f1_T=2635000000 #电信频段起点
f2_T=2655000000 #电信频段终点
f1_edge1=2655000000 #edge1频段起点
f2_edge1=2675000000 #edge1频段终点
f1_edge2=2675000000 #edge2频段起点
f2_edge2=2700000000 #edge2频段终点
f1_NR=2515000000 #NR频段起点
f2_NR=2615000000 #NR频段终点
f1_Total=0 #所有频段起点
f2_Total=12555000000#所有频段起点                  
for file in os.listdir(dirs):
    filename=os.path.splitext(file)                       
    if filename[1] == ".csv": 
        dataset = pd.read_csv(dirs+"\\"+file)
        frqtable1=powerFreq(f1_1,f2_1,dataset)
        frqtableD4=powerFreq(f1_D4,f2_D4,dataset)
        frqtableD5=powerFreq(f1_D5,f2_D5,dataset)
        frqtableD1=powerFreq(f1_D1,f2_D1,dataset)
        frqtableD2=powerFreq(f1_D2,f2_D2,dataset)
        frqtableD3=powerFreq(f1_D3,f2_D3,dataset)
        frqtable_edge1=powerFreq(f1_edge1,f2_edge1,dataset)
        frqtable_edge2=powerFreq(f1_edge2,f2_edge2,dataset)
        frqtable_U=powerFreq(f1_U,f2_U,dataset)
        frqtable_T=powerFreq(f1_T,f2_T,dataset)
        frqtable_NR=powerFreq(f1_NR,f2_NR,dataset)
        frqtable_Total=powerFreq(f1_Total,f2_Total,dataset)
        frqtable=pd.concat([frqtable1,frqtableD4,frqtableD5,frqtable_U,frqtableD1,frqtableD2,frqtableD3,frqtable_T,frqtable_edge1,frqtable_edge2,frqtable_NR,frqtable_Total], axis=1,join='outer')
        frqtable.to_csv(dirs1+"\\"+filename[0]+"_newdatafile.csv",index=True)
print("已完成")

        
