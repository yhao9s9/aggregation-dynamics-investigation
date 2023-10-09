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
## d2_800/6min/2toppercent = data[14][3][2] -> 2D array = num_node * [PointZ, elongation, shear rate, shear stress, velocity]


# m1_800 = np.concatenate([data[0][0][2],data[3][0][2],data[10][0][2],data[13][0][2],data[14][0][2],data[15][0][2],data[16][0][2]])
# m2_800 = np.concatenate([data[0][1][2],data[3][1][2],data[10][1][2],data[13][1][2],data[14][1][2],data[15][1][2],data[16][1][2]])
# m4_800 = np.concatenate([data[0][2][2],data[3][2][2],data[10][2][2],data[13][2][2],data[14][2][2],data[15][2][2],data[16][2][2]])
# m6_800 = np.concatenate([data[0][3][2],data[3][3][2],data[10][3][2],data[13][3][2],data[14][3][2],data[15][3][2],data[16][3][2]])
# m9_800 = np.concatenate([data[0][4][2],data[3][4][2],data[10][4][2],data[13][4][2],data[14][4][2],data[15][4][2],data[16][4][2]])
# m12_800 = np.concatenate([data[0][5][2],data[3][5][2],data[10][5][2],data[13][5][2],data[14][5][2],data[15][5][2],data[16][5][2]])
# print(m1_800.shape)

# sns.kdeplot(m1_800[:,2],label='1 min')
# sns.kdeplot(m2_800[:,2],label='2 min')
# sns.kdeplot(m4_800[:,2],label='4 min')
# sns.kdeplot(m6_800[:,2],label='6 min')
# sns.kdeplot(m9_800[:,2],label='9 min')
# sns.kdeplot(m12_800[:,2],label='12 min')

# plt.legend()
# plt.show()

## Average rate of elongation
meanelon800face = np.array([np.mean([np.mean(data[0][0][4],axis=0)[1],np.mean(data[3][0][4],axis=0)[1],np.mean(data[10][0][4],axis=0)[1],\
                                    np.mean(data[13][0][4],axis=0)[1],np.mean(data[14][0][4],axis=0)[1],np.mean(data[15][0][4],axis=0)[1],np.mean(data[16][0][4],axis=0)[1]]),\
                       np.mean([np.mean(data[0][1][4],axis=0)[1],np.mean(data[3][1][4],axis=0)[1],np.mean(data[10][1][4],axis=0)[1],\
                                    np.mean(data[13][1][4],axis=0)[1],np.mean(data[14][1][4],axis=0)[1],np.mean(data[15][1][4],axis=0)[1],np.mean(data[16][1][4],axis=0)[1]]),\
                       np.mean([np.mean(data[0][2][4],axis=0)[1],np.mean(data[3][2][4],axis=0)[1],np.mean(data[10][2][4],axis=0)[1],\
                                    np.mean(data[13][2][4],axis=0)[1],np.mean(data[14][2][4],axis=0)[1],np.mean(data[15][2][4],axis=0)[1],np.mean(data[16][2][4],axis=0)[1]]),\
                       np.mean([np.mean(data[0][3][4],axis=0)[1],np.mean(data[3][3][4],axis=0)[1],np.mean(data[10][3][4],axis=0)[1],\
                                    np.mean(data[13][3][4],axis=0)[1],np.mean(data[14][3][4],axis=0)[1],np.mean(data[15][3][4],axis=0)[1],np.mean(data[16][3][4],axis=0)[1]]),\
                       np.mean([np.mean(data[0][4][4],axis=0)[1],np.mean(data[3][4][4],axis=0)[1],np.mean(data[10][4][4],axis=0)[1],\
                                    np.mean(data[13][4][4],axis=0)[1],np.mean(data[14][4][4],axis=0)[1],np.mean(data[15][4][4],axis=0)[1],np.mean(data[16][4][4],axis=0)[1]]),\
                       np.mean([np.mean(data[0][5][4],axis=0)[1],np.mean(data[3][5][4],axis=0)[1],np.mean(data[10][5][4],axis=0)[1],\
                                    np.mean(data[13][5][4],axis=0)[1],np.mean(data[14][5][4],axis=0)[1],np.mean(data[15][5][4],axis=0)[1],np.mean(data[16][5][4],axis=0)[1]])])
meanelon1600face = np.array([np.mean([np.mean(data[2][0][4],axis=0)[1],np.mean(data[4][0][4],axis=0)[1],np.mean(data[6][0][4],axis=0)[1],\
                                 np.mean(data[8][0][4],axis=0)[1],np.mean(data[11][0][4],axis=0)[1]]),\
                       np.mean([np.mean(data[2][1][4],axis=0)[1],np.mean(data[4][1][4],axis=0)[1],np.mean(data[6][1][4],axis=0)[1],\
                                 np.mean(data[8][1][4],axis=0)[1],np.mean(data[11][1][4],axis=0)[1]]),\
                       np.mean([np.mean(data[2][2][4],axis=0)[1],np.mean(data[4][2][4],axis=0)[1],np.mean(data[6][2][4],axis=0)[1],\
                                 np.mean(data[8][2][4],axis=0)[1],np.mean(data[11][2][4],axis=0)[1]]),\
                       np.mean([np.mean(data[2][3][4],axis=0)[1],np.mean(data[4][3][4],axis=0)[1],np.mean(data[6][3][4],axis=0)[1],\
                                 np.mean(data[8][3][4],axis=0)[1],np.mean(data[11][3][4],axis=0)[1]]),\
                       np.mean([np.mean(data[2][4][4],axis=0)[1],np.mean(data[4][4][4],axis=0)[1],np.mean(data[6][4][4],axis=0)[1],\
                                 np.mean(data[8][4][4],axis=0)[1],np.mean(data[11][4][4],axis=0)[1]]),\
                       np.mean([np.mean(data[2][5][4],axis=0)[1],np.mean(data[4][5][4],axis=0)[1],np.mean(data[6][5][4],axis=0)[1],\
                                 np.mean(data[8][5][4],axis=0)[1],np.mean(data[11][5][4],axis=0)[1]])])
meanelon4000face = np.array([np.mean([np.mean(data[5][0][4],axis=0)[1],np.mean(data[9][0][4],axis=0)[1],np.mean(data[12][0][4],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][4],axis=0)[1],np.mean(data[9][1][4],axis=0)[1],np.mean(data[12][1][4],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][4],axis=0)[1],np.mean(data[9][2][4],axis=0)[1],np.mean(data[12][2][4],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][4],axis=0)[1],np.mean(data[9][3][4],axis=0)[1],np.mean(data[12][3][4],axis=0)[1]])])

stdelon800face = np.array([np.std([np.mean(data[0][0][4],axis=0)[1],np.mean(data[3][0][4],axis=0)[1],np.mean(data[10][0][4],axis=0)[1],\
                                    np.mean(data[13][0][4],axis=0)[1],np.mean(data[14][0][4],axis=0)[1],np.mean(data[15][0][4],axis=0)[1],np.mean(data[16][0][4],axis=0)[1]]),\
                       np.std([np.mean(data[0][1][4],axis=0)[1],np.mean(data[3][1][4],axis=0)[1],np.mean(data[10][1][4],axis=0)[1],\
                                    np.mean(data[13][1][4],axis=0)[1],np.mean(data[14][1][4],axis=0)[1],np.mean(data[15][1][4],axis=0)[1],np.mean(data[16][1][4],axis=0)[1]]),\
                       np.std([np.mean(data[0][2][4],axis=0)[1],np.mean(data[3][2][4],axis=0)[1],np.mean(data[10][2][4],axis=0)[1],\
                                    np.mean(data[13][2][4],axis=0)[1],np.mean(data[14][2][4],axis=0)[1],np.mean(data[15][2][4],axis=0)[1],np.mean(data[16][2][4],axis=0)[1]]),\
                       np.std([np.mean(data[0][3][4],axis=0)[1],np.mean(data[3][3][4],axis=0)[1],np.mean(data[10][3][4],axis=0)[1],\
                                    np.mean(data[13][3][4],axis=0)[1],np.mean(data[14][3][4],axis=0)[1],np.mean(data[15][3][4],axis=0)[1],np.mean(data[16][3][4],axis=0)[1]]),\
                       np.std([np.mean(data[0][4][4],axis=0)[1],np.mean(data[3][4][4],axis=0)[1],np.mean(data[10][4][4],axis=0)[1],\
                                    np.mean(data[13][4][4],axis=0)[1],np.mean(data[14][4][4],axis=0)[1],np.mean(data[15][4][4],axis=0)[1],np.mean(data[16][4][4],axis=0)[1]]),\
                       np.std([np.mean(data[0][5][4],axis=0)[1],np.mean(data[3][5][4],axis=0)[1],np.mean(data[10][5][4],axis=0)[1],\
                                    np.mean(data[13][5][4],axis=0)[1],np.mean(data[14][5][4],axis=0)[1],np.mean(data[15][5][4],axis=0)[1],np.mean(data[16][5][4],axis=0)[1]])])
stdelon1600face = np.array([np.std([np.mean(data[2][0][4],axis=0)[1],np.mean(data[4][0][4],axis=0)[1],np.mean(data[6][0][4],axis=0)[1],\
                                 np.mean(data[8][0][4],axis=0)[1],np.mean(data[11][0][4],axis=0)[1]]),\
                       np.std([np.mean(data[2][1][4],axis=0)[1],np.mean(data[4][1][4],axis=0)[1],np.mean(data[6][1][4],axis=0)[1],\
                                 np.mean(data[8][1][4],axis=0)[1],np.mean(data[11][1][4],axis=0)[1]]),\
                       np.std([np.mean(data[2][2][4],axis=0)[1],np.mean(data[4][2][4],axis=0)[1],np.mean(data[6][2][4],axis=0)[1],\
                                 np.mean(data[8][2][4],axis=0)[1],np.mean(data[11][2][4],axis=0)[1]]),\
                       np.std([np.mean(data[2][3][4],axis=0)[1],np.mean(data[4][3][4],axis=0)[1],np.mean(data[6][3][4],axis=0)[1],\
                                 np.mean(data[8][3][4],axis=0)[1],np.mean(data[11][3][4],axis=0)[1]]),\
                       np.std([np.mean(data[2][4][4],axis=0)[1],np.mean(data[4][4][4],axis=0)[1],np.mean(data[6][4][4],axis=0)[1],\
                                 np.mean(data[8][4][4],axis=0)[1],np.mean(data[11][4][4],axis=0)[1]]),\
                       np.std([np.mean(data[2][5][4],axis=0)[1],np.mean(data[4][5][4],axis=0)[1],np.mean(data[6][5][4],axis=0)[1],\
                                 np.mean(data[8][5][4],axis=0)[1],np.mean(data[11][5][4],axis=0)[1]])])
stdelon4000face = np.array([np.std([np.mean(data[5][0][4],axis=0)[1],np.mean(data[9][0][4],axis=0)[1],np.mean(data[12][0][4],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][4],axis=0)[1],np.mean(data[9][1][4],axis=0)[1],np.mean(data[12][1][4],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][4],axis=0)[1],np.mean(data[9][2][4],axis=0)[1],np.mean(data[12][2][4],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][4],axis=0)[1],np.mean(data[9][3][4],axis=0)[1],np.mean(data[12][3][4],axis=0)[1]])])

meanelon800back = np.array([np.mean([np.mean(data[0][0][5],axis=0)[1],np.mean(data[3][0][5],axis=0)[1],np.mean(data[10][0][5],axis=0)[1],\
                                    np.mean(data[13][0][5],axis=0)[1],np.mean(data[14][0][5],axis=0)[1],np.mean(data[15][0][5],axis=0)[1],np.mean(data[16][0][5],axis=0)[1]]),\
                       np.mean([np.mean(data[0][1][5],axis=0)[1],np.mean(data[3][1][5],axis=0)[1],np.mean(data[10][1][5],axis=0)[1],\
                                    np.mean(data[13][1][5],axis=0)[1],np.mean(data[14][1][5],axis=0)[1],np.mean(data[15][1][5],axis=0)[1],np.mean(data[16][1][5],axis=0)[1]]),\
                       np.mean([np.mean(data[0][2][5],axis=0)[1],np.mean(data[3][2][5],axis=0)[1],np.mean(data[10][2][5],axis=0)[1],\
                                    np.mean(data[13][2][5],axis=0)[1],np.mean(data[14][2][5],axis=0)[1],np.mean(data[15][2][5],axis=0)[1],np.mean(data[16][2][5],axis=0)[1]]),\
                       np.mean([np.mean(data[0][3][5],axis=0)[1],np.mean(data[3][3][5],axis=0)[1],np.mean(data[10][3][5],axis=0)[1],\
                                    np.mean(data[13][3][5],axis=0)[1],np.mean(data[14][3][5],axis=0)[1],np.mean(data[15][3][5],axis=0)[1],np.mean(data[16][3][5],axis=0)[1]]),\
                       np.mean([np.mean(data[0][4][5],axis=0)[1],np.mean(data[3][4][5],axis=0)[1],np.mean(data[10][4][5],axis=0)[1],\
                                    np.mean(data[13][4][5],axis=0)[1],np.mean(data[14][4][5],axis=0)[1],np.mean(data[15][4][5],axis=0)[1],np.mean(data[16][4][5],axis=0)[1]]),\
                       np.mean([np.mean(data[0][5][5],axis=0)[1],np.mean(data[3][5][5],axis=0)[1],np.mean(data[10][5][5],axis=0)[1],\
                                    np.mean(data[13][5][5],axis=0)[1],np.mean(data[14][5][5],axis=0)[1],np.mean(data[15][5][5],axis=0)[1],np.mean(data[16][5][5],axis=0)[1]])])
meanelon1600back = np.array([np.mean([np.mean(data[2][0][5],axis=0)[1],np.mean(data[4][0][5],axis=0)[1],np.mean(data[6][0][5],axis=0)[1],\
                                 np.mean(data[8][0][5],axis=0)[1],np.mean(data[11][0][5],axis=0)[1]]),\
                       np.mean([np.mean(data[2][1][5],axis=0)[1],np.mean(data[4][1][5],axis=0)[1],np.mean(data[6][1][5],axis=0)[1],\
                                 np.mean(data[8][1][5],axis=0)[1],np.mean(data[11][1][5],axis=0)[1]]),\
                       np.mean([np.mean(data[2][2][5],axis=0)[1],np.mean(data[4][2][5],axis=0)[1],np.mean(data[6][2][5],axis=0)[1],\
                                 np.mean(data[8][2][5],axis=0)[1],np.mean(data[11][2][5],axis=0)[1]]),\
                       np.mean([np.mean(data[2][3][5],axis=0)[1],np.mean(data[4][3][5],axis=0)[1],np.mean(data[6][3][5],axis=0)[1],\
                                 np.mean(data[8][3][5],axis=0)[1],np.mean(data[11][3][5],axis=0)[1]]),\
                       np.mean([np.mean(data[2][4][5],axis=0)[1],np.mean(data[4][4][5],axis=0)[1],np.mean(data[6][4][5],axis=0)[1],\
                                 np.mean(data[8][4][5],axis=0)[1],np.mean(data[11][4][5],axis=0)[1]]),\
                       np.mean([np.mean(data[2][5][5],axis=0)[1],np.mean(data[4][5][5],axis=0)[1],np.mean(data[6][5][5],axis=0)[1],\
                                 np.mean(data[8][5][5],axis=0)[1],np.mean(data[11][5][5],axis=0)[1]])])
meanelon4000back = np.array([np.mean([np.mean(data[5][0][5],axis=0)[1],np.mean(data[9][0][5],axis=0)[1],np.mean(data[12][0][5],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][5],axis=0)[1],np.mean(data[9][1][5],axis=0)[1],np.mean(data[12][1][5],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][5],axis=0)[1],np.mean(data[9][2][5],axis=0)[1],np.mean(data[12][2][5],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][5],axis=0)[1],np.mean(data[9][3][5],axis=0)[1],np.mean(data[12][3][5],axis=0)[1]])])

stdelon800back = np.array([np.std([np.mean(data[0][0][5],axis=0)[1],np.mean(data[3][0][5],axis=0)[1],np.mean(data[10][0][5],axis=0)[1],\
                                    np.mean(data[13][0][5],axis=0)[1],np.mean(data[14][0][5],axis=0)[1],np.mean(data[15][0][5],axis=0)[1],np.mean(data[16][0][5],axis=0)[1]]),\
                       np.std([np.mean(data[0][1][5],axis=0)[1],np.mean(data[3][1][5],axis=0)[1],np.mean(data[10][1][5],axis=0)[1],\
                                    np.mean(data[13][1][5],axis=0)[1],np.mean(data[14][1][5],axis=0)[1],np.mean(data[15][1][5],axis=0)[1],np.mean(data[16][1][5],axis=0)[1]]),\
                       np.std([np.mean(data[0][2][5],axis=0)[1],np.mean(data[3][2][5],axis=0)[1],np.mean(data[10][2][5],axis=0)[1],\
                                    np.mean(data[13][2][5],axis=0)[1],np.mean(data[14][2][5],axis=0)[1],np.mean(data[15][2][5],axis=0)[1],np.mean(data[16][2][5],axis=0)[1]]),\
                       np.std([np.mean(data[0][3][5],axis=0)[1],np.mean(data[3][3][5],axis=0)[1],np.mean(data[10][3][5],axis=0)[1],\
                                    np.mean(data[13][3][5],axis=0)[1],np.mean(data[14][3][5],axis=0)[1],np.mean(data[15][3][5],axis=0)[1],np.mean(data[16][3][5],axis=0)[1]]),\
                       np.std([np.mean(data[0][4][5],axis=0)[1],np.mean(data[3][4][5],axis=0)[1],np.mean(data[10][4][5],axis=0)[1],\
                                    np.mean(data[13][4][5],axis=0)[1],np.mean(data[14][4][5],axis=0)[1],np.mean(data[15][4][5],axis=0)[1],np.mean(data[16][4][5],axis=0)[1]]),\
                       np.std([np.mean(data[0][5][5],axis=0)[1],np.mean(data[3][5][5],axis=0)[1],np.mean(data[10][5][5],axis=0)[1],\
                                    np.mean(data[13][5][5],axis=0)[1],np.mean(data[14][5][5],axis=0)[1],np.mean(data[15][5][5],axis=0)[1],np.mean(data[16][5][5],axis=0)[1]])])
stdelon1600back = np.array([np.std([np.mean(data[2][0][5],axis=0)[1],np.mean(data[4][0][5],axis=0)[1],np.mean(data[6][0][5],axis=0)[1],\
                                 np.mean(data[8][0][5],axis=0)[1],np.mean(data[11][0][5],axis=0)[1]]),\
                       np.std([np.mean(data[2][1][5],axis=0)[1],np.mean(data[4][1][5],axis=0)[1],np.mean(data[6][1][5],axis=0)[1],\
                                 np.mean(data[8][1][5],axis=0)[1],np.mean(data[11][1][5],axis=0)[1]]),\
                       np.std([np.mean(data[2][2][5],axis=0)[1],np.mean(data[4][2][5],axis=0)[1],np.mean(data[6][2][5],axis=0)[1],\
                                 np.mean(data[8][2][5],axis=0)[1],np.mean(data[11][2][5],axis=0)[1]]),\
                       np.std([np.mean(data[2][3][5],axis=0)[1],np.mean(data[4][3][5],axis=0)[1],np.mean(data[6][3][5],axis=0)[1],\
                                 np.mean(data[8][3][5],axis=0)[1],np.mean(data[11][3][5],axis=0)[1]]),\
                       np.std([np.mean(data[2][4][5],axis=0)[1],np.mean(data[4][4][5],axis=0)[1],np.mean(data[6][4][5],axis=0)[1],\
                                 np.mean(data[8][4][5],axis=0)[1],np.mean(data[11][4][5],axis=0)[1]]),\
                       np.std([np.mean(data[2][5][5],axis=0)[1],np.mean(data[4][5][5],axis=0)[1],np.mean(data[6][5][5],axis=0)[1],\
                                 np.mean(data[8][5][5],axis=0)[1],np.mean(data[11][5][5],axis=0)[1]])])
stdelon4000back = np.array([np.std([np.mean(data[5][0][5],axis=0)[1],np.mean(data[9][0][5],axis=0)[1],np.mean(data[12][0][5],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][5],axis=0)[1],np.mean(data[9][1][5],axis=0)[1],np.mean(data[12][1][5],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][5],axis=0)[1],np.mean(data[9][2][5],axis=0)[1],np.mean(data[12][2][5],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][5],axis=0)[1],np.mean(data[9][3][5],axis=0)[1],np.mean(data[12][3][5],axis=0)[1]])])

meanelon800topp = np.array([np.mean([np.mean(data[0][0][2],axis=0)[1],np.mean(data[3][0][2],axis=0)[1],np.mean(data[10][0][2],axis=0)[1],\
                                    np.mean(data[13][0][2],axis=0)[1],np.mean(data[14][0][2],axis=0)[1],np.mean(data[15][0][2],axis=0)[1],np.mean(data[16][0][2],axis=0)[1]]),\
                       np.mean([np.mean(data[0][1][2],axis=0)[1],np.mean(data[3][1][2],axis=0)[1],np.mean(data[10][1][2],axis=0)[1],\
                                    np.mean(data[13][1][2],axis=0)[1],np.mean(data[14][1][2],axis=0)[1],np.mean(data[15][1][2],axis=0)[1],np.mean(data[16][1][2],axis=0)[1]]),\
                       np.mean([np.mean(data[0][2][2],axis=0)[1],np.mean(data[3][2][2],axis=0)[1],np.mean(data[10][2][2],axis=0)[1],\
                                    np.mean(data[13][2][2],axis=0)[1],np.mean(data[14][2][2],axis=0)[1],np.mean(data[15][2][2],axis=0)[1],np.mean(data[16][2][2],axis=0)[1]]),\
                       np.mean([np.mean(data[0][3][2],axis=0)[1],np.mean(data[3][3][2],axis=0)[1],np.mean(data[10][3][2],axis=0)[1],\
                                    np.mean(data[13][3][2],axis=0)[1],np.mean(data[14][3][2],axis=0)[1],np.mean(data[15][3][2],axis=0)[1],np.mean(data[16][3][2],axis=0)[1]]),\
                       np.mean([np.mean(data[0][4][2],axis=0)[1],np.mean(data[3][4][2],axis=0)[1],np.mean(data[10][4][2],axis=0)[1],\
                                    np.mean(data[13][4][2],axis=0)[1],np.mean(data[14][4][2],axis=0)[1],np.mean(data[15][4][2],axis=0)[1],np.mean(data[16][4][2],axis=0)[1]]),\
                       np.mean([np.mean(data[0][5][2],axis=0)[1],np.mean(data[3][5][2],axis=0)[1],np.mean(data[10][5][2],axis=0)[1],\
                                    np.mean(data[13][5][2],axis=0)[1],np.mean(data[14][5][2],axis=0)[1],np.mean(data[15][5][2],axis=0)[1],np.mean(data[16][5][2],axis=0)[1]])])
