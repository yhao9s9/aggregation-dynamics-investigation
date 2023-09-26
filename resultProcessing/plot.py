## Plot the redundant part as two aggregates

import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


dirt = ['d1_800/','d2_800/','d2_1600/','d3_800/','d3_1600/','d3_4000/','d4_1600/','d5_800/','d5_1600/','d5_4000/','d6_800/','d6_1600/','d6_4000/']
time = ['1min/','2min/','4min/','6min/','9min/','12min/']
name = ['volume','surface','faceward','backward','top']

data= []
for i in dirt:
    data_dirt = []
    for j in time:
        data_time = []
        for k in name:
            try:
                a = np.load(i+j+'npy/'+k+'.npy')
                data_time.append(a)
            except:
                data_time.append([])
        data_dirt.append(data_time)
    data.append(data_dirt)


name2 = ['1volume','1surface','1faceward','1backward','1top']
name3 = ['2volume','2surface','2faceward','2backward','2top']

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
## d1_800/4min/volume = data[0][2][0]
## d2_800/6min/2top = data[14][3][4] -> 2D array = num_node * [elongation, shear rate, shear stress, velocity]


# print(np.mean(data[14][4][3], axis=0)[0])

## Average elongational rate
meanelon800face = np.array([np.mean([np.mean(data[0][0][2],axis=0)[0],np.mean(data[3][0][2],axis=0)[0],np.mean(data[10][0][2],axis=0)[0],\
                                    np.mean(data[13][0][2],axis=0)[0],np.mean(data[14][0][2],axis=0)[0],np.mean(data[15][0][2],axis=0)[0],np.mean(data[16][0][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][1][2],axis=0)[0],np.mean(data[3][1][2],axis=0)[0],np.mean(data[10][1][2],axis=0)[0],\
                                    np.mean(data[13][1][2],axis=0)[0],np.mean(data[14][1][2],axis=0)[0],np.mean(data[15][1][2],axis=0)[0],np.mean(data[16][1][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][2][2],axis=0)[0],np.mean(data[3][2][2],axis=0)[0],np.mean(data[10][2][2],axis=0)[0],\
                                    np.mean(data[13][2][2],axis=0)[0],np.mean(data[14][2][2],axis=0)[0],np.mean(data[15][2][2],axis=0)[0],np.mean(data[16][2][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][3][2],axis=0)[0],np.mean(data[3][3][2],axis=0)[0],np.mean(data[10][3][2],axis=0)[0],\
                                    np.mean(data[13][3][2],axis=0)[0],np.mean(data[14][3][2],axis=0)[0],np.mean(data[15][3][2],axis=0)[0],np.mean(data[16][3][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][4][2],axis=0)[0],np.mean(data[3][4][2],axis=0)[0],np.mean(data[10][4][2],axis=0)[0],\
                                    np.mean(data[13][4][2],axis=0)[0],np.mean(data[14][4][2],axis=0)[0],np.mean(data[15][4][2],axis=0)[0],np.mean(data[16][4][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][5][2],axis=0)[0],np.mean(data[3][5][2],axis=0)[0],np.mean(data[10][5][2],axis=0)[0],\
                                    np.mean(data[13][5][2],axis=0)[0],np.mean(data[14][5][2],axis=0)[0],np.mean(data[15][5][2],axis=0)[0],np.mean(data[16][5][2],axis=0)[0]])])
meanelon1600face = np.array([np.mean([np.mean(data[2][0][2],axis=0)[0],np.mean(data[4][0][2],axis=0)[0],np.mean(data[6][0][2],axis=0)[0],\
                                 np.mean(data[8][0][2],axis=0)[0],np.mean(data[11][0][2],axis=0)[0]]),\
                       np.mean([np.mean(data[2][1][2],axis=0)[0],np.mean(data[4][1][2],axis=0)[0],np.mean(data[6][1][2],axis=0)[0],\
                                 np.mean(data[8][1][2],axis=0)[0],np.mean(data[11][1][2],axis=0)[0]]),\
                       np.mean([np.mean(data[2][2][2],axis=0)[0],np.mean(data[4][2][2],axis=0)[0],np.mean(data[6][2][2],axis=0)[0],\
                                 np.mean(data[8][2][2],axis=0)[0],np.mean(data[11][2][2],axis=0)[0]]),\
                       np.mean([np.mean(data[2][3][2],axis=0)[0],np.mean(data[4][3][2],axis=0)[0],np.mean(data[6][3][2],axis=0)[0],\
                                 np.mean(data[8][3][2],axis=0)[0],np.mean(data[11][3][2],axis=0)[0]]),\
                       np.mean([np.mean(data[2][4][2],axis=0)[0],np.mean(data[4][4][2],axis=0)[0],np.mean(data[6][4][2],axis=0)[0],\
                                 np.mean(data[8][4][2],axis=0)[0],np.mean(data[11][4][2],axis=0)[0]]),\
                       np.mean([np.mean(data[2][5][2],axis=0)[0],np.mean(data[4][5][2],axis=0)[0],np.mean(data[6][5][2],axis=0)[0],\
                                 np.mean(data[8][5][2],axis=0)[0],np.mean(data[11][5][2],axis=0)[0]])])
meanelon4000face = np.array([np.mean([np.mean(data[5][0][2],axis=0)[0],np.mean(data[9][0][2],axis=0)[0],np.mean(data[12][0][2],axis=0)[0]]),\
                       np.mean([np.mean(data[5][1][2],axis=0)[0],np.mean(data[9][1][2],axis=0)[0],np.mean(data[12][1][2],axis=0)[0]]),\
                       np.mean([np.mean(data[5][2][2],axis=0)[0],np.mean(data[9][2][2],axis=0)[0],np.mean(data[12][2][2],axis=0)[0]]),\
                       np.mean([np.mean(data[5][3][2],axis=0)[0],np.mean(data[9][3][2],axis=0)[0],np.mean(data[12][3][2],axis=0)[0]])])

