## Plot the redundant part as two aggregates

import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.lines as mlines
import seaborn as sns


dirt = ['d1_800/','d2_800/','d2_1600/','d3_800/','d3_1600/','d3_4000/','d4_1600/','d5_800/','d5_1600/','d5_4000/','d6_800/','d6_1600/','d6_4000/']
time = ['1min/','2min/','4min/','6min/','9min/','12min/']
name1 = ['volume','surface','toppercent','topfix','faceward','backward']

data= []
for i in dirt:
    data_dirt = []
    for j in time:
        data_time = []
        for k in name1:
            try:
                a = np.load(i+j+'npy/'+k+'.npy')
                data_time.append(a)
            except:
                data_time.append([])
        data_dirt.append(data_time)
    data.append(data_dirt)


name2 = ['1volume','1surface','1toppercent','1topfix','1faceward','1backward']
name3 = ['2volume','2surface','2toppercent','2topfix','2faceward','2backward']

data_d2800_dirt_1 = []
for j in time:
    data_d2800_time = []
    for k in name2:
        a = np.load('d2_800/'+j+'npy/'+k+'.npy')
        data_d2800_time.append(a)
    data_d2800_dirt_1.append(data_d2800_time)
data.append(data_d2800_dirt_1)

data_d2800_dirt_2 = []
for j in time:
    data_d2800_time = []
    for k in name3:
        a = np.load('d2_800/'+j+'npy/'+k+'.npy')
        data_d2800_time.append(a)
    data_d2800_dirt_2.append(data_d2800_time)
data.append(data_d2800_dirt_2)

data_d5800_dirt_1 = []
for j in time:
    data_d5800_time = []
    for k in name2:
        a = np.load('d5_800/'+j+'npy/'+k+'.npy')
        data_d5800_time.append(a)
    data_d5800_dirt_1.append(data_d5800_time)
data.append(data_d5800_dirt_1)

data_d5800_dirt_2 = []
for j in time:
    data_d5800_time = []
    for k in name3:
        a = np.load('d5_800/'+j+'npy/'+k+'.npy')
        data_d5800_time.append(a)
    data_d5800_dirt_2.append(data_d5800_time)
data.append(data_d5800_dirt_2)

## data = [d1_800[6][5],d2_800,d2_1600,d3_800,d3_1600,d3_4000,d4_1600,d5_800,d5_1600,d5_4000[6][5],d6_800,d6_1600,d6_4000[6][5],
#           d2_800_solid1[6][5],d2_800_solid2[6][5],d5_800_solid1[6][5],d5_800_solid2[6][5]]
## d5_4000 9min & 12min: []
## d1_800/4min/volume = data[0][2][0] -> 2D array = num_node * [elongation, shear rate, shear stress, velocity]
## d2_800/6min/2toppercent = data[14][3][2] -> 2D array = num_node * [elongation, PointZ, shear rate, shear stress, velocity]


## Average rate of elongation
meanelon800surface = np.array([np.mean([np.mean(data[0][0][1],axis=0)[0],np.mean(data[3][0][1],axis=0)[0],np.mean(data[10][0][1],axis=0)[0],\
                                    np.mean(data[13][0][1],axis=0)[0],np.mean(data[14][0][1],axis=0)[0],np.mean(data[15][0][1],axis=0)[0],np.mean(data[16][0][1],axis=0)[0]]),\
                       np.mean([np.mean(data[0][1][1],axis=0)[0],np.mean(data[3][1][1],axis=0)[0],np.mean(data[10][1][1],axis=0)[0],\
                                    np.mean(data[13][1][1],axis=0)[0],np.mean(data[14][1][1],axis=0)[0],np.mean(data[15][1][1],axis=0)[0],np.mean(data[16][1][1],axis=0)[0]]),\
                       np.mean([np.mean(data[0][2][1],axis=0)[0],np.mean(data[3][2][1],axis=0)[0],np.mean(data[10][2][1],axis=0)[0],\
                                    np.mean(data[13][2][1],axis=0)[0],np.mean(data[14][2][1],axis=0)[0],np.mean(data[15][2][1],axis=0)[0],np.mean(data[16][2][1],axis=0)[0]]),\
                       np.mean([np.mean(data[0][3][1],axis=0)[0],np.mean(data[3][3][1],axis=0)[0],np.mean(data[10][3][1],axis=0)[0],\
                                    np.mean(data[13][3][1],axis=0)[0],np.mean(data[14][3][1],axis=0)[0],np.mean(data[15][3][1],axis=0)[0],np.mean(data[16][3][1],axis=0)[0]]),\
                       np.mean([np.mean(data[0][4][1],axis=0)[0],np.mean(data[3][4][1],axis=0)[0],np.mean(data[10][4][1],axis=0)[0],\
                                    np.mean(data[13][4][1],axis=0)[0],np.mean(data[14][4][1],axis=0)[0],np.mean(data[15][4][1],axis=0)[0],np.mean(data[16][4][1],axis=0)[0]]),\
                       np.mean([np.mean(data[0][5][1],axis=0)[0],np.mean(data[3][5][1],axis=0)[0],np.mean(data[10][5][1],axis=0)[0],\
                                    np.mean(data[13][5][1],axis=0)[0],np.mean(data[14][5][1],axis=0)[0],np.mean(data[15][5][1],axis=0)[0],np.mean(data[16][5][1],axis=0)[0]])])