meanelon1600topp = np.array([np.mean([np.mean(data[2][0][2],axis=0)[1],np.mean(data[4][0][2],axis=0)[1],np.mean(data[6][0][2],axis=0)[1],\
                                 np.mean(data[8][0][2],axis=0)[1],np.mean(data[11][0][2],axis=0)[1]]),\
                       np.mean([np.mean(data[2][1][2],axis=0)[1],np.mean(data[4][1][2],axis=0)[1],np.mean(data[6][1][2],axis=0)[1],\
                                 np.mean(data[8][1][2],axis=0)[1],np.mean(data[11][1][2],axis=0)[1]]),\
                       np.mean([np.mean(data[2][2][2],axis=0)[1],np.mean(data[4][2][2],axis=0)[1],np.mean(data[6][2][2],axis=0)[1],\
                                 np.mean(data[8][2][2],axis=0)[1],np.mean(data[11][2][2],axis=0)[1]]),\
                       np.mean([np.mean(data[2][3][2],axis=0)[1],np.mean(data[4][3][2],axis=0)[1],np.mean(data[6][3][2],axis=0)[1],\
                                 np.mean(data[8][3][2],axis=0)[1],np.mean(data[11][3][2],axis=0)[1]]),\
                       np.mean([np.mean(data[2][4][2],axis=0)[1],np.mean(data[4][4][2],axis=0)[1],np.mean(data[6][4][2],axis=0)[1],\
                                 np.mean(data[8][4][2],axis=0)[1],np.mean(data[11][4][2],axis=0)[1]]),\
                       np.mean([np.mean(data[2][5][2],axis=0)[1],np.mean(data[4][5][2],axis=0)[1],np.mean(data[6][5][2],axis=0)[1],\
                                 np.mean(data[8][5][2],axis=0)[1],np.mean(data[11][5][2],axis=0)[1]])])
meanelon4000topp = np.array([np.mean([np.mean(data[5][0][2],axis=0)[1],np.mean(data[9][0][2],axis=0)[1],np.mean(data[12][0][2],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][2],axis=0)[1],np.mean(data[9][1][2],axis=0)[1],np.mean(data[12][1][2],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][2],axis=0)[1],np.mean(data[9][2][2],axis=0)[1],np.mean(data[12][2][2],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][2],axis=0)[1],np.mean(data[9][3][2],axis=0)[1],np.mean(data[12][3][2],axis=0)[1]])])

stdelon800topp = np.array([np.std([np.mean(data[0][0][2],axis=0)[1],np.mean(data[3][0][2],axis=0)[1],np.mean(data[10][0][2],axis=0)[1],\
                                    np.mean(data[13][0][2],axis=0)[1],np.mean(data[14][0][2],axis=0)[1],np.mean(data[15][0][2],axis=0)[1],np.mean(data[16][0][2],axis=0)[1]]),\
                       np.std([np.mean(data[0][1][2],axis=0)[1],np.mean(data[3][1][2],axis=0)[1],np.mean(data[10][1][2],axis=0)[1],\
                                    np.mean(data[13][1][2],axis=0)[1],np.mean(data[14][1][2],axis=0)[1],np.mean(data[15][1][2],axis=0)[1],np.mean(data[16][1][2],axis=0)[1]]),\
                       np.std([np.mean(data[0][2][2],axis=0)[1],np.mean(data[3][2][2],axis=0)[1],np.mean(data[10][2][2],axis=0)[1],\
                                    np.mean(data[13][2][2],axis=0)[1],np.mean(data[14][2][2],axis=0)[1],np.mean(data[15][2][2],axis=0)[1],np.mean(data[16][2][2],axis=0)[1]]),\
                       np.std([np.mean(data[0][3][2],axis=0)[1],np.mean(data[3][3][2],axis=0)[1],np.mean(data[10][3][2],axis=0)[1],\
                                    np.mean(data[13][3][2],axis=0)[1],np.mean(data[14][3][2],axis=0)[1],np.mean(data[15][3][2],axis=0)[1],np.mean(data[16][3][2],axis=0)[1]]),\
                       np.std([np.mean(data[0][4][2],axis=0)[1],np.mean(data[3][4][2],axis=0)[1],np.mean(data[10][4][2],axis=0)[1],\
                                    np.mean(data[13][4][2],axis=0)[1],np.mean(data[14][4][2],axis=0)[1],np.mean(data[15][4][2],axis=0)[1],np.mean(data[16][4][2],axis=0)[1]]),\
                       np.std([np.mean(data[0][5][2],axis=0)[1],np.mean(data[3][5][2],axis=0)[1],np.mean(data[10][5][2],axis=0)[1],\
                                    np.mean(data[13][5][2],axis=0)[1],np.mean(data[14][5][2],axis=0)[1],np.mean(data[15][5][2],axis=0)[1],np.mean(data[16][5][2],axis=0)[1]])])
stdelon1600topp = np.array([np.std([np.mean(data[2][0][2],axis=0)[1],np.mean(data[4][0][2],axis=0)[1],np.mean(data[6][0][2],axis=0)[1],\
                                 np.mean(data[8][0][2],axis=0)[1],np.mean(data[11][0][2],axis=0)[1]]),\
                       np.std([np.mean(data[2][1][2],axis=0)[1],np.mean(data[4][1][2],axis=0)[1],np.mean(data[6][1][2],axis=0)[1],\
                                 np.mean(data[8][1][2],axis=0)[1],np.mean(data[11][1][2],axis=0)[1]]),\
                       np.std([np.mean(data[2][2][2],axis=0)[1],np.mean(data[4][2][2],axis=0)[1],np.mean(data[6][2][2],axis=0)[1],\
                                 np.mean(data[8][2][2],axis=0)[1],np.mean(data[11][2][2],axis=0)[1]]),\
                       np.std([np.mean(data[2][3][2],axis=0)[1],np.mean(data[4][3][2],axis=0)[1],np.mean(data[6][3][2],axis=0)[1],\
                                 np.mean(data[8][3][2],axis=0)[1],np.mean(data[11][3][2],axis=0)[1]]),\
                       np.std([np.mean(data[2][4][2],axis=0)[1],np.mean(data[4][4][2],axis=0)[1],np.mean(data[6][4][2],axis=0)[1],\
                                 np.mean(data[8][4][2],axis=0)[1],np.mean(data[11][4][2],axis=0)[1]]),\
                       np.std([np.mean(data[2][5][2],axis=0)[1],np.mean(data[4][5][2],axis=0)[1],np.mean(data[6][5][2],axis=0)[1],\
                                 np.mean(data[8][5][2],axis=0)[1],np.mean(data[11][5][2],axis=0)[1]])])
stdelon4000topp = np.array([np.std([np.mean(data[5][0][2],axis=0)[1],np.mean(data[9][0][2],axis=0)[1],np.mean(data[12][0][2],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][2],axis=0)[1],np.mean(data[9][1][2],axis=0)[1],np.mean(data[12][1][2],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][2],axis=0)[1],np.mean(data[9][2][2],axis=0)[1],np.mean(data[12][2][2],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][2],axis=0)[1],np.mean(data[9][3][2],axis=0)[1],np.mean(data[12][3][2],axis=0)[1]])])

meanelon800topf = np.array([np.mean([np.mean(data[0][0][3],axis=0)[1],np.mean(data[3][0][3],axis=0)[1],np.mean(data[10][0][3],axis=0)[1],\
                                    np.mean(data[13][0][3],axis=0)[1],np.mean(data[14][0][3],axis=0)[1],np.mean(data[15][0][3],axis=0)[1],np.mean(data[16][0][3],axis=0)[1]]),\
                       np.mean([np.mean(data[0][1][3],axis=0)[1],np.mean(data[3][1][3],axis=0)[1],np.mean(data[10][1][3],axis=0)[1],\
                                    np.mean(data[13][1][3],axis=0)[1],np.mean(data[14][1][3],axis=0)[1],np.mean(data[15][1][3],axis=0)[1],np.mean(data[16][1][3],axis=0)[1]]),\
                       np.mean([np.mean(data[0][2][3],axis=0)[1],np.mean(data[3][2][3],axis=0)[1],np.mean(data[10][2][3],axis=0)[1],\
                                    np.mean(data[13][2][3],axis=0)[1],np.mean(data[14][2][3],axis=0)[1],np.mean(data[15][2][3],axis=0)[1],np.mean(data[16][2][3],axis=0)[1]]),\
                       np.mean([np.mean(data[0][3][3],axis=0)[1],np.mean(data[3][3][3],axis=0)[1],np.mean(data[10][3][3],axis=0)[1],\
                                    np.mean(data[13][3][3],axis=0)[1],np.mean(data[14][3][3],axis=0)[1],np.mean(data[15][3][3],axis=0)[1],np.mean(data[16][3][3],axis=0)[1]]),\
                       np.mean([np.mean(data[0][4][3],axis=0)[1],np.mean(data[3][4][3],axis=0)[1],np.mean(data[10][4][3],axis=0)[1],\
                                    np.mean(data[13][4][3],axis=0)[1],np.mean(data[14][4][3],axis=0)[1],np.mean(data[15][4][3],axis=0)[1],np.mean(data[16][4][3],axis=0)[1]]),\
                       np.mean([np.mean(data[0][5][3],axis=0)[1],np.mean(data[3][5][3],axis=0)[1],np.mean(data[10][5][3],axis=0)[1],\
                                    np.mean(data[13][5][3],axis=0)[1],np.mean(data[14][5][3],axis=0)[1],np.mean(data[15][5][3],axis=0)[1],np.mean(data[16][5][3],axis=0)[1]])])
meanelon1600topf = np.array([np.mean([np.mean(data[2][0][3],axis=0)[1],np.mean(data[4][0][3],axis=0)[1],np.mean(data[6][0][3],axis=0)[1],\
                                 np.mean(data[8][0][3],axis=0)[1],np.mean(data[11][0][3],axis=0)[1]]),\
                       np.mean([np.mean(data[2][1][3],axis=0)[1],np.mean(data[4][1][3],axis=0)[1],np.mean(data[6][1][3],axis=0)[1],\
                                 np.mean(data[8][1][3],axis=0)[1],np.mean(data[11][1][3],axis=0)[1]]),\
                       np.mean([np.mean(data[2][2][3],axis=0)[1],np.mean(data[4][2][3],axis=0)[1],np.mean(data[6][2][3],axis=0)[1],\
                                 np.mean(data[8][2][3],axis=0)[1],np.mean(data[11][2][3],axis=0)[1]]),\
                       np.mean([np.mean(data[2][3][3],axis=0)[1],np.mean(data[4][3][3],axis=0)[1],np.mean(data[6][3][3],axis=0)[1],\
                                 np.mean(data[8][3][3],axis=0)[1],np.mean(data[11][3][3],axis=0)[1]]),\
                       np.mean([np.mean(data[2][4][3],axis=0)[1],np.mean(data[4][4][3],axis=0)[1],np.mean(data[6][4][3],axis=0)[1],\
                                 np.mean(data[8][4][3],axis=0)[1],np.mean(data[11][4][3],axis=0)[1]]),\
                       np.mean([np.mean(data[2][5][3],axis=0)[1],np.mean(data[4][5][3],axis=0)[1],np.mean(data[6][5][3],axis=0)[1],\
                                 np.mean(data[8][5][3],axis=0)[1],np.mean(data[11][5][3],axis=0)[1]])])
meanelon4000topf = np.array([np.mean([np.mean(data[5][0][3],axis=0)[1],np.mean(data[9][0][3],axis=0)[1],np.mean(data[12][0][3],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][3],axis=0)[1],np.mean(data[9][1][3],axis=0)[1],np.mean(data[12][1][3],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][3],axis=0)[1],np.mean(data[9][2][3],axis=0)[1],np.mean(data[12][2][3],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][3],axis=0)[1],np.mean(data[9][3][3],axis=0)[1],np.mean(data[12][3][3],axis=0)[1]])])

stdelon800topf = np.array([np.std([np.mean(data[0][0][3],axis=0)[1],np.mean(data[3][0][3],axis=0)[1],np.mean(data[10][0][3],axis=0)[1],\
                                    np.mean(data[13][0][3],axis=0)[1],np.mean(data[14][0][3],axis=0)[1],np.mean(data[15][0][3],axis=0)[1],np.mean(data[16][0][3],axis=0)[1]]),\
                       np.std([np.mean(data[0][1][3],axis=0)[1],np.mean(data[3][1][3],axis=0)[1],np.mean(data[10][1][3],axis=0)[1],\
                                    np.mean(data[13][1][3],axis=0)[1],np.mean(data[14][1][3],axis=0)[1],np.mean(data[15][1][3],axis=0)[1],np.mean(data[16][1][3],axis=0)[1]]),\
                       np.std([np.mean(data[0][2][3],axis=0)[1],np.mean(data[3][2][3],axis=0)[1],np.mean(data[10][2][3],axis=0)[1],\
                                    np.mean(data[13][2][3],axis=0)[1],np.mean(data[14][2][3],axis=0)[1],np.mean(data[15][2][3],axis=0)[1],np.mean(data[16][2][3],axis=0)[1]]),\
                       np.std([np.mean(data[0][3][3],axis=0)[1],np.mean(data[3][3][3],axis=0)[1],np.mean(data[10][3][3],axis=0)[1],\
                                    np.mean(data[13][3][3],axis=0)[1],np.mean(data[14][3][3],axis=0)[1],np.mean(data[15][3][3],axis=0)[1],np.mean(data[16][3][3],axis=0)[1]]),\
                       np.std([np.mean(data[0][4][3],axis=0)[1],np.mean(data[3][4][3],axis=0)[1],np.mean(data[10][4][3],axis=0)[1],\
                                    np.mean(data[13][4][3],axis=0)[1],np.mean(data[14][4][3],axis=0)[1],np.mean(data[15][4][3],axis=0)[1],np.mean(data[16][4][3],axis=0)[1]]),\
                       np.std([np.mean(data[0][5][3],axis=0)[1],np.mean(data[3][5][3],axis=0)[1],np.mean(data[10][5][3],axis=0)[1],\
                                    np.mean(data[13][5][3],axis=0)[1],np.mean(data[14][5][3],axis=0)[1],np.mean(data[15][5][3],axis=0)[1],np.mean(data[16][5][3],axis=0)[1]])])
stdelon1600topf = np.array([np.std([np.mean(data[2][0][3],axis=0)[1],np.mean(data[4][0][3],axis=0)[1],np.mean(data[6][0][3],axis=0)[1],\
                                 np.mean(data[8][0][3],axis=0)[1],np.mean(data[11][0][3],axis=0)[1]]),\
                       np.std([np.mean(data[2][1][3],axis=0)[1],np.mean(data[4][1][3],axis=0)[1],np.mean(data[6][1][3],axis=0)[1],\
                                 np.mean(data[8][1][3],axis=0)[1],np.mean(data[11][1][3],axis=0)[1]]),\
                       np.std([np.mean(data[2][2][3],axis=0)[1],np.mean(data[4][2][3],axis=0)[1],np.mean(data[6][2][3],axis=0)[1],\
                                 np.mean(data[8][2][3],axis=0)[1],np.mean(data[11][2][3],axis=0)[1]]),\
                       np.std([np.mean(data[2][3][3],axis=0)[1],np.mean(data[4][3][3],axis=0)[1],np.mean(data[6][3][3],axis=0)[1],\
                                 np.mean(data[8][3][3],axis=0)[1],np.mean(data[11][3][3],axis=0)[1]]),\
                       np.std([np.mean(data[2][4][3],axis=0)[1],np.mean(data[4][4][3],axis=0)[1],np.mean(data[6][4][3],axis=0)[1],\
                                 np.mean(data[8][4][3],axis=0)[1],np.mean(data[11][4][3],axis=0)[1]]),\
                       np.std([np.mean(data[2][5][3],axis=0)[1],np.mean(data[4][5][3],axis=0)[1],np.mean(data[6][5][3],axis=0)[1],\
                                 np.mean(data[8][5][3],axis=0)[1],np.mean(data[11][5][3],axis=0)[1]])])
stdelon4000topf = np.array([np.std([np.mean(data[5][0][3],axis=0)[1],np.mean(data[9][0][3],axis=0)[1],np.mean(data[12][0][3],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][3],axis=0)[1],np.mean(data[9][1][3],axis=0)[1],np.mean(data[12][1][3],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][3],axis=0)[1],np.mean(data[9][2][3],axis=0)[1],np.mean(data[12][2][3],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][3],axis=0)[1],np.mean(data[9][3][3],axis=0)[1],np.mean(data[12][3][3],axis=0)[1]])])

meanelon800surface = np.array([np.mean([np.mean(data[0][0][1],axis=0)[1],np.mean(data[3][0][1],axis=0)[1],np.mean(data[10][0][1],axis=0)[1],\
                                    np.mean(data[13][0][1],axis=0)[1],np.mean(data[14][0][1],axis=0)[1],np.mean(data[15][0][1],axis=0)[1],np.mean(data[16][0][1],axis=0)[1]]),\
                       np.mean([np.mean(data[0][1][1],axis=0)[1],np.mean(data[3][1][1],axis=0)[1],np.mean(data[10][1][1],axis=0)[1],\
                                    np.mean(data[13][1][1],axis=0)[1],np.mean(data[14][1][1],axis=0)[1],np.mean(data[15][1][1],axis=0)[1],np.mean(data[16][1][1],axis=0)[1]]),\
                       np.mean([np.mean(data[0][2][1],axis=0)[1],np.mean(data[3][2][1],axis=0)[1],np.mean(data[10][2][1],axis=0)[1],\
                                    np.mean(data[13][2][1],axis=0)[1],np.mean(data[14][2][1],axis=0)[1],np.mean(data[15][2][1],axis=0)[1],np.mean(data[16][2][1],axis=0)[1]]),\
                       np.mean([np.mean(data[0][3][1],axis=0)[1],np.mean(data[3][3][1],axis=0)[1],np.mean(data[10][3][1],axis=0)[1],\
                                    np.mean(data[13][3][1],axis=0)[1],np.mean(data[14][3][1],axis=0)[1],np.mean(data[15][3][1],axis=0)[1],np.mean(data[16][3][1],axis=0)[1]]),\
                       np.mean([np.mean(data[0][4][1],axis=0)[1],np.mean(data[3][4][1],axis=0)[1],np.mean(data[10][4][1],axis=0)[1],\
                                    np.mean(data[13][4][1],axis=0)[1],np.mean(data[14][4][1],axis=0)[1],np.mean(data[15][4][1],axis=0)[1],np.mean(data[16][4][1],axis=0)[1]]),\
                       np.mean([np.mean(data[0][5][1],axis=0)[1],np.mean(data[3][5][1],axis=0)[1],np.mean(data[10][5][1],axis=0)[1],\
                                    np.mean(data[13][5][1],axis=0)[1],np.mean(data[14][5][1],axis=0)[1],np.mean(data[15][5][1],axis=0)[1],np.mean(data[16][5][1],axis=0)[1]])])
meanelon1600surface = np.array([np.mean([np.mean(data[2][0][1],axis=0)[1],np.mean(data[4][0][1],axis=0)[1],np.mean(data[6][0][1],axis=0)[1],\
                                 np.mean(data[8][0][1],axis=0)[1],np.mean(data[11][0][1],axis=0)[1]]),\
                       np.mean([np.mean(data[2][1][1],axis=0)[1],np.mean(data[4][1][1],axis=0)[1],np.mean(data[6][1][1],axis=0)[1],\
                                 np.mean(data[8][1][1],axis=0)[1],np.mean(data[11][1][1],axis=0)[1]]),\
                       np.mean([np.mean(data[2][2][1],axis=0)[1],np.mean(data[4][2][1],axis=0)[1],np.mean(data[6][2][1],axis=0)[1],\
                                 np.mean(data[8][2][1],axis=0)[1],np.mean(data[11][2][1],axis=0)[1]]),\
                       np.mean([np.mean(data[2][3][1],axis=0)[1],np.mean(data[4][3][1],axis=0)[1],np.mean(data[6][3][1],axis=0)[1],\
                                 np.mean(data[8][3][1],axis=0)[1],np.mean(data[11][3][1],axis=0)[1]]),\
                       np.mean([np.mean(data[2][4][1],axis=0)[1],np.mean(data[4][4][1],axis=0)[1],np.mean(data[6][4][1],axis=0)[1],\
                                 np.mean(data[8][4][1],axis=0)[1],np.mean(data[11][4][1],axis=0)[1]]),\
                       np.mean([np.mean(data[2][5][1],axis=0)[1],np.mean(data[4][5][1],axis=0)[1],np.mean(data[6][5][1],axis=0)[1],\
                                 np.mean(data[8][5][1],axis=0)[1],np.mean(data[11][5][1],axis=0)[1]])])
meanelon4000surface = np.array([np.mean([np.mean(data[5][0][1],axis=0)[1],np.mean(data[9][0][1],axis=0)[1],np.mean(data[12][0][1],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][1],axis=0)[1],np.mean(data[9][1][1],axis=0)[1],np.mean(data[12][1][1],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][1],axis=0)[1],np.mean(data[9][2][1],axis=0)[1],np.mean(data[12][2][1],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][1],axis=0)[1],np.mean(data[9][3][1],axis=0)[1],np.mean(data[12][3][1],axis=0)[1]])])

stdelon800surface = np.array([np.std([np.mean(data[0][0][1],axis=0)[1],np.mean(data[3][0][1],axis=0)[1],np.mean(data[10][0][1],axis=0)[1],\
                                    np.mean(data[13][0][1],axis=0)[1],np.mean(data[14][0][1],axis=0)[1],np.mean(data[15][0][1],axis=0)[1],np.mean(data[16][0][1],axis=0)[1]]),\
                       np.std([np.mean(data[0][1][1],axis=0)[1],np.mean(data[3][1][1],axis=0)[1],np.mean(data[10][1][1],axis=0)[1],\
                                    np.mean(data[13][1][1],axis=0)[1],np.mean(data[14][1][1],axis=0)[1],np.mean(data[15][1][1],axis=0)[1],np.mean(data[16][1][1],axis=0)[1]]),\
                       np.std([np.mean(data[0][2][1],axis=0)[1],np.mean(data[3][2][1],axis=0)[1],np.mean(data[10][2][1],axis=0)[1],\
                                    np.mean(data[13][2][1],axis=0)[1],np.mean(data[14][2][1],axis=0)[1],np.mean(data[15][2][1],axis=0)[1],np.mean(data[16][2][1],axis=0)[1]]),\
                       np.std([np.mean(data[0][3][1],axis=0)[1],np.mean(data[3][3][1],axis=0)[1],np.mean(data[10][3][1],axis=0)[1],\
                                    np.mean(data[13][3][1],axis=0)[1],np.mean(data[14][3][1],axis=0)[1],np.mean(data[15][3][1],axis=0)[1],np.mean(data[16][3][1],axis=0)[1]]),\
                       np.std([np.mean(data[0][4][1],axis=0)[1],np.mean(data[3][4][1],axis=0)[1],np.mean(data[10][4][1],axis=0)[1],\
                                    np.mean(data[13][4][1],axis=0)[1],np.mean(data[14][4][1],axis=0)[1],np.mean(data[15][4][1],axis=0)[1],np.mean(data[16][4][1],axis=0)[1]]),\
                       np.std([np.mean(data[0][5][1],axis=0)[1],np.mean(data[3][5][1],axis=0)[1],np.mean(data[10][5][1],axis=0)[1],\
                                    np.mean(data[13][5][1],axis=0)[1],np.mean(data[14][5][1],axis=0)[1],np.mean(data[15][5][1],axis=0)[1],np.mean(data[16][5][1],axis=0)[1]])])