stdelon800face = np.array([np.std([np.mean(data[0][0][2],axis=0)[0],np.mean(data[3][0][2],axis=0)[0],np.mean(data[10][0][2],axis=0)[0],\
                                    np.mean(data[13][0][2],axis=0)[0],np.mean(data[14][0][2],axis=0)[0],np.mean(data[15][0][2],axis=0)[0],np.mean(data[16][0][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][1][2],axis=0)[0],np.mean(data[3][1][2],axis=0)[0],np.mean(data[10][1][2],axis=0)[0],\
                                    np.mean(data[13][1][2],axis=0)[0],np.mean(data[14][1][2],axis=0)[0],np.mean(data[15][1][2],axis=0)[0],np.mean(data[16][1][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][2][2],axis=0)[0],np.mean(data[3][2][2],axis=0)[0],np.mean(data[10][2][2],axis=0)[0],\
                                    np.mean(data[13][2][2],axis=0)[0],np.mean(data[14][2][2],axis=0)[0],np.mean(data[15][2][2],axis=0)[0],np.mean(data[16][2][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][3][2],axis=0)[0],np.mean(data[3][3][2],axis=0)[0],np.mean(data[10][3][2],axis=0)[0],\
                                    np.mean(data[13][3][2],axis=0)[0],np.mean(data[14][3][2],axis=0)[0],np.mean(data[15][3][2],axis=0)[0],np.mean(data[16][3][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][4][2],axis=0)[0],np.mean(data[3][4][2],axis=0)[0],np.mean(data[10][4][2],axis=0)[0],\
                                    np.mean(data[13][4][2],axis=0)[0],np.mean(data[14][4][2],axis=0)[0],np.mean(data[15][4][2],axis=0)[0],np.mean(data[16][4][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][5][2],axis=0)[0],np.mean(data[3][5][2],axis=0)[0],np.mean(data[10][5][2],axis=0)[0],\
                                    np.mean(data[13][5][2],axis=0)[0],np.mean(data[14][5][2],axis=0)[0],np.mean(data[15][5][2],axis=0)[0],np.mean(data[16][5][2],axis=0)[0]])])
stdelon1600face = np.array([np.std([np.mean(data[2][0][2],axis=0)[0],np.mean(data[4][0][2],axis=0)[0],np.mean(data[6][0][2],axis=0)[0],\
                                 np.mean(data[8][0][2],axis=0)[0],np.mean(data[11][0][2],axis=0)[0]]),\
                       np.std([np.mean(data[2][1][2],axis=0)[0],np.mean(data[4][1][2],axis=0)[0],np.mean(data[6][1][2],axis=0)[0],\
                                 np.mean(data[8][1][2],axis=0)[0],np.mean(data[11][1][2],axis=0)[0]]),\
                       np.std([np.mean(data[2][2][2],axis=0)[0],np.mean(data[4][2][2],axis=0)[0],np.mean(data[6][2][2],axis=0)[0],\
                                 np.mean(data[8][2][2],axis=0)[0],np.mean(data[11][2][2],axis=0)[0]]),\
                       np.std([np.mean(data[2][3][2],axis=0)[0],np.mean(data[4][3][2],axis=0)[0],np.mean(data[6][3][2],axis=0)[0],\
                                 np.mean(data[8][3][2],axis=0)[0],np.mean(data[11][3][2],axis=0)[0]]),\
                       np.std([np.mean(data[2][4][2],axis=0)[0],np.mean(data[4][4][2],axis=0)[0],np.mean(data[6][4][2],axis=0)[0],\
                                 np.mean(data[8][4][2],axis=0)[0],np.mean(data[11][4][2],axis=0)[0]]),\
                       np.std([np.mean(data[2][5][2],axis=0)[0],np.mean(data[4][5][2],axis=0)[0],np.mean(data[6][5][2],axis=0)[0],\
                                 np.mean(data[8][5][2],axis=0)[0],np.mean(data[11][5][2],axis=0)[0]])])
stdelon4000face = np.array([np.std([np.mean(data[5][0][2],axis=0)[0],np.mean(data[9][0][2],axis=0)[0],np.mean(data[12][0][2],axis=0)[0]]),\
                       np.std([np.mean(data[5][1][2],axis=0)[0],np.mean(data[9][1][2],axis=0)[0],np.mean(data[12][1][2],axis=0)[0]]),\
                       np.std([np.mean(data[5][2][2],axis=0)[0],np.mean(data[9][2][2],axis=0)[0],np.mean(data[12][2][2],axis=0)[0]]),\
                       np.std([np.mean(data[5][3][2],axis=0)[0],np.mean(data[9][3][2],axis=0)[0],np.mean(data[12][3][2],axis=0)[0]])])

