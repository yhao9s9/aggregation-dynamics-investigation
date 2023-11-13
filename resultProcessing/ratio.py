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

data800 = np.array([0,3,10,13,14,15,16])
data1600 = np.array([2,4,6,8,11])
data4000 = np.array([5,9,12])


## Local binding availability time: rupture distance 100nm, threshold 1ms
rt800ratio = []
rt1600ratio = []
rt4000ratio = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = 1/data[data800[i]][j][1][:,4]*45*1e-6*1e3 ## 1/velocity(mm/s) * binding distance: 100*1e-6(mm) * 1e-3 [s->ms]
        temp800_gt1 = temp800[temp800>1]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    rt800ratio.append(timearray)
rt800ratio = np.array(rt800ratio)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = 1/data[data1600[i]][j][1][:,4]*45*1e-6*1e3
        temp1600_gt1 = temp1600[temp1600>1]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    rt1600ratio.append(timearray)
rt1600ratio = np.array(rt1600ratio)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = 1/data[data4000[i]][j][1][:,4]*45*1e-6*1e3
        temp4000_gt1 = temp4000[temp4000>1]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    rt4000ratio.append(timearray)
rt4000ratio = np.array(rt4000ratio)



## Shear rate
shear800ratio = []
shear1600ratio = []
shear4000ratio = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = data[data800[i]][j][1][:,2]
        temp800_gt1 = temp800[temp800>2500]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    shear800ratio.append(timearray)
shear800ratio = np.array(shear800ratio)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = data[data1600[i]][j][1][:,2]
        temp1600_gt1 = temp1600[temp1600>2500]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    shear1600ratio.append(timearray)
shear1600ratio = np.array(shear1600ratio)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = data[data4000[i]][j][1][:,2]
        temp4000_gt1 = temp4000[temp4000>2500]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    shear4000ratio.append(timearray)
shear4000ratio = np.array(shear4000ratio)


## Elongation rate
elon800ratio = []
elon1600ratio = []
elon4000ratio = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = data[data800[i]][j][1][:,0]
        temp800_gt1 = temp800[temp800>600]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    elon800ratio.append(timearray)
elon800ratio = np.array(elon800ratio)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = data[data1600[i]][j][1][:,0]
        temp1600_gt1 = temp1600[temp1600>600]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    elon1600ratio.append(timearray)
elon1600ratio = np.array(elon1600ratio)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = data[data4000[i]][j][1][:,0]
        temp4000_gt1 = temp4000[temp4000>600]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    elon4000ratio.append(timearray)
elon4000ratio = np.array(elon4000ratio)


## Rupture force: shear stress * rupture area (size of fibrinogen, diameter: 15A[Angstrom: 1e-10m])
bf800ratio = []
bf1600ratio = []
bf4000ratio = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = data[data800[i]][j][1][:,3]*(7.5*1e-10*1e3)**2*np.pi*1e12 ## *1e12: N -> pN
        temp800_gt1 = temp800[temp800>20]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    bf800ratio.append(timearray)
bf800ratio = np.array(bf800ratio)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = data[data1600[i]][j][1][:,3]*(7.5*1e-10*1e3)**2*np.pi*1e12
        temp1600_gt1 = temp1600[temp1600>20]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    bf1600ratio.append(timearray)
bf1600ratio = np.array(bf1600ratio)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = data[data4000[i]][j][1][:,3]*(7.5*1e-10*1e3)**2*np.pi*1e12
        temp4000_gt1 = temp4000[temp4000>20]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    bf4000ratio.append(timearray)
bf4000ratio = np.array(bf4000ratio)


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


## Local binding availability time ratio
fig, ax = plt.subplots()
ax.errorbar(time[0:6],np.mean(rt800ratio,axis=0)*100,yerr=np.std(rt800ratio,axis=0)*100,fmt='--^', color=color1, markersize=8, capsize=5, label='800 1/s')
ax.errorbar(time[0:6],np.mean(rt1600ratio,axis=0)*100,yerr=np.std(rt1600ratio,axis=0)*100,fmt='--o', color=color2, markersize=8, capsize=5, label='1600 1/s')
ax.errorbar(time[0:4],np.mean(rt4000ratio,axis=0)*100,yerr=np.std(rt4000ratio,axis=0)*100,fmt='--s', color=color3, markersize=8, capsize=5, label='4000 1/s')

ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Ratio of surface with local binding availability \n time larger than 1 $ms$', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=4,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('rtRatio.png',bbox_inches='tight')
plt.show()


### Shear rate ratio
fig, ax = plt.subplots()
ax.errorbar(time[0:6],np.mean(shear800ratio,axis=0)*100,yerr=np.std(shear800ratio,axis=0)*100,fmt='--^', color=color1, markersize=8, capsize=5, label='800 1/s')
ax.errorbar(time[0:6],np.mean(shear1600ratio,axis=0)*100,yerr=np.std(shear1600ratio,axis=0)*100,fmt='--o', color=color2, markersize=8, capsize=5, label='1600 1/s')
ax.errorbar(time[0:4],np.mean(shear4000ratio,axis=0)*100,yerr=np.std(shear4000ratio,axis=0)*100,fmt='--s', color=color3, markersize=8, capsize=5, label='4000 1/s')

ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Ratio of surface with shear rate larger \n than 2500 $1/s$', fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('shearRatio.png',bbox_inches='tight')
plt.show()



### Elongation rate ratio
fig, ax = plt.subplots()
ax.errorbar(time[0:6],np.mean(elon800ratio,axis=0)*100,yerr=np.std(elon800ratio,axis=0)*100,fmt='--^', color=color1, markersize=8, capsize=5, label='800 1/s')
ax.errorbar(time[0:6],np.mean(elon1600ratio,axis=0)*100,yerr=np.std(elon1600ratio,axis=0)*100,fmt='--o', color=color2, markersize=8, capsize=5, label='1600 1/s')
ax.errorbar(time[0:4],np.mean(elon4000ratio,axis=0)*100,yerr=np.std(elon4000ratio,axis=0)*100,fmt='--s', color=color3, markersize=8, capsize=5, label='4000 1/s')

ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Ratio of surface with rate of elongation \n larger than 600 $1/s$', fontsize=fontsize)

# ax.set_ylim(0,5)
plt.yticks(np.arange(10,81,20))
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('elonRatio.png',bbox_inches='tight')
plt.show()



# ### Rupture force ratio
# fig, ax = plt.subplots()
# ax.errorbar(time[0:6],np.mean(bf800ratio,axis=0)*100,yerr=np.std(bf800ratio,axis=0)*100,fmt='--^', color=color1, markersize=8, capsize=5, label='800 1/s')
# ax.errorbar(time[0:6],np.mean(bf1600ratio,axis=0)*100,yerr=np.std(bf1600ratio,axis=0)*100,fmt='--o', color=color2, markersize=8, capsize=5, label='1600 1/s')
# ax.errorbar(time[0:4],np.mean(bf4000ratio,axis=0)*100,yerr=np.std(bf4000ratio,axis=0)*100,fmt='--s', color=color3, markersize=8, capsize=5, label='4000 1/s')

# ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average ratio of surface with rupture \n force larger than 20 $pN$', fontsize=fontsize)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('rfRatio.png',bbox_inches='tight')
# plt.show()