stdelon1600surface = np.array([np.std([np.mean(data[2][0][1],axis=0)[1],np.mean(data[4][0][1],axis=0)[1],np.mean(data[6][0][1],axis=0)[1],\
                                 np.mean(data[8][0][1],axis=0)[1],np.mean(data[11][0][1],axis=0)[1]]),\
                       np.std([np.mean(data[2][1][1],axis=0)[1],np.mean(data[4][1][1],axis=0)[1],np.mean(data[6][1][1],axis=0)[1],\
                                 np.mean(data[8][1][1],axis=0)[1],np.mean(data[11][1][1],axis=0)[1]]),\
                       np.std([np.mean(data[2][2][1],axis=0)[1],np.mean(data[4][2][1],axis=0)[1],np.mean(data[6][2][1],axis=0)[1],\
                                 np.mean(data[8][2][1],axis=0)[1],np.mean(data[11][2][1],axis=0)[1]]),\
                       np.std([np.mean(data[2][3][1],axis=0)[1],np.mean(data[4][3][1],axis=0)[1],np.mean(data[6][3][1],axis=0)[1],\
                                 np.mean(data[8][3][1],axis=0)[1],np.mean(data[11][3][1],axis=0)[1]]),\
                       np.std([np.mean(data[2][4][1],axis=0)[1],np.mean(data[4][4][1],axis=0)[1],np.mean(data[6][4][1],axis=0)[1],\
                                 np.mean(data[8][4][1],axis=0)[1],np.mean(data[11][4][1],axis=0)[1]]),\
                       np.std([np.mean(data[2][5][1],axis=0)[1],np.mean(data[4][5][1],axis=0)[1],np.mean(data[6][5][1],axis=0)[1],\
                                 np.mean(data[8][5][1],axis=0)[1],np.mean(data[11][5][1],axis=0)[1]])])
stdelon4000surface = np.array([np.std([np.mean(data[5][0][1],axis=0)[1],np.mean(data[9][0][1],axis=0)[1],np.mean(data[12][0][1],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][1],axis=0)[1],np.mean(data[9][1][1],axis=0)[1],np.mean(data[12][1][1],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][1],axis=0)[1],np.mean(data[9][2][1],axis=0)[1],np.mean(data[12][2][1],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][1],axis=0)[1],np.mean(data[9][3][1],axis=0)[1],np.mean(data[12][3][1],axis=0)[1]])])


## Average shear rate
meanshear800face = np.array([np.mean([np.mean(data[0][0][4],axis=0)[2],np.mean(data[3][0][4],axis=0)[2],np.mean(data[10][0][4],axis=0)[2],\
                                    np.mean(data[13][0][4],axis=0)[2],np.mean(data[14][0][4],axis=0)[2],np.mean(data[15][0][4],axis=0)[2],np.mean(data[16][0][4],axis=0)[2]]),\
                       np.mean([np.mean(data[0][1][4],axis=0)[2],np.mean(data[3][1][4],axis=0)[2],np.mean(data[10][1][4],axis=0)[2],\
                                    np.mean(data[13][1][4],axis=0)[2],np.mean(data[14][1][4],axis=0)[2],np.mean(data[15][1][4],axis=0)[2],np.mean(data[16][1][4],axis=0)[2]]),\
                       np.mean([np.mean(data[0][2][4],axis=0)[2],np.mean(data[3][2][4],axis=0)[2],np.mean(data[10][2][4],axis=0)[2],\
                                    np.mean(data[13][2][4],axis=0)[2],np.mean(data[14][2][4],axis=0)[2],np.mean(data[15][2][4],axis=0)[2],np.mean(data[16][2][4],axis=0)[2]]),\
                       np.mean([np.mean(data[0][3][4],axis=0)[2],np.mean(data[3][3][4],axis=0)[2],np.mean(data[10][3][4],axis=0)[2],\
                                    np.mean(data[13][3][4],axis=0)[2],np.mean(data[14][3][4],axis=0)[2],np.mean(data[15][3][4],axis=0)[2],np.mean(data[16][3][4],axis=0)[2]]),\
                       np.mean([np.mean(data[0][4][4],axis=0)[2],np.mean(data[3][4][4],axis=0)[2],np.mean(data[10][4][4],axis=0)[2],\
                                    np.mean(data[13][4][4],axis=0)[2],np.mean(data[14][4][4],axis=0)[2],np.mean(data[15][4][4],axis=0)[2],np.mean(data[16][4][4],axis=0)[2]]),\
                       np.mean([np.mean(data[0][5][4],axis=0)[2],np.mean(data[3][5][4],axis=0)[2],np.mean(data[10][5][4],axis=0)[2],\
                                    np.mean(data[13][5][4],axis=0)[2],np.mean(data[14][5][4],axis=0)[2],np.mean(data[15][5][4],axis=0)[2],np.mean(data[16][5][4],axis=0)[2]])])
meanshear1600face = np.array([np.mean([np.mean(data[2][0][4],axis=0)[2],np.mean(data[4][0][4],axis=0)[2],np.mean(data[6][0][4],axis=0)[2],\
                                 np.mean(data[8][0][4],axis=0)[2],np.mean(data[11][0][4],axis=0)[2]]),\
                       np.mean([np.mean(data[2][1][4],axis=0)[2],np.mean(data[4][1][4],axis=0)[2],np.mean(data[6][1][4],axis=0)[2],\
                                 np.mean(data[8][1][4],axis=0)[2],np.mean(data[11][1][4],axis=0)[2]]),\
                       np.mean([np.mean(data[2][2][4],axis=0)[2],np.mean(data[4][2][4],axis=0)[2],np.mean(data[6][2][4],axis=0)[2],\
                                 np.mean(data[8][2][4],axis=0)[2],np.mean(data[11][2][4],axis=0)[2]]),\
                       np.mean([np.mean(data[2][3][4],axis=0)[2],np.mean(data[4][3][4],axis=0)[2],np.mean(data[6][3][4],axis=0)[2],\
                                 np.mean(data[8][3][4],axis=0)[2],np.mean(data[11][3][4],axis=0)[2]]),\
                       np.mean([np.mean(data[2][4][4],axis=0)[2],np.mean(data[4][4][4],axis=0)[2],np.mean(data[6][4][4],axis=0)[2],\
                                 np.mean(data[8][4][4],axis=0)[2],np.mean(data[11][4][4],axis=0)[2]]),\
                       np.mean([np.mean(data[2][5][4],axis=0)[2],np.mean(data[4][5][4],axis=0)[2],np.mean(data[6][5][4],axis=0)[2],\
                                 np.mean(data[8][5][4],axis=0)[2],np.mean(data[11][5][4],axis=0)[2]])])
meanshear4000face = np.array([np.mean([np.mean(data[5][0][4],axis=0)[2],np.mean(data[9][0][4],axis=0)[2],np.mean(data[12][0][4],axis=0)[2]]),\
                       np.mean([np.mean(data[5][1][4],axis=0)[2],np.mean(data[9][1][4],axis=0)[2],np.mean(data[12][1][4],axis=0)[2]]),\
                       np.mean([np.mean(data[5][2][4],axis=0)[2],np.mean(data[9][2][4],axis=0)[2],np.mean(data[12][2][4],axis=0)[2]]),\
                       np.mean([np.mean(data[5][3][4],axis=0)[2],np.mean(data[9][3][4],axis=0)[2],np.mean(data[12][3][4],axis=0)[2]])])

stdshear800face = np.array([np.std([np.mean(data[0][0][4],axis=0)[2],np.mean(data[3][0][4],axis=0)[2],np.mean(data[10][0][4],axis=0)[2],\
                                    np.mean(data[13][0][4],axis=0)[2],np.mean(data[14][0][4],axis=0)[2],np.mean(data[15][0][4],axis=0)[2],np.mean(data[16][0][4],axis=0)[2]]),\
                       np.std([np.mean(data[0][1][4],axis=0)[2],np.mean(data[3][1][4],axis=0)[2],np.mean(data[10][1][4],axis=0)[2],\
                                    np.mean(data[13][1][4],axis=0)[2],np.mean(data[14][1][4],axis=0)[2],np.mean(data[15][1][4],axis=0)[2],np.mean(data[16][1][4],axis=0)[2]]),\
                       np.std([np.mean(data[0][2][4],axis=0)[2],np.mean(data[3][2][4],axis=0)[2],np.mean(data[10][2][4],axis=0)[2],\
                                    np.mean(data[13][2][4],axis=0)[2],np.mean(data[14][2][4],axis=0)[2],np.mean(data[15][2][4],axis=0)[2],np.mean(data[16][2][4],axis=0)[2]]),\
                       np.std([np.mean(data[0][3][4],axis=0)[2],np.mean(data[3][3][4],axis=0)[2],np.mean(data[10][3][4],axis=0)[2],\
                                    np.mean(data[13][3][4],axis=0)[2],np.mean(data[14][3][4],axis=0)[2],np.mean(data[15][3][4],axis=0)[2],np.mean(data[16][3][4],axis=0)[2]]),\
                       np.std([np.mean(data[0][4][4],axis=0)[2],np.mean(data[3][4][4],axis=0)[2],np.mean(data[10][4][4],axis=0)[2],\
                                    np.mean(data[13][4][4],axis=0)[2],np.mean(data[14][4][4],axis=0)[2],np.mean(data[15][4][4],axis=0)[2],np.mean(data[16][4][4],axis=0)[2]]),\
                       np.std([np.mean(data[0][5][4],axis=0)[2],np.mean(data[3][5][4],axis=0)[2],np.mean(data[10][5][4],axis=0)[2],\
                                    np.mean(data[13][5][4],axis=0)[2],np.mean(data[14][5][4],axis=0)[2],np.mean(data[15][5][4],axis=0)[2],np.mean(data[16][5][4],axis=0)[2]])])
stdshear1600face = np.array([np.std([np.mean(data[2][0][4],axis=0)[2],np.mean(data[4][0][4],axis=0)[2],np.mean(data[6][0][4],axis=0)[2],\
                                 np.mean(data[8][0][4],axis=0)[2],np.mean(data[11][0][4],axis=0)[2]]),\
                       np.std([np.mean(data[2][1][4],axis=0)[2],np.mean(data[4][1][4],axis=0)[2],np.mean(data[6][1][4],axis=0)[2],\
                                 np.mean(data[8][1][4],axis=0)[2],np.mean(data[11][1][4],axis=0)[2]]),\
                       np.std([np.mean(data[2][2][4],axis=0)[2],np.mean(data[4][2][4],axis=0)[2],np.mean(data[6][2][4],axis=0)[2],\
                                 np.mean(data[8][2][4],axis=0)[2],np.mean(data[11][2][4],axis=0)[2]]),\
                       np.std([np.mean(data[2][3][4],axis=0)[2],np.mean(data[4][3][4],axis=0)[2],np.mean(data[6][3][4],axis=0)[2],\
                                 np.mean(data[8][3][4],axis=0)[2],np.mean(data[11][3][4],axis=0)[2]]),\
                       np.std([np.mean(data[2][4][4],axis=0)[2],np.mean(data[4][4][4],axis=0)[2],np.mean(data[6][4][4],axis=0)[2],\
                                 np.mean(data[8][4][4],axis=0)[2],np.mean(data[11][4][4],axis=0)[2]]),\
                       np.std([np.mean(data[2][5][4],axis=0)[2],np.mean(data[4][5][4],axis=0)[2],np.mean(data[6][5][4],axis=0)[2],\
                                 np.mean(data[8][5][4],axis=0)[2],np.mean(data[11][5][4],axis=0)[2]])])
stdshear4000face = np.array([np.std([np.mean(data[5][0][4],axis=0)[2],np.mean(data[9][0][4],axis=0)[2],np.mean(data[12][0][4],axis=0)[2]]),\
                       np.std([np.mean(data[5][1][4],axis=0)[2],np.mean(data[9][1][4],axis=0)[2],np.mean(data[12][1][4],axis=0)[2]]),\
                       np.std([np.mean(data[5][2][4],axis=0)[2],np.mean(data[9][2][4],axis=0)[2],np.mean(data[12][2][4],axis=0)[2]]),\
                       np.std([np.mean(data[5][3][4],axis=0)[2],np.mean(data[9][3][4],axis=0)[2],np.mean(data[12][3][4],axis=0)[2]])])

meanshear800back = np.array([np.mean([np.mean(data[0][0][5],axis=0)[2],np.mean(data[3][0][5],axis=0)[2],np.mean(data[10][0][5],axis=0)[2],\
                                    np.mean(data[13][0][5],axis=0)[2],np.mean(data[14][0][5],axis=0)[2],np.mean(data[15][0][5],axis=0)[2],np.mean(data[16][0][5],axis=0)[2]]),\
                       np.mean([np.mean(data[0][1][5],axis=0)[2],np.mean(data[3][1][5],axis=0)[2],np.mean(data[10][1][5],axis=0)[2],\
                                    np.mean(data[13][1][5],axis=0)[2],np.mean(data[14][1][5],axis=0)[2],np.mean(data[15][1][5],axis=0)[2],np.mean(data[16][1][5],axis=0)[2]]),\
                       np.mean([np.mean(data[0][2][5],axis=0)[2],np.mean(data[3][2][5],axis=0)[2],np.mean(data[10][2][5],axis=0)[2],\
                                    np.mean(data[13][2][5],axis=0)[2],np.mean(data[14][2][5],axis=0)[2],np.mean(data[15][2][5],axis=0)[2],np.mean(data[16][2][5],axis=0)[2]]),\
                       np.mean([np.mean(data[0][3][5],axis=0)[2],np.mean(data[3][3][5],axis=0)[2],np.mean(data[10][3][5],axis=0)[2],\
                                    np.mean(data[13][3][5],axis=0)[2],np.mean(data[14][3][5],axis=0)[2],np.mean(data[15][3][5],axis=0)[2],np.mean(data[16][3][5],axis=0)[2]]),\
                       np.mean([np.mean(data[0][4][5],axis=0)[2],np.mean(data[3][4][5],axis=0)[2],np.mean(data[10][4][5],axis=0)[2],\
                                    np.mean(data[13][4][5],axis=0)[2],np.mean(data[14][4][5],axis=0)[2],np.mean(data[15][4][5],axis=0)[2],np.mean(data[16][4][5],axis=0)[2]]),\
                       np.mean([np.mean(data[0][5][5],axis=0)[2],np.mean(data[3][5][5],axis=0)[2],np.mean(data[10][5][5],axis=0)[2],\
                                    np.mean(data[13][5][5],axis=0)[2],np.mean(data[14][5][5],axis=0)[2],np.mean(data[15][5][5],axis=0)[2],np.mean(data[16][5][5],axis=0)[2]])])
meanshear1600back = np.array([np.mean([np.mean(data[2][0][5],axis=0)[2],np.mean(data[4][0][5],axis=0)[2],np.mean(data[6][0][5],axis=0)[2],\
                                 np.mean(data[8][0][5],axis=0)[2],np.mean(data[11][0][5],axis=0)[2]]),\
                       np.mean([np.mean(data[2][1][5],axis=0)[2],np.mean(data[4][1][5],axis=0)[2],np.mean(data[6][1][5],axis=0)[2],\
                                 np.mean(data[8][1][5],axis=0)[2],np.mean(data[11][1][5],axis=0)[2]]),\
                       np.mean([np.mean(data[2][2][5],axis=0)[2],np.mean(data[4][2][5],axis=0)[2],np.mean(data[6][2][5],axis=0)[2],\
                                 np.mean(data[8][2][5],axis=0)[2],np.mean(data[11][2][5],axis=0)[2]]),\
                       np.mean([np.mean(data[2][3][5],axis=0)[2],np.mean(data[4][3][5],axis=0)[2],np.mean(data[6][3][5],axis=0)[2],\
                                 np.mean(data[8][3][5],axis=0)[2],np.mean(data[11][3][5],axis=0)[2]]),\
                       np.mean([np.mean(data[2][4][5],axis=0)[2],np.mean(data[4][4][5],axis=0)[2],np.mean(data[6][4][5],axis=0)[2],\
                                 np.mean(data[8][4][5],axis=0)[2],np.mean(data[11][4][5],axis=0)[2]]),\
                       np.mean([np.mean(data[2][5][5],axis=0)[2],np.mean(data[4][5][5],axis=0)[2],np.mean(data[6][5][5],axis=0)[2],\
                                 np.mean(data[8][5][5],axis=0)[2],np.mean(data[11][5][5],axis=0)[2]])])
meanshear4000back = np.array([np.mean([np.mean(data[5][0][5],axis=0)[2],np.mean(data[9][0][5],axis=0)[2],np.mean(data[12][0][5],axis=0)[2]]),\
                       np.mean([np.mean(data[5][1][5],axis=0)[2],np.mean(data[9][1][5],axis=0)[2],np.mean(data[12][1][5],axis=0)[2]]),\
                       np.mean([np.mean(data[5][2][5],axis=0)[2],np.mean(data[9][2][5],axis=0)[2],np.mean(data[12][2][5],axis=0)[2]]),\
                       np.mean([np.mean(data[5][3][5],axis=0)[2],np.mean(data[9][3][5],axis=0)[2],np.mean(data[12][3][5],axis=0)[2]])])

stdshear800back = np.array([np.std([np.mean(data[0][0][5],axis=0)[2],np.mean(data[3][0][5],axis=0)[2],np.mean(data[10][0][5],axis=0)[2],\
                                    np.mean(data[13][0][5],axis=0)[2],np.mean(data[14][0][5],axis=0)[2],np.mean(data[15][0][5],axis=0)[2],np.mean(data[16][0][5],axis=0)[2]]),\
                       np.std([np.mean(data[0][1][5],axis=0)[2],np.mean(data[3][1][5],axis=0)[2],np.mean(data[10][1][5],axis=0)[2],\
                                    np.mean(data[13][1][5],axis=0)[2],np.mean(data[14][1][5],axis=0)[2],np.mean(data[15][1][5],axis=0)[2],np.mean(data[16][1][5],axis=0)[2]]),\
                       np.std([np.mean(data[0][2][5],axis=0)[2],np.mean(data[3][2][5],axis=0)[2],np.mean(data[10][2][5],axis=0)[2],\
                                    np.mean(data[13][2][5],axis=0)[2],np.mean(data[14][2][5],axis=0)[2],np.mean(data[15][2][5],axis=0)[2],np.mean(data[16][2][5],axis=0)[2]]),\
                       np.std([np.mean(data[0][3][5],axis=0)[2],np.mean(data[3][3][5],axis=0)[2],np.mean(data[10][3][5],axis=0)[2],\
                                    np.mean(data[13][3][5],axis=0)[2],np.mean(data[14][3][5],axis=0)[2],np.mean(data[15][3][5],axis=0)[2],np.mean(data[16][3][5],axis=0)[2]]),\
                       np.std([np.mean(data[0][4][5],axis=0)[2],np.mean(data[3][4][5],axis=0)[2],np.mean(data[10][4][5],axis=0)[2],\
                                    np.mean(data[13][4][5],axis=0)[2],np.mean(data[14][4][5],axis=0)[2],np.mean(data[15][4][5],axis=0)[2],np.mean(data[16][4][5],axis=0)[2]]),\
                       np.std([np.mean(data[0][5][5],axis=0)[2],np.mean(data[3][5][5],axis=0)[2],np.mean(data[10][5][5],axis=0)[2],\
                                    np.mean(data[13][5][5],axis=0)[2],np.mean(data[14][5][5],axis=0)[2],np.mean(data[15][5][5],axis=0)[2],np.mean(data[16][5][5],axis=0)[2]])])
stdshear1600back = np.array([np.std([np.mean(data[2][0][5],axis=0)[2],np.mean(data[4][0][5],axis=0)[2],np.mean(data[6][0][5],axis=0)[2],\
                                 np.mean(data[8][0][5],axis=0)[2],np.mean(data[11][0][5],axis=0)[2]]),\
                       np.std([np.mean(data[2][1][5],axis=0)[2],np.mean(data[4][1][5],axis=0)[2],np.mean(data[6][1][5],axis=0)[2],\
                                 np.mean(data[8][1][5],axis=0)[2],np.mean(data[11][1][5],axis=0)[2]]),\
                       np.std([np.mean(data[2][2][5],axis=0)[2],np.mean(data[4][2][5],axis=0)[2],np.mean(data[6][2][5],axis=0)[2],\
                                 np.mean(data[8][2][5],axis=0)[2],np.mean(data[11][2][5],axis=0)[2]]),\
                       np.std([np.mean(data[2][3][5],axis=0)[2],np.mean(data[4][3][5],axis=0)[2],np.mean(data[6][3][5],axis=0)[2],\
                                 np.mean(data[8][3][5],axis=0)[2],np.mean(data[11][3][5],axis=0)[2]]),\
                       np.std([np.mean(data[2][4][5],axis=0)[2],np.mean(data[4][4][5],axis=0)[2],np.mean(data[6][4][5],axis=0)[2],\
                                 np.mean(data[8][4][5],axis=0)[2],np.mean(data[11][4][5],axis=0)[2]]),\
                       np.std([np.mean(data[2][5][5],axis=0)[2],np.mean(data[4][5][5],axis=0)[2],np.mean(data[6][5][5],axis=0)[2],\
                                 np.mean(data[8][5][5],axis=0)[2],np.mean(data[11][5][5],axis=0)[2]])])
stdshear4000back = np.array([np.std([np.mean(data[5][0][5],axis=0)[2],np.mean(data[9][0][5],axis=0)[2],np.mean(data[12][0][5],axis=0)[2]]),\
                       np.std([np.mean(data[5][1][5],axis=0)[2],np.mean(data[9][1][5],axis=0)[2],np.mean(data[12][1][5],axis=0)[2]]),\
                       np.std([np.mean(data[5][2][5],axis=0)[2],np.mean(data[9][2][5],axis=0)[2],np.mean(data[12][2][5],axis=0)[2]]),\
                       np.std([np.mean(data[5][3][5],axis=0)[2],np.mean(data[9][3][5],axis=0)[2],np.mean(data[12][3][5],axis=0)[2]])])

meanshear800topp = np.array([np.mean([np.mean(data[0][0][2],axis=0)[2],np.mean(data[3][0][2],axis=0)[2],np.mean(data[10][0][2],axis=0)[2],\
                                    np.mean(data[13][0][2],axis=0)[2],np.mean(data[14][0][2],axis=0)[2],np.mean(data[15][0][2],axis=0)[2],np.mean(data[16][0][2],axis=0)[2]]),\
                       np.mean([np.mean(data[0][1][2],axis=0)[2],np.mean(data[3][1][2],axis=0)[2],np.mean(data[10][1][2],axis=0)[2],\
                                    np.mean(data[13][1][2],axis=0)[2],np.mean(data[14][1][2],axis=0)[2],np.mean(data[15][1][2],axis=0)[2],np.mean(data[16][1][2],axis=0)[2]]),\
                       np.mean([np.mean(data[0][2][2],axis=0)[2],np.mean(data[3][2][2],axis=0)[2],np.mean(data[10][2][2],axis=0)[2],\
                                    np.mean(data[13][2][2],axis=0)[2],np.mean(data[14][2][2],axis=0)[2],np.mean(data[15][2][2],axis=0)[2],np.mean(data[16][2][2],axis=0)[2]]),\
                       np.mean([np.mean(data[0][3][2],axis=0)[2],np.mean(data[3][3][2],axis=0)[2],np.mean(data[10][3][2],axis=0)[2],\
                                    np.mean(data[13][3][2],axis=0)[2],np.mean(data[14][3][2],axis=0)[2],np.mean(data[15][3][2],axis=0)[2],np.mean(data[16][3][2],axis=0)[2]]),\
                       np.mean([np.mean(data[0][4][2],axis=0)[2],np.mean(data[3][4][2],axis=0)[2],np.mean(data[10][4][2],axis=0)[2],\
                                    np.mean(data[13][4][2],axis=0)[2],np.mean(data[14][4][2],axis=0)[2],np.mean(data[15][4][2],axis=0)[2],np.mean(data[16][4][2],axis=0)[2]]),\
                       np.mean([np.mean(data[0][5][2],axis=0)[2],np.mean(data[3][5][2],axis=0)[2],np.mean(data[10][5][2],axis=0)[2],\
                                    np.mean(data[13][5][2],axis=0)[2],np.mean(data[14][5][2],axis=0)[2],np.mean(data[15][5][2],axis=0)[2],np.mean(data[16][5][2],axis=0)[2]])])
