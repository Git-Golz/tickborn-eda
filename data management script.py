# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 22:43:39 2025

@author: golzm"
"""

import pandas as pd
import os
import glob

os.chdir("C:\\Users\\golzm\\OneDrive\\Desktop\\Capstone\\Precipitation\\")

items=[glob.glob("Ave Temp/*.csv"),glob.glob("Max Temp/*.csv"),
       glob.glob("Min Temp/*.csv"),glob.glob("Precip/*.csv")]

year=["2016","2017","2018","2019","2020","2021","2022"]

months=["January","February","March","April","May","June","July","August",
        "September","October","November","December"]

df=pd.DataFrame(columns=["ID","Name","State","Value",
                           "Anomaly (1901-2000 base period)","Rank",
                           "1901-2000 Mean","Year","Month"])

i=-1

for item in items:
    i+=1
    for file in item:
        for m in months:
            tmp=pd.read_csv(file,header=4)
            tmp["Month"]=m
            tmp["Year"]=year[i]
            df = pd.concat([df,tmp])

df=df.drop(labels=['ID','Anomaly (1901-2000 base period)','Rank',
                '1901-2000 Mean'],axis=1)     


df.to_csv('precipitation.csv',index=False)  

os.chdir("C:\\Users\\golzm\\OneDrive\\Desktop\\Capstone\\Temperature Data\\Average")

df1=pd.DataFrame(columns=["ID","Name","State","Value",
                           "Anomaly (1901-2000 base period)","Rank",
                           "1901-2000 Mean","Year","Month"])

i=-1

for item in items:
    i+=1
    for file in item:
        for m in months:
            tmp=pd.read_csv(file,header=4)
            tmp["Month"]=m
            tmp["Year"]=year[i]
            df1 = pd.concat([df1,tmp])

df1=df1.drop(labels=['ID','Anomaly (1901-2000 base period)','Rank',
                '1901-2000 Mean'],axis=1)      

df1.to_csv('avetemp.csv',index=False)  