meanelon800back = np.array([np.mean([np.mean(data[0][0][3],axis=0)[0],np.mean(data[3][0][3],axis=0)[0],np.mean(data[10][0][3],axis=0)[0],\
                                    np.mean(data[13][0][3],axis=0)[0],np.mean(data[14][0][3],axis=0)[0],np.mean(data[15][0][3],axis=0)[0],np.mean(data[16][0][3],axis=0)[0]]),\
                       np.mean([np.mean(data[0][1][3],axis=0)[0],np.mean(data[3][1][3],axis=0)[0],np.mean(data[10][1][3],axis=0)[0],\
                                    np.mean(data[13][1][3],axis=0)[0],np.mean(data[14][1][3],axis=0)[0],np.mean(data[15][1][3],axis=0)[0],np.mean(data[16][1][3],axis=0)[0]]),\
                       np.mean([np.mean(data[0][2][3],axis=0)[0],np.mean(data[3][2][3],axis=0)[0],np.mean(data[10][2][3],axis=0)[0],\
                                    np.mean(data[13][2][3],axis=0)[0],np.mean(data[14][2][3],axis=0)[0],np.mean(data[15][2][3],axis=0)[0],np.mean(data[16][2][3],axis=0)[0]]),\
                       np.mean([np.mean(data[0][3][3],axis=0)[0],np.mean(data[3][3][3],axis=0)[0],np.mean(data[10][3][3],axis=0)[0],\
                                    np.mean(data[13][3][3],axis=0)[0],np.mean(data[14][3][3],axis=0)[0],np.mean(data[15][3][3],axis=0)[0],np.mean(data[16][3][3],axis=0)[0]]),\
                       np.mean([np.mean(data[0][4][3],axis=0)[0],np.mean(data[3][4][3],axis=0)[0],np.mean(data[10][4][3],axis=0)[0],\
                                    np.mean(data[13][4][3],axis=0)[0],np.mean(data[14][4][3],axis=0)[0],np.mean(data[15][4][3],axis=0)[0],np.mean(data[16][4][3],axis=0)[0]]),\
                       np.mean([np.mean(data[0][5][3],axis=0)[0],np.mean(data[3][5][3],axis=0)[0],np.mean(data[10][5][3],axis=0)[0],\
                                    np.mean(data[13][5][3],axis=0)[0],np.mean(data[14][5][3],axis=0)[0],np.mean(data[15][5][3],axis=0)[0],np.mean(data[16][5][3],axis=0)[0]])])
meanelon1600back = np.array([np.mean([np.mean(data[2][0][3],axis=0)[0],np.mean(data[4][0][3],axis=0)[0],np.mean(data[6][0][3],axis=0)[0],\
                                 np.mean(data[8][0][3],axis=0)[0],np.mean(data[11][0][3],axis=0)[0]]),\
                       np.mean([np.mean(data[2][1][3],axis=0)[0],np.mean(data[4][1][3],axis=0)[0],np.mean(data[6][1][3],axis=0)[0],\
                                 np.mean(data[8][1][3],axis=0)[0],np.mean(data[11][1][3],axis=0)[0]]),\
                       np.mean([np.mean(data[2][2][3],axis=0)[0],np.mean(data[4][2][3],axis=0)[0],np.mean(data[6][2][3],axis=0)[0],\
                                 np.mean(data[8][2][3],axis=0)[0],np.mean(data[11][2][3],axis=0)[0]]),\
                       np.mean([np.mean(data[2][3][3],axis=0)[0],np.mean(data[4][3][3],axis=0)[0],np.mean(data[6][3][3],axis=0)[0],\
                                 np.mean(data[8][3][3],axis=0)[0],np.mean(data[11][3][3],axis=0)[0]]),\
                       np.mean([np.mean(data[2][4][3],axis=0)[0],np.mean(data[4][4][3],axis=0)[0],np.mean(data[6][4][3],axis=0)[0],\
                                 np.mean(data[8][4][3],axis=0)[0],np.mean(data[11][4][3],axis=0)[0]]),\
                       np.mean([np.mean(data[2][5][3],axis=0)[0],np.mean(data[4][5][3],axis=0)[0],np.mean(data[6][5][3],axis=0)[0],\
                                 np.mean(data[8][5][3],axis=0)[0],np.mean(data[11][5][3],axis=0)[0]])])
meanelon4000back = np.array([np.mean([np.mean(data[5][0][3],axis=0)[0],np.mean(data[9][0][3],axis=0)[0],np.mean(data[12][0][3],axis=0)[0]]),\
                       np.mean([np.mean(data[5][1][3],axis=0)[0],np.mean(data[9][1][3],axis=0)[0],np.mean(data[12][1][3],axis=0)[0]]),\
                       np.mean([np.mean(data[5][2][3],axis=0)[0],np.mean(data[9][2][3],axis=0)[0],np.mean(data[12][2][3],axis=0)[0]]),\
                       np.mean([np.mean(data[5][3][3],axis=0)[0],np.mean(data[9][3][3],axis=0)[0],np.mean(data[12][3][3],axis=0)[0]])])

stdelon800back = np.array([np.std([np.mean(data[0][0][3],axis=0)[0],np.mean(data[3][0][3],axis=0)[0],np.mean(data[10][0][3],axis=0)[0],\
                                    np.mean(data[13][0][3],axis=0)[0],np.mean(data[14][0][3],axis=0)[0],np.mean(data[15][0][3],axis=0)[0],np.mean(data[16][0][3],axis=0)[0]]),\
                       np.std([np.mean(data[0][1][3],axis=0)[0],np.mean(data[3][1][3],axis=0)[0],np.mean(data[10][1][3],axis=0)[0],\
                                    np.mean(data[13][1][3],axis=0)[0],np.mean(data[14][1][3],axis=0)[0],np.mean(data[15][1][3],axis=0)[0],np.mean(data[16][1][3],axis=0)[0]]),\
                       np.std([np.mean(data[0][2][3],axis=0)[0],np.mean(data[3][2][3],axis=0)[0],np.mean(data[10][2][3],axis=0)[0],\
                                    np.mean(data[13][2][3],axis=0)[0],np.mean(data[14][2][3],axis=0)[0],np.mean(data[15][2][3],axis=0)[0],np.mean(data[16][2][3],axis=0)[0]]),\
                       np.std([np.mean(data[0][3][3],axis=0)[0],np.mean(data[3][3][3],axis=0)[0],np.mean(data[10][3][3],axis=0)[0],\
                                    np.mean(data[13][3][3],axis=0)[0],np.mean(data[14][3][3],axis=0)[0],np.mean(data[15][3][3],axis=0)[0],np.mean(data[16][3][3],axis=0)[0]]),\
                       np.std([np.mean(data[0][4][3],axis=0)[0],np.mean(data[3][4][3],axis=0)[0],np.mean(data[10][4][3],axis=0)[0],\
                                    np.mean(data[13][4][3],axis=0)[0],np.mean(data[14][4][3],axis=0)[0],np.mean(data[15][4][3],axis=0)[0],np.mean(data[16][4][3],axis=0)[0]]),\
                       np.std([np.mean(data[0][5][3],axis=0)[0],np.mean(data[3][5][3],axis=0)[0],np.mean(data[10][5][3],axis=0)[0],\
                                    np.mean(data[13][5][3],axis=0)[0],np.mean(data[14][5][3],axis=0)[0],np.mean(data[15][5][3],axis=0)[0],np.mean(data[16][5][3],axis=0)[0]])])
