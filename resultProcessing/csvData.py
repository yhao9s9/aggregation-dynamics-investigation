## This script is used to read .csv file, delete the first row and then save results in .npy file.

import numpy as np
import csv
import pandas as pd


dirt = ['d1_800/','d2_800/','d2_1600/','d3_800/','d3_1600/','d3_4000/','d4_1600/','d5_800/','d5_1600/','d5_4000/','d6_800/','d6_1600/','d6_4000/']
time = ['1min/','2min/','4min/','6min/']
name = ['volume','surface','toppercent','topfix','faceward','backward']

for i in dirt:
    for j in time:
        for k in name:
            df = pd.read_csv(i+j+'csv/'+k+'.csv', sep=",")
            np.save(i+j+'npy/'+k+'.npy',np.array(df.values))

dirt1 = ['d1_800/','d2_800/','d2_1600/','d3_800/','d3_1600/','d3_4000/','d4_1600/','d5_800/','d5_1600/','d6_800/','d6_1600/']
time1 = ['9min/','12min/']

for i in dirt1:
    for j in time1:
        for k in name:
            df = pd.read_csv(i+j+'csv/'+k+'.csv', sep=",")
            np.save(i+j+'npy/'+k+'.npy',np.array(df.values))

dirt2 = ['d2_800/','d5_800/']
time2 = ['1min/','2min/','4min/','6min/','9min/','12min/']
name2 = ['1volume','1surface','1toppercent','1topfix','1faceward','1backward','2volume','2surface','2toppercent','2topfix','2faceward','2backward']

for i in dirt2:
    for j in time2:
        for k in name2:
            df = pd.read_csv(i+j+'csv/'+k+'.csv', sep=",")
            np.save(i+j+'npy/'+k+'.npy',np.array(df.values))