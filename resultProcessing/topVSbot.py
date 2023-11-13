## Plot the redundant part as two aggregates

import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.lines as mlines
import seaborn as sns


dirt = ['d1_800/','d2_1600/','d3_800/','d3_1600/','d3_4000/','d4_1600/','d5_1600/','d5_4000/','d6_800/','d6_1600/','d6_4000/']
time = ['1min/','2min/','4min/','6min/','9min/','12min/']
name1 = ['toppercent','middle10','bottom10','top3','middle3','bottom3']

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


name2 = ['1toppercent','1middle10','1bottom10','1top3','1middle3','1bottom3']
name3 = ['2toppercent','2middle10','2bottom10','2top3','2middle3','2bottom3']

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

## data = [d1_800[6][5],d2_1600,d3_800,d3_1600,d3_4000,d4_1600,d5_1600,d5_4000[6][5],d6_800,d6_1600,d6_4000[6][5],
#           d2_800_solid1[6][5],d2_800_solid2[6][5],d5_800_solid1[6][5],d5_800_solid2[6][5]]
## d5_4000 9min & 12min: []
## d2_800/6min/bottom10 = data[14][3][2] -> 2D array = num_node * [PointZ, elongation, shear rate, shear stress, velocity]

data800 = np.array([0,2,8,11,12,13,14])
data1600 = np.array([1,3,5,6,9])
data4000 = np.array([4,7,10])


## Local binding availability time: rupture distance 100nm, threshold 1ms
# Top10
rt800top10 = []
rt1600top10 = []
rt4000top10 = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = 1/data[data800[i]][j][0][:,4]*45*1e-6*1e3 ## 1/velocity(mm/s) * binding distance: 100*1e-6(mm) * 1e-3 [s->ms]
        temp800_gt1 = temp800[temp800>1]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    rt800top10.append(timearray)
rt800top10 = np.array(rt800top10)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = 1/data[data1600[i]][j][0][:,4]*45*1e-6*1e3
        temp1600_gt1 = temp1600[temp1600>1]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    rt1600top10.append(timearray)
rt1600top10 = np.array(rt1600top10)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = 1/data[data4000[i]][j][0][:,4]*45*1e-6*1e3
        temp4000_gt1 = temp4000[temp4000>1]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    rt4000top10.append(timearray)
rt4000top10 = np.array(rt4000top10)

# Bottom10
rt800bottom10 = []
rt1600bottom10 = []
rt4000bottom10 = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = 1/data[data800[i]][j][2][:,4]*45*1e-6*1e3 ## 1/velocity(mm/s) * rupture distance: 100*1e-6(mm) * 1e-3 [s->ms]
        temp800_gt1 = temp800[temp800>1]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    rt800bottom10.append(timearray)
rt800bottom10 = np.array(rt800bottom10)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = 1/data[data1600[i]][j][2][:,4]*45*1e-6*1e3
        temp1600_gt1 = temp1600[temp1600>1]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    rt1600bottom10.append(timearray)
rt1600bottom10 = np.array(rt1600bottom10)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = 1/data[data4000[i]][j][2][:,4]*45*1e-6*1e3
        temp4000_gt1 = temp4000[temp4000>1]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    rt4000bottom10.append(timearray)
rt4000bottom10 = np.array(rt4000bottom10)


# Top3
rt800top3 = []
rt1600top3 = []
rt4000top3 = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = 1/data[data800[i]][j][3][:,4]*45*1e-6*1e3 ## 1/velocity(mm/s) * binding distance: 100*1e-6(mm) * 1e-3 [s->ms]
        temp800_gt1 = temp800[temp800>1]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    rt800top3.append(timearray)
rt800top3 = np.array(rt800top3)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = 1/data[data1600[i]][j][3][:,4]*45*1e-6*1e3
        temp1600_gt1 = temp1600[temp1600>1]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    rt1600top3.append(timearray)
rt1600top3 = np.array(rt1600top3)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = 1/data[data4000[i]][j][3][:,4]*45*1e-6*1e3
        temp4000_gt1 = temp4000[temp4000>1]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    rt4000top3.append(timearray)
rt4000top3 = np.array(rt4000top3)

# Bottom3
rt800bottom3 = []
rt1600bottom3 = []
rt4000bottom3 = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = 1/data[data800[i]][j][5][:,4]*45*1e-6*1e3 ## 1/velocity(mm/s) * rupture distance: 100*1e-6(mm) * 1e-3 [s->ms]
        temp800_gt1 = temp800[temp800>1]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    rt800bottom3.append(timearray)
rt800bottom3 = np.array(rt800bottom3)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = 1/data[data1600[i]][j][5][:,4]*45*1e-6*1e3
        temp1600_gt1 = temp1600[temp1600>1]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    rt1600bottom3.append(timearray)
rt1600bottom3 = np.array(rt1600bottom3)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = 1/data[data4000[i]][j][5][:,4]*45*1e-6*1e3
        temp4000_gt1 = temp4000[temp4000>1]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    rt4000bottom3.append(timearray)