meanshear1600topp = np.array([np.mean([np.mean(data[2][0][2],axis=0)[2],np.mean(data[4][0][2],axis=0)[2],np.mean(data[6][0][2],axis=0)[2],\
                                 np.mean(data[8][0][2],axis=0)[2],np.mean(data[11][0][2],axis=0)[2]]),\
                       np.mean([np.mean(data[2][1][2],axis=0)[2],np.mean(data[4][1][2],axis=0)[2],np.mean(data[6][1][2],axis=0)[2],\
                                 np.mean(data[8][1][2],axis=0)[2],np.mean(data[11][1][2],axis=0)[2]]),\
                       np.mean([np.mean(data[2][2][2],axis=0)[2],np.mean(data[4][2][2],axis=0)[2],np.mean(data[6][2][2],axis=0)[2],\
                                 np.mean(data[8][2][2],axis=0)[2],np.mean(data[11][2][2],axis=0)[2]]),\
                       np.mean([np.mean(data[2][3][2],axis=0)[2],np.mean(data[4][3][2],axis=0)[2],np.mean(data[6][3][2],axis=0)[2],\
                                 np.mean(data[8][3][2],axis=0)[2],np.mean(data[11][3][2],axis=0)[2]]),\
                       np.mean([np.mean(data[2][4][2],axis=0)[2],np.mean(data[4][4][2],axis=0)[2],np.mean(data[6][4][2],axis=0)[2],\
                                 np.mean(data[8][4][2],axis=0)[2],np.mean(data[11][4][2],axis=0)[2]]),\
                       np.mean([np.mean(data[2][5][2],axis=0)[2],np.mean(data[4][5][2],axis=0)[2],np.mean(data[6][5][2],axis=0)[2],\
                                 np.mean(data[8][5][2],axis=0)[2],np.mean(data[11][5][2],axis=0)[2]])])
meanshear4000topp = np.array([np.mean([np.mean(data[5][0][2],axis=0)[2],np.mean(data[9][0][2],axis=0)[2],np.mean(data[12][0][2],axis=0)[2]]),\
                       np.mean([np.mean(data[5][1][2],axis=0)[2],np.mean(data[9][1][2],axis=0)[2],np.mean(data[12][1][2],axis=0)[2]]),\
                       np.mean([np.mean(data[5][2][2],axis=0)[2],np.mean(data[9][2][2],axis=0)[2],np.mean(data[12][2][2],axis=0)[2]]),\
                       np.mean([np.mean(data[5][3][2],axis=0)[2],np.mean(data[9][3][2],axis=0)[2],np.mean(data[12][3][2],axis=0)[2]])])

stdshear800topp = np.array([np.std([np.mean(data[0][0][2],axis=0)[2],np.mean(data[3][0][2],axis=0)[2],np.mean(data[10][0][2],axis=0)[2],\
                                    np.mean(data[13][0][2],axis=0)[2],np.mean(data[14][0][2],axis=0)[2],np.mean(data[15][0][2],axis=0)[2],np.mean(data[16][0][2],axis=0)[2]]),\
                       np.std([np.mean(data[0][1][2],axis=0)[2],np.mean(data[3][1][2],axis=0)[2],np.mean(data[10][1][2],axis=0)[2],\
                                    np.mean(data[13][1][2],axis=0)[2],np.mean(data[14][1][2],axis=0)[2],np.mean(data[15][1][2],axis=0)[2],np.mean(data[16][1][2],axis=0)[2]]),\
                       np.std([np.mean(data[0][2][2],axis=0)[2],np.mean(data[3][2][2],axis=0)[2],np.mean(data[10][2][2],axis=0)[2],\
                                    np.mean(data[13][2][2],axis=0)[2],np.mean(data[14][2][2],axis=0)[2],np.mean(data[15][2][2],axis=0)[2],np.mean(data[16][2][2],axis=0)[2]]),\
                       np.std([np.mean(data[0][3][2],axis=0)[2],np.mean(data[3][3][2],axis=0)[2],np.mean(data[10][3][2],axis=0)[2],\
                                    np.mean(data[13][3][2],axis=0)[2],np.mean(data[14][3][2],axis=0)[2],np.mean(data[15][3][2],axis=0)[2],np.mean(data[16][3][2],axis=0)[2]]),\
                       np.std([np.mean(data[0][4][2],axis=0)[2],np.mean(data[3][4][2],axis=0)[2],np.mean(data[10][4][2],axis=0)[2],\
                                    np.mean(data[13][4][2],axis=0)[2],np.mean(data[14][4][2],axis=0)[2],np.mean(data[15][4][2],axis=0)[2],np.mean(data[16][4][2],axis=0)[2]]),\
                       np.std([np.mean(data[0][5][2],axis=0)[2],np.mean(data[3][5][2],axis=0)[2],np.mean(data[10][5][2],axis=0)[2],\
                                    np.mean(data[13][5][2],axis=0)[2],np.mean(data[14][5][2],axis=0)[2],np.mean(data[15][5][2],axis=0)[2],np.mean(data[16][5][2],axis=0)[2]])])
stdshear1600topp = np.array([np.std([np.mean(data[2][0][2],axis=0)[2],np.mean(data[4][0][2],axis=0)[2],np.mean(data[6][0][2],axis=0)[2],\
                                 np.mean(data[8][0][2],axis=0)[2],np.mean(data[11][0][2],axis=0)[2]]),\
                       np.std([np.mean(data[2][1][2],axis=0)[2],np.mean(data[4][1][2],axis=0)[2],np.mean(data[6][1][2],axis=0)[2],\
                                 np.mean(data[8][1][2],axis=0)[2],np.mean(data[11][1][2],axis=0)[2]]),\
                       np.std([np.mean(data[2][2][2],axis=0)[2],np.mean(data[4][2][2],axis=0)[2],np.mean(data[6][2][2],axis=0)[2],\
                                 np.mean(data[8][2][2],axis=0)[2],np.mean(data[11][2][2],axis=0)[2]]),\
                       np.std([np.mean(data[2][3][2],axis=0)[2],np.mean(data[4][3][2],axis=0)[2],np.mean(data[6][3][2],axis=0)[2],\
                                 np.mean(data[8][3][2],axis=0)[2],np.mean(data[11][3][2],axis=0)[2]]),\
                       np.std([np.mean(data[2][4][2],axis=0)[2],np.mean(data[4][4][2],axis=0)[2],np.mean(data[6][4][2],axis=0)[2],\
                                 np.mean(data[8][4][2],axis=0)[2],np.mean(data[11][4][2],axis=0)[2]]),\
                       np.std([np.mean(data[2][5][2],axis=0)[2],np.mean(data[4][5][2],axis=0)[2],np.mean(data[6][5][2],axis=0)[2],\
                                 np.mean(data[8][5][2],axis=0)[2],np.mean(data[11][5][2],axis=0)[2]])])
stdshear4000topp = np.array([np.std([np.mean(data[5][0][2],axis=0)[2],np.mean(data[9][0][2],axis=0)[2],np.mean(data[12][0][2],axis=0)[2]]),\
                       np.std([np.mean(data[5][1][2],axis=0)[2],np.mean(data[9][1][2],axis=0)[2],np.mean(data[12][1][2],axis=0)[2]]),\
                       np.std([np.mean(data[5][2][2],axis=0)[2],np.mean(data[9][2][2],axis=0)[2],np.mean(data[12][2][2],axis=0)[2]]),\
                       np.std([np.mean(data[5][3][2],axis=0)[2],np.mean(data[9][3][2],axis=0)[2],np.mean(data[12][3][2],axis=0)[2]])])

meanshear800topf = np.array([np.mean([np.mean(data[0][0][3],axis=0)[2],np.mean(data[3][0][3],axis=0)[2],np.mean(data[10][0][3],axis=0)[2],\
                                    np.mean(data[13][0][3],axis=0)[2],np.mean(data[14][0][3],axis=0)[2],np.mean(data[15][0][3],axis=0)[2],np.mean(data[16][0][3],axis=0)[2]]),\
                       np.mean([np.mean(data[0][1][3],axis=0)[2],np.mean(data[3][1][3],axis=0)[2],np.mean(data[10][1][3],axis=0)[2],\
                                    np.mean(data[13][1][3],axis=0)[2],np.mean(data[14][1][3],axis=0)[2],np.mean(data[15][1][3],axis=0)[2],np.mean(data[16][1][3],axis=0)[2]]),\
                       np.mean([np.mean(data[0][2][3],axis=0)[2],np.mean(data[3][2][3],axis=0)[2],np.mean(data[10][2][3],axis=0)[2],\
                                    np.mean(data[13][2][3],axis=0)[2],np.mean(data[14][2][3],axis=0)[2],np.mean(data[15][2][3],axis=0)[2],np.mean(data[16][2][3],axis=0)[2]]),\
                       np.mean([np.mean(data[0][3][3],axis=0)[2],np.mean(data[3][3][3],axis=0)[2],np.mean(data[10][3][3],axis=0)[2],\
                                    np.mean(data[13][3][3],axis=0)[2],np.mean(data[14][3][3],axis=0)[2],np.mean(data[15][3][3],axis=0)[2],np.mean(data[16][3][3],axis=0)[2]]),\
                       np.mean([np.mean(data[0][4][3],axis=0)[2],np.mean(data[3][4][3],axis=0)[2],np.mean(data[10][4][3],axis=0)[2],\
                                    np.mean(data[13][4][3],axis=0)[2],np.mean(data[14][4][3],axis=0)[2],np.mean(data[15][4][3],axis=0)[2],np.mean(data[16][4][3],axis=0)[2]]),\
                       np.mean([np.mean(data[0][5][3],axis=0)[2],np.mean(data[3][5][3],axis=0)[2],np.mean(data[10][5][3],axis=0)[2],\
                                    np.mean(data[13][5][3],axis=0)[2],np.mean(data[14][5][3],axis=0)[2],np.mean(data[15][5][3],axis=0)[2],np.mean(data[16][5][3],axis=0)[2]])])
meanshear1600topf = np.array([np.mean([np.mean(data[2][0][3],axis=0)[2],np.mean(data[4][0][3],axis=0)[2],np.mean(data[6][0][3],axis=0)[2],\
                                 np.mean(data[8][0][3],axis=0)[2],np.mean(data[11][0][3],axis=0)[2]]),\
                       np.mean([np.mean(data[2][1][3],axis=0)[2],np.mean(data[4][1][3],axis=0)[2],np.mean(data[6][1][3],axis=0)[2],\
                                 np.mean(data[8][1][3],axis=0)[2],np.mean(data[11][1][3],axis=0)[2]]),\
                       np.mean([np.mean(data[2][2][3],axis=0)[2],np.mean(data[4][2][3],axis=0)[2],np.mean(data[6][2][3],axis=0)[2],\
                                 np.mean(data[8][2][3],axis=0)[2],np.mean(data[11][2][3],axis=0)[2]]),\
                       np.mean([np.mean(data[2][3][3],axis=0)[2],np.mean(data[4][3][3],axis=0)[2],np.mean(data[6][3][3],axis=0)[2],\
                                 np.mean(data[8][3][3],axis=0)[2],np.mean(data[11][3][3],axis=0)[2]]),\
                       np.mean([np.mean(data[2][4][3],axis=0)[2],np.mean(data[4][4][3],axis=0)[2],np.mean(data[6][4][3],axis=0)[2],\
                                 np.mean(data[8][4][3],axis=0)[2],np.mean(data[11][4][3],axis=0)[2]]),\
                       np.mean([np.mean(data[2][5][3],axis=0)[2],np.mean(data[4][5][3],axis=0)[2],np.mean(data[6][5][3],axis=0)[2],\
                                 np.mean(data[8][5][3],axis=0)[2],np.mean(data[11][5][3],axis=0)[2]])])
meanshear4000topf = np.array([np.mean([np.mean(data[5][0][3],axis=0)[2],np.mean(data[9][0][3],axis=0)[2],np.mean(data[12][0][3],axis=0)[2]]),\
                       np.mean([np.mean(data[5][1][3],axis=0)[2],np.mean(data[9][1][3],axis=0)[2],np.mean(data[12][1][3],axis=0)[2]]),\
                       np.mean([np.mean(data[5][2][3],axis=0)[2],np.mean(data[9][2][3],axis=0)[2],np.mean(data[12][2][3],axis=0)[2]]),\
                       np.mean([np.mean(data[5][3][3],axis=0)[2],np.mean(data[9][3][3],axis=0)[2],np.mean(data[12][3][3],axis=0)[2]])])

stdshear800topf = np.array([np.std([np.mean(data[0][0][3],axis=0)[2],np.mean(data[3][0][3],axis=0)[2],np.mean(data[10][0][3],axis=0)[2],\
                                    np.mean(data[13][0][3],axis=0)[2],np.mean(data[14][0][3],axis=0)[2],np.mean(data[15][0][3],axis=0)[2],np.mean(data[16][0][3],axis=0)[2]]),\
                       np.std([np.mean(data[0][1][3],axis=0)[2],np.mean(data[3][1][3],axis=0)[2],np.mean(data[10][1][3],axis=0)[2],\
                                    np.mean(data[13][1][3],axis=0)[2],np.mean(data[14][1][3],axis=0)[2],np.mean(data[15][1][3],axis=0)[2],np.mean(data[16][1][3],axis=0)[2]]),\
                       np.std([np.mean(data[0][2][3],axis=0)[2],np.mean(data[3][2][3],axis=0)[2],np.mean(data[10][2][3],axis=0)[2],\
                                    np.mean(data[13][2][3],axis=0)[2],np.mean(data[14][2][3],axis=0)[2],np.mean(data[15][2][3],axis=0)[2],np.mean(data[16][2][3],axis=0)[2]]),\
                       np.std([np.mean(data[0][3][3],axis=0)[2],np.mean(data[3][3][3],axis=0)[2],np.mean(data[10][3][3],axis=0)[2],\
                                    np.mean(data[13][3][3],axis=0)[2],np.mean(data[14][3][3],axis=0)[2],np.mean(data[15][3][3],axis=0)[2],np.mean(data[16][3][3],axis=0)[2]]),\
                       np.std([np.mean(data[0][4][3],axis=0)[2],np.mean(data[3][4][3],axis=0)[2],np.mean(data[10][4][3],axis=0)[2],\
                                    np.mean(data[13][4][3],axis=0)[2],np.mean(data[14][4][3],axis=0)[2],np.mean(data[15][4][3],axis=0)[2],np.mean(data[16][4][3],axis=0)[2]]),\
                       np.std([np.mean(data[0][5][3],axis=0)[2],np.mean(data[3][5][3],axis=0)[2],np.mean(data[10][5][3],axis=0)[2],\
                                    np.mean(data[13][5][3],axis=0)[2],np.mean(data[14][5][3],axis=0)[2],np.mean(data[15][5][3],axis=0)[2],np.mean(data[16][5][3],axis=0)[2]])])
stdshear1600topf = np.array([np.std([np.mean(data[2][0][3],axis=0)[2],np.mean(data[4][0][3],axis=0)[2],np.mean(data[6][0][3],axis=0)[2],\
                                 np.mean(data[8][0][3],axis=0)[2],np.mean(data[11][0][3],axis=0)[2]]),\
                       np.std([np.mean(data[2][1][3],axis=0)[2],np.mean(data[4][1][3],axis=0)[2],np.mean(data[6][1][3],axis=0)[2],\
                                 np.mean(data[8][1][3],axis=0)[2],np.mean(data[11][1][3],axis=0)[2]]),\
                       np.std([np.mean(data[2][2][3],axis=0)[2],np.mean(data[4][2][3],axis=0)[2],np.mean(data[6][2][3],axis=0)[2],\
                                 np.mean(data[8][2][3],axis=0)[2],np.mean(data[11][2][3],axis=0)[2]]),\
                       np.std([np.mean(data[2][3][3],axis=0)[2],np.mean(data[4][3][3],axis=0)[2],np.mean(data[6][3][3],axis=0)[2],\
                                 np.mean(data[8][3][3],axis=0)[2],np.mean(data[11][3][3],axis=0)[2]]),\
                       np.std([np.mean(data[2][4][3],axis=0)[2],np.mean(data[4][4][3],axis=0)[2],np.mean(data[6][4][3],axis=0)[2],\
                                 np.mean(data[8][4][3],axis=0)[2],np.mean(data[11][4][3],axis=0)[2]]),\
                       np.std([np.mean(data[2][5][3],axis=0)[2],np.mean(data[4][5][3],axis=0)[2],np.mean(data[6][5][3],axis=0)[2],\
                                 np.mean(data[8][5][3],axis=0)[2],np.mean(data[11][5][3],axis=0)[2]])])
stdshear4000topf = np.array([np.std([np.mean(data[5][0][3],axis=0)[2],np.mean(data[9][0][3],axis=0)[2],np.mean(data[12][0][3],axis=0)[2]]),\
                       np.std([np.mean(data[5][1][3],axis=0)[2],np.mean(data[9][1][3],axis=0)[2],np.mean(data[12][1][3],axis=0)[2]]),\
                       np.std([np.mean(data[5][2][3],axis=0)[2],np.mean(data[9][2][3],axis=0)[2],np.mean(data[12][2][3],axis=0)[2]]),\
                       np.std([np.mean(data[5][3][3],axis=0)[2],np.mean(data[9][3][3],axis=0)[2],np.mean(data[12][3][3],axis=0)[2]])])

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


## Average velocity
meanvel800face = np.array([np.mean([np.mean(data[0][0][4],axis=0)[4],np.mean(data[3][0][4],axis=0)[4],np.mean(data[10][0][4],axis=0)[4],\
                                    np.mean(data[13][0][4],axis=0)[4],np.mean(data[14][0][4],axis=0)[4],np.mean(data[15][0][4],axis=0)[4],np.mean(data[16][0][4],axis=0)[4]]),\
                       np.mean([np.mean(data[0][1][4],axis=0)[4],np.mean(data[3][1][4],axis=0)[4],np.mean(data[10][1][4],axis=0)[4],\
                                    np.mean(data[13][1][4],axis=0)[4],np.mean(data[14][1][4],axis=0)[4],np.mean(data[15][1][4],axis=0)[4],np.mean(data[16][1][4],axis=0)[4]]),\
                       np.mean([np.mean(data[0][2][4],axis=0)[4],np.mean(data[3][2][4],axis=0)[4],np.mean(data[10][2][4],axis=0)[4],\
                                    np.mean(data[13][2][4],axis=0)[4],np.mean(data[14][2][4],axis=0)[4],np.mean(data[15][2][4],axis=0)[4],np.mean(data[16][2][4],axis=0)[4]]),\
                       np.mean([np.mean(data[0][3][4],axis=0)[4],np.mean(data[3][3][4],axis=0)[4],np.mean(data[10][3][4],axis=0)[4],\
                                    np.mean(data[13][3][4],axis=0)[4],np.mean(data[14][3][4],axis=0)[4],np.mean(data[15][3][4],axis=0)[4],np.mean(data[16][3][4],axis=0)[4]]),\
                       np.mean([np.mean(data[0][4][4],axis=0)[4],np.mean(data[3][4][4],axis=0)[4],np.mean(data[10][4][4],axis=0)[4],\
                                    np.mean(data[13][4][4],axis=0)[4],np.mean(data[14][4][4],axis=0)[4],np.mean(data[15][4][4],axis=0)[4],np.mean(data[16][4][4],axis=0)[4]]),\
                       np.mean([np.mean(data[0][5][4],axis=0)[4],np.mean(data[3][5][4],axis=0)[4],np.mean(data[10][5][4],axis=0)[4],\
                                    np.mean(data[13][5][4],axis=0)[4],np.mean(data[14][5][4],axis=0)[4],np.mean(data[15][5][4],axis=0)[4],np.mean(data[16][5][4],axis=0)[4]])])
meanvel1600face = np.array([np.mean([np.mean(data[2][0][4],axis=0)[4],np.mean(data[4][0][4],axis=0)[4],np.mean(data[6][0][4],axis=0)[4],\
                                 np.mean(data[8][0][4],axis=0)[4],np.mean(data[11][0][4],axis=0)[4]]),\
                       np.mean([np.mean(data[2][1][4],axis=0)[4],np.mean(data[4][1][4],axis=0)[4],np.mean(data[6][1][4],axis=0)[4],\
                                 np.mean(data[8][1][4],axis=0)[4],np.mean(data[11][1][4],axis=0)[4]]),\
                       np.mean([np.mean(data[2][2][4],axis=0)[4],np.mean(data[4][2][4],axis=0)[4],np.mean(data[6][2][4],axis=0)[4],\
                                 np.mean(data[8][2][4],axis=0)[4],np.mean(data[11][2][4],axis=0)[4]]),\
                       np.mean([np.mean(data[2][3][4],axis=0)[4],np.mean(data[4][3][4],axis=0)[4],np.mean(data[6][3][4],axis=0)[4],\
                                 np.mean(data[8][3][4],axis=0)[4],np.mean(data[11][3][4],axis=0)[4]]),\
                       np.mean([np.mean(data[2][4][4],axis=0)[4],np.mean(data[4][4][4],axis=0)[4],np.mean(data[6][4][4],axis=0)[4],\
                                 np.mean(data[8][4][4],axis=0)[4],np.mean(data[11][4][4],axis=0)[4]]),\
                       np.mean([np.mean(data[2][5][4],axis=0)[4],np.mean(data[4][5][4],axis=0)[4],np.mean(data[6][5][4],axis=0)[4],\
                                 np.mean(data[8][5][4],axis=0)[4],np.mean(data[11][5][4],axis=0)[4]])])
meanvel4000face = np.array([np.mean([np.mean(data[5][0][4],axis=0)[4],np.mean(data[9][0][4],axis=0)[4],np.mean(data[12][0][4],axis=0)[4]]),\
                       np.mean([np.mean(data[5][1][4],axis=0)[4],np.mean(data[9][1][4],axis=0)[4],np.mean(data[12][1][4],axis=0)[4]]),\
                       np.mean([np.mean(data[5][2][4],axis=0)[4],np.mean(data[9][2][4],axis=0)[4],np.mean(data[12][2][4],axis=0)[4]]),\
                       np.mean([np.mean(data[5][3][4],axis=0)[4],np.mean(data[9][3][4],axis=0)[4],np.mean(data[12][3][4],axis=0)[4]])])

stdvel800face = np.array([np.std([np.mean(data[0][0][4],axis=0)[4],np.mean(data[3][0][4],axis=0)[4],np.mean(data[10][0][4],axis=0)[4],\
                                    np.mean(data[13][0][4],axis=0)[4],np.mean(data[14][0][4],axis=0)[4],np.mean(data[15][0][4],axis=0)[4],np.mean(data[16][0][4],axis=0)[4]]),\
                       np.std([np.mean(data[0][1][4],axis=0)[4],np.mean(data[3][1][4],axis=0)[4],np.mean(data[10][1][4],axis=0)[4],\
                                    np.mean(data[13][1][4],axis=0)[4],np.mean(data[14][1][4],axis=0)[4],np.mean(data[15][1][4],axis=0)[4],np.mean(data[16][1][4],axis=0)[4]]),\
                       np.std([np.mean(data[0][2][4],axis=0)[4],np.mean(data[3][2][4],axis=0)[4],np.mean(data[10][2][4],axis=0)[4],\
                                    np.mean(data[13][2][4],axis=0)[4],np.mean(data[14][2][4],axis=0)[4],np.mean(data[15][2][4],axis=0)[4],np.mean(data[16][2][4],axis=0)[4]]),\
                       np.std([np.mean(data[0][3][4],axis=0)[4],np.mean(data[3][3][4],axis=0)[4],np.mean(data[10][3][4],axis=0)[4],\
                                    np.mean(data[13][3][4],axis=0)[4],np.mean(data[14][3][4],axis=0)[4],np.mean(data[15][3][4],axis=0)[4],np.mean(data[16][3][4],axis=0)[4]]),\
                       np.std([np.mean(data[0][4][4],axis=0)[4],np.mean(data[3][4][4],axis=0)[4],np.mean(data[10][4][4],axis=0)[4],\
                                    np.mean(data[13][4][4],axis=0)[4],np.mean(data[14][4][4],axis=0)[4],np.mean(data[15][4][4],axis=0)[4],np.mean(data[16][4][4],axis=0)[4]]),\
                       np.std([np.mean(data[0][5][4],axis=0)[4],np.mean(data[3][5][4],axis=0)[4],np.mean(data[10][5][4],axis=0)[4],\
                                    np.mean(data[13][5][4],axis=0)[4],np.mean(data[14][5][4],axis=0)[4],np.mean(data[15][5][4],axis=0)[4],np.mean(data[16][5][4],axis=0)[4]])])