meanelon1600surface = np.array([np.mean([np.mean(data[2][0][1],axis=0)[0],np.mean(data[4][0][1],axis=0)[0],np.mean(data[6][0][1],axis=0)[0],\
                                 np.mean(data[8][0][1],axis=0)[0],np.mean(data[11][0][1],axis=0)[0]]),\
                       np.mean([np.mean(data[2][1][1],axis=0)[0],np.mean(data[4][1][1],axis=0)[0],np.mean(data[6][1][1],axis=0)[0],\
                                 np.mean(data[8][1][1],axis=0)[0],np.mean(data[11][1][1],axis=0)[0]]),\
                       np.mean([np.mean(data[2][2][1],axis=0)[0],np.mean(data[4][2][1],axis=0)[0],np.mean(data[6][2][1],axis=0)[0],\
                                 np.mean(data[8][2][1],axis=0)[0],np.mean(data[11][2][1],axis=0)[0]]),\
                       np.mean([np.mean(data[2][3][1],axis=0)[0],np.mean(data[4][3][1],axis=0)[0],np.mean(data[6][3][1],axis=0)[0],\
                                 np.mean(data[8][3][1],axis=0)[0],np.mean(data[11][3][1],axis=0)[0]]),\
                       np.mean([np.mean(data[2][4][1],axis=0)[0],np.mean(data[4][4][1],axis=0)[0],np.mean(data[6][4][1],axis=0)[0],\
                                 np.mean(data[8][4][1],axis=0)[0],np.mean(data[11][4][1],axis=0)[0]]),\
                       np.mean([np.mean(data[2][5][1],axis=0)[0],np.mean(data[4][5][1],axis=0)[0],np.mean(data[6][5][1],axis=0)[0],\
                                 np.mean(data[8][5][1],axis=0)[0],np.mean(data[11][5][1],axis=0)[0]])])
meanelon4000surface = np.array([np.mean([np.mean(data[5][0][1],axis=0)[0],np.mean(data[9][0][1],axis=0)[0],np.mean(data[12][0][1],axis=0)[0]]),\
                       np.mean([np.mean(data[5][1][1],axis=0)[0],np.mean(data[9][1][1],axis=0)[0],np.mean(data[12][1][1],axis=0)[0]]),\
                       np.mean([np.mean(data[5][2][1],axis=0)[0],np.mean(data[9][2][1],axis=0)[0],np.mean(data[12][2][1],axis=0)[0]]),\
                       np.mean([np.mean(data[5][3][1],axis=0)[0],np.mean(data[9][3][1],axis=0)[0],np.mean(data[12][3][1],axis=0)[0]])])

stdelon800surface = np.array([np.std([np.mean(data[0][0][1],axis=0)[0],np.mean(data[3][0][1],axis=0)[0],np.mean(data[10][0][1],axis=0)[0],\
                                    np.mean(data[13][0][1],axis=0)[0],np.mean(data[14][0][1],axis=0)[0],np.mean(data[15][0][1],axis=0)[0],np.mean(data[16][0][1],axis=0)[0]]),\
                       np.std([np.mean(data[0][1][1],axis=0)[0],np.mean(data[3][1][1],axis=0)[0],np.mean(data[10][1][1],axis=0)[0],\
                                    np.mean(data[13][1][1],axis=0)[0],np.mean(data[14][1][1],axis=0)[0],np.mean(data[15][1][1],axis=0)[0],np.mean(data[16][1][1],axis=0)[0]]),\
                       np.std([np.mean(data[0][2][1],axis=0)[0],np.mean(data[3][2][1],axis=0)[0],np.mean(data[10][2][1],axis=0)[0],\
                                    np.mean(data[13][2][1],axis=0)[0],np.mean(data[14][2][1],axis=0)[0],np.mean(data[15][2][1],axis=0)[0],np.mean(data[16][2][1],axis=0)[0]]),\
                       np.std([np.mean(data[0][3][1],axis=0)[0],np.mean(data[3][3][1],axis=0)[0],np.mean(data[10][3][1],axis=0)[0],\
                                    np.mean(data[13][3][1],axis=0)[0],np.mean(data[14][3][1],axis=0)[0],np.mean(data[15][3][1],axis=0)[0],np.mean(data[16][3][1],axis=0)[0]]),\
                       np.std([np.mean(data[0][4][1],axis=0)[0],np.mean(data[3][4][1],axis=0)[0],np.mean(data[10][4][1],axis=0)[0],\
                                    np.mean(data[13][4][1],axis=0)[0],np.mean(data[14][4][1],axis=0)[0],np.mean(data[15][4][1],axis=0)[0],np.mean(data[16][4][1],axis=0)[0]]),\
                       np.std([np.mean(data[0][5][1],axis=0)[0],np.mean(data[3][5][1],axis=0)[0],np.mean(data[10][5][1],axis=0)[0],\
                                    np.mean(data[13][5][1],axis=0)[0],np.mean(data[14][5][1],axis=0)[0],np.mean(data[15][5][1],axis=0)[0],np.mean(data[16][5][1],axis=0)[0]])])