stdelon1600back = np.array([np.std([np.mean(data[2][0][3],axis=0)[0],np.mean(data[4][0][3],axis=0)[0],np.mean(data[6][0][3],axis=0)[0],\
                                 np.mean(data[8][0][3],axis=0)[0],np.mean(data[11][0][3],axis=0)[0]]),\
                       np.std([np.mean(data[2][1][3],axis=0)[0],np.mean(data[4][1][3],axis=0)[0],np.mean(data[6][1][3],axis=0)[0],\
                                 np.mean(data[8][1][3],axis=0)[0],np.mean(data[11][1][3],axis=0)[0]]),\
                       np.std([np.mean(data[2][2][3],axis=0)[0],np.mean(data[4][2][3],axis=0)[0],np.mean(data[6][2][3],axis=0)[0],\
                                 np.mean(data[8][2][3],axis=0)[0],np.mean(data[11][2][3],axis=0)[0]]),\
                       np.std([np.mean(data[2][3][3],axis=0)[0],np.mean(data[4][3][3],axis=0)[0],np.mean(data[6][3][3],axis=0)[0],\
                                 np.mean(data[8][3][3],axis=0)[0],np.mean(data[11][3][3],axis=0)[0]]),\
                       np.std([np.mean(data[2][4][3],axis=0)[0],np.mean(data[4][4][3],axis=0)[0],np.mean(data[6][4][3],axis=0)[0],\
                                 np.mean(data[8][4][3],axis=0)[0],np.mean(data[11][4][3],axis=0)[0]]),\
                       np.std([np.mean(data[2][5][3],axis=0)[0],np.mean(data[4][5][3],axis=0)[0],np.mean(data[6][5][3],axis=0)[0],\
                                 np.mean(data[8][5][3],axis=0)[0],np.mean(data[11][5][3],axis=0)[0]])])
stdelon4000back = np.array([np.std([np.mean(data[5][0][3],axis=0)[0],np.mean(data[9][0][3],axis=0)[0],np.mean(data[12][0][3],axis=0)[0]]),\
                       np.std([np.mean(data[5][1][3],axis=0)[0],np.mean(data[9][1][3],axis=0)[0],np.mean(data[12][1][3],axis=0)[0]]),\
                       np.std([np.mean(data[5][2][3],axis=0)[0],np.mean(data[9][2][3],axis=0)[0],np.mean(data[12][2][3],axis=0)[0]]),\
                       np.std([np.mean(data[5][3][3],axis=0)[0],np.mean(data[9][3][3],axis=0)[0],np.mean(data[12][3][3],axis=0)[0]])])

meanelon800top = np.array([np.mean([np.mean(data[0][0][4],axis=0)[0],np.mean(data[3][0][4],axis=0)[0],np.mean(data[10][0][4],axis=0)[0],\
                                    np.mean(data[13][0][4],axis=0)[0],np.mean(data[14][0][4],axis=0)[0],np.mean(data[15][0][4],axis=0)[0],np.mean(data[16][0][4],axis=0)[0]]),\
                       np.mean([np.mean(data[0][1][4],axis=0)[0],np.mean(data[3][1][4],axis=0)[0],np.mean(data[10][1][4],axis=0)[0],\
                                    np.mean(data[13][1][4],axis=0)[0],np.mean(data[14][1][4],axis=0)[0],np.mean(data[15][1][4],axis=0)[0],np.mean(data[16][1][4],axis=0)[0]]),\
                       np.mean([np.mean(data[0][2][4],axis=0)[0],np.mean(data[3][2][4],axis=0)[0],np.mean(data[10][2][4],axis=0)[0],\
                                    np.mean(data[13][2][4],axis=0)[0],np.mean(data[14][2][4],axis=0)[0],np.mean(data[15][2][4],axis=0)[0],np.mean(data[16][2][4],axis=0)[0]]),\
                       np.mean([np.mean(data[0][3][4],axis=0)[0],np.mean(data[3][3][4],axis=0)[0],np.mean(data[10][3][4],axis=0)[0],\
                                    np.mean(data[13][3][4],axis=0)[0],np.mean(data[14][3][4],axis=0)[0],np.mean(data[15][3][4],axis=0)[0],np.mean(data[16][3][4],axis=0)[0]]),\
                       np.mean([np.mean(data[0][4][4],axis=0)[0],np.mean(data[3][4][4],axis=0)[0],np.mean(data[10][4][4],axis=0)[0],\
                                    np.mean(data[13][4][4],axis=0)[0],np.mean(data[14][4][4],axis=0)[0],np.mean(data[15][4][4],axis=0)[0],np.mean(data[16][4][4],axis=0)[0]]),\
                       np.mean([np.mean(data[0][5][4],axis=0)[0],np.mean(data[3][5][4],axis=0)[0],np.mean(data[10][5][4],axis=0)[0],\
                                    np.mean(data[13][5][4],axis=0)[0],np.mean(data[14][5][4],axis=0)[0],np.mean(data[15][5][4],axis=0)[0],np.mean(data[16][5][4],axis=0)[0]])])