stdvel1600face = np.array([np.std([np.mean(data[2][0][4],axis=0)[4],np.mean(data[4][0][4],axis=0)[4],np.mean(data[6][0][4],axis=0)[4],\
                                 np.mean(data[8][0][4],axis=0)[4],np.mean(data[11][0][4],axis=0)[4]]),\
                       np.std([np.mean(data[2][1][4],axis=0)[4],np.mean(data[4][1][4],axis=0)[4],np.mean(data[6][1][4],axis=0)[4],\
                                 np.mean(data[8][1][4],axis=0)[4],np.mean(data[11][1][4],axis=0)[4]]),\
                       np.std([np.mean(data[2][2][4],axis=0)[4],np.mean(data[4][2][4],axis=0)[4],np.mean(data[6][2][4],axis=0)[4],\
                                 np.mean(data[8][2][4],axis=0)[4],np.mean(data[11][2][4],axis=0)[4]]),\
                       np.std([np.mean(data[2][3][4],axis=0)[4],np.mean(data[4][3][4],axis=0)[4],np.mean(data[6][3][4],axis=0)[4],\
                                 np.mean(data[8][3][4],axis=0)[4],np.mean(data[11][3][4],axis=0)[4]]),\
                       np.std([np.mean(data[2][4][4],axis=0)[4],np.mean(data[4][4][4],axis=0)[4],np.mean(data[6][4][4],axis=0)[4],\
                                 np.mean(data[8][4][4],axis=0)[4],np.mean(data[11][4][4],axis=0)[4]]),\
                       np.std([np.mean(data[2][5][4],axis=0)[4],np.mean(data[4][5][4],axis=0)[4],np.mean(data[6][5][4],axis=0)[4],\
                                 np.mean(data[8][5][4],axis=0)[4],np.mean(data[11][5][4],axis=0)[4]])])
stdvel4000face = np.array([np.std([np.mean(data[5][0][4],axis=0)[4],np.mean(data[9][0][4],axis=0)[4],np.mean(data[12][0][4],axis=0)[4]]),\
                       np.std([np.mean(data[5][1][4],axis=0)[4],np.mean(data[9][1][4],axis=0)[4],np.mean(data[12][1][4],axis=0)[4]]),\
                       np.std([np.mean(data[5][2][4],axis=0)[4],np.mean(data[9][2][4],axis=0)[4],np.mean(data[12][2][4],axis=0)[4]]),\
                       np.std([np.mean(data[5][3][4],axis=0)[4],np.mean(data[9][3][4],axis=0)[4],np.mean(data[12][3][4],axis=0)[4]])])

meanvel800back = np.array([np.mean([np.mean(data[0][0][5],axis=0)[4],np.mean(data[3][0][5],axis=0)[4],np.mean(data[10][0][5],axis=0)[4],\
                                    np.mean(data[13][0][5],axis=0)[4],np.mean(data[14][0][5],axis=0)[4],np.mean(data[15][0][5],axis=0)[4],np.mean(data[16][0][5],axis=0)[4]]),\
                       np.mean([np.mean(data[0][1][5],axis=0)[4],np.mean(data[3][1][5],axis=0)[4],np.mean(data[10][1][5],axis=0)[4],\
                                    np.mean(data[13][1][5],axis=0)[4],np.mean(data[14][1][5],axis=0)[4],np.mean(data[15][1][5],axis=0)[4],np.mean(data[16][1][5],axis=0)[4]]),\
                       np.mean([np.mean(data[0][2][5],axis=0)[4],np.mean(data[3][2][5],axis=0)[4],np.mean(data[10][2][5],axis=0)[4],\
                                    np.mean(data[13][2][5],axis=0)[4],np.mean(data[14][2][5],axis=0)[4],np.mean(data[15][2][5],axis=0)[4],np.mean(data[16][2][5],axis=0)[4]]),\
                       np.mean([np.mean(data[0][3][5],axis=0)[4],np.mean(data[3][3][5],axis=0)[4],np.mean(data[10][3][5],axis=0)[4],\
                                    np.mean(data[13][3][5],axis=0)[4],np.mean(data[14][3][5],axis=0)[4],np.mean(data[15][3][5],axis=0)[4],np.mean(data[16][3][5],axis=0)[4]]),\
                       np.mean([np.mean(data[0][4][5],axis=0)[4],np.mean(data[3][4][5],axis=0)[4],np.mean(data[10][4][5],axis=0)[4],\
                                    np.mean(data[13][4][5],axis=0)[4],np.mean(data[14][4][5],axis=0)[4],np.mean(data[15][4][5],axis=0)[4],np.mean(data[16][4][5],axis=0)[4]]),\
                       np.mean([np.mean(data[0][5][5],axis=0)[4],np.mean(data[3][5][5],axis=0)[4],np.mean(data[10][5][5],axis=0)[4],\
                                    np.mean(data[13][5][5],axis=0)[4],np.mean(data[14][5][5],axis=0)[4],np.mean(data[15][5][5],axis=0)[4],np.mean(data[16][5][5],axis=0)[4]])])
meanvel1600back = np.array([np.mean([np.mean(data[2][0][5],axis=0)[4],np.mean(data[4][0][5],axis=0)[4],np.mean(data[6][0][5],axis=0)[4],\
                                 np.mean(data[8][0][5],axis=0)[4],np.mean(data[11][0][5],axis=0)[4]]),\
                       np.mean([np.mean(data[2][1][5],axis=0)[4],np.mean(data[4][1][5],axis=0)[4],np.mean(data[6][1][5],axis=0)[4],\
                                 np.mean(data[8][1][5],axis=0)[4],np.mean(data[11][1][5],axis=0)[4]]),\
                       np.mean([np.mean(data[2][2][5],axis=0)[4],np.mean(data[4][2][5],axis=0)[4],np.mean(data[6][2][5],axis=0)[4],\
                                 np.mean(data[8][2][5],axis=0)[4],np.mean(data[11][2][5],axis=0)[4]]),\
                       np.mean([np.mean(data[2][3][5],axis=0)[4],np.mean(data[4][3][5],axis=0)[4],np.mean(data[6][3][5],axis=0)[4],\
                                 np.mean(data[8][3][5],axis=0)[4],np.mean(data[11][3][5],axis=0)[4]]),\
                       np.mean([np.mean(data[2][4][5],axis=0)[4],np.mean(data[4][4][5],axis=0)[4],np.mean(data[6][4][5],axis=0)[4],\
                                 np.mean(data[8][4][5],axis=0)[4],np.mean(data[11][4][5],axis=0)[4]]),\
                       np.mean([np.mean(data[2][5][5],axis=0)[4],np.mean(data[4][5][5],axis=0)[4],np.mean(data[6][5][5],axis=0)[4],\
                                 np.mean(data[8][5][5],axis=0)[4],np.mean(data[11][5][5],axis=0)[4]])])
meanvel4000back = np.array([np.mean([np.mean(data[5][0][5],axis=0)[4],np.mean(data[9][0][5],axis=0)[4],np.mean(data[12][0][5],axis=0)[4]]),\
                       np.mean([np.mean(data[5][1][5],axis=0)[4],np.mean(data[9][1][5],axis=0)[4],np.mean(data[12][1][5],axis=0)[4]]),\
                       np.mean([np.mean(data[5][2][5],axis=0)[4],np.mean(data[9][2][5],axis=0)[4],np.mean(data[12][2][5],axis=0)[4]]),\
                       np.mean([np.mean(data[5][3][5],axis=0)[4],np.mean(data[9][3][5],axis=0)[4],np.mean(data[12][3][5],axis=0)[4]])])

stdvel800back = np.array([np.std([np.mean(data[0][0][5],axis=0)[4],np.mean(data[3][0][5],axis=0)[4],np.mean(data[10][0][5],axis=0)[4],\
                                    np.mean(data[13][0][5],axis=0)[4],np.mean(data[14][0][5],axis=0)[4],np.mean(data[15][0][5],axis=0)[4],np.mean(data[16][0][5],axis=0)[4]]),\
                       np.std([np.mean(data[0][1][5],axis=0)[4],np.mean(data[3][1][5],axis=0)[4],np.mean(data[10][1][5],axis=0)[4],\
                                    np.mean(data[13][1][5],axis=0)[4],np.mean(data[14][1][5],axis=0)[4],np.mean(data[15][1][5],axis=0)[4],np.mean(data[16][1][5],axis=0)[4]]),\
                       np.std([np.mean(data[0][2][5],axis=0)[4],np.mean(data[3][2][5],axis=0)[4],np.mean(data[10][2][5],axis=0)[4],\
                                    np.mean(data[13][2][5],axis=0)[4],np.mean(data[14][2][5],axis=0)[4],np.mean(data[15][2][5],axis=0)[4],np.mean(data[16][2][5],axis=0)[4]]),\
                       np.std([np.mean(data[0][3][5],axis=0)[4],np.mean(data[3][3][5],axis=0)[4],np.mean(data[10][3][5],axis=0)[4],\
                                    np.mean(data[13][3][5],axis=0)[4],np.mean(data[14][3][5],axis=0)[4],np.mean(data[15][3][5],axis=0)[4],np.mean(data[16][3][5],axis=0)[4]]),\
                       np.std([np.mean(data[0][4][5],axis=0)[4],np.mean(data[3][4][5],axis=0)[4],np.mean(data[10][4][5],axis=0)[4],\
                                    np.mean(data[13][4][5],axis=0)[4],np.mean(data[14][4][5],axis=0)[4],np.mean(data[15][4][5],axis=0)[4],np.mean(data[16][4][5],axis=0)[4]]),\
                       np.std([np.mean(data[0][5][5],axis=0)[4],np.mean(data[3][5][5],axis=0)[4],np.mean(data[10][5][5],axis=0)[4],\
                                    np.mean(data[13][5][5],axis=0)[4],np.mean(data[14][5][5],axis=0)[4],np.mean(data[15][5][5],axis=0)[4],np.mean(data[16][5][5],axis=0)[4]])])
stdvel1600back = np.array([np.std([np.mean(data[2][0][5],axis=0)[4],np.mean(data[4][0][5],axis=0)[4],np.mean(data[6][0][5],axis=0)[4],\
                                 np.mean(data[8][0][5],axis=0)[4],np.mean(data[11][0][5],axis=0)[4]]),\
                       np.std([np.mean(data[2][1][5],axis=0)[4],np.mean(data[4][1][5],axis=0)[4],np.mean(data[6][1][5],axis=0)[4],\
                                 np.mean(data[8][1][5],axis=0)[4],np.mean(data[11][1][5],axis=0)[4]]),\
                       np.std([np.mean(data[2][2][5],axis=0)[4],np.mean(data[4][2][5],axis=0)[4],np.mean(data[6][2][5],axis=0)[4],\
                                 np.mean(data[8][2][5],axis=0)[4],np.mean(data[11][2][5],axis=0)[4]]),\
                       np.std([np.mean(data[2][3][5],axis=0)[4],np.mean(data[4][3][5],axis=0)[4],np.mean(data[6][3][5],axis=0)[4],\
                                 np.mean(data[8][3][5],axis=0)[4],np.mean(data[11][3][5],axis=0)[4]]),\
                       np.std([np.mean(data[2][4][5],axis=0)[4],np.mean(data[4][4][5],axis=0)[4],np.mean(data[6][4][5],axis=0)[4],\
                                 np.mean(data[8][4][5],axis=0)[4],np.mean(data[11][4][5],axis=0)[4]]),\
                       np.std([np.mean(data[2][5][5],axis=0)[4],np.mean(data[4][5][5],axis=0)[4],np.mean(data[6][5][5],axis=0)[4],\
                                 np.mean(data[8][5][5],axis=0)[4],np.mean(data[11][5][5],axis=0)[4]])])
stdvel4000back = np.array([np.std([np.mean(data[5][0][5],axis=0)[4],np.mean(data[9][0][5],axis=0)[4],np.mean(data[12][0][5],axis=0)[4]]),\
                       np.std([np.mean(data[5][1][5],axis=0)[4],np.mean(data[9][1][5],axis=0)[4],np.mean(data[12][1][5],axis=0)[4]]),\
                       np.std([np.mean(data[5][2][5],axis=0)[4],np.mean(data[9][2][5],axis=0)[4],np.mean(data[12][2][5],axis=0)[4]]),\
                       np.std([np.mean(data[5][3][5],axis=0)[4],np.mean(data[9][3][5],axis=0)[4],np.mean(data[12][3][5],axis=0)[4]])])

meanvel800topp = np.array([np.mean([np.mean(data[0][0][2],axis=0)[4],np.mean(data[3][0][2],axis=0)[4],np.mean(data[10][0][2],axis=0)[4],\
                                    np.mean(data[13][0][2],axis=0)[4],np.mean(data[14][0][2],axis=0)[4],np.mean(data[15][0][2],axis=0)[4],np.mean(data[16][0][2],axis=0)[4]]),\
                       np.mean([np.mean(data[0][1][2],axis=0)[4],np.mean(data[3][1][2],axis=0)[4],np.mean(data[10][1][2],axis=0)[4],\
                                    np.mean(data[13][1][2],axis=0)[4],np.mean(data[14][1][2],axis=0)[4],np.mean(data[15][1][2],axis=0)[4],np.mean(data[16][1][2],axis=0)[4]]),\
                       np.mean([np.mean(data[0][2][2],axis=0)[4],np.mean(data[3][2][2],axis=0)[4],np.mean(data[10][2][2],axis=0)[4],\
                                    np.mean(data[13][2][2],axis=0)[4],np.mean(data[14][2][2],axis=0)[4],np.mean(data[15][2][2],axis=0)[4],np.mean(data[16][2][2],axis=0)[4]]),\
                       np.mean([np.mean(data[0][3][2],axis=0)[4],np.mean(data[3][3][2],axis=0)[4],np.mean(data[10][3][2],axis=0)[4],\
                                    np.mean(data[13][3][2],axis=0)[4],np.mean(data[14][3][2],axis=0)[4],np.mean(data[15][3][2],axis=0)[4],np.mean(data[16][3][2],axis=0)[4]]),\
                       np.mean([np.mean(data[0][4][2],axis=0)[4],np.mean(data[3][4][2],axis=0)[4],np.mean(data[10][4][2],axis=0)[4],\
                                    np.mean(data[13][4][2],axis=0)[4],np.mean(data[14][4][2],axis=0)[4],np.mean(data[15][4][2],axis=0)[4],np.mean(data[16][4][2],axis=0)[4]]),\
                       np.mean([np.mean(data[0][5][2],axis=0)[4],np.mean(data[3][5][2],axis=0)[4],np.mean(data[10][5][2],axis=0)[4],\
                                    np.mean(data[13][5][2],axis=0)[4],np.mean(data[14][5][2],axis=0)[4],np.mean(data[15][5][2],axis=0)[4],np.mean(data[16][5][2],axis=0)[4]])])
meanvel1600topp = np.array([np.mean([np.mean(data[2][0][2],axis=0)[4],np.mean(data[4][0][2],axis=0)[4],np.mean(data[6][0][2],axis=0)[4],\
                                 np.mean(data[8][0][2],axis=0)[4],np.mean(data[11][0][2],axis=0)[4]]),\
                       np.mean([np.mean(data[2][1][2],axis=0)[4],np.mean(data[4][1][2],axis=0)[4],np.mean(data[6][1][2],axis=0)[4],\
                                 np.mean(data[8][1][2],axis=0)[4],np.mean(data[11][1][2],axis=0)[4]]),\
                       np.mean([np.mean(data[2][2][2],axis=0)[4],np.mean(data[4][2][2],axis=0)[4],np.mean(data[6][2][2],axis=0)[4],\
                                 np.mean(data[8][2][2],axis=0)[4],np.mean(data[11][2][2],axis=0)[4]]),\
                       np.mean([np.mean(data[2][3][2],axis=0)[4],np.mean(data[4][3][2],axis=0)[4],np.mean(data[6][3][2],axis=0)[4],\
                                 np.mean(data[8][3][2],axis=0)[4],np.mean(data[11][3][2],axis=0)[4]]),\
                       np.mean([np.mean(data[2][4][2],axis=0)[4],np.mean(data[4][4][2],axis=0)[4],np.mean(data[6][4][2],axis=0)[4],\
                                 np.mean(data[8][4][2],axis=0)[4],np.mean(data[11][4][2],axis=0)[4]]),\
                       np.mean([np.mean(data[2][5][2],axis=0)[4],np.mean(data[4][5][2],axis=0)[4],np.mean(data[6][5][2],axis=0)[4],\
                                 np.mean(data[8][5][2],axis=0)[4],np.mean(data[11][5][2],axis=0)[4]])])
meanvel4000topp = np.array([np.mean([np.mean(data[5][0][2],axis=0)[4],np.mean(data[9][0][2],axis=0)[4],np.mean(data[12][0][2],axis=0)[4]]),\
                       np.mean([np.mean(data[5][1][2],axis=0)[4],np.mean(data[9][1][2],axis=0)[4],np.mean(data[12][1][2],axis=0)[4]]),\
                       np.mean([np.mean(data[5][2][2],axis=0)[4],np.mean(data[9][2][2],axis=0)[4],np.mean(data[12][2][2],axis=0)[4]]),\
                       np.mean([np.mean(data[5][3][2],axis=0)[4],np.mean(data[9][3][2],axis=0)[4],np.mean(data[12][3][2],axis=0)[4]])])

stdvel800topp = np.array([np.std([np.mean(data[0][0][2],axis=0)[4],np.mean(data[3][0][2],axis=0)[4],np.mean(data[10][0][2],axis=0)[4],\
                                    np.mean(data[13][0][2],axis=0)[4],np.mean(data[14][0][2],axis=0)[4],np.mean(data[15][0][2],axis=0)[4],np.mean(data[16][0][2],axis=0)[4]]),\
                       np.std([np.mean(data[0][1][2],axis=0)[4],np.mean(data[3][1][2],axis=0)[4],np.mean(data[10][1][2],axis=0)[4],\
                                    np.mean(data[13][1][2],axis=0)[4],np.mean(data[14][1][2],axis=0)[4],np.mean(data[15][1][2],axis=0)[4],np.mean(data[16][1][2],axis=0)[4]]),\
                       np.std([np.mean(data[0][2][2],axis=0)[4],np.mean(data[3][2][2],axis=0)[4],np.mean(data[10][2][2],axis=0)[4],\
                                    np.mean(data[13][2][2],axis=0)[4],np.mean(data[14][2][2],axis=0)[4],np.mean(data[15][2][2],axis=0)[4],np.mean(data[16][2][2],axis=0)[4]]),\
                       np.std([np.mean(data[0][3][2],axis=0)[4],np.mean(data[3][3][2],axis=0)[4],np.mean(data[10][3][2],axis=0)[4],\
                                    np.mean(data[13][3][2],axis=0)[4],np.mean(data[14][3][2],axis=0)[4],np.mean(data[15][3][2],axis=0)[4],np.mean(data[16][3][2],axis=0)[4]]),\
                       np.std([np.mean(data[0][4][2],axis=0)[4],np.mean(data[3][4][2],axis=0)[4],np.mean(data[10][4][2],axis=0)[4],\
                                    np.mean(data[13][4][2],axis=0)[4],np.mean(data[14][4][2],axis=0)[4],np.mean(data[15][4][2],axis=0)[4],np.mean(data[16][4][2],axis=0)[4]]),\
                       np.std([np.mean(data[0][5][2],axis=0)[4],np.mean(data[3][5][2],axis=0)[4],np.mean(data[10][5][2],axis=0)[4],\
                                    np.mean(data[13][5][2],axis=0)[4],np.mean(data[14][5][2],axis=0)[4],np.mean(data[15][5][2],axis=0)[4],np.mean(data[16][5][2],axis=0)[4]])])
stdvel1600topp = np.array([np.std([np.mean(data[2][0][2],axis=0)[4],np.mean(data[4][0][2],axis=0)[4],np.mean(data[6][0][2],axis=0)[4],\
                                 np.mean(data[8][0][2],axis=0)[4],np.mean(data[11][0][2],axis=0)[4]]),\
                       np.std([np.mean(data[2][1][2],axis=0)[4],np.mean(data[4][1][2],axis=0)[4],np.mean(data[6][1][2],axis=0)[4],\
                                 np.mean(data[8][1][2],axis=0)[4],np.mean(data[11][1][2],axis=0)[4]]),\
                       np.std([np.mean(data[2][2][2],axis=0)[4],np.mean(data[4][2][2],axis=0)[4],np.mean(data[6][2][2],axis=0)[4],\
                                 np.mean(data[8][2][2],axis=0)[4],np.mean(data[11][2][2],axis=0)[4]]),\
                       np.std([np.mean(data[2][3][2],axis=0)[4],np.mean(data[4][3][2],axis=0)[4],np.mean(data[6][3][2],axis=0)[4],\
                                 np.mean(data[8][3][2],axis=0)[4],np.mean(data[11][3][2],axis=0)[4]]),\
                       np.std([np.mean(data[2][4][2],axis=0)[4],np.mean(data[4][4][2],axis=0)[4],np.mean(data[6][4][2],axis=0)[4],\
                                 np.mean(data[8][4][2],axis=0)[4],np.mean(data[11][4][2],axis=0)[4]]),\
                       np.std([np.mean(data[2][5][2],axis=0)[4],np.mean(data[4][5][2],axis=0)[4],np.mean(data[6][5][2],axis=0)[4],\
                                 np.mean(data[8][5][2],axis=0)[4],np.mean(data[11][5][2],axis=0)[4]])])
stdvel4000topp = np.array([np.std([np.mean(data[5][0][2],axis=0)[4],np.mean(data[9][0][2],axis=0)[4],np.mean(data[12][0][2],axis=0)[4]]),\
                       np.std([np.mean(data[5][1][2],axis=0)[4],np.mean(data[9][1][2],axis=0)[4],np.mean(data[12][1][2],axis=0)[4]]),\
                       np.std([np.mean(data[5][2][2],axis=0)[4],np.mean(data[9][2][2],axis=0)[4],np.mean(data[12][2][2],axis=0)[4]]),\
                       np.std([np.mean(data[5][3][2],axis=0)[4],np.mean(data[9][3][2],axis=0)[4],np.mean(data[12][3][2],axis=0)[4]])])