stdelon1600surface = np.array([np.std([np.mean(data[2][0][1],axis=0)[0],np.mean(data[4][0][1],axis=0)[0],np.mean(data[6][0][1],axis=0)[0],\
                                 np.mean(data[8][0][1],axis=0)[0],np.mean(data[11][0][1],axis=0)[0]]),\
                       np.std([np.mean(data[2][1][1],axis=0)[0],np.mean(data[4][1][1],axis=0)[0],np.mean(data[6][1][1],axis=0)[0],\
                                 np.mean(data[8][1][1],axis=0)[0],np.mean(data[11][1][1],axis=0)[0]]),\
                       np.std([np.mean(data[2][2][1],axis=0)[0],np.mean(data[4][2][1],axis=0)[0],np.mean(data[6][2][1],axis=0)[0],\
                                 np.mean(data[8][2][1],axis=0)[0],np.mean(data[11][2][1],axis=0)[0]]),\
                       np.std([np.mean(data[2][3][1],axis=0)[0],np.mean(data[4][3][1],axis=0)[0],np.mean(data[6][3][1],axis=0)[0],\
                                 np.mean(data[8][3][1],axis=0)[0],np.mean(data[11][3][1],axis=0)[0]]),\
                       np.std([np.mean(data[2][4][1],axis=0)[0],np.mean(data[4][4][1],axis=0)[0],np.mean(data[6][4][1],axis=0)[0],\
                                 np.mean(data[8][4][1],axis=0)[0],np.mean(data[11][4][1],axis=0)[0]]),\
                       np.std([np.mean(data[2][5][1],axis=0)[0],np.mean(data[4][5][1],axis=0)[0],np.mean(data[6][5][1],axis=0)[0],\
                                 np.mean(data[8][5][1],axis=0)[0],np.mean(data[11][5][1],axis=0)[0]])])
stdelon4000surface = np.array([np.std([np.mean(data[5][0][1],axis=0)[0],np.mean(data[9][0][1],axis=0)[0],np.mean(data[12][0][1],axis=0)[0]]),\
                       np.std([np.mean(data[5][1][1],axis=0)[0],np.mean(data[9][1][1],axis=0)[0],np.mean(data[12][1][1],axis=0)[0]]),\
                       np.std([np.mean(data[5][2][1],axis=0)[0],np.mean(data[9][2][1],axis=0)[0],np.mean(data[12][2][1],axis=0)[0]]),\
                       np.std([np.mean(data[5][3][1],axis=0)[0],np.mean(data[9][3][1],axis=0)[0],np.mean(data[12][3][1],axis=0)[0]])])


## Average shear rate
meanshear800surface = np.array([np.mean([np.mean(data[0][0][1],axis=0)[2],np.mean(data[3][0][1],axis=0)[2],np.mean(data[10][0][1],axis=0)[2],\
                                    np.mean(data[13][0][1],axis=0)[2],np.mean(data[14][0][1],axis=0)[2],np.mean(data[15][0][1],axis=0)[2],np.mean(data[16][0][1],axis=0)[2]]),\
                       np.mean([np.mean(data[0][1][1],axis=0)[2],np.mean(data[3][1][1],axis=0)[2],np.mean(data[10][1][1],axis=0)[2],\
                                    np.mean(data[13][1][1],axis=0)[2],np.mean(data[14][1][1],axis=0)[2],np.mean(data[15][1][1],axis=0)[2],np.mean(data[16][1][1],axis=0)[2]]),\
                       np.mean([np.mean(data[0][2][1],axis=0)[2],np.mean(data[3][2][1],axis=0)[2],np.mean(data[10][2][1],axis=0)[2],\
                                    np.mean(data[13][2][1],axis=0)[2],np.mean(data[14][2][1],axis=0)[2],np.mean(data[15][2][1],axis=0)[2],np.mean(data[16][2][1],axis=0)[2]]),\
                       np.mean([np.mean(data[0][3][1],axis=0)[2],np.mean(data[3][3][1],axis=0)[2],np.mean(data[10][3][1],axis=0)[2],\
                                    np.mean(data[13][3][1],axis=0)[2],np.mean(data[14][3][1],axis=0)[2],np.mean(data[15][3][1],axis=0)[2],np.mean(data[16][3][1],axis=0)[2]]),\
                       np.mean([np.mean(data[0][4][1],axis=0)[2],np.mean(data[3][4][1],axis=0)[2],np.mean(data[10][4][1],axis=0)[2],\
                                    np.mean(data[13][4][1],axis=0)[2],np.mean(data[14][4][1],axis=0)[2],np.mean(data[15][4][1],axis=0)[2],np.mean(data[16][4][1],axis=0)[2]]),\
                       np.mean([np.mean(data[0][5][1],axis=0)[2],np.mean(data[3][5][1],axis=0)[2],np.mean(data[10][5][1],axis=0)[2],\
                                    np.mean(data[13][5][1],axis=0)[2],np.mean(data[14][5][1],axis=0)[2],np.mean(data[15][5][1],axis=0)[2],np.mean(data[16][5][1],axis=0)[2]])])