rt4000bottom3 = np.array(rt4000bottom3)


## Shear rate
# Top3
shear800top3 = []
shear1600top3 = []
shear4000top3 = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = data[data800[i]][j][3][:,2]
        temp800_gt1 = temp800[temp800>2500]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    shear800top3.append(timearray)
shear800top3 = np.array(shear800top3)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = data[data1600[i]][j][3][:,2]
        temp1600_gt1 = temp1600[temp1600>2500]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    shear1600top3.append(timearray)
shear1600top3 = np.array(shear1600top3)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = data[data4000[i]][j][3][:,2]
        temp4000_gt1 = temp4000[temp4000>2500]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    shear4000top3.append(timearray)
shear4000top3 = np.array(shear4000top3)

# Bottom3
shear800bottom3 = []
shear1600bottom3 = []
shear4000bottom3 = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = data[data800[i]][j][5][:,2]
        temp800_gt1 = temp800[temp800>2500]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    shear800bottom3.append(timearray)
shear800bottom3 = np.array(shear800bottom3)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = data[data1600[i]][j][5][:,2]
        temp1600_gt1 = temp1600[temp1600>2500]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    shear1600bottom3.append(timearray)
shear1600bottom3 = np.array(shear1600bottom3)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = data[data4000[i]][j][5][:,2]
        temp4000_gt1 = temp4000[temp4000>2500]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    shear4000bottom3.append(timearray)
shear4000bottom3 = np.array(shear4000bottom3)


## Elongation rate
# Top3 
elon800top3 = []
elon1600top3 = []
elon4000top3 = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = data[data800[i]][j][3][:,0]
        temp800_gt1 = temp800[temp800>600]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    elon800top3.append(timearray)
elon800top3 = np.array(elon800top3)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = data[data1600[i]][j][3][:,0]
        temp1600_gt1 = temp1600[temp1600>600]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    elon1600top3.append(timearray)
elon1600top3 = np.array(elon1600top3)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = data[data4000[i]][j][3][:,0]
        temp4000_gt1 = temp4000[temp4000>600]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    elon4000top3.append(timearray)
elon4000top3 = np.array(elon4000top3)

# Bottom3 
elon800bottom3 = []
elon1600bottom3 = []
elon4000bottom3 = []
for i in range(data800.shape[0]):
    timearray = []
    for j in range(6):
        temp800 = data[data800[i]][j][5][:,0]
        temp800_gt1 = temp800[temp800>600]
        ratio = temp800_gt1.shape[0]/temp800.shape[0]
        timearray.append(ratio)
    elon800bottom3.append(timearray)
elon800bottom3 = np.array(elon800bottom3)

for i in range(data1600.shape[0]):
    timearray = []
    for j in range(6):
        temp1600 = data[data1600[i]][j][5][:,0]
        temp1600_gt1 = temp1600[temp1600>600]
        ratio = temp1600_gt1.shape[0]/temp1600.shape[0]
        timearray.append(ratio)
    elon1600bottom3.append(timearray)
elon1600bottom3 = np.array(elon1600bottom3)

for i in range(data4000.shape[0]):
    timearray = []
    for j in range(4):
        temp4000 = data[data4000[i]][j][5][:,0]
        temp4000_gt1 = temp4000[temp4000>600]
        ratio = temp4000_gt1.shape[0]/temp4000.shape[0]
        timearray.append(ratio)
    elon4000bottom3.append(timearray)
elon4000bottom3 = np.array(elon4000bottom3)


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
width12backup = 0.9
width34 = 0.6

# ### Legend
# fig, ax = plt.subplots()
# marker800 = mlines.Line2D([0], [0], color=color1, lw=4, label='800 1/s')
# marker1600 = mlines.Line2D([0], [0], color=color2, lw=4, label='1600 1/s')
# marker4000 = mlines.Line2D([0], [0], color=color3, lw=4, label='4000 1/s')
# linetop13 = Patch(facecolor='k', edgecolor='k',label='top')
# linetop2 = Patch(facecolor='none', hatch='////', edgecolor='k',label='bottom')
# ax.legend(
#     handles=[marker800, marker1600, marker4000, linetop13, linetop2],
#     loc="lower center", # "upper center" puts it below the line
#     ncol=5,
#     bbox_to_anchor=(0.5, 0.88),
#     bbox_transform=fig.transFigure,
#     fontsize=20
# );
# plt.savefig('legend.png',bbox_inches='tight', transparent=True)
# plt.show()