meanvel800topf = np.array([np.mean([np.mean(data[0][0][3],axis=0)[4],np.mean(data[3][0][3],axis=0)[4],np.mean(data[10][0][3],axis=0)[4],\
                                    np.mean(data[13][0][3],axis=0)[4],np.mean(data[14][0][3],axis=0)[4],np.mean(data[15][0][3],axis=0)[4],np.mean(data[16][0][3],axis=0)[4]]),\
                       np.mean([np.mean(data[0][1][3],axis=0)[4],np.mean(data[3][1][3],axis=0)[4],np.mean(data[10][1][3],axis=0)[4],\
                                    np.mean(data[13][1][3],axis=0)[4],np.mean(data[14][1][3],axis=0)[4],np.mean(data[15][1][3],axis=0)[4],np.mean(data[16][1][3],axis=0)[4]]),\
                       np.mean([np.mean(data[0][2][3],axis=0)[4],np.mean(data[3][2][3],axis=0)[4],np.mean(data[10][2][3],axis=0)[4],\
                                    np.mean(data[13][2][3],axis=0)[4],np.mean(data[14][2][3],axis=0)[4],np.mean(data[15][2][3],axis=0)[4],np.mean(data[16][2][3],axis=0)[4]]),\
                       np.mean([np.mean(data[0][3][3],axis=0)[4],np.mean(data[3][3][3],axis=0)[4],np.mean(data[10][3][3],axis=0)[4],\
                                    np.mean(data[13][3][3],axis=0)[4],np.mean(data[14][3][3],axis=0)[4],np.mean(data[15][3][3],axis=0)[4],np.mean(data[16][3][3],axis=0)[4]]),\
                       np.mean([np.mean(data[0][4][3],axis=0)[4],np.mean(data[3][4][3],axis=0)[4],np.mean(data[10][4][3],axis=0)[4],\
                                    np.mean(data[13][4][3],axis=0)[4],np.mean(data[14][4][3],axis=0)[4],np.mean(data[15][4][3],axis=0)[4],np.mean(data[16][4][3],axis=0)[4]]),\
                       np.mean([np.mean(data[0][5][3],axis=0)[4],np.mean(data[3][5][3],axis=0)[4],np.mean(data[10][5][3],axis=0)[4],\
                                    np.mean(data[13][5][3],axis=0)[4],np.mean(data[14][5][3],axis=0)[4],np.mean(data[15][5][3],axis=0)[4],np.mean(data[16][5][3],axis=0)[4]])])
meanvel1600topf = np.array([np.mean([np.mean(data[2][0][3],axis=0)[4],np.mean(data[4][0][3],axis=0)[4],np.mean(data[6][0][3],axis=0)[4],\
                                 np.mean(data[8][0][3],axis=0)[4],np.mean(data[11][0][3],axis=0)[4]]),\
                       np.mean([np.mean(data[2][1][3],axis=0)[4],np.mean(data[4][1][3],axis=0)[4],np.mean(data[6][1][3],axis=0)[4],\
                                 np.mean(data[8][1][3],axis=0)[4],np.mean(data[11][1][3],axis=0)[4]]),\
                       np.mean([np.mean(data[2][2][3],axis=0)[4],np.mean(data[4][2][3],axis=0)[4],np.mean(data[6][2][3],axis=0)[4],\
                                 np.mean(data[8][2][3],axis=0)[4],np.mean(data[11][2][3],axis=0)[4]]),\
                       np.mean([np.mean(data[2][3][3],axis=0)[4],np.mean(data[4][3][3],axis=0)[4],np.mean(data[6][3][3],axis=0)[4],\
                                 np.mean(data[8][3][3],axis=0)[4],np.mean(data[11][3][3],axis=0)[4]]),\
                       np.mean([np.mean(data[2][4][3],axis=0)[4],np.mean(data[4][4][3],axis=0)[4],np.mean(data[6][4][3],axis=0)[4],\
                                 np.mean(data[8][4][3],axis=0)[4],np.mean(data[11][4][3],axis=0)[4]]),\
                       np.mean([np.mean(data[2][5][3],axis=0)[4],np.mean(data[4][5][3],axis=0)[4],np.mean(data[6][5][3],axis=0)[4],\
                                 np.mean(data[8][5][3],axis=0)[4],np.mean(data[11][5][3],axis=0)[4]])])
meanvel4000topf = np.array([np.mean([np.mean(data[5][0][3],axis=0)[4],np.mean(data[9][0][3],axis=0)[4],np.mean(data[12][0][3],axis=0)[4]]),\
                       np.mean([np.mean(data[5][1][3],axis=0)[4],np.mean(data[9][1][3],axis=0)[4],np.mean(data[12][1][3],axis=0)[4]]),\
                       np.mean([np.mean(data[5][2][3],axis=0)[4],np.mean(data[9][2][3],axis=0)[4],np.mean(data[12][2][3],axis=0)[4]]),\
                       np.mean([np.mean(data[5][3][3],axis=0)[4],np.mean(data[9][3][3],axis=0)[4],np.mean(data[12][3][3],axis=0)[4]])])

stdvel800topf = np.array([np.std([np.mean(data[0][0][3],axis=0)[4],np.mean(data[3][0][3],axis=0)[4],np.mean(data[10][0][3],axis=0)[4],\
                                    np.mean(data[13][0][3],axis=0)[4],np.mean(data[14][0][3],axis=0)[4],np.mean(data[15][0][3],axis=0)[4],np.mean(data[16][0][3],axis=0)[4]]),\
                       np.std([np.mean(data[0][1][3],axis=0)[4],np.mean(data[3][1][3],axis=0)[4],np.mean(data[10][1][3],axis=0)[4],\
                                    np.mean(data[13][1][3],axis=0)[4],np.mean(data[14][1][3],axis=0)[4],np.mean(data[15][1][3],axis=0)[4],np.mean(data[16][1][3],axis=0)[4]]),\
                       np.std([np.mean(data[0][2][3],axis=0)[4],np.mean(data[3][2][3],axis=0)[4],np.mean(data[10][2][3],axis=0)[4],\
                                    np.mean(data[13][2][3],axis=0)[4],np.mean(data[14][2][3],axis=0)[4],np.mean(data[15][2][3],axis=0)[4],np.mean(data[16][2][3],axis=0)[4]]),\
                       np.std([np.mean(data[0][3][3],axis=0)[4],np.mean(data[3][3][3],axis=0)[4],np.mean(data[10][3][3],axis=0)[4],\
                                    np.mean(data[13][3][3],axis=0)[4],np.mean(data[14][3][3],axis=0)[4],np.mean(data[15][3][3],axis=0)[4],np.mean(data[16][3][3],axis=0)[4]]),\
                       np.std([np.mean(data[0][4][3],axis=0)[4],np.mean(data[3][4][3],axis=0)[4],np.mean(data[10][4][3],axis=0)[4],\
                                    np.mean(data[13][4][3],axis=0)[4],np.mean(data[14][4][3],axis=0)[4],np.mean(data[15][4][3],axis=0)[4],np.mean(data[16][4][3],axis=0)[4]]),\
                       np.std([np.mean(data[0][5][3],axis=0)[4],np.mean(data[3][5][3],axis=0)[4],np.mean(data[10][5][3],axis=0)[4],\
                                    np.mean(data[13][5][3],axis=0)[4],np.mean(data[14][5][3],axis=0)[4],np.mean(data[15][5][3],axis=0)[4],np.mean(data[16][5][3],axis=0)[4]])])
stdvel1600topf = np.array([np.std([np.mean(data[2][0][3],axis=0)[4],np.mean(data[4][0][3],axis=0)[4],np.mean(data[6][0][3],axis=0)[4],\
                                 np.mean(data[8][0][3],axis=0)[4],np.mean(data[11][0][3],axis=0)[4]]),\
                       np.std([np.mean(data[2][1][3],axis=0)[4],np.mean(data[4][1][3],axis=0)[4],np.mean(data[6][1][3],axis=0)[4],\
                                 np.mean(data[8][1][3],axis=0)[4],np.mean(data[11][1][3],axis=0)[4]]),\
                       np.std([np.mean(data[2][2][3],axis=0)[4],np.mean(data[4][2][3],axis=0)[4],np.mean(data[6][2][3],axis=0)[4],\
                                 np.mean(data[8][2][3],axis=0)[4],np.mean(data[11][2][3],axis=0)[4]]),\
                       np.std([np.mean(data[2][3][3],axis=0)[4],np.mean(data[4][3][3],axis=0)[4],np.mean(data[6][3][3],axis=0)[4],\
                                 np.mean(data[8][3][3],axis=0)[4],np.mean(data[11][3][3],axis=0)[4]]),\
                       np.std([np.mean(data[2][4][3],axis=0)[4],np.mean(data[4][4][3],axis=0)[4],np.mean(data[6][4][3],axis=0)[4],\
                                 np.mean(data[8][4][3],axis=0)[4],np.mean(data[11][4][3],axis=0)[4]]),\
                       np.std([np.mean(data[2][5][3],axis=0)[4],np.mean(data[4][5][3],axis=0)[4],np.mean(data[6][5][3],axis=0)[4],\
                                 np.mean(data[8][5][3],axis=0)[4],np.mean(data[11][5][3],axis=0)[4]])])
stdvel4000topf = np.array([np.std([np.mean(data[5][0][3],axis=0)[4],np.mean(data[9][0][3],axis=0)[4],np.mean(data[12][0][3],axis=0)[4]]),\
                       np.std([np.mean(data[5][1][3],axis=0)[4],np.mean(data[9][1][3],axis=0)[4],np.mean(data[12][1][3],axis=0)[4]]),\
                       np.std([np.mean(data[5][2][3],axis=0)[4],np.mean(data[9][2][3],axis=0)[4],np.mean(data[12][2][3],axis=0)[4]]),\
                       np.std([np.mean(data[5][3][3],axis=0)[4],np.mean(data[9][3][3],axis=0)[4],np.mean(data[12][3][3],axis=0)[4]])])

meanvel800surface = np.array([np.mean([np.mean(data[0][0][1],axis=0)[4],np.mean(data[3][0][1],axis=0)[4],np.mean(data[10][0][1],axis=0)[4],\
                                    np.mean(data[13][0][1],axis=0)[4],np.mean(data[14][0][1],axis=0)[4],np.mean(data[15][0][1],axis=0)[4],np.mean(data[16][0][1],axis=0)[4]]),\
                       np.mean([np.mean(data[0][1][1],axis=0)[4],np.mean(data[3][1][1],axis=0)[4],np.mean(data[10][1][1],axis=0)[4],\
                                    np.mean(data[13][1][1],axis=0)[4],np.mean(data[14][1][1],axis=0)[4],np.mean(data[15][1][1],axis=0)[4],np.mean(data[16][1][1],axis=0)[4]]),\
                       np.mean([np.mean(data[0][2][1],axis=0)[4],np.mean(data[3][2][1],axis=0)[4],np.mean(data[10][2][1],axis=0)[4],\
                                    np.mean(data[13][2][1],axis=0)[4],np.mean(data[14][2][1],axis=0)[4],np.mean(data[15][2][1],axis=0)[4],np.mean(data[16][2][1],axis=0)[4]]),\
                       np.mean([np.mean(data[0][3][1],axis=0)[4],np.mean(data[3][3][1],axis=0)[4],np.mean(data[10][3][1],axis=0)[4],\
                                    np.mean(data[13][3][1],axis=0)[4],np.mean(data[14][3][1],axis=0)[4],np.mean(data[15][3][1],axis=0)[4],np.mean(data[16][3][1],axis=0)[4]]),\
                       np.mean([np.mean(data[0][4][1],axis=0)[4],np.mean(data[3][4][1],axis=0)[4],np.mean(data[10][4][1],axis=0)[4],\
                                    np.mean(data[13][4][1],axis=0)[4],np.mean(data[14][4][1],axis=0)[4],np.mean(data[15][4][1],axis=0)[4],np.mean(data[16][4][1],axis=0)[4]]),\
                       np.mean([np.mean(data[0][5][1],axis=0)[4],np.mean(data[3][5][1],axis=0)[4],np.mean(data[10][5][1],axis=0)[4],\
                                    np.mean(data[13][5][1],axis=0)[4],np.mean(data[14][5][1],axis=0)[4],np.mean(data[15][5][1],axis=0)[4],np.mean(data[16][5][1],axis=0)[4]])])
meanvel1600surface = np.array([np.mean([np.mean(data[2][0][1],axis=0)[4],np.mean(data[4][0][1],axis=0)[4],np.mean(data[6][0][1],axis=0)[4],\
                                 np.mean(data[8][0][1],axis=0)[4],np.mean(data[11][0][1],axis=0)[4]]),\
                       np.mean([np.mean(data[2][1][1],axis=0)[4],np.mean(data[4][1][1],axis=0)[4],np.mean(data[6][1][1],axis=0)[4],\
                                 np.mean(data[8][1][1],axis=0)[4],np.mean(data[11][1][1],axis=0)[4]]),\
                       np.mean([np.mean(data[2][2][1],axis=0)[4],np.mean(data[4][2][1],axis=0)[4],np.mean(data[6][2][1],axis=0)[4],\
                                 np.mean(data[8][2][1],axis=0)[4],np.mean(data[11][2][1],axis=0)[4]]),\
                       np.mean([np.mean(data[2][3][1],axis=0)[4],np.mean(data[4][3][1],axis=0)[4],np.mean(data[6][3][1],axis=0)[4],\
                                 np.mean(data[8][3][1],axis=0)[4],np.mean(data[11][3][1],axis=0)[4]]),\
                       np.mean([np.mean(data[2][4][1],axis=0)[4],np.mean(data[4][4][1],axis=0)[4],np.mean(data[6][4][1],axis=0)[4],\
                                 np.mean(data[8][4][1],axis=0)[4],np.mean(data[11][4][1],axis=0)[4]]),\
                       np.mean([np.mean(data[2][5][1],axis=0)[4],np.mean(data[4][5][1],axis=0)[4],np.mean(data[6][5][1],axis=0)[4],\
                                 np.mean(data[8][5][1],axis=0)[4],np.mean(data[11][5][1],axis=0)[4]])])
meanvel4000surface = np.array([np.mean([np.mean(data[5][0][1],axis=0)[4],np.mean(data[9][0][1],axis=0)[4],np.mean(data[12][0][1],axis=0)[4]]),\
                       np.mean([np.mean(data[5][1][1],axis=0)[4],np.mean(data[9][1][1],axis=0)[4],np.mean(data[12][1][1],axis=0)[4]]),\
                       np.mean([np.mean(data[5][2][1],axis=0)[4],np.mean(data[9][2][1],axis=0)[4],np.mean(data[12][2][1],axis=0)[4]]),\
                       np.mean([np.mean(data[5][3][1],axis=0)[4],np.mean(data[9][3][1],axis=0)[4],np.mean(data[12][3][1],axis=0)[4]])])

stdvel800surface = np.array([np.std([np.mean(data[0][0][1],axis=0)[4],np.mean(data[3][0][1],axis=0)[4],np.mean(data[10][0][1],axis=0)[4],\
                                    np.mean(data[13][0][1],axis=0)[4],np.mean(data[14][0][1],axis=0)[4],np.mean(data[15][0][1],axis=0)[4],np.mean(data[16][0][1],axis=0)[4]]),\
                       np.std([np.mean(data[0][1][1],axis=0)[4],np.mean(data[3][1][1],axis=0)[4],np.mean(data[10][1][1],axis=0)[4],\
                                    np.mean(data[13][1][1],axis=0)[4],np.mean(data[14][1][1],axis=0)[4],np.mean(data[15][1][1],axis=0)[4],np.mean(data[16][1][1],axis=0)[4]]),\
                       np.std([np.mean(data[0][2][1],axis=0)[4],np.mean(data[3][2][1],axis=0)[4],np.mean(data[10][2][1],axis=0)[4],\
                                    np.mean(data[13][2][1],axis=0)[4],np.mean(data[14][2][1],axis=0)[4],np.mean(data[15][2][1],axis=0)[4],np.mean(data[16][2][1],axis=0)[4]]),\
                       np.std([np.mean(data[0][3][1],axis=0)[4],np.mean(data[3][3][1],axis=0)[4],np.mean(data[10][3][1],axis=0)[4],\
                                    np.mean(data[13][3][1],axis=0)[4],np.mean(data[14][3][1],axis=0)[4],np.mean(data[15][3][1],axis=0)[4],np.mean(data[16][3][1],axis=0)[4]]),\
                       np.std([np.mean(data[0][4][1],axis=0)[4],np.mean(data[3][4][1],axis=0)[4],np.mean(data[10][4][1],axis=0)[4],\
                                    np.mean(data[13][4][1],axis=0)[4],np.mean(data[14][4][1],axis=0)[4],np.mean(data[15][4][1],axis=0)[4],np.mean(data[16][4][1],axis=0)[4]]),\
                       np.std([np.mean(data[0][5][1],axis=0)[4],np.mean(data[3][5][1],axis=0)[4],np.mean(data[10][5][1],axis=0)[4],\
                                    np.mean(data[13][5][1],axis=0)[4],np.mean(data[14][5][1],axis=0)[4],np.mean(data[15][5][1],axis=0)[4],np.mean(data[16][5][1],axis=0)[4]])])
stdvel1600surface = np.array([np.std([np.mean(data[2][0][1],axis=0)[4],np.mean(data[4][0][1],axis=0)[4],np.mean(data[6][0][1],axis=0)[4],\
                                 np.mean(data[8][0][1],axis=0)[4],np.mean(data[11][0][1],axis=0)[4]]),\
                       np.std([np.mean(data[2][1][1],axis=0)[4],np.mean(data[4][1][1],axis=0)[4],np.mean(data[6][1][1],axis=0)[4],\
                                 np.mean(data[8][1][1],axis=0)[4],np.mean(data[11][1][1],axis=0)[4]]),\
                       np.std([np.mean(data[2][2][1],axis=0)[4],np.mean(data[4][2][1],axis=0)[4],np.mean(data[6][2][1],axis=0)[4],\
                                 np.mean(data[8][2][1],axis=0)[4],np.mean(data[11][2][1],axis=0)[4]]),\
                       np.std([np.mean(data[2][3][1],axis=0)[4],np.mean(data[4][3][1],axis=0)[4],np.mean(data[6][3][1],axis=0)[4],\
                                 np.mean(data[8][3][1],axis=0)[4],np.mean(data[11][3][1],axis=0)[4]]),\
                       np.std([np.mean(data[2][4][1],axis=0)[4],np.mean(data[4][4][1],axis=0)[4],np.mean(data[6][4][1],axis=0)[4],\
                                 np.mean(data[8][4][1],axis=0)[4],np.mean(data[11][4][1],axis=0)[4]]),\
                       np.std([np.mean(data[2][5][1],axis=0)[4],np.mean(data[4][5][1],axis=0)[4],np.mean(data[6][5][1],axis=0)[4],\
                                 np.mean(data[8][5][1],axis=0)[4],np.mean(data[11][5][1],axis=0)[4]])])
stdvel4000surface = np.array([np.std([np.mean(data[5][0][1],axis=0)[4],np.mean(data[9][0][1],axis=0)[4],np.mean(data[12][0][1],axis=0)[4]]),\
                       np.std([np.mean(data[5][1][1],axis=0)[4],np.mean(data[9][1][1],axis=0)[4],np.mean(data[12][1][1],axis=0)[4]]),\
                       np.std([np.mean(data[5][2][1],axis=0)[4],np.mean(data[9][2][1],axis=0)[4],np.mean(data[12][2][1],axis=0)[4]]),\
                       np.std([np.mean(data[5][3][1],axis=0)[4],np.mean(data[9][3][1],axis=0)[4],np.mean(data[12][3][1],axis=0)[4]])])

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
width34 = 0.6

# ### Legend
# fig, ax = plt.subplots()
# marker800 = mlines.Line2D([], [], color='k', marker='^', linestyle='None', markersize=12, label='800 $1/s$')
# marker1600 = mlines.Line2D([], [], color='k', marker='o', linestyle='None', markersize=12, label='1600 $1/s$')
# marker4000 = mlines.Line2D([], [], color='k', marker='s', linestyle='None', markersize=12, label='4000 $1/s$')
# linetop13 = mlines.Line2D([], [], color=color5, marker='None', linestyle='-', linewidth=3, label='top 1/3')
# linetop2 = mlines.Line2D([], [], color=color4, marker='None', linestyle='--', linewidth=3, label='top 2 $\mu m$')
# ax.legend(
#     handles=[marker800, marker1600, marker4000, linetop13, linetop2],
#     loc="lower center", # "upper center" puts it below the line
#     ncol=5,
#     bbox_to_anchor=(0.5, 0.88),
#     bbox_transform=fig.transFigure,
#     fontsize=20
# );
# plt.savefig('legend.png',bbox_inches='tight')
# plt.show()


# ### velocity
# fig, ax = plt.subplots()
# ax.plot(time[0:6],meanvel800volume,'--^', color=color1, markersize=6, label='800 1/s')
# ax.fill_between(time[0:6],meanvel800volume-stdvel800volume, meanvel800volume+stdvel800volume, color=color1, alpha=0.3)
# ax.plot(time[0:6],meanvel1600volume,'--o', color=color2, markersize=6, label='1600 1/s')
# ax.fill_between(time[0:6],meanvel1600volume-stdvel1600volume, meanvel1600volume+stdvel1600volume, color=color2, alpha=0.3)
# # ax.errorbar(time[0:6],meanvel1600surface,yerr=stdvel1600surface,fmt='--o', color=color2, ecolor='k', markersize=6, capsize=3, label='1600 1/s')
# # ax.errorbar(time[0:4],meanvel4000surface,yerr=stdvel4000surface,fmt='--o', color=color3, ecolor='k', markersize=6, capsize=3, label='4000 1/s')
# ax.plot(time[0:4],meanvel4000volume,'--s', color=color3, markersize=6, label='4000 1/s')
# ax.fill_between(time[0:4],meanvel4000volume-stdvel4000volume, meanvel4000volume+stdvel4000volume, color=color3, alpha=0.3)

# ax.set_ylabel('velocity $[mm/s]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average velocity', fontsize=fontsize)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('vel.png',bbox_inches='tight')
# plt.show()


# ### velocity -- zoom in
# fig, ax = plt.subplots()
# ax.plot(time[0:6],meanvel800volume,'--^', color=color1, markersize=6, label='800 1/s')
# ax.fill_between(time[0:6],meanvel800volume-stdvel800volume, meanvel800volume+stdvel800volume, color=color1, alpha=0.3)
# ax.plot(time[0:6],meanvel1600volume,'--o', color=color2, markersize=6, label='1600 1/s')
# ax.fill_between(time[0:6],meanvel1600volume-stdvel1600volume, meanvel1600volume+stdvel1600volume, color=color2, alpha=0.3)
# ax.plot(time[0:4],meanvel4000volume,'--s', color=color3, markersize=6, label='4000 1/s')
# ax.fill_between(time[0:4],meanvel4000volume-stdvel4000volume, meanvel4000volume+stdvel4000volume, color=color3, alpha=0.3)

# ax.set_ylim(ymax=0.25)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('vel_zoom.png',bbox_inches='tight')
# plt.show()


# ### Rate of elongation faceward vs. backward
# fig, ax = plt.subplots()
# ax.bar(time1-2.5*width12, meanelon800face, yerr=stdelon800face, alpha=0.9, color=color1, ecolor='black', capsize=2, width=width12)
# ax.bar(time1-0.5*width12, meanelon1600face, yerr=stdelon1600face, alpha=0.9, color=color2, ecolor='black', capsize=2, width=width12)
# ax.bar(time2+1.5*width12, meanelon4000face, yerr=stdelon4000face, alpha=0.9, color=color3, ecolor='black', capsize=2, width=width12)
# ax.bar(time1-1.5*width12, meanelon800back, yerr=stdelon800face, hatch='////', color='none', edgecolor=color1, ecolor='black', capsize=2, width=width12)
# ax.bar(time1+0.5*width12, meanelon1600back, yerr=stdelon1600face, hatch='////', color='none', edgecolor=color2, ecolor='black', capsize=2, width=width12)
# ax.bar(time2+2.5*width12, meanelon4000back, yerr=stdelon4000face, hatch='////', color='none', edgecolor=color3, ecolor='black', capsize=2, width=width12)