meanshear1600surface = np.array([np.mean([np.mean(data[2][0][1],axis=0)[2],np.mean(data[4][0][1],axis=0)[2],np.mean(data[6][0][1],axis=0)[2],\
                                 np.mean(data[8][0][1],axis=0)[2],np.mean(data[11][0][1],axis=0)[2]]),\
                       np.mean([np.mean(data[2][1][1],axis=0)[2],np.mean(data[4][1][1],axis=0)[2],np.mean(data[6][1][1],axis=0)[2],\
                                 np.mean(data[8][1][1],axis=0)[2],np.mean(data[11][1][1],axis=0)[2]]),\
                       np.mean([np.mean(data[2][2][1],axis=0)[2],np.mean(data[4][2][1],axis=0)[2],np.mean(data[6][2][1],axis=0)[2],\
                                 np.mean(data[8][2][1],axis=0)[2],np.mean(data[11][2][1],axis=0)[2]]),\
                       np.mean([np.mean(data[2][3][1],axis=0)[2],np.mean(data[4][3][1],axis=0)[2],np.mean(data[6][3][1],axis=0)[2],\
                                 np.mean(data[8][3][1],axis=0)[2],np.mean(data[11][3][1],axis=0)[2]]),\
                       np.mean([np.mean(data[2][4][1],axis=0)[2],np.mean(data[4][4][1],axis=0)[2],np.mean(data[6][4][1],axis=0)[2],\
                                 np.mean(data[8][4][1],axis=0)[2],np.mean(data[11][4][1],axis=0)[2]]),\
                       np.mean([np.mean(data[2][5][1],axis=0)[2],np.mean(data[4][5][1],axis=0)[2],np.mean(data[6][5][1],axis=0)[2],\
                                 np.mean(data[8][5][1],axis=0)[2],np.mean(data[11][5][1],axis=0)[2]])])
meanshear4000surface = np.array([np.mean([np.mean(data[5][0][1],axis=0)[2],np.mean(data[9][0][1],axis=0)[2],np.mean(data[12][0][1],axis=0)[2]]),\
                       np.mean([np.mean(data[5][1][1],axis=0)[2],np.mean(data[9][1][1],axis=0)[2],np.mean(data[12][1][1],axis=0)[2]]),\
                       np.mean([np.mean(data[5][2][1],axis=0)[2],np.mean(data[9][2][1],axis=0)[2],np.mean(data[12][2][1],axis=0)[2]]),\
                       np.mean([np.mean(data[5][3][1],axis=0)[2],np.mean(data[9][3][1],axis=0)[2],np.mean(data[12][3][1],axis=0)[2]])])

