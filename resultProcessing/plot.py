import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt


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

time = np.array([1,2,4,6,9,12])
time1 = np.array([1,3,5,7,9,11])
time2 = np.array([1,3,5,7])

meanelon800face = np.array([np.mean([np.mean(data[0][0][2],axis=0)[0],np.mean(data[1][0][2],axis=0)[0],np.mean(data[3][0][2],axis=0)[0],\
                                 np.mean(data[7][0][2],axis=0)[0],np.mean(data[10][0][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][1][2],axis=0)[0],np.mean(data[1][1][2],axis=0)[0],np.mean(data[3][1][2],axis=0)[0],\
                                 np.mean(data[7][1][2],axis=0)[0],np.mean(data[10][1][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][2][2],axis=0)[0],np.mean(data[1][2][2],axis=0)[0],np.mean(data[3][2][2],axis=0)[0],\
                                 np.mean(data[7][2][2],axis=0)[0],np.mean(data[10][2][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][3][2],axis=0)[0],np.mean(data[1][3][2],axis=0)[0],np.mean(data[3][3][2],axis=0)[0],\
                                 np.mean(data[7][3][2],axis=0)[0],np.mean(data[10][3][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][4][2],axis=0)[0],np.mean(data[1][4][2],axis=0)[0],np.mean(data[3][4][2],axis=0)[0],\
                                 np.mean(data[7][4][2],axis=0)[0],np.mean(data[10][4][2],axis=0)[0]]),\
                       np.mean([np.mean(data[0][5][2],axis=0)[0],np.mean(data[1][5][2],axis=0)[0],np.mean(data[3][5][2],axis=0)[0],\
                                 np.mean(data[7][5][2],axis=0)[0],np.mean(data[10][5][2],axis=0)[0]])])
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

stdelon800face = np.array([np.std([np.mean(data[0][0][2],axis=0)[0],np.mean(data[1][0][2],axis=0)[0],np.mean(data[3][0][2],axis=0)[0],\
                                 np.mean(data[7][0][2],axis=0)[0],np.mean(data[10][0][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][1][2],axis=0)[0],np.mean(data[1][1][2],axis=0)[0],np.mean(data[3][1][2],axis=0)[0],\
                                 np.mean(data[7][1][2],axis=0)[0],np.mean(data[10][1][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][2][2],axis=0)[0],np.mean(data[1][2][2],axis=0)[0],np.mean(data[3][2][2],axis=0)[0],\
                                 np.mean(data[7][2][2],axis=0)[0],np.mean(data[10][2][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][3][2],axis=0)[0],np.mean(data[1][3][2],axis=0)[0],np.mean(data[3][3][2],axis=0)[0],\
                                 np.mean(data[7][3][2],axis=0)[0],np.mean(data[10][3][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][4][2],axis=0)[0],np.mean(data[1][4][2],axis=0)[0],np.mean(data[3][4][2],axis=0)[0],\
                                 np.mean(data[7][4][2],axis=0)[0],np.mean(data[10][4][2],axis=0)[0]]),\
                       np.std([np.mean(data[0][5][2],axis=0)[0],np.mean(data[1][5][2],axis=0)[0],np.mean(data[3][5][2],axis=0)[0],\
                                 np.mean(data[7][5][2],axis=0)[0],np.mean(data[10][5][2],axis=0)[0]])])
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

width = 0.4

### bottom area vs. time
fig, ax = plt.subplots()
ax.bar(time1-width, meanelon800face, yerr=stdelon800face, alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width)
ax.bar(time1, meanelon1600face, yerr=stdelon1600face, alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width)
ax.bar(time2+width, meanelon4000face, yerr=stdelon4000face, alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width)
# ax.bar(time-width, np.mean(data800[6:12,0:6],axis=0), alpha=0.5, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width)
# ax.bar(time, np.mean(data1600[5:10,0:6],axis=0), alpha=0.5, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width)
# ax.bar(time+width, np.mean(data4000[4:8,0:6],axis=0), alpha=0.5, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width)

ax.set_ylabel('elongational rate $[1/s]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Elongational rate', fontsize=fontsize)

# ax.set_xlim(3,12)
ax.set_ylim(0,)

plt.xticks(time1, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=2,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('elonFB.png',bbox_inches='tight')
plt.show()