# ax.set_ylabel('rate of elongation $[1/s]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average rate of elongation', fontsize=fontsize)

# # ax.set_xlim(3,12)
# ax.set_ylim(0,)

# plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# legend_elements = [Line2D([0], [0], color=color1, lw=3, label='800 1/s'),
#                    Line2D([0], [0], color=color2, lw=3, label='1600 1/s'), 
#                    Line2D([0], [0], color=color3, lw=3, label='4000 1/s'),
#                    Patch(facecolor='k', edgecolor='k',label='faceward'),
#                    Patch(facecolor='none', hatch='////', edgecolor='k',label='backward'),]

# plt.legend(handles=legend_elements,loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('elonFB.png',bbox_inches='tight')
# plt.show()


# ### Rate of elongation faceward vs. backward zoom in
# fig, ax = plt.subplots(figsize=(12, 4))
# ax.bar(time3-0.5*width34, meanelon800face, yerr=stdelon800face, alpha=0.9, color=color1, ecolor='black', capsize=6, width=width34)
# ax.plot(time3[0:6]-0.5*width34,meanelon800face,'--o', color=color4, markersize=10, linewidth=3,label='faceward')
# # ax.bar(time3-0.5*width34, meanelon1600face, yerr=stdelon1600face, alpha=0.9, color=color2, ecolor='black', capsize=6, width=width34)
# # ax.plot(time3[0:6]-0.5*width34,meanelon1600face,'--o', color=color4, markersize=10, linewidth=3,label='faceward')
# ax.bar(time3+0.5*width34, meanelon800back, yerr=stdelon800face, hatch='//', color='none', edgecolor=color1, ecolor='black', capsize=6, width=width34)
# ax.plot(time3[0:6]+0.5*width34,meanelon800back,'--o', color=color5, markersize=10, linewidth=3, label='backward')
# # ax.bar(time3+0.5*width34, meanelon1600back, yerr=stdelon1600face, hatch='//', color='none', edgecolor=color2, ecolor='black', capsize=6, width=width34)
# # ax.plot(time3[0:6]+0.5*width34,meanelon1600back,'--o', color=color5, markersize=10, linewidth=3, label='backward')

# # ax.set_xlim(3,12)
# ax.set_ylim(100,250)

# plt.xticks(time3, labels=labels)
# plt.yticks(np.arange(100,251,50))
# ax.tick_params(axis='x', labelsize= ticksizeZoom)
# ax.tick_params(axis='y', labelsize= ticksizeZoom)

# plt.legend(loc=1,fontsize=ticksizeZoom)
# plt.grid(alpha=0.3)

# plt.savefig('elonFB_800.png',bbox_inches='tight')
# plt.show()


# ### Shear rate faceward vs. backward
# fig, ax = plt.subplots()
# ax.bar(time1-2.5*width12, meanshear800face, yerr=stdshear800face, alpha=0.9, color=color1, ecolor='black', capsize=2, width=width12)
# ax.bar(time1-0.5*width12, meanshear1600face, yerr=stdshear1600face, alpha=0.9, color=color2, ecolor='black', capsize=2, width=width12)
# ax.bar(time2+1.5*width12, meanshear4000face, yerr=stdshear4000face, alpha=0.9, color=color3, ecolor='black', capsize=2, width=width12)
# ax.bar(time1-1.5*width12, meanshear800back, yerr=stdshear800face, hatch='////', color='none', edgecolor=color1, ecolor='black', capsize=2, width=width12)
# ax.bar(time1+0.5*width12, meanshear1600back, yerr=stdshear1600face, hatch='////', color='none', edgecolor=color2, ecolor='black', capsize=2, width=width12)
# ax.bar(time2+2.5*width12, meanshear4000back, yerr=stdshear4000face, hatch='////', color='none', edgecolor=color3, ecolor='black', capsize=2, width=width12)

# ax.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average shear rate', fontsize=fontsize)

# # ax.set_xlim(3,12)
# ax.set_ylim(0,)

# plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# legend_elements = [Line2D([0], [0], color=color1, lw=3, label='800 1/s'),
#                    Line2D([0], [0], color=color2, lw=3, label='1600 1/s'), 
#                    Line2D([0], [0], color=color3, lw=3, label='4000 1/s'),
#                    Patch(facecolor='k', edgecolor='k',label='faceward'),
#                    Patch(facecolor='none', hatch='////', edgecolor='k',label='backward'),]

# plt.legend(handles=legend_elements,loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('shearFB.png',bbox_inches='tight')
# plt.show()

# ### Shear rate faceward vs. backward zoom in
# fig, ax = plt.subplots(figsize=(12, 4))
# # ax.bar(time3-0.5*width34, meanshear800face, yerr=stdshear800face, alpha=0.9, color=color1, ecolor='black', capsize=6, width=width34)
# # ax.plot(time3[0:6]-0.5*width34,meanshear800face,'--o', color=color4, markersize=10, linewidth=3,label='faceward')
# ax.bar(time3-0.5*width34, meanshear1600face, yerr=stdshear1600face, alpha=0.9, color=color2, ecolor='black', capsize=6, width=width34)
# ax.plot(time3[0:6]-0.5*width34,meanshear1600face,'--o', color=color4, markersize=10, linewidth=3,label='faceward')
# # ax.bar(time3+0.5*width34, meanshear800back, yerr=stdshear800face, hatch='//', color='none', edgecolor=color1, ecolor='black', capsize=6, width=width34)
# # ax.plot(time3[0:6]+0.5*width34,meanshear800back,'--o', color=color5, markersize=10, linewidth=3, label='backward')
# ax.bar(time3+0.5*width34, meanshear1600back, yerr=stdshear1600face, hatch='//', color='none', edgecolor=color2, ecolor='black', capsize=6, width=width34)
# ax.plot(time3[0:6]+0.5*width34,meanshear1600back,'--o', color=color5, markersize=10, linewidth=3, label='backward')

# # ax.set_xlim(3,12)
# ax.set_ylim(700,1150)

# plt.xticks(time3, labels=labels)
# plt.yticks(np.arange(700,1151,150))
# ax.tick_params(axis='x', labelsize= ticksizeZoom)
# ax.tick_params(axis='y', labelsize= ticksizeZoom)

# plt.legend(loc=1,fontsize=ticksizeZoom)
# plt.grid(alpha=0.3)

# plt.savefig('shearFB_1600.png',bbox_inches='tight')
# plt.show()


# ### Shear rate top
# fig, ax = plt.subplots()
# ax.errorbar(time[0:6],meanshear800topp,yerr=stdshear800topp,fmt='-^', color=color5, markersize=8, capsize=3)
# ax.errorbar(time[0:6],meanshear1600topp,yerr=stdshear1600topp,fmt='-o', color=color5, markersize=8, capsize=3)
# ax.errorbar(time[0:4],meanshear4000topp,yerr=stdshear4000topp,fmt='-s', color=color5, markersize=8, capsize=3)
# ax.errorbar(time[0:6],meanshear800topf,yerr=stdshear800topf,fmt='--^', color=color4, markersize=8, capsize=3)
# ax.errorbar(time[0:6],meanshear1600topf,yerr=stdshear1600topf,fmt='--o', color=color4, markersize=8, capsize=3)
# ax.errorbar(time[0:4],meanshear4000topf,yerr=stdshear4000topf,fmt='--s', color=color4, markersize=8, capsize=3)

# ax.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average shear rate on top part', fontsize=fontsize)
# # plt.title('Average shear rate on top part', fontsize=fontsize, y=1.2)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# marker800 = mlines.Line2D([], [], color='k', marker='^', linestyle='None', markersize=8, label='800 $1/s$')
# marker1600 = mlines.Line2D([], [], color='k', marker='o', linestyle='None', markersize=8, label='1600 $1/s$')
# marker4000 = mlines.Line2D([], [], color='k', marker='s', linestyle='None', markersize=8, label='4000 $1/s$')
# linetop13 = mlines.Line2D([], [], color=color5, marker='None', linestyle='-', linewidth=2, label='top 1/3')
# linetop2 = mlines.Line2D([], [], color=color4, marker='None', linestyle='--', linewidth=2, label='top 2 $\mu m$')

# # ax.legend(
# #     handles=[marker800, linetop13, marker1600, linetop2, marker4000],
# #     loc="lower center", # "upper center" puts it below the line
# #     ncol=3,
# #     bbox_to_anchor=(0.5, 0.88),
# #     bbox_transform=fig.transFigure,
# #     fontsize=12
# # );

# plt.grid(alpha=0.3)

# plt.savefig('shearT.png',bbox_inches='tight')
# plt.show()


# ### shear rate top zoom in
# fig, ax = plt.subplots()
# ax.errorbar(time[0:6],meanshear800topp,yerr=stdshear800topp,fmt='-^', color=color5, linewidth=3, markersize=12, capsize=6)
# ax.errorbar(time[0:6],meanshear1600topp,yerr=stdshear1600topp,fmt='-o', color=color5, linewidth=3, markersize=12, capsize=6)
# ax.errorbar(time[0:6],meanshear800topf,yerr=stdshear800topf,fmt='--^', color=color4, linewidth=3, markersize=12, capsize=6)
# ax.errorbar(time[0:6],meanshear1600topf,yerr=stdshear1600topf,fmt='--o', color=color4, linewidth=3, markersize=12, capsize=6)

# ax.set_ylim(500,2000)

# plt.xticks(np.arange(2,13,2))
# ax.tick_params(axis='x', labelsize= ticksizeZoom)
# ax.tick_params(axis='y', labelsize= ticksizeZoom)

# plt.grid(alpha=0.3)

# plt.savefig('shearT_zoom.png',bbox_inches='tight')
# plt.show()


# ### Rate of elongation top
# fig, ax = plt.subplots()
# ax.errorbar(time[0:6],meanelon800topp,yerr=stdelon800topp,fmt='-^', color=color5, markersize=8, capsize=3)
# ax.errorbar(time[0:6],meanelon1600topp,yerr=stdelon1600topp,fmt='-o', color=color5, markersize=8, capsize=3)
# ax.errorbar(time[0:4],meanelon4000topp,yerr=stdelon4000topp,fmt='-s', color=color5, markersize=8, capsize=3)
# ax.errorbar(time[0:6],meanelon800topf,yerr=stdelon800topf,fmt='--^', color=color4, markersize=8, capsize=3)
# ax.errorbar(time[0:6],meanelon1600topf,yerr=stdelon1600topf,fmt='--o', color=color4, markersize=8, capsize=3)
# ax.errorbar(time[0:4],meanelon4000topf,yerr=stdelon4000topf,fmt='--s', color=color4, markersize=8, capsize=3)

# ax.set_ylabel('rate of elongation $[1/s]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average rate of elongation on top part', fontsize=fontsize)
# # plt.title('Average rate of elongation on top part', fontsize=fontsize, y=1.2)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# marker800 = mlines.Line2D([], [], color='k', marker='^', linestyle='None', markersize=8, label='800 $1/s$')
# marker1600 = mlines.Line2D([], [], color='k', marker='o', linestyle='None', markersize=8, label='1600 $1/s$')
# marker4000 = mlines.Line2D([], [], color='k', marker='s', linestyle='None', markersize=8, label='4000 $1/s$')
# linetop13 = mlines.Line2D([], [], color=color5, marker='None', linestyle='-', linewidth=2, label='top 1/3')
# linetop2 = mlines.Line2D([], [], color=color4, marker='None', linestyle='--', linewidth=2, label='top 2 $\mu m$')

# # ax.legend(
# #     handles=[marker800, linetop13, marker1600, linetop2, marker4000],
# #     loc="lower center", # "upper center" puts it below the line
# #     ncol=3,
# #     bbox_to_anchor=(0.5, 0.88),
# #     bbox_transform=fig.transFigure,
# #     fontsize=12
# # );

# plt.grid(alpha=0.3)

# plt.savefig('elonT.png',bbox_inches='tight')
# plt.show()


# ### rate of elongation top zoom in
# fig, ax = plt.subplots()
# ax.errorbar(time[0:6],meanelon800topp,yerr=stdelon800topp,fmt='-^', color=color5, linewidth=3, markersize=12, capsize=6)
# ax.errorbar(time[0:6],meanelon1600topp,yerr=stdelon1600topp,fmt='-o', color=color5, linewidth=3, markersize=12, capsize=6)
# ax.errorbar(time[0:6],meanelon800topf,yerr=stdelon800topf,fmt='--^', color=color4, linewidth=3, markersize=12, capsize=6)
# ax.errorbar(time[0:6],meanelon1600topf,yerr=stdelon1600topf,fmt='--o', color=color4, linewidth=3, markersize=12, capsize=6)

# # ax.set_ylim(0,5)

# plt.xticks(np.arange(2,13,2))
# ax.tick_params(axis='x', labelsize= ticksizeZoom)
# ax.tick_params(axis='y', labelsize= ticksizeZoom)

# plt.grid(alpha=0.3)

# plt.savefig('elonT_zoom.png',bbox_inches='tight')
# plt.show()




### Shear rate surface
fig, ax = plt.subplots()
ax.plot(time[0:6],meanshear800surface,'--^', color=color1, markersize=8, label='800 1/s')
ax.fill_between(time[0:6],meanshear800surface-stdshear800surface, meanshear800surface+stdshear800surface, color=color1, alpha=0.2)
ax.plot(time[0:6],meanshear1600surface,'--o', color=color2, markersize=8, label='1600 1/s')
ax.fill_between(time[0:6],meanshear1600surface-stdshear1600surface, meanshear1600surface+stdshear1600surface, color=color2, alpha=0.2)
ax.plot(time[0:4],meanshear4000surface,'--s', color=color3, markersize=8, label='4000 1/s')
ax.fill_between(time[0:4],meanshear4000surface-stdshear4000surface, meanshear4000surface+stdshear4000surface, color=color3, alpha=0.2)
# ax.errorbar(time[0:6],meanshear800surface,yerr=stdshear800surface,fmt='--o', color=color1, markersize=6, capsize=3, label='800 1/s')
# ax.errorbar(time[0:6],meanshear1600surface,yerr=stdshear1600surface,fmt='--o', color=color2, markersize=6, capsize=3, label='1600 1/s')
# ax.errorbar(time[0:4],meanshear4000surface,yerr=stdshear4000surface,fmt='--o', color=color3, markersize=6, capsize=3, label='4000 1/s')

ax.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average shear rate on surface', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('shearS.png',bbox_inches='tight')
plt.show()


## rate of elongation surface
fig, ax = plt.subplots()
ax.plot(time[0:6],meanelon800surface,'--^', color=color1, markersize=8, label='800 1/s')
ax.fill_between(time[0:6],meanelon800surface-stdelon800surface, meanelon800surface+stdelon800surface, color=color1, alpha=0.2)
ax.plot(time[0:6],meanelon1600surface,'--o', color=color2, markersize=8, label='1600 1/s')
ax.fill_between(time[0:6],meanelon1600surface-stdelon1600surface, meanelon1600surface+stdelon1600surface, color=color2, alpha=0.2)
ax.plot(time[0:4],meanelon4000surface,'--s', color=color3, markersize=8, label='4000 1/s')
ax.fill_between(time[0:4],meanelon4000surface-stdelon4000surface, meanelon4000surface+stdelon4000surface, color=color3, alpha=0.2)
# ax.errorbar(time[0:6],meanelon800surface,yerr=stdelon800surface,fmt='--o', color=color1, ecolor='k', markersize=6, capsize=3, label='800 1/s')
# ax.errorbar(time[0:6],meanelon1600surface,yerr=stdelon1600surface,fmt='--o', color=color2, ecolor='k', markersize=6, capsize=3, label='1600 1/s')
# ax.errorbar(time[0:4],meanelon4000surface,yerr=stdelon4000surface,fmt='--o', color=color3, ecolor='k', markersize=6, capsize=3, label='4000 1/s')