stdshear800surface = np.array([np.std([np.mean(data[0][0][1],axis=0)[2],np.mean(data[3][0][1],axis=0)[2],np.mean(data[10][0][1],axis=0)[2],\
                                    np.mean(data[13][0][1],axis=0)[2],np.mean(data[14][0][1],axis=0)[2],np.mean(data[15][0][1],axis=0)[2],np.mean(data[16][0][1],axis=0)[2]]),\
                       np.std([np.mean(data[0][1][1],axis=0)[2],np.mean(data[3][1][1],axis=0)[2],np.mean(data[10][1][1],axis=0)[2],\
                                    np.mean(data[13][1][1],axis=0)[2],np.mean(data[14][1][1],axis=0)[2],np.mean(data[15][1][1],axis=0)[2],np.mean(data[16][1][1],axis=0)[2]]),\
                       np.std([np.mean(data[0][2][1],axis=0)[2],np.mean(data[3][2][1],axis=0)[2],np.mean(data[10][2][1],axis=0)[2],\
                                    np.mean(data[13][2][1],axis=0)[2],np.mean(data[14][2][1],axis=0)[2],np.mean(data[15][2][1],axis=0)[2],np.mean(data[16][2][1],axis=0)[2]]),\
                       np.std([np.mean(data[0][3][1],axis=0)[2],np.mean(data[3][3][1],axis=0)[2],np.mean(data[10][3][1],axis=0)[2],\
                                    np.mean(data[13][3][1],axis=0)[2],np.mean(data[14][3][1],axis=0)[2],np.mean(data[15][3][1],axis=0)[2],np.mean(data[16][3][1],axis=0)[2]]),\
                       np.std([np.mean(data[0][4][1],axis=0)[2],np.mean(data[3][4][1],axis=0)[2],np.mean(data[10][4][1],axis=0)[2],\
                                    np.mean(data[13][4][1],axis=0)[2],np.mean(data[14][4][1],axis=0)[2],np.mean(data[15][4][1],axis=0)[2],np.mean(data[16][4][1],axis=0)[2]]),\
                       np.std([np.mean(data[0][5][1],axis=0)[2],np.mean(data[3][5][1],axis=0)[2],np.mean(data[10][5][1],axis=0)[2],\
                                    np.mean(data[13][5][1],axis=0)[2],np.mean(data[14][5][1],axis=0)[2],np.mean(data[15][5][1],axis=0)[2],np.mean(data[16][5][1],axis=0)[2]])])
stdshear1600surface = np.array([np.std([np.mean(data[2][0][1],axis=0)[2],np.mean(data[4][0][1],axis=0)[2],np.mean(data[6][0][1],axis=0)[2],\
                                 np.mean(data[8][0][1],axis=0)[2],np.mean(data[11][0][1],axis=0)[2]]),\
                       np.std([np.mean(data[2][1][1],axis=0)[2],np.mean(data[4][1][1],axis=0)[2],np.mean(data[6][1][1],axis=0)[2],\
                                 np.mean(data[8][1][1],axis=0)[2],np.mean(data[11][1][1],axis=0)[2]]),\
                       np.std([np.mean(data[2][2][1],axis=0)[2],np.mean(data[4][2][1],axis=0)[2],np.mean(data[6][2][1],axis=0)[2],\
                                 np.mean(data[8][2][1],axis=0)[2],np.mean(data[11][2][1],axis=0)[2]]),\
                       np.std([np.mean(data[2][3][1],axis=0)[2],np.mean(data[4][3][1],axis=0)[2],np.mean(data[6][3][1],axis=0)[2],\
                                 np.mean(data[8][3][1],axis=0)[2],np.mean(data[11][3][1],axis=0)[2]]),\
                       np.std([np.mean(data[2][4][1],axis=0)[2],np.mean(data[4][4][1],axis=0)[2],np.mean(data[6][4][1],axis=0)[2],\
                                 np.mean(data[8][4][1],axis=0)[2],np.mean(data[11][4][1],axis=0)[2]]),\
                       np.std([np.mean(data[2][5][1],axis=0)[2],np.mean(data[4][5][1],axis=0)[2],np.mean(data[6][5][1],axis=0)[2],\
                                 np.mean(data[8][5][1],axis=0)[2],np.mean(data[11][5][1],axis=0)[2]])])
stdshear4000surface = np.array([np.std([np.mean(data[5][0][1],axis=0)[2],np.mean(data[9][0][1],axis=0)[2],np.mean(data[12][0][1],axis=0)[2]]),\
                       np.std([np.mean(data[5][1][1],axis=0)[2],np.mean(data[9][1][1],axis=0)[2],np.mean(data[12][1][1],axis=0)[2]]),\
                       np.std([np.mean(data[5][2][1],axis=0)[2],np.mean(data[9][2][1],axis=0)[2],np.mean(data[12][2][1],axis=0)[2]]),\
                       np.std([np.mean(data[5][3][1],axis=0)[2],np.mean(data[9][3][1],axis=0)[2],np.mean(data[12][3][1],axis=0)[2]])])