## Local binding availability time ratio
fig, ax = plt.subplots()
ax.bar(time1-2.5*width12, np.mean(rt800top3,axis=0)*100, yerr=np.std(rt800top3,axis=0)*100, alpha=0.9, color=color1, ecolor='black', capsize=2, width=width12)
ax.bar(time1-0.5*width12, np.mean(rt1600top3,axis=0)*100, yerr=np.std(rt1600top3,axis=0)*100, alpha=0.9, color=color2, ecolor='black', capsize=2, width=width12)
ax.bar(time2+1.5*width12, np.mean(rt4000top3,axis=0)*100, yerr=np.std(rt4000top3,axis=0)*100, alpha=0.9, color=color3, ecolor='black', capsize=2, width=width12)
ax.bar(time1-1.5*width12, np.mean(rt800bottom3,axis=0)*100, yerr=np.std(rt800bottom3,axis=0)*100, hatch='////', color='none', edgecolor=color1, ecolor='black', capsize=2, width=width12)
ax.bar(time1+0.5*width12, np.mean(rt1600bottom3,axis=0)*100, yerr=np.std(rt1600bottom3,axis=0)*100, hatch='////', color='none', edgecolor=color2, ecolor='black', capsize=2, width=width12)
ax.bar(time2+2.5*width12, np.mean(rt4000bottom3,axis=0)*100, yerr=np.std(rt4000bottom3,axis=0)*100, hatch='////', color='none', edgecolor=color3, ecolor='black', capsize=2, width=width12)

ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Local binding availability time $>$ 1 $ms$', fontsize=fontsize)

ax.set_ylim(0,)
plt.xticks(time1, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=2,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('TBrtRatio.png',bbox_inches='tight')
plt.show()


## Shear rate ratio
fig, ax = plt.subplots()
ax.bar(time1-1.5*width12backup, np.mean(shear1600top3,axis=0)*100, yerr=np.std(shear1600top3,axis=0)*100, alpha=0.9, color=color2, ecolor='black', capsize=2, width=width12backup)
ax.bar(time2+0.5*width12backup, np.mean(shear4000top3,axis=0)*100, yerr=np.std(shear4000top3,axis=0)*100, alpha=0.9, color=color3, ecolor='black', capsize=2, width=width12backup)
ax.bar(time1-0.5*width12backup, np.mean(shear1600bottom3,axis=0)*100, yerr=np.std(shear1600bottom3,axis=0)*100, hatch='////', color='none', edgecolor=color2, ecolor='black', capsize=2, width=width12backup)
ax.bar(time2+1.5*width12backup, np.mean(shear4000bottom3,axis=0)*100, yerr=np.std(shear4000bottom3,axis=0)*100, hatch='////', color='none', edgecolor=color3, ecolor='black', capsize=2, width=width12backup)

ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Shear rate $>$ 2500 $1/s$', fontsize=fontsize)

ax.set_ylim(0,)

plt.xticks(time1, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=2,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('TBshearRatio.png',bbox_inches='tight')
plt.show()


## Shear rate ratio -- zoom in
fig, ax = plt.subplots(figsize=(12, 4))
bars = ax.bar(time3, np.mean(shear1600bottom3,axis=0)*100, hatch='//', color='none', edgecolor=color2, ecolor='black', capsize=6, width=width12)

ax.bar_label(bars,fmt='%0.3f',fontsize=22)

ax.set_ylim(0,0.2)

plt.xticks(time3, labels=labels)
ax.tick_params(axis='x', labelsize= ticksizeZoom)
ax.tick_params(axis='y', labelsize= ticksizeZoom)

plt.savefig('TBshearRatio_zoom.png',bbox_inches='tight', transparent=True)
plt.show()


## Elongation rate ratio
fig, ax = plt.subplots()
ax.bar(time1-1.5*width12backup, np.mean(elon1600top3,axis=0)*100, yerr=np.std(elon1600top3,axis=0)*100, alpha=0.9, color=color2, ecolor='black', capsize=2, width=width12backup)
ax.bar(time2+0.5*width12backup, np.mean(elon4000top3,axis=0)*100, yerr=np.std(elon4000top3,axis=0)*100, alpha=0.9, color=color3, ecolor='black', capsize=2, width=width12backup)
ax.bar(time1-0.5*width12backup, np.mean(elon1600bottom3,axis=0)*100, yerr=np.std(elon1600bottom3,axis=0)*100, hatch='////', color='none', edgecolor=color2, ecolor='black', capsize=2, width=width12backup)
ax.bar(time2+1.5*width12backup, np.mean(elon4000bottom3,axis=0)*100, yerr=np.std(elon4000bottom3,axis=0)*100, hatch='////', color='none', edgecolor=color3, ecolor='black', capsize=2, width=width12backup)

ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Rate of elongation $>$ 600 $1/s$', fontsize=fontsize)

ax.set_ylim(0,)

plt.xticks(time1, labels=labels)
ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=2,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('TBelonRatio.png',bbox_inches='tight')
plt.show()

## Elongation rate ratio -- zoom in
fig, ax = plt.subplots(figsize=(12, 4))
bars = ax.bar(time3, np.mean(elon1600bottom3,axis=0)*100, hatch='//', color='none', edgecolor=color2, ecolor='black', capsize=6, width=width12)

ax.bar_label(bars,fmt='%0.3f',fontsize=20)

ax.set_ylim(0,2)

plt.xticks(time3, labels=labels)
ax.tick_params(axis='x', labelsize= ticksizeZoom)
ax.tick_params(axis='y', labelsize= ticksizeZoom)

plt.savefig('TBelongRatio_zoom.png',bbox_inches='tight', transparent=True)
plt.show()