ax.set_ylabel('rate of elongation $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average rate of elongation on surface', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('elonS.png',bbox_inches='tight')
plt.show()



### Normalised result surface
fig, ax = plt.subplots()
ax.plot(time[0:6],meanelon800surface/meanelon800surface[0]*100,'-^', color=color5, markersize=8)
ax.plot(time[0:6],meanelon1600surface/meanelon1600surface[0]*100,'-o', color=color5, markersize=8)
ax.plot(time[0:4],meanelon4000surface/meanelon4000surface[0]*100,'-s', color=color5, markersize=8)
ax.plot(time[0:6],meanshear800surface/meanshear800surface[0]*100,'--^', color=color4, markersize=8)
ax.plot(time[0:6],meanshear1600surface/meanshear1600surface[0]*100,'--o', color=color4, markersize=8)
ax.plot(time[0:4],meanshear4000surface/meanshear4000surface[0]*100,'--s', color=color4, markersize=8)


ax.set_ylabel('percentage $[\%]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Normalised average results', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

marker800 = mlines.Line2D([], [], color='k', marker='^', linestyle='None', markersize=8, label='800 $1/s$')
marker1600 = mlines.Line2D([], [], color='k', marker='o', linestyle='None', markersize=8, label='1600 $1/s$')
marker4000 = mlines.Line2D([], [], color='k', marker='s', linestyle='None', markersize=8, label='4000 $1/s$')
lineElon = mlines.Line2D([], [], color=color5, marker='None', linestyle='-', linewidth=2, label='shear rate')
lineShear = mlines.Line2D([], [], color=color4, marker='None', linestyle='--', linewidth=2, label='rate of elongation')

ax.legend(
    handles=[marker800, marker1600, marker4000, lineElon, lineShear],
    loc=1, # "upper center" puts it below the line
    ncol=1,
    fontsize=12
);

plt.grid(alpha=0.3)

plt.savefig('normalS.png',bbox_inches='tight')
plt.show()

####-----------------------------not used---------------------------------####
## PointZ -- height
# meanH800face = np.array([np.mean([np.mean(data[0][0][4],axis=0)[0],np.mean(data[3][0][4],axis=0)[0],np.mean(data[10][0][4],axis=0)[0],\
#                                     np.mean(data[13][0][4],axis=0)[0],np.mean(data[14][0][4],axis=0)[0],np.mean(data[15][0][4],axis=0)[0],np.mean(data[16][0][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][1][4],axis=0)[0],np.mean(data[3][1][4],axis=0)[0],np.mean(data[10][1][4],axis=0)[0],\
#                                     np.mean(data[13][1][4],axis=0)[0],np.mean(data[14][1][4],axis=0)[0],np.mean(data[15][1][4],axis=0)[0],np.mean(data[16][1][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][2][4],axis=0)[0],np.mean(data[3][2][4],axis=0)[0],np.mean(data[10][2][4],axis=0)[0],\
#                                     np.mean(data[13][2][4],axis=0)[0],np.mean(data[14][2][4],axis=0)[0],np.mean(data[15][2][4],axis=0)[0],np.mean(data[16][2][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][3][4],axis=0)[0],np.mean(data[3][3][4],axis=0)[0],np.mean(data[10][3][4],axis=0)[0],\
#                                     np.mean(data[13][3][4],axis=0)[0],np.mean(data[14][3][4],axis=0)[0],np.mean(data[15][3][4],axis=0)[0],np.mean(data[16][3][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][4][4],axis=0)[0],np.mean(data[3][4][4],axis=0)[0],np.mean(data[10][4][4],axis=0)[0],\
#                                     np.mean(data[13][4][4],axis=0)[0],np.mean(data[14][4][4],axis=0)[0],np.mean(data[15][4][4],axis=0)[0],np.mean(data[16][4][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][5][4],axis=0)[0],np.mean(data[3][5][4],axis=0)[0],np.mean(data[10][5][4],axis=0)[0],\
#                                     np.mean(data[13][5][4],axis=0)[0],np.mean(data[14][5][4],axis=0)[0],np.mean(data[15][5][4],axis=0)[0],np.mean(data[16][5][4],axis=0)[0]])])
# meanH1600face = np.array([np.mean([np.mean(data[2][0][4],axis=0)[0],np.mean(data[4][0][4],axis=0)[0],np.mean(data[6][0][4],axis=0)[0],\
#                                  np.mean(data[8][0][4],axis=0)[0],np.mean(data[11][0][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][1][4],axis=0)[0],np.mean(data[4][1][4],axis=0)[0],np.mean(data[6][1][4],axis=0)[0],\
#                                  np.mean(data[8][1][4],axis=0)[0],np.mean(data[11][1][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][2][4],axis=0)[0],np.mean(data[4][2][4],axis=0)[0],np.mean(data[6][2][4],axis=0)[0],\
#                                  np.mean(data[8][2][4],axis=0)[0],np.mean(data[11][2][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][3][4],axis=0)[0],np.mean(data[4][3][4],axis=0)[0],np.mean(data[6][3][4],axis=0)[0],\
#                                  np.mean(data[8][3][4],axis=0)[0],np.mean(data[11][3][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][4][4],axis=0)[0],np.mean(data[4][4][4],axis=0)[0],np.mean(data[6][4][4],axis=0)[0],\
#                                  np.mean(data[8][4][4],axis=0)[0],np.mean(data[11][4][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][5][4],axis=0)[0],np.mean(data[4][5][4],axis=0)[0],np.mean(data[6][5][4],axis=0)[0],\
#                                  np.mean(data[8][5][4],axis=0)[0],np.mean(data[11][5][4],axis=0)[0]])])
# meanH4000face = np.array([np.mean([np.mean(data[5][0][4],axis=0)[0],np.mean(data[9][0][4],axis=0)[0],np.mean(data[12][0][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][1][4],axis=0)[0],np.mean(data[9][1][4],axis=0)[0],np.mean(data[12][1][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][2][4],axis=0)[0],np.mean(data[9][2][4],axis=0)[0],np.mean(data[12][2][4],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][3][4],axis=0)[0],np.mean(data[9][3][4],axis=0)[0],np.mean(data[12][3][4],axis=0)[0]])])

# stdH800face = np.array([np.std([np.mean(data[0][0][4],axis=0)[0],np.mean(data[3][0][4],axis=0)[0],np.mean(data[10][0][4],axis=0)[0],\
#                                     np.mean(data[13][0][4],axis=0)[0],np.mean(data[14][0][4],axis=0)[0],np.mean(data[15][0][4],axis=0)[0],np.mean(data[16][0][4],axis=0)[0]]),\
#                        np.std([np.mean(data[0][1][4],axis=0)[0],np.mean(data[3][1][4],axis=0)[0],np.mean(data[10][1][4],axis=0)[0],\
#                                     np.mean(data[13][1][4],axis=0)[0],np.mean(data[14][1][4],axis=0)[0],np.mean(data[15][1][4],axis=0)[0],np.mean(data[16][1][4],axis=0)[0]]),\
#                        np.std([np.mean(data[0][2][4],axis=0)[0],np.mean(data[3][2][4],axis=0)[0],np.mean(data[10][2][4],axis=0)[0],\
#                                     np.mean(data[13][2][4],axis=0)[0],np.mean(data[14][2][4],axis=0)[0],np.mean(data[15][2][4],axis=0)[0],np.mean(data[16][2][4],axis=0)[0]]),\
#                        np.std([np.mean(data[0][3][4],axis=0)[0],np.mean(data[3][3][4],axis=0)[0],np.mean(data[10][3][4],axis=0)[0],\
#                                     np.mean(data[13][3][4],axis=0)[0],np.mean(data[14][3][4],axis=0)[0],np.mean(data[15][3][4],axis=0)[0],np.mean(data[16][3][4],axis=0)[0]]),\
#                        np.std([np.mean(data[0][4][4],axis=0)[0],np.mean(data[3][4][4],axis=0)[0],np.mean(data[10][4][4],axis=0)[0],\
#                                     np.mean(data[13][4][4],axis=0)[0],np.mean(data[14][4][4],axis=0)[0],np.mean(data[15][4][4],axis=0)[0],np.mean(data[16][4][4],axis=0)[0]]),\
#                        np.std([np.mean(data[0][5][4],axis=0)[0],np.mean(data[3][5][4],axis=0)[0],np.mean(data[10][5][4],axis=0)[0],\
#                                     np.mean(data[13][5][4],axis=0)[0],np.mean(data[14][5][4],axis=0)[0],np.mean(data[15][5][4],axis=0)[0],np.mean(data[16][5][4],axis=0)[0]])])
# stdH1600face = np.array([np.std([np.mean(data[2][0][4],axis=0)[0],np.mean(data[4][0][4],axis=0)[0],np.mean(data[6][0][4],axis=0)[0],\
#                                  np.mean(data[8][0][4],axis=0)[0],np.mean(data[11][0][4],axis=0)[0]]),\
#                        np.std([np.mean(data[2][1][4],axis=0)[0],np.mean(data[4][1][4],axis=0)[0],np.mean(data[6][1][4],axis=0)[0],\
#                                  np.mean(data[8][1][4],axis=0)[0],np.mean(data[11][1][4],axis=0)[0]]),\
#                        np.std([np.mean(data[2][2][4],axis=0)[0],np.mean(data[4][2][4],axis=0)[0],np.mean(data[6][2][4],axis=0)[0],\
#                                  np.mean(data[8][2][4],axis=0)[0],np.mean(data[11][2][4],axis=0)[0]]),\
#                        np.std([np.mean(data[2][3][4],axis=0)[0],np.mean(data[4][3][4],axis=0)[0],np.mean(data[6][3][4],axis=0)[0],\
#                                  np.mean(data[8][3][4],axis=0)[0],np.mean(data[11][3][4],axis=0)[0]]),\
#                        np.std([np.mean(data[2][4][4],axis=0)[0],np.mean(data[4][4][4],axis=0)[0],np.mean(data[6][4][4],axis=0)[0],\
#                                  np.mean(data[8][4][4],axis=0)[0],np.mean(data[11][4][4],axis=0)[0]]),\
#                        np.std([np.mean(data[2][5][4],axis=0)[0],np.mean(data[4][5][4],axis=0)[0],np.mean(data[6][5][4],axis=0)[0],\
#                                  np.mean(data[8][5][4],axis=0)[0],np.mean(data[11][5][4],axis=0)[0]])])
# stdH4000face = np.array([np.std([np.mean(data[5][0][4],axis=0)[0],np.mean(data[9][0][4],axis=0)[0],np.mean(data[12][0][4],axis=0)[0]]),\
#                        np.std([np.mean(data[5][1][4],axis=0)[0],np.mean(data[9][1][4],axis=0)[0],np.mean(data[12][1][4],axis=0)[0]]),\
#                        np.std([np.mean(data[5][2][4],axis=0)[0],np.mean(data[9][2][4],axis=0)[0],np.mean(data[12][2][4],axis=0)[0]]),\
#                        np.std([np.mean(data[5][3][4],axis=0)[0],np.mean(data[9][3][4],axis=0)[0],np.mean(data[12][3][4],axis=0)[0]])])

# meanH800back = np.array([np.mean([np.mean(data[0][0][5],axis=0)[0],np.mean(data[3][0][5],axis=0)[0],np.mean(data[10][0][5],axis=0)[0],\
#                                     np.mean(data[13][0][5],axis=0)[0],np.mean(data[14][0][5],axis=0)[0],np.mean(data[15][0][5],axis=0)[0],np.mean(data[16][0][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][1][5],axis=0)[0],np.mean(data[3][1][5],axis=0)[0],np.mean(data[10][1][5],axis=0)[0],\
#                                     np.mean(data[13][1][5],axis=0)[0],np.mean(data[14][1][5],axis=0)[0],np.mean(data[15][1][5],axis=0)[0],np.mean(data[16][1][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][2][5],axis=0)[0],np.mean(data[3][2][5],axis=0)[0],np.mean(data[10][2][5],axis=0)[0],\
#                                     np.mean(data[13][2][5],axis=0)[0],np.mean(data[14][2][5],axis=0)[0],np.mean(data[15][2][5],axis=0)[0],np.mean(data[16][2][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][3][5],axis=0)[0],np.mean(data[3][3][5],axis=0)[0],np.mean(data[10][3][5],axis=0)[0],\
#                                     np.mean(data[13][3][5],axis=0)[0],np.mean(data[14][3][5],axis=0)[0],np.mean(data[15][3][5],axis=0)[0],np.mean(data[16][3][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][4][5],axis=0)[0],np.mean(data[3][4][5],axis=0)[0],np.mean(data[10][4][5],axis=0)[0],\
#                                     np.mean(data[13][4][5],axis=0)[0],np.mean(data[14][4][5],axis=0)[0],np.mean(data[15][4][5],axis=0)[0],np.mean(data[16][4][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][5][5],axis=0)[0],np.mean(data[3][5][5],axis=0)[0],np.mean(data[10][5][5],axis=0)[0],\
#                                     np.mean(data[13][5][5],axis=0)[0],np.mean(data[14][5][5],axis=0)[0],np.mean(data[15][5][5],axis=0)[0],np.mean(data[16][5][5],axis=0)[0]])])
# meanH1600back = np.array([np.mean([np.mean(data[2][0][5],axis=0)[0],np.mean(data[4][0][5],axis=0)[0],np.mean(data[6][0][5],axis=0)[0],\
#                                  np.mean(data[8][0][5],axis=0)[0],np.mean(data[11][0][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][1][5],axis=0)[0],np.mean(data[4][1][5],axis=0)[0],np.mean(data[6][1][5],axis=0)[0],\
#                                  np.mean(data[8][1][5],axis=0)[0],np.mean(data[11][1][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][2][5],axis=0)[0],np.mean(data[4][2][5],axis=0)[0],np.mean(data[6][2][5],axis=0)[0],\
#                                  np.mean(data[8][2][5],axis=0)[0],np.mean(data[11][2][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][3][5],axis=0)[0],np.mean(data[4][3][5],axis=0)[0],np.mean(data[6][3][5],axis=0)[0],\
#                                  np.mean(data[8][3][5],axis=0)[0],np.mean(data[11][3][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][4][5],axis=0)[0],np.mean(data[4][4][5],axis=0)[0],np.mean(data[6][4][5],axis=0)[0],\
#                                  np.mean(data[8][4][5],axis=0)[0],np.mean(data[11][4][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][5][5],axis=0)[0],np.mean(data[4][5][5],axis=0)[0],np.mean(data[6][5][5],axis=0)[0],\
#                                  np.mean(data[8][5][5],axis=0)[0],np.mean(data[11][5][5],axis=0)[0]])])
# meanH4000back = np.array([np.mean([np.mean(data[5][0][5],axis=0)[0],np.mean(data[9][0][5],axis=0)[0],np.mean(data[12][0][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][1][5],axis=0)[0],np.mean(data[9][1][5],axis=0)[0],np.mean(data[12][1][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][2][5],axis=0)[0],np.mean(data[9][2][5],axis=0)[0],np.mean(data[12][2][5],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][3][5],axis=0)[0],np.mean(data[9][3][5],axis=0)[0],np.mean(data[12][3][5],axis=0)[0]])])

# stdH800back = np.array([np.std([np.mean(data[0][0][5],axis=0)[0],np.mean(data[3][0][5],axis=0)[0],np.mean(data[10][0][5],axis=0)[0],\
#                                     np.mean(data[13][0][5],axis=0)[0],np.mean(data[14][0][5],axis=0)[0],np.mean(data[15][0][5],axis=0)[0],np.mean(data[16][0][5],axis=0)[0]]),\
#                        np.std([np.mean(data[0][1][5],axis=0)[0],np.mean(data[3][1][5],axis=0)[0],np.mean(data[10][1][5],axis=0)[0],\
#                                     np.mean(data[13][1][5],axis=0)[0],np.mean(data[14][1][5],axis=0)[0],np.mean(data[15][1][5],axis=0)[0],np.mean(data[16][1][5],axis=0)[0]]),\
#                        np.std([np.mean(data[0][2][5],axis=0)[0],np.mean(data[3][2][5],axis=0)[0],np.mean(data[10][2][5],axis=0)[0],\
#                                     np.mean(data[13][2][5],axis=0)[0],np.mean(data[14][2][5],axis=0)[0],np.mean(data[15][2][5],axis=0)[0],np.mean(data[16][2][5],axis=0)[0]]),\
#                        np.std([np.mean(data[0][3][5],axis=0)[0],np.mean(data[3][3][5],axis=0)[0],np.mean(data[10][3][5],axis=0)[0],\
#                                     np.mean(data[13][3][5],axis=0)[0],np.mean(data[14][3][5],axis=0)[0],np.mean(data[15][3][5],axis=0)[0],np.mean(data[16][3][5],axis=0)[0]]),\
#                        np.std([np.mean(data[0][4][5],axis=0)[0],np.mean(data[3][4][5],axis=0)[0],np.mean(data[10][4][5],axis=0)[0],\
#                                     np.mean(data[13][4][5],axis=0)[0],np.mean(data[14][4][5],axis=0)[0],np.mean(data[15][4][5],axis=0)[0],np.mean(data[16][4][5],axis=0)[0]]),\
#                        np.std([np.mean(data[0][5][5],axis=0)[0],np.mean(data[3][5][5],axis=0)[0],np.mean(data[10][5][5],axis=0)[0],\
#                                     np.mean(data[13][5][5],axis=0)[0],np.mean(data[14][5][5],axis=0)[0],np.mean(data[15][5][5],axis=0)[0],np.mean(data[16][5][5],axis=0)[0]])])
# stdH1600back = np.array([np.std([np.mean(data[2][0][5],axis=0)[0],np.mean(data[4][0][5],axis=0)[0],np.mean(data[6][0][5],axis=0)[0],\
#                                  np.mean(data[8][0][5],axis=0)[0],np.mean(data[11][0][5],axis=0)[0]]),\
#                        np.std([np.mean(data[2][1][5],axis=0)[0],np.mean(data[4][1][5],axis=0)[0],np.mean(data[6][1][5],axis=0)[0],\
#                                  np.mean(data[8][1][5],axis=0)[0],np.mean(data[11][1][5],axis=0)[0]]),\
#                        np.std([np.mean(data[2][2][5],axis=0)[0],np.mean(data[4][2][5],axis=0)[0],np.mean(data[6][2][5],axis=0)[0],\
#                                  np.mean(data[8][2][5],axis=0)[0],np.mean(data[11][2][5],axis=0)[0]]),\
#                        np.std([np.mean(data[2][3][5],axis=0)[0],np.mean(data[4][3][5],axis=0)[0],np.mean(data[6][3][5],axis=0)[0],\
#                                  np.mean(data[8][3][5],axis=0)[0],np.mean(data[11][3][5],axis=0)[0]]),\
#                        np.std([np.mean(data[2][4][5],axis=0)[0],np.mean(data[4][4][5],axis=0)[0],np.mean(data[6][4][5],axis=0)[0],\
#                                  np.mean(data[8][4][5],axis=0)[0],np.mean(data[11][4][5],axis=0)[0]]),\
#                        np.std([np.mean(data[2][5][5],axis=0)[0],np.mean(data[4][5][5],axis=0)[0],np.mean(data[6][5][5],axis=0)[0],\
#                                  np.mean(data[8][5][5],axis=0)[0],np.mean(data[11][5][5],axis=0)[0]])])
# stdH4000back = np.array([np.std([np.mean(data[5][0][5],axis=0)[0],np.mean(data[9][0][5],axis=0)[0],np.mean(data[12][0][5],axis=0)[0]]),\
#                        np.std([np.mean(data[5][1][5],axis=0)[0],np.mean(data[9][1][5],axis=0)[0],np.mean(data[12][1][5],axis=0)[0]]),\
#                        np.std([np.mean(data[5][2][5],axis=0)[0],np.mean(data[9][2][5],axis=0)[0],np.mean(data[12][2][5],axis=0)[0]]),\
#                        np.std([np.mean(data[5][3][5],axis=0)[0],np.mean(data[9][3][5],axis=0)[0],np.mean(data[12][3][5],axis=0)[0]])])

# meanH800surface = np.array([np.mean([np.mean(data[0][0][1],axis=0)[0],np.mean(data[3][0][1],axis=0)[0],np.mean(data[10][0][1],axis=0)[0],\
#                                     np.mean(data[13][0][1],axis=0)[0],np.mean(data[14][0][1],axis=0)[0],np.mean(data[15][0][1],axis=0)[0],np.mean(data[16][0][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][1][1],axis=0)[0],np.mean(data[3][1][1],axis=0)[0],np.mean(data[10][1][1],axis=0)[0],\
#                                     np.mean(data[13][1][1],axis=0)[0],np.mean(data[14][1][1],axis=0)[0],np.mean(data[15][1][1],axis=0)[0],np.mean(data[16][1][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][2][1],axis=0)[0],np.mean(data[3][2][1],axis=0)[0],np.mean(data[10][2][1],axis=0)[0],\
#                                     np.mean(data[13][2][1],axis=0)[0],np.mean(data[14][2][1],axis=0)[0],np.mean(data[15][2][1],axis=0)[0],np.mean(data[16][2][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][3][1],axis=0)[0],np.mean(data[3][3][1],axis=0)[0],np.mean(data[10][3][1],axis=0)[0],\
#                                     np.mean(data[13][3][1],axis=0)[0],np.mean(data[14][3][1],axis=0)[0],np.mean(data[15][3][1],axis=0)[0],np.mean(data[16][3][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][4][1],axis=0)[0],np.mean(data[3][4][1],axis=0)[0],np.mean(data[10][4][1],axis=0)[0],\
#                                     np.mean(data[13][4][1],axis=0)[0],np.mean(data[14][4][1],axis=0)[0],np.mean(data[15][4][1],axis=0)[0],np.mean(data[16][4][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[0][5][1],axis=0)[0],np.mean(data[3][5][1],axis=0)[0],np.mean(data[10][5][1],axis=0)[0],\
#                                     np.mean(data[13][5][1],axis=0)[0],np.mean(data[14][5][1],axis=0)[0],np.mean(data[15][5][1],axis=0)[0],np.mean(data[16][5][1],axis=0)[0]])])
# meanH1600surface = np.array([np.mean([np.mean(data[2][0][1],axis=0)[0],np.mean(data[4][0][1],axis=0)[0],np.mean(data[6][0][1],axis=0)[0],\
#                                  np.mean(data[8][0][1],axis=0)[0],np.mean(data[11][0][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][1][1],axis=0)[0],np.mean(data[4][1][1],axis=0)[0],np.mean(data[6][1][1],axis=0)[0],\
#                                  np.mean(data[8][1][1],axis=0)[0],np.mean(data[11][1][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][2][1],axis=0)[0],np.mean(data[4][2][1],axis=0)[0],np.mean(data[6][2][1],axis=0)[0],\
#                                  np.mean(data[8][2][1],axis=0)[0],np.mean(data[11][2][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][3][1],axis=0)[0],np.mean(data[4][3][1],axis=0)[0],np.mean(data[6][3][1],axis=0)[0],\
#                                  np.mean(data[8][3][1],axis=0)[0],np.mean(data[11][3][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][4][1],axis=0)[0],np.mean(data[4][4][1],axis=0)[0],np.mean(data[6][4][1],axis=0)[0],\
#                                  np.mean(data[8][4][1],axis=0)[0],np.mean(data[11][4][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[2][5][1],axis=0)[0],np.mean(data[4][5][1],axis=0)[0],np.mean(data[6][5][1],axis=0)[0],\
#                                  np.mean(data[8][5][1],axis=0)[0],np.mean(data[11][5][1],axis=0)[0]])])
# meanH4000surface = np.array([np.mean([np.mean(data[5][0][1],axis=0)[0],np.mean(data[9][0][1],axis=0)[0],np.mean(data[12][0][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][1][1],axis=0)[0],np.mean(data[9][1][1],axis=0)[0],np.mean(data[12][1][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][2][1],axis=0)[0],np.mean(data[9][2][1],axis=0)[0],np.mean(data[12][2][1],axis=0)[0]]),\
#                        np.mean([np.mean(data[5][3][1],axis=0)[0],np.mean(data[9][3][1],axis=0)[0],np.mean(data[12][3][1],axis=0)[0]])])

# stdH800surface = np.array([np.std([np.mean(data[0][0][1],axis=0)[0],np.mean(data[3][0][1],axis=0)[0],np.mean(data[10][0][1],axis=0)[0],\
#                                     np.mean(data[13][0][1],axis=0)[0],np.mean(data[14][0][1],axis=0)[0],np.mean(data[15][0][1],axis=0)[0],np.mean(data[16][0][1],axis=0)[0]]),\
#                        np.std([np.mean(data[0][1][1],axis=0)[0],np.mean(data[3][1][1],axis=0)[0],np.mean(data[10][1][1],axis=0)[0],\
#                                     np.mean(data[13][1][1],axis=0)[0],np.mean(data[14][1][1],axis=0)[0],np.mean(data[15][1][1],axis=0)[0],np.mean(data[16][1][1],axis=0)[0]]),\
#                        np.std([np.mean(data[0][2][1],axis=0)[0],np.mean(data[3][2][1],axis=0)[0],np.mean(data[10][2][1],axis=0)[0],\
#                                     np.mean(data[13][2][1],axis=0)[0],np.mean(data[14][2][1],axis=0)[0],np.mean(data[15][2][1],axis=0)[0],np.mean(data[16][2][1],axis=0)[0]]),\
#                        np.std([np.mean(data[0][3][1],axis=0)[0],np.mean(data[3][3][1],axis=0)[0],np.mean(data[10][3][1],axis=0)[0],\
#                                     np.mean(data[13][3][1],axis=0)[0],np.mean(data[14][3][1],axis=0)[0],np.mean(data[15][3][1],axis=0)[0],np.mean(data[16][3][1],axis=0)[0]]),\
#                        np.std([np.mean(data[0][4][1],axis=0)[0],np.mean(data[3][4][1],axis=0)[0],np.mean(data[10][4][1],axis=0)[0],\
#                                     np.mean(data[13][4][1],axis=0)[0],np.mean(data[14][4][1],axis=0)[0],np.mean(data[15][4][1],axis=0)[0],np.mean(data[16][4][1],axis=0)[0]]),\
#                        np.std([np.mean(data[0][5][1],axis=0)[0],np.mean(data[3][5][1],axis=0)[0],np.mean(data[10][5][1],axis=0)[0],\
#                                     np.mean(data[13][5][1],axis=0)[0],np.mean(data[14][5][1],axis=0)[0],np.mean(data[15][5][1],axis=0)[0],np.mean(data[16][5][1],axis=0)[0]])])
# stdH1600surface = np.array([np.std([np.mean(data[2][0][1],axis=0)[0],np.mean(data[4][0][1],axis=0)[0],np.mean(data[6][0][1],axis=0)[0],\
#                                  np.mean(data[8][0][1],axis=0)[0],np.mean(data[11][0][1],axis=0)[0]]),\
#                        np.std([np.mean(data[2][1][1],axis=0)[0],np.mean(data[4][1][1],axis=0)[0],np.mean(data[6][1][1],axis=0)[0],\
#                                  np.mean(data[8][1][1],axis=0)[0],np.mean(data[11][1][1],axis=0)[0]]),\
#                        np.std([np.mean(data[2][2][1],axis=0)[0],np.mean(data[4][2][1],axis=0)[0],np.mean(data[6][2][1],axis=0)[0],\
#                                  np.mean(data[8][2][1],axis=0)[0],np.mean(data[11][2][1],axis=0)[0]]),\
#                        np.std([np.mean(data[2][3][1],axis=0)[0],np.mean(data[4][3][1],axis=0)[0],np.mean(data[6][3][1],axis=0)[0],\
#                                  np.mean(data[8][3][1],axis=0)[0],np.mean(data[11][3][1],axis=0)[0]]),\
#                        np.std([np.mean(data[2][4][1],axis=0)[0],np.mean(data[4][4][1],axis=0)[0],np.mean(data[6][4][1],axis=0)[0],\
#                                  np.mean(data[8][4][1],axis=0)[0],np.mean(data[11][4][1],axis=0)[0]]),\
#                        np.std([np.mean(data[2][5][1],axis=0)[0],np.mean(data[4][5][1],axis=0)[0],np.mean(data[6][5][1],axis=0)[0],\
#                                  np.mean(data[8][5][1],axis=0)[0],np.mean(data[11][5][1],axis=0)[0]])])
# stdH4000surface = np.array([np.std([np.mean(data[5][0][1],axis=0)[0],np.mean(data[9][0][1],axis=0)[0],np.mean(data[12][0][1],axis=0)[0]]),\
#                        np.std([np.mean(data[5][1][1],axis=0)[0],np.mean(data[9][1][1],axis=0)[0],np.mean(data[12][1][1],axis=0)[0]]),\
#                        np.std([np.mean(data[5][2][1],axis=0)[0],np.mean(data[9][2][1],axis=0)[0],np.mean(data[12][2][1],axis=0)[0]]),\
#                        np.std([np.mean(data[5][3][1],axis=0)[0],np.mean(data[9][3][1],axis=0)[0],np.mean(data[12][3][1],axis=0)[0]])])



# def align_yaxis(ax1, ax2):
#     y_lims = np.array([ax.get_ylim() for ax in [ax1, ax2]])

#     # force 0 to appear on both axes, comment if don't need
#     y_lims[:, 0] = y_lims[:, 0].clip(None, 0)
#     y_lims[:, 1] = y_lims[:, 1].clip(0, None)

#     # normalize both axes
#     y_mags = (y_lims[:,1] - y_lims[:,0]).reshape(len(y_lims),1)
#     y_lims_normalized = y_lims / y_mags

#     # find combined range
#     y_new_lims_normalized = np.array([np.min(y_lims_normalized), np.max(y_lims_normalized)])

#     # denormalize combined range to get new axes
#     new_lim1, new_lim2 = y_new_lims_normalized * y_mags
#     ax1.set_ylim(new_lim1)
#     ax2.set_ylim(new_lim2)
# ### Differences of average shear rate vs. height faceward/backward
# fig, ax1 = plt.subplots()

# ax2 = ax1.twinx()
# ax1.plot(time3[0:6],meanshear800face-meanshear800back,'--o', color=color1, markersize=6, label='800 1/s')
# ax1.plot(time3[0:6],meanshear1600face-meanshear1600back,'--o', color=color2, markersize=6, label='1600 1/s')
# ax1.plot(time3[0:4],meanshear4000face-meanshear4000back,'--o', color=color3, markersize=6, label='4000 1/s')
# ax2.bar(time3-width34,(meanH800face-meanH800back)*1e3, alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width34)
# ax2.bar(time3,(meanH1600face-meanH1600back)*1e3, alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width34)
# ax2.bar(time4+width34,(meanH4000face-meanH4000back)*1e3, alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width34)

# ax1.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
# ax2.set_ylabel('height $[\mu m]$',fontsize=fontsize)
# ax1.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Differences', fontsize=fontsize)

# # ax.set_xlim(3,12)
# # ax.set_ylim(0,)
# align_yaxis(ax1, ax2)

# plt.xticks(time, labels=labels)
# ax1.tick_params(axis='x', labelsize= ticksize)
# ax1.tick_params(axis='y', labelsize= ticksize)
# ax2.tick_params(axis='y', labelsize= ticksize)

# fig.legend(bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)
# plt.grid(alpha=0.3)

# plt.savefig('hDshearFB.png',bbox_inches='tight')
# plt.show()