meanelon1600top = np.array([np.mean([np.mean(data[2][0][4],axis=0)[0],np.mean(data[4][0][4],axis=0)[0],np.mean(data[6][0][4],axis=0)[0],\
                                 np.mean(data[8][0][4],axis=0)[0],np.mean(data[11][0][4],axis=0)[0]]),\
                       np.mean([np.mean(data[2][1][4],axis=0)[0],np.mean(data[4][1][4],axis=0)[0],np.mean(data[6][1][4],axis=0)[0],\
                                 np.mean(data[8][1][4],axis=0)[0],np.mean(data[11][1][4],axis=0)[0]]),\
                       np.mean([np.mean(data[2][2][4],axis=0)[0],np.mean(data[4][2][4],axis=0)[0],np.mean(data[6][2][4],axis=0)[0],\
                                 np.mean(data[8][2][4],axis=0)[0],np.mean(data[11][2][4],axis=0)[0]]),\
                       np.mean([np.mean(data[2][3][4],axis=0)[0],np.mean(data[4][3][4],axis=0)[0],np.mean(data[6][3][4],axis=0)[0],\
                                 np.mean(data[8][3][4],axis=0)[0],np.mean(data[11][3][4],axis=0)[0]]),\
                       np.mean([np.mean(data[2][4][4],axis=0)[0],np.mean(data[4][4][4],axis=0)[0],np.mean(data[6][4][4],axis=0)[0],\
                                 np.mean(data[8][4][4],axis=0)[0],np.mean(data[11][4][4],axis=0)[0]]),\
                       np.mean([np.mean(data[2][5][4],axis=0)[0],np.mean(data[4][5][4],axis=0)[0],np.mean(data[6][5][4],axis=0)[0],\
                                 np.mean(data[8][5][4],axis=0)[0],np.mean(data[11][5][4],axis=0)[0]])])
meanelon4000top = np.array([np.mean([np.mean(data[5][0][4],axis=0)[0],np.mean(data[9][0][4],axis=0)[0],np.mean(data[12][0][4],axis=0)[0]]),\
                       np.mean([np.mean(data[5][1][4],axis=0)[0],np.mean(data[9][1][4],axis=0)[0],np.mean(data[12][1][4],axis=0)[0]]),\
                       np.mean([np.mean(data[5][2][4],axis=0)[0],np.mean(data[9][2][4],axis=0)[0],np.mean(data[12][2][4],axis=0)[0]]),\
                       np.mean([np.mean(data[5][3][4],axis=0)[0],np.mean(data[9][3][4],axis=0)[0],np.mean(data[12][3][4],axis=0)[0]])])

stdelon800top = np.array([np.std([np.mean(data[0][0][4],axis=0)[0],np.mean(data[3][0][4],axis=0)[0],np.mean(data[10][0][4],axis=0)[0],\
                                    np.mean(data[13][0][4],axis=0)[0],np.mean(data[14][0][4],axis=0)[0],np.mean(data[15][0][4],axis=0)[0],np.mean(data[16][0][4],axis=0)[0]]),\
                       np.std([np.mean(data[0][1][4],axis=0)[0],np.mean(data[3][1][4],axis=0)[0],np.mean(data[10][1][4],axis=0)[0],\
                                    np.mean(data[13][1][4],axis=0)[0],np.mean(data[14][1][4],axis=0)[0],np.mean(data[15][1][4],axis=0)[0],np.mean(data[16][1][4],axis=0)[0]]),\
                       np.std([np.mean(data[0][2][4],axis=0)[0],np.mean(data[3][2][4],axis=0)[0],np.mean(data[10][2][4],axis=0)[0],\
                                    np.mean(data[13][2][4],axis=0)[0],np.mean(data[14][2][4],axis=0)[0],np.mean(data[15][2][4],axis=0)[0],np.mean(data[16][2][4],axis=0)[0]]),\
                       np.std([np.mean(data[0][3][4],axis=0)[0],np.mean(data[3][3][4],axis=0)[0],np.mean(data[10][3][4],axis=0)[0],\
                                    np.mean(data[13][3][4],axis=0)[0],np.mean(data[14][3][4],axis=0)[0],np.mean(data[15][3][4],axis=0)[0],np.mean(data[16][3][4],axis=0)[0]]),\
                       np.std([np.mean(data[0][4][4],axis=0)[0],np.mean(data[3][4][4],axis=0)[0],np.mean(data[10][4][4],axis=0)[0],\
                                    np.mean(data[13][4][4],axis=0)[0],np.mean(data[14][4][4],axis=0)[0],np.mean(data[15][4][4],axis=0)[0],np.mean(data[16][4][4],axis=0)[0]]),\
                       np.std([np.mean(data[0][5][4],axis=0)[0],np.mean(data[3][5][4],axis=0)[0],np.mean(data[10][5][4],axis=0)[0],\
                                    np.mean(data[13][5][4],axis=0)[0],np.mean(data[14][5][4],axis=0)[0],np.mean(data[15][5][4],axis=0)[0],np.mean(data[16][5][4],axis=0)[0]])])
stdelon1600top = np.array([np.std([np.mean(data[2][0][4],axis=0)[0],np.mean(data[4][0][4],axis=0)[0],np.mean(data[6][0][4],axis=0)[0],\
                                 np.mean(data[8][0][4],axis=0)[0],np.mean(data[11][0][4],axis=0)[0]]),\
                       np.std([np.mean(data[2][1][4],axis=0)[0],np.mean(data[4][1][4],axis=0)[0],np.mean(data[6][1][4],axis=0)[0],\
                                 np.mean(data[8][1][4],axis=0)[0],np.mean(data[11][1][4],axis=0)[0]]),\
                       np.std([np.mean(data[2][2][4],axis=0)[0],np.mean(data[4][2][4],axis=0)[0],np.mean(data[6][2][4],axis=0)[0],\
                                 np.mean(data[8][2][4],axis=0)[0],np.mean(data[11][2][4],axis=0)[0]]),\
                       np.std([np.mean(data[2][3][4],axis=0)[0],np.mean(data[4][3][4],axis=0)[0],np.mean(data[6][3][4],axis=0)[0],\
                                 np.mean(data[8][3][4],axis=0)[0],np.mean(data[11][3][4],axis=0)[0]]),\
                       np.std([np.mean(data[2][4][4],axis=0)[0],np.mean(data[4][4][4],axis=0)[0],np.mean(data[6][4][4],axis=0)[0],\
                                 np.mean(data[8][4][4],axis=0)[0],np.mean(data[11][4][4],axis=0)[0]]),\
                       np.std([np.mean(data[2][5][4],axis=0)[0],np.mean(data[4][5][4],axis=0)[0],np.mean(data[6][5][4],axis=0)[0],\
                                 np.mean(data[8][5][4],axis=0)[0],np.mean(data[11][5][4],axis=0)[0]])])