## Average local binding availability time
meanrt800surface = np.array([np.mean([1/np.mean(data[0][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][0][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][0][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[0][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][1][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][1][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[0][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][2][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][2][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[0][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][3][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][3][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[0][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][4][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][4][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[0][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][5][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][5][1],axis=0)[4]*45*1e-6*1e3])])
meanrt1600surface = np.array([np.mean([1/np.mean(data[2][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][0][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][0][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[2][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][1][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][1][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[2][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][2][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][2][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[2][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][3][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][3][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[2][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][4][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][4][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[2][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][5][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][5][1],axis=0)[4]*45*1e-6*1e3])])
meanrt4000surface = np.array([np.mean([1/np.mean(data[5][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[9][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[12][0][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[5][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[9][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[12][1][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[5][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[9][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[12][2][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.mean([1/np.mean(data[5][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[9][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[12][3][1],axis=0)[4]*45*1e-6*1e3])])

stdrt800surface = np.array([np.std([1/np.mean(data[0][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][0][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][0][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[0][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][1][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][1][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[0][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][2][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][2][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[0][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][3][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][3][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[0][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][4][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][4][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[0][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[3][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[10][5][1],axis=0)[4]*45*1e-6*1e3,\
                                    np.mean(data[13][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[14][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[15][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[16][5][1],axis=0)[4]*45*1e-6*1e3])])
stdrt1600surface = np.array([np.std([1/np.mean(data[2][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][0][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][0][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[2][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][1][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][1][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[2][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][2][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][2][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[2][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][3][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][3][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[2][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][4][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][4][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][4][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[2][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[4][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[6][5][1],axis=0)[4]*45*1e-6*1e3,\
                                 np.mean(data[8][5][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[11][5][1],axis=0)[4]*45*1e-6*1e3])])
stdrt4000surface = np.array([np.std([1/np.mean(data[5][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[9][0][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[12][0][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[5][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[9][1][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[12][1][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[5][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[9][2][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[12][2][1],axis=0)[4]*45*1e-6*1e3]),\
                       np.std([1/np.mean(data[5][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[9][3][1],axis=0)[4]*45*1e-6*1e3,1/np.mean(data[12][3][1],axis=0)[4]*45*1e-6*1e3])])

meanvel800volume = np.array([np.mean([np.mean(data[0][0][0],axis=0)[3],np.mean(data[3][0][0],axis=0)[3],np.mean(data[10][0][0],axis=0)[3],\
                                    np.mean(data[13][0][0],axis=0)[3],np.mean(data[14][0][0],axis=0)[3],np.mean(data[15][0][0],axis=0)[3],np.mean(data[16][0][0],axis=0)[3]]),\
                       np.mean([np.mean(data[0][1][0],axis=0)[3],np.mean(data[3][1][0],axis=0)[3],np.mean(data[10][1][0],axis=0)[3],\
                                    np.mean(data[13][1][0],axis=0)[3],np.mean(data[14][1][0],axis=0)[3],np.mean(data[15][1][0],axis=0)[3],np.mean(data[16][1][0],axis=0)[3]]),\
                       np.mean([np.mean(data[0][2][0],axis=0)[3],np.mean(data[3][2][0],axis=0)[3],np.mean(data[10][2][0],axis=0)[3],\
                                    np.mean(data[13][2][0],axis=0)[3],np.mean(data[14][2][0],axis=0)[3],np.mean(data[15][2][0],axis=0)[3],np.mean(data[16][2][0],axis=0)[3]]),\
                       np.mean([np.mean(data[0][3][0],axis=0)[3],np.mean(data[3][3][0],axis=0)[3],np.mean(data[10][3][0],axis=0)[3],\
                                    np.mean(data[13][3][0],axis=0)[3],np.mean(data[14][3][0],axis=0)[3],np.mean(data[15][3][0],axis=0)[3],np.mean(data[16][3][0],axis=0)[3]]),\
                       np.mean([np.mean(data[0][4][0],axis=0)[3],np.mean(data[3][4][0],axis=0)[3],np.mean(data[10][4][0],axis=0)[3],\
                                    np.mean(data[13][4][0],axis=0)[3],np.mean(data[14][4][0],axis=0)[3],np.mean(data[15][4][0],axis=0)[3],np.mean(data[16][4][0],axis=0)[3]]),\
                       np.mean([np.mean(data[0][5][0],axis=0)[3],np.mean(data[3][5][0],axis=0)[3],np.mean(data[10][5][0],axis=0)[3],\
                                    np.mean(data[13][5][0],axis=0)[3],np.mean(data[14][5][0],axis=0)[3],np.mean(data[15][5][0],axis=0)[3],np.mean(data[16][5][0],axis=0)[3]])])
meanvel1600volume = np.array([np.mean([np.mean(data[2][0][0],axis=0)[3],np.mean(data[4][0][0],axis=0)[3],np.mean(data[6][0][0],axis=0)[3],\
                                 np.mean(data[8][0][0],axis=0)[3],np.mean(data[11][0][0],axis=0)[3]]),\
                       np.mean([np.mean(data[2][1][0],axis=0)[3],np.mean(data[4][1][0],axis=0)[3],np.mean(data[6][1][0],axis=0)[3],\
                                 np.mean(data[8][1][0],axis=0)[3],np.mean(data[11][1][0],axis=0)[3]]),\
                       np.mean([np.mean(data[2][2][0],axis=0)[3],np.mean(data[4][2][0],axis=0)[3],np.mean(data[6][2][0],axis=0)[3],\
                                 np.mean(data[8][2][0],axis=0)[3],np.mean(data[11][2][0],axis=0)[3]]),\
                       np.mean([np.mean(data[2][3][0],axis=0)[3],np.mean(data[4][3][0],axis=0)[3],np.mean(data[6][3][0],axis=0)[3],\
                                 np.mean(data[8][3][0],axis=0)[3],np.mean(data[11][3][0],axis=0)[3]]),\
                       np.mean([np.mean(data[2][4][0],axis=0)[3],np.mean(data[4][4][0],axis=0)[3],np.mean(data[6][4][0],axis=0)[3],\
                                 np.mean(data[8][4][0],axis=0)[3],np.mean(data[11][4][0],axis=0)[3]]),\
                       np.mean([np.mean(data[2][5][0],axis=0)[3],np.mean(data[4][5][0],axis=0)[3],np.mean(data[6][5][0],axis=0)[3],\
                                 np.mean(data[8][5][0],axis=0)[3],np.mean(data[11][5][0],axis=0)[3]])])
meanvel4000volume = np.array([np.mean([np.mean(data[5][0][0],axis=0)[3],np.mean(data[9][0][0],axis=0)[3],np.mean(data[12][0][0],axis=0)[3]]),\
                       np.mean([np.mean(data[5][1][0],axis=0)[3],np.mean(data[9][1][0],axis=0)[3],np.mean(data[12][1][0],axis=0)[3]]),\
                       np.mean([np.mean(data[5][2][0],axis=0)[3],np.mean(data[9][2][0],axis=0)[3],np.mean(data[12][2][0],axis=0)[3]]),\
                       np.mean([np.mean(data[5][3][0],axis=0)[3],np.mean(data[9][3][0],axis=0)[3],np.mean(data[12][3][0],axis=0)[3]])])

stdvel800volume = np.array([np.std([np.mean(data[0][0][0],axis=0)[3],np.mean(data[3][0][0],axis=0)[3],np.mean(data[10][0][0],axis=0)[3],\
                                    np.mean(data[13][0][0],axis=0)[3],np.mean(data[14][0][0],axis=0)[3],np.mean(data[15][0][0],axis=0)[3],np.mean(data[16][0][0],axis=0)[3]]),\
                       np.std([np.mean(data[0][1][0],axis=0)[3],np.mean(data[3][1][0],axis=0)[3],np.mean(data[10][1][0],axis=0)[3],\
                                    np.mean(data[13][1][0],axis=0)[3],np.mean(data[14][1][0],axis=0)[3],np.mean(data[15][1][0],axis=0)[3],np.mean(data[16][1][0],axis=0)[3]]),\
                       np.std([np.mean(data[0][2][0],axis=0)[3],np.mean(data[3][2][0],axis=0)[3],np.mean(data[10][2][0],axis=0)[3],\
                                    np.mean(data[13][2][0],axis=0)[3],np.mean(data[14][2][0],axis=0)[3],np.mean(data[15][2][0],axis=0)[3],np.mean(data[16][2][0],axis=0)[3]]),\
                       np.std([np.mean(data[0][3][0],axis=0)[3],np.mean(data[3][3][0],axis=0)[3],np.mean(data[10][3][0],axis=0)[3],\
                                    np.mean(data[13][3][0],axis=0)[3],np.mean(data[14][3][0],axis=0)[3],np.mean(data[15][3][0],axis=0)[3],np.mean(data[16][3][0],axis=0)[3]]),\
                       np.std([np.mean(data[0][4][0],axis=0)[3],np.mean(data[3][4][0],axis=0)[3],np.mean(data[10][4][0],axis=0)[3],\
                                    np.mean(data[13][4][0],axis=0)[3],np.mean(data[14][4][0],axis=0)[3],np.mean(data[15][4][0],axis=0)[3],np.mean(data[16][4][0],axis=0)[3]]),\
                       np.std([np.mean(data[0][5][0],axis=0)[3],np.mean(data[3][5][0],axis=0)[3],np.mean(data[10][5][0],axis=0)[3],\
                                    np.mean(data[13][5][0],axis=0)[3],np.mean(data[14][5][0],axis=0)[3],np.mean(data[15][5][0],axis=0)[3],np.mean(data[16][5][0],axis=0)[3]])])
stdvel1600volume = np.array([np.std([np.mean(data[2][0][0],axis=0)[3],np.mean(data[4][0][0],axis=0)[3],np.mean(data[6][0][0],axis=0)[3],\
                                 np.mean(data[8][0][0],axis=0)[3],np.mean(data[11][0][0],axis=0)[3]]),\
                       np.std([np.mean(data[2][1][0],axis=0)[3],np.mean(data[4][1][0],axis=0)[3],np.mean(data[6][1][0],axis=0)[3],\
                                 np.mean(data[8][1][0],axis=0)[3],np.mean(data[11][1][0],axis=0)[3]]),\
                       np.std([np.mean(data[2][2][0],axis=0)[3],np.mean(data[4][2][0],axis=0)[3],np.mean(data[6][2][0],axis=0)[3],\
                                 np.mean(data[8][2][0],axis=0)[3],np.mean(data[11][2][0],axis=0)[3]]),\
                       np.std([np.mean(data[2][3][0],axis=0)[3],np.mean(data[4][3][0],axis=0)[3],np.mean(data[6][3][0],axis=0)[3],\
                                 np.mean(data[8][3][0],axis=0)[3],np.mean(data[11][3][0],axis=0)[3]]),\
                       np.std([np.mean(data[2][4][0],axis=0)[3],np.mean(data[4][4][0],axis=0)[3],np.mean(data[6][4][0],axis=0)[3],\
                                 np.mean(data[8][4][0],axis=0)[3],np.mean(data[11][4][0],axis=0)[3]]),\
                       np.std([np.mean(data[2][5][0],axis=0)[3],np.mean(data[4][5][0],axis=0)[3],np.mean(data[6][5][0],axis=0)[3],\
                                 np.mean(data[8][5][0],axis=0)[3],np.mean(data[11][5][0],axis=0)[3]])])
stdvel4000volume = np.array([np.std([np.mean(data[5][0][0],axis=0)[3],np.mean(data[9][0][0],axis=0)[3],np.mean(data[12][0][0],axis=0)[3]]),\
                       np.std([np.mean(data[5][1][0],axis=0)[3],np.mean(data[9][1][0],axis=0)[3],np.mean(data[12][1][0],axis=0)[3]]),\
                       np.std([np.mean(data[5][2][0],axis=0)[3],np.mean(data[9][2][0],axis=0)[3],np.mean(data[12][2][0],axis=0)[3]]),\
                       np.std([np.mean(data[5][3][0],axis=0)[3],np.mean(data[9][3][0],axis=0)[3],np.mean(data[12][3][0],axis=0)[3]])])


###----------------------------------------------------- Plot -----------------------------------------------------###
time = np.array([1,2,4,6,9,12])
time1 = np.array([1,6,11,16,21,26])
time2 = np.array([1,6,11,16])
time3 = np.array([1,3,5,7,9,11])
time4 = np.array([1,3,5,7])

labels=['1','2','4','6','9','12']
fontsize = 16
ticksize = 14
ticksizeZoom = 24

# color1 = 'tab:red'
# color2 = 'tab:blue'
# color3 = 'tab:orange'
color1 = (235/255,153/255,156/255) ## pink
color2 = (161/255,125/255,180/255) ## purple
color3 = (142/255,165/255,200/255) ## blue
edgecolor = (102/255,100/255,100/255)
color4 = 'blue'
color5 = 'fuchsia'
color6 = 'darkorange'
color7 = 'green'

width12 = 0.7
width34 = 0.4


## Residence time
fig, ax = plt.subplots()
ax.bar(time3-width34, meanrt800surface, yerr=stdrt800surface, alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width34)
ax.bar(time3, meanrt1600surface, yerr=stdrt1600surface, alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width34)
ax.bar(time4+width34, meanrt4000surface, yerr=stdrt4000surface, alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width34)

rtThreshold = 1
plt.axhline(rtThreshold, color='red', ls='--', linewidth=3)

ax.set_ylabel('local binding availability time $[ms]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average local binding availability time on surface', fontsize=fontsize)

plt.xticks(time3, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=2,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('rtS.png',bbox_inches='tight')
plt.show()



## Shear rate
fig, ax = plt.subplots()
ax.bar(time3-width34, meanshear800surface, yerr=stdshear800surface, alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width34)
ax.bar(time3, meanshear1600surface, yerr=stdshear1600surface, alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width34)
ax.bar(time4+width34, meanshear4000surface, yerr=stdshear4000surface, alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width34)

srThreshold = 2500
plt.axhline(srThreshold, color='red', ls='--', linewidth=3)

ax.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average shear rate on surface', fontsize=fontsize)

plt.xticks(time3, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('shearS.png',bbox_inches='tight')
plt.show()


## rate of elongation surface
fig, ax = plt.subplots()
ax.bar(time3-width34, meanelon800surface, yerr=stdelon800surface, alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width34)
ax.bar(time3, meanelon1600surface, yerr=stdelon1600surface, alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width34)
ax.bar(time4+width34, meanelon4000surface, yerr=stdelon4000surface, alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width34)

erThreshold = 600
plt.axhline(erThreshold, color='red', ls='--', linewidth=3)

ax.set_ylabel('rate of elongation $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average rate of elongation on surface', fontsize=fontsize)

plt.xticks(time3, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('elonS.png',bbox_inches='tight')
plt.show()