stdelon4000top = np.array([np.std([np.mean(data[5][0][4],axis=0)[0],np.mean(data[9][0][4],axis=0)[0],np.mean(data[12][0][4],axis=0)[0]]),\
                       np.std([np.mean(data[5][1][4],axis=0)[0],np.mean(data[9][1][4],axis=0)[0],np.mean(data[12][1][4],axis=0)[0]]),\
                       np.std([np.mean(data[5][2][4],axis=0)[0],np.mean(data[9][2][4],axis=0)[0],np.mean(data[12][2][4],axis=0)[0]]),\
                       np.std([np.mean(data[5][3][4],axis=0)[0],np.mean(data[9][3][4],axis=0)[0],np.mean(data[12][3][4],axis=0)[0]])])

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
meanshear800face = np.array([np.mean([np.mean(data[0][0][2],axis=0)[1],np.mean(data[3][0][2],axis=0)[1],np.mean(data[10][0][2],axis=0)[1],\
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
meanshear1600face = np.array([np.mean([np.mean(data[2][0][2],axis=0)[1],np.mean(data[4][0][2],axis=0)[1],np.mean(data[6][0][2],axis=0)[1],\
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
meanshear4000face = np.array([np.mean([np.mean(data[5][0][2],axis=0)[1],np.mean(data[9][0][2],axis=0)[1],np.mean(data[12][0][2],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][2],axis=0)[1],np.mean(data[9][1][2],axis=0)[1],np.mean(data[12][1][2],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][2],axis=0)[1],np.mean(data[9][2][2],axis=0)[1],np.mean(data[12][2][2],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][2],axis=0)[1],np.mean(data[9][3][2],axis=0)[1],np.mean(data[12][3][2],axis=0)[1]])])

stdshear800face = np.array([np.std([np.mean(data[0][0][2],axis=0)[1],np.mean(data[3][0][2],axis=0)[1],np.mean(data[10][0][2],axis=0)[1],\
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
stdshear1600face = np.array([np.std([np.mean(data[2][0][2],axis=0)[1],np.mean(data[4][0][2],axis=0)[1],np.mean(data[6][0][2],axis=0)[1],\
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
stdshear4000face = np.array([np.std([np.mean(data[5][0][2],axis=0)[1],np.mean(data[9][0][2],axis=0)[1],np.mean(data[12][0][2],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][2],axis=0)[1],np.mean(data[9][1][2],axis=0)[1],np.mean(data[12][1][2],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][2],axis=0)[1],np.mean(data[9][2][2],axis=0)[1],np.mean(data[12][2][2],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][2],axis=0)[1],np.mean(data[9][3][2],axis=0)[1],np.mean(data[12][3][2],axis=0)[1]])])

meanshear800back = np.array([np.mean([np.mean(data[0][0][3],axis=0)[1],np.mean(data[3][0][3],axis=0)[1],np.mean(data[10][0][3],axis=0)[1],\
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
meanshear1600back = np.array([np.mean([np.mean(data[2][0][3],axis=0)[1],np.mean(data[4][0][3],axis=0)[1],np.mean(data[6][0][3],axis=0)[1],\
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
meanshear4000back = np.array([np.mean([np.mean(data[5][0][3],axis=0)[1],np.mean(data[9][0][3],axis=0)[1],np.mean(data[12][0][3],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][3],axis=0)[1],np.mean(data[9][1][3],axis=0)[1],np.mean(data[12][1][3],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][3],axis=0)[1],np.mean(data[9][2][3],axis=0)[1],np.mean(data[12][2][3],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][3],axis=0)[1],np.mean(data[9][3][3],axis=0)[1],np.mean(data[12][3][3],axis=0)[1]])])

stdshear800back = np.array([np.std([np.mean(data[0][0][3],axis=0)[1],np.mean(data[3][0][3],axis=0)[1],np.mean(data[10][0][3],axis=0)[1],\
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
stdshear1600back = np.array([np.std([np.mean(data[2][0][3],axis=0)[1],np.mean(data[4][0][3],axis=0)[1],np.mean(data[6][0][3],axis=0)[1],\
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
stdshear4000back = np.array([np.std([np.mean(data[5][0][3],axis=0)[1],np.mean(data[9][0][3],axis=0)[1],np.mean(data[12][0][3],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][3],axis=0)[1],np.mean(data[9][1][3],axis=0)[1],np.mean(data[12][1][3],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][3],axis=0)[1],np.mean(data[9][2][3],axis=0)[1],np.mean(data[12][2][3],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][3],axis=0)[1],np.mean(data[9][3][3],axis=0)[1],np.mean(data[12][3][3],axis=0)[1]])])

meanshear800top = np.array([np.mean([np.mean(data[0][0][4],axis=0)[1],np.mean(data[3][0][4],axis=0)[1],np.mean(data[10][0][4],axis=0)[1],\
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
meanshear1600top = np.array([np.mean([np.mean(data[2][0][4],axis=0)[1],np.mean(data[4][0][4],axis=0)[1],np.mean(data[6][0][4],axis=0)[1],\
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
meanshear4000top = np.array([np.mean([np.mean(data[5][0][4],axis=0)[1],np.mean(data[9][0][4],axis=0)[1],np.mean(data[12][0][4],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][4],axis=0)[1],np.mean(data[9][1][4],axis=0)[1],np.mean(data[12][1][4],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][4],axis=0)[1],np.mean(data[9][2][4],axis=0)[1],np.mean(data[12][2][4],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][4],axis=0)[1],np.mean(data[9][3][4],axis=0)[1],np.mean(data[12][3][4],axis=0)[1]])])

stdshear800top = np.array([np.std([np.mean(data[0][0][4],axis=0)[1],np.mean(data[3][0][4],axis=0)[1],np.mean(data[10][0][4],axis=0)[1],\
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
stdshear1600top = np.array([np.std([np.mean(data[2][0][4],axis=0)[1],np.mean(data[4][0][4],axis=0)[1],np.mean(data[6][0][4],axis=0)[1],\
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
stdshear4000top = np.array([np.std([np.mean(data[5][0][4],axis=0)[1],np.mean(data[9][0][4],axis=0)[1],np.mean(data[12][0][4],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][4],axis=0)[1],np.mean(data[9][1][4],axis=0)[1],np.mean(data[12][1][4],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][4],axis=0)[1],np.mean(data[9][2][4],axis=0)[1],np.mean(data[12][2][4],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][4],axis=0)[1],np.mean(data[9][3][4],axis=0)[1],np.mean(data[12][3][4],axis=0)[1]])])

meanshear800surface = np.array([np.mean([np.mean(data[0][0][1],axis=0)[1],np.mean(data[3][0][1],axis=0)[1],np.mean(data[10][0][1],axis=0)[1],\
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
meanshear1600surface = np.array([np.mean([np.mean(data[2][0][1],axis=0)[1],np.mean(data[4][0][1],axis=0)[1],np.mean(data[6][0][1],axis=0)[1],\
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
meanshear4000surface = np.array([np.mean([np.mean(data[5][0][1],axis=0)[1],np.mean(data[9][0][1],axis=0)[1],np.mean(data[12][0][1],axis=0)[1]]),\
                       np.mean([np.mean(data[5][1][1],axis=0)[1],np.mean(data[9][1][1],axis=0)[1],np.mean(data[12][1][1],axis=0)[1]]),\
                       np.mean([np.mean(data[5][2][1],axis=0)[1],np.mean(data[9][2][1],axis=0)[1],np.mean(data[12][2][1],axis=0)[1]]),\
                       np.mean([np.mean(data[5][3][1],axis=0)[1],np.mean(data[9][3][1],axis=0)[1],np.mean(data[12][3][1],axis=0)[1]])])

stdshear800surface = np.array([np.std([np.mean(data[0][0][1],axis=0)[1],np.mean(data[3][0][1],axis=0)[1],np.mean(data[10][0][1],axis=0)[1],\
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
stdshear1600surface = np.array([np.std([np.mean(data[2][0][1],axis=0)[1],np.mean(data[4][0][1],axis=0)[1],np.mean(data[6][0][1],axis=0)[1],\
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
stdshear4000surface = np.array([np.std([np.mean(data[5][0][1],axis=0)[1],np.mean(data[9][0][1],axis=0)[1],np.mean(data[12][0][1],axis=0)[1]]),\
                       np.std([np.mean(data[5][1][1],axis=0)[1],np.mean(data[9][1][1],axis=0)[1],np.mean(data[12][1][1],axis=0)[1]]),\
                       np.std([np.mean(data[5][2][1],axis=0)[1],np.mean(data[9][2][1],axis=0)[1],np.mean(data[12][2][1],axis=0)[1]]),\
                       np.std([np.mean(data[5][3][1],axis=0)[1],np.mean(data[9][3][1],axis=0)[1],np.mean(data[12][3][1],axis=0)[1]])])


### Plot
time = np.array([1,2,4,6,9,12])
time1 = np.array([1,6,11,16,21,26])
time2 = np.array([1,6,11,16])
time3 = np.array([1,3,5,7,9,11])
time4 = np.array([1,3,5,7])

labels=['1','2','4','6','9','12']
fontsize = 16
ticksize = 14

# color1 = 'tab:red'
# color2 = 'tab:blue'
# color3 = 'tab:orange'
color1 = (235/255,153/255,156/255) ## pink
color2 = (161/255,125/255,180/255) ## purple
color3 = (142/255,165/255,200/255) ## blue
edgecolor = (102/255,100/255,100/255)

width12 = 0.7
width34 = 0.4

### Elongational rate faceward vs. backward
fig, ax = plt.subplots()
ax.bar(time1-2.5*width12, meanelon800face, yerr=stdelon800face, alpha=0.9, color=color1, ecolor='black', capsize=2, width=width12)
ax.bar(time1-0.5*width12, meanelon1600face, yerr=stdelon1600face, alpha=0.9, color=color2, ecolor='black', capsize=2, width=width12)
ax.bar(time2+1.5*width12, meanelon4000face, yerr=stdelon4000face, alpha=0.9, color=color3, ecolor='black', capsize=2, width=width12)
ax.bar(time1-1.5*width12, meanelon800back, yerr=stdelon800face, hatch='////', color='none', edgecolor=color1, ecolor='black', capsize=2, width=width12)
ax.bar(time1+0.5*width12, meanelon1600back, yerr=stdelon1600face, hatch='////', color='none', edgecolor=color2, ecolor='black', capsize=2, width=width12)
ax.bar(time2+2.5*width12, meanelon4000back, yerr=stdelon4000face, hatch='////', color='none', edgecolor=color3, ecolor='black', capsize=2, width=width12)

ax.set_ylabel('elongational rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average elongational rate', fontsize=fontsize)

# ax.set_xlim(3,12)
ax.set_ylim(0,)

plt.xticks(time1, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

legend_elements = [Line2D([0], [0], color=color1, lw=3, label='800 1/s'),
                   Line2D([0], [0], color=color2, lw=3, label='1600 1/s'), 
                   Line2D([0], [0], color=color3, lw=3, label='4000 1/s'),
                   Patch(facecolor='k', edgecolor='k',label='faceward'),
                   Patch(facecolor='none', hatch='///', edgecolor='k',label='backward'),]

plt.legend(handles=legend_elements,loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('elonFB.png',bbox_inches='tight')
plt.show()

### Shear rate faceward vs. backward
fig, ax = plt.subplots()
ax.bar(time1-2.5*width12, meanshear800face, yerr=stdshear800face, alpha=0.9, color=color1, ecolor='black', capsize=2, width=width12)
ax.bar(time1-0.5*width12, meanshear1600face, yerr=stdshear1600face, alpha=0.9, color=color2, ecolor='black', capsize=2, width=width12)
ax.bar(time2+1.5*width12, meanshear4000face, yerr=stdshear4000face, alpha=0.9, color=color3, ecolor='black', capsize=2, width=width12)
ax.bar(time1-1.5*width12, meanshear800back, yerr=stdshear800face, hatch='///', color='none', edgecolor=color1, ecolor='black', capsize=2, width=width12)
ax.bar(time1+0.5*width12, meanshear1600back, yerr=stdshear1600face, hatch='///', color='none', edgecolor=color2, ecolor='black', capsize=2, width=width12)
ax.bar(time2+2.5*width12, meanshear4000back, yerr=stdshear4000face, hatch='///', color='none', edgecolor=color3, ecolor='black', capsize=2, width=width12)

ax.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average shear rate', fontsize=fontsize)

# ax.set_xlim(3,12)
ax.set_ylim(0,)

plt.xticks(time1, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

legend_elements = [Line2D([0], [0], color=color1, lw=3, label='800 1/s'),
                   Line2D([0], [0], color=color2, lw=3, label='1600 1/s'), 
                   Line2D([0], [0], color=color3, lw=3, label='4000 1/s'),
                   Patch(facecolor='k', edgecolor='k',label='faceward'),
                   Patch(facecolor='none', hatch='///', edgecolor='k',label='backward'),]

plt.legend(handles=legend_elements,loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('shearFB.png',bbox_inches='tight')
plt.show()


### Shear rate top
# fig, ax = plt.subplots()
# ax.bar(time3-width34, meanshear800top, yerr=stdshear800top, alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width34)
# ax.bar(time3, meanshear1600top, yerr=stdshear1600top, alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width34)
# ax.bar(time4+width34, meanshear4000top, yerr=stdshear4000top, alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width34)

# ax.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average shear rate', fontsize=fontsize)

# # ax.set_xlim(3,12)
# ax.set_ylim(0,)

# plt.xticks(time3, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('shearT.png',bbox_inches='tight')
# plt.show()
fig, ax = plt.subplots()
ax.errorbar(time[0:6],meanshear800top,yerr=stdshear800top,fmt='-o', color=color1, ecolor='k', markersize=6, capsize=3, label='800 1/s')
ax.errorbar(time[0:6],meanshear1600top,yerr=stdshear1600top,fmt='-o', color=color2, ecolor='k', markersize=6, capsize=3, label='1600 1/s')
ax.errorbar(time[0:4],meanshear4000top,yerr=stdshear4000top,fmt='-o', color=color3, ecolor='k', markersize=6, capsize=3, label='4000 1/s')

ax.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average shear rate on top part', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('shearTline.png',bbox_inches='tight')
plt.show()


### Elongational rate top
fig, ax = plt.subplots()
ax.errorbar(time[0:6],meanelon800top,yerr=stdelon800top,fmt='-o', color=color1, ecolor='k', markersize=6, capsize=3, label='800 1/s')
ax.errorbar(time[0:6],meanelon1600top,yerr=stdelon1600top,fmt='-o', color=color2, ecolor='k', markersize=6, capsize=3, label='1600 1/s')
ax.errorbar(time[0:4],meanelon4000top,yerr=stdelon4000top,fmt='-o', color=color3, ecolor='k', markersize=6, capsize=3, label='4000 1/s')

ax.set_ylabel('elongational rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average elongational rate on top part', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('elonTline.png',bbox_inches='tight')
plt.show()


### Shear rate surface
fig, ax = plt.subplots()
ax.errorbar(time[0:6],meanshear800surface,yerr=stdshear800surface,fmt='-o', color=color1, ecolor='k', markersize=6, capsize=3, label='800 1/s')
ax.errorbar(time[0:6],meanshear1600surface,yerr=stdshear1600surface,fmt='-o', color=color2, ecolor='k', markersize=6, capsize=3, label='1600 1/s')
ax.errorbar(time[0:4],meanshear4000surface,yerr=stdshear4000surface,fmt='-o', color=color3, ecolor='k', markersize=6, capsize=3, label='4000 1/s')

ax.set_ylabel('shear rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average shear rate on the whole surface', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('shearSline.png',bbox_inches='tight')
plt.show()


### Elongational rate surface
fig, ax = plt.subplots()
ax.errorbar(time[0:6],meanelon800surface,yerr=stdelon800surface,fmt='-o', color=color1, ecolor='k', markersize=6, capsize=3, label='800 1/s')
ax.errorbar(time[0:6],meanelon1600surface,yerr=stdelon1600surface,fmt='-o', color=color2, ecolor='k', markersize=6, capsize=3, label='1600 1/s')
ax.errorbar(time[0:4],meanelon4000surface,yerr=stdelon4000surface,fmt='-o', color=color3, ecolor='k', markersize=6, capsize=3, label='4000 1/s')

ax.set_ylabel('elongational rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average elongational rate on the whole surface', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('elonSline.png',bbox_inches='tight')
plt.show()