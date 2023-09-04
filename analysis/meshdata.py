import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Replace 'data.txt' with the actual path to your TXT file
def readdata(directory):
    file_path = directory

    data_list = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == '6 6' or line.strip() == '4 6' or line.strip() == '5 6':
                # Skip the header line
                continue
            # Split the line by whitespace and convert each element to a float
            row_data = [float(x) for x in line.split()]
            data_list.append(row_data)

    # Convert the list of lists to a NumPy array
    data_list.remove([])
    data_array = np.array(data_list)
    return data_array

data800 = readdata('../meshData/data800.txt')
data1600 = readdata('../meshData/data1600.txt')
data4000 = readdata('../meshData/data4000.txt')
# print(data800.shape)

# print(np.insert(data800[:6,0:5],0,0,axis=1).shape)

time = np.array([1,2,4,6,9,12])
time1 = np.array([1,3,5,7,9,11])
time2 = np.array([1,3,5,7])
grV800 = (data800[:6,0:6]-np.insert(data800[:6,0:5],0,0,axis=1))/(time[0:6]-np.insert(time[0:5],0,0))
grV1600 = (data1600[:5,0:6]-np.insert(data1600[:5,0:5],0,0,axis=1))/(time[0:6]-np.insert(time[0:5],0,0))
grV4000 = (data4000[1:4,0:4]-np.insert(data4000[1:4,0:3],0,0,axis=1))/(time[0:4]-np.insert(time[0:3],0,0))

grA800 = (data800[6:12,0:6]-np.insert(data800[6:12,0:5],0,0,axis=1))/(time[0:6]-np.insert(time[0:5],0,0))
grA1600 = (data1600[5:10,0:6]-np.insert(data1600[5:10,0:5],0,0,axis=1))/(time[0:6]-np.insert(time[0:5],0,0))
grA4000 = (data4000[5:8,0:4]-np.insert(data4000[5:8,0:3],0,0,axis=1))/(time[0:4]-np.insert(time[0:3],0,0))

grH800 = (data800[12:18,0:6]-np.insert(data800[12:18,0:5],0,0,axis=1))/(time[0:6]-np.insert(time[0:5],0,0))
grH1600 = (data1600[10:15,0:6]-np.insert(data1600[10:15,0:5],0,0,axis=1))/(time[0:6]-np.insert(time[0:5],0,0))
grH4000 = (data4000[9:12,0:4]-np.insert(data4000[9:12,0:3],0,0,axis=1))/(time[0:4]-np.insert(time[0:3],0,0))

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

# ### bottom area vs. time
# fig, ax = plt.subplots()
# ax.bar(time1-width, np.mean(data800[6:12,0:6],axis=0), yerr=np.std(data800[6:12,0:6],axis=0), alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width)
# ax.bar(time1, np.mean(data1600[5:10,0:6],axis=0), yerr=np.std(data1600[5:10,0:6],axis=0), alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width)
# ax.bar(time2+width, np.mean(data4000[5:8,0:4],axis=0), yerr=np.std(data4000[5:8,0:4],axis=0), alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width)
# # ax.bar(time-width, np.mean(data800[6:12,0:6],axis=0), alpha=0.5, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width)
# # ax.bar(time, np.mean(data1600[5:10,0:6],axis=0), alpha=0.5, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width)
# # ax.bar(time+width, np.mean(data4000[4:8,0:6],axis=0), alpha=0.5, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width)

# ax.set_ylabel('area $[\mu m^2]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average aggregation bottom area', fontsize=fontsize)

# # ax.set_xlim(3,12)
# ax.set_ylim(0,)

# plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=2,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('TB.png',bbox_inches='tight')
# plt.show()



# ### height vs. time
# fig, ax = plt.subplots()
# ax.bar(time1-width, np.mean(data800[12:18,0:6],axis=0), yerr=np.std(data800[12:18,0:6],axis=0), alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width)
# ax.bar(time1, np.mean(data1600[10:15,0:6],axis=0), yerr=np.std(data1600[10:15,0:6],axis=0), alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width)
# ax.bar(time2+width, np.mean(data4000[9:12,0:4],axis=0), yerr=np.std(data4000[9:12,0:4],axis=0), alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width)

# ax.set_ylabel('average height $[\mu m]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average aggregation height', fontsize=fontsize)

# # ax.set_xlim(3,12)
# ax.set_ylim(0,)

# plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=2,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('TH.png',bbox_inches='tight')
# plt.show()


# ### average ratio (height/bottom area) vs. time
# fig, ax = plt.subplots()
# ax.bar(time1-width, np.mean(data800[12:18,0:6]/data800[6:12,0:6],axis=0), yerr=np.std(data800[12:18,0:6]/data800[6:12,0:6],axis=0), alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width)
# ax.bar(time1, np.mean(data1600[10:15,0:6]/data1600[5:10,0:6],axis=0), yerr=np.std(data1600[10:15,0:6]/data1600[5:10,0:6],axis=0), alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width)
# ax.bar(time2+width, np.mean(data4000[9:12,0:4]/data4000[5:8,0:4],axis=0), yerr=np.std(data4000[9:12,0:4]/data4000[5:8,0:4],axis=0), alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width)

# ax.set_ylabel('ratio $[1/\mu m]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average ratio of aggregation height \n with bottom area',fontsize=fontsize)

# # ax.set_xlim(3,12)
# # ax.set_ylim(0,3)

# plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('arHB.png',bbox_inches='tight')
# plt.show()



# ### average ratio (height/length) vs. time
# fig, ax = plt.subplots()
# ax.bar(time1-width, np.mean(data800[12:18,0:6]/data800[18:24,0:6],axis=0), yerr=np.std(data800[12:18,0:6]/data800[18:24,0:6],axis=0), alpha=0.9, color=color1, ecolor='black', capsize=2, label='800 1/s', width=width)
# ax.bar(time1, np.mean(data1600[10:15,0:6]/data1600[15:20,0:6],axis=0), yerr=np.std(data1600[10:15,0:6]/data1600[15:20,0:6],axis=0), alpha=0.9, color=color2, ecolor='black', capsize=2, label='1600 1/s', width=width)
# ax.bar(time2+width, np.mean(data4000[9:12,0:4]/data4000[13:16,0:4],axis=0), yerr=np.std(data4000[9:12,0:4]/data4000[13:16,0:4],axis=0), alpha=0.9, color=color3, ecolor='black', capsize=2, label='4000 1/s', width=width)

# ax.set_ylabel('ratio',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average ratio of aggregation height \n with maximum length',fontsize=fontsize)

# # ax.set_ylim(0,60000)

# plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('arHL.png',bbox_inches='tight')
# plt.show()



## average growth rate - maximum height
fig, ax = plt.subplots()
ax.plot(time[0:6],np.mean(grH800,axis=0),'^--', color=color1, markersize=6, label='800 1/s')
ax.fill_between(time[0:6],np.mean(grH800,axis=0)-np.std(grH800,axis=0), np.mean(grH800,axis=0)+np.std(grH800,axis=0), color=color1, alpha=0.3)
ax.plot(time[0:6],np.mean(grH1600,axis=0),'o--', color=color2, markersize=6,label='1600 1/s')
ax.fill_between(time[0:6],np.mean(grH1600,axis=0)-np.std(grH1600,axis=0), np.mean(grH1600,axis=0)+np.std(grH1600,axis=0), color=color2, alpha=0.3)
ax.plot(time[0:4],np.mean(grH4000,axis=0),'s--', color=color3, markersize=6,label='4000 1/s')
ax.fill_between(time[0:4],np.mean(grH4000,axis=0)-np.std(grH4000,axis=0), np.mean(grH4000,axis=0)+np.std(grH4000,axis=0), color=color3, alpha=0.3)

ax.set_ylabel('growth rate $[\mu m/min]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average growth rate -- aggregation height',fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('grH.png',bbox_inches='tight')
plt.show()


# print('aggregate height growth rate: \n800: \nmean: ',np.mean(grH800,axis=0),"\nstd: ",np.std(grH800,axis=0) \
#       , '\n1600: \nmean: ',np.mean(grH1600,axis=0),"\nstd: ",np.std(grH1600,axis=0) \
#       , '\n4000: \nmean: ',np.mean(grH4000,axis=0),"\nstd: ",np.std(grH4000,axis=0))


## average growth rate - bottom area
fig, ax = plt.subplots()
ax.plot(time[0:6],np.mean(grA800,axis=0),'^--', color=color1, markersize=6, label='800 1/s')
ax.fill_between(time[0:6],np.mean(grA800,axis=0)-np.std(grA800,axis=0), np.mean(grA800,axis=0)+np.std(grA800,axis=0), color=color1, alpha=0.3)
ax.plot(time[0:6],np.mean(grA1600,axis=0),'o--', color=color2, markersize=6,label='1600 1/s')
ax.fill_between(time[0:6],np.mean(grA1600,axis=0)-np.std(grA1600,axis=0), np.mean(grA1600,axis=0)+np.std(grA1600,axis=0), color=color2, alpha=0.3)
ax.plot(time[0:4],np.mean(grA4000,axis=0),'s--', color=color3, markersize=6,label='4000 1/s')
ax.fill_between(time[0:4],np.mean(grA4000,axis=0)-np.std(grA4000,axis=0), np.mean(grA4000,axis=0)+np.std(grA4000,axis=0), color=color3, alpha=0.3)

ax.set_ylabel('growth rate $[\mu m^2/min]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average growth rate -- aggregation bottom area',fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('grA.png',bbox_inches='tight')
plt.show()


# print('aggregate bottom area growth rate: \n800: \nmean: ',np.mean(grA800,axis=0),"\nstd: ",np.std(grA800,axis=0) \
#       , '\n1600: \nmean: ',np.mean(grA1600,axis=0),"\nstd: ",np.std(grA1600,axis=0) \
#       , '\n4000: \nmean: ',np.mean(grA4000,axis=0),"\nstd: ",np.std(grA4000,axis=0))


### average growth rate - volume
fig, ax = plt.subplots()
ax.plot(time[0:6],np.mean(grV800,axis=0),'^--', color=color1, markersize=6, label='800 1/s')
ax.fill_between(time[0:6],np.mean(grV800,axis=0)-np.std(grV800,axis=0), np.mean(grV800,axis=0)+np.std(grV800,axis=0), color=color1, alpha=0.3)
ax.plot(time[0:6],np.mean(grV1600,axis=0),'o--', color=color2, markersize=6, label='1600 1/s')
ax.fill_between(time[0:6],np.mean(grV1600,axis=0)-np.std(grV1600,axis=0), np.mean(grV1600,axis=0)+np.std(grV1600,axis=0), color=color2, alpha=0.3)
ax.plot(time[0:4],np.mean(grV4000,axis=0),'s--', color=color3, markersize=6, label='4000 1/s')
ax.fill_between(time[0:4],np.mean(grV4000,axis=0)-np.std(grV4000,axis=0), np.mean(grV4000,axis=0)+np.std(grV4000,axis=0), color=color3, alpha=0.3)

ax.set_ylabel('growth rate $[\mu m^3/min]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average growth rate -- aggregation volume',fontsize=fontsize)

# ax.set_ylim(-250,1700)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('grV.png',bbox_inches='tight')
plt.show()


# print('aggregate volume growth rate: \n800: \nmean: ',np.mean(grV800,axis=0),"\nstd: ",np.std(grV800,axis=0) \
#       , '\n1600: \nmean: ',np.mean(grV1600,axis=0),"\nstd: ",np.std(grV1600,axis=0) \
#       , '\n4000: \nmean: ',np.mean(grV4000,axis=0),"\nstd: ",np.std(grV4000,axis=0))


### average growth rate - volume zooming
fig, ax = plt.subplots()
ax.plot(time[0:6],np.mean(grV800,axis=0),'^--', color=color1, markersize=6, label='800 1/s')
ax.fill_between(time[0:6],np.mean(grV800,axis=0)-np.std(grV800,axis=0), np.mean(grV800,axis=0)+np.std(grV800,axis=0), color=color1, alpha=0.3)
ax.plot(time[0:6],np.mean(grV1600,axis=0),'o--', color=color2, markersize=6, label='1600 1/s')
ax.fill_between(time[0:6],np.mean(grV1600,axis=0)-np.std(grV1600,axis=0), np.mean(grV1600,axis=0)+np.std(grV1600,axis=0), color=color2, alpha=0.3)

ax.set_ylabel('growth rate $[\mu m^3/min]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)

ax.set_ylim(-250,1700)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('grV_zooming.png',bbox_inches='tight')
plt.show()


### distribution of aggregate volume
# fig, ax = plt.subplots()
# bp1=ax.boxplot(data800[0:6,:],vert=True,sym='',patch_artist=True, labels=labels,
#                     boxprops=dict(facecolor=color1, color=color1),
#                     capprops=dict(color=color1),
#                     whiskerprops=dict(color=color1),
#                     flierprops=dict(color=color1, markeredgecolor=color1),
#                     medianprops=dict(color=color1))
# bp2=ax.boxplot(data1600[0:5,:],vert=True,sym='',patch_artist=True, labels=labels,
#                     boxprops=dict(facecolor=color2, color=color2),
#                     capprops=dict(color=color2),
#                     whiskerprops=dict(color=color2),
#                     flierprops=dict(color=color2, markeredgecolor=color2),
#                     medianprops=dict(color=color2))

# ax.set_ylabel('volume $[\mu m^3]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)

# # ax.set_ylim(0,7000)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# # ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]], ['800 1/s', '1600 1/s', '4000 1/s'], loc=2, fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('vD2.png',bbox_inches='tight')
# plt.show()



# ### distribution of aggregate volume
# fig, ax = plt.subplots()
# bp1=ax.boxplot(data800[0:6,:],vert=True,sym='',patch_artist=True, labels=labels,
#                     boxprops=dict(facecolor=color1, color=color1),
#                     capprops=dict(color=color1),
#                     whiskerprops=dict(color=color1),
#                     flierprops=dict(color=color1, markeredgecolor=color1),
#                     medianprops=dict(color=color1))
# bp2=ax.boxplot(data1600[0:5,:],vert=True,sym='',patch_artist=True, labels=labels,
#                     boxprops=dict(facecolor=color2, color=color2),
#                     capprops=dict(color=color2),
#                     whiskerprops=dict(color=color2),
#                     flierprops=dict(color=color2, markeredgecolor=color2),
#                     medianprops=dict(color=color2))
# bp3=ax.boxplot(data4000[1:4,0:4],vert=True,sym='',patch_artist=True, labels=labels[:4],
#                     boxprops=dict(facecolor=color3, color=color3),
#                     capprops=dict(color=color3),
#                     whiskerprops=dict(color=color3),
#                     flierprops=dict(color=color3, markeredgecolor=color3),
#                     medianprops=dict(color=color3))

# ax.set_ylabel('volume $[\mu m^3]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average platelet aggregation volume',fontsize=fontsize)

# # ax.set_ylim(0,7000)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]], ['800 1/s', '1600 1/s', '4000 1/s'], loc=2, fontsize=12)
# # ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]], ['800 1/s', '1600 1/s', '4000 1/s'], loc=2, fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('vD3.png',bbox_inches='tight')
# plt.show()



### distribution of aggregate height
# fig, ax = plt.subplots()
# bp1=ax.boxplot(data800[12:18,:],vert=True,sym='',patch_artist=True, labels=labels,
#                     boxprops=dict(facecolor=color1, color=color1),
#                     capprops=dict(color=color1),
#                     whiskerprops=dict(color=color1),
#                     flierprops=dict(color=color1, markeredgecolor=color1),
#                     medianprops=dict(color=color1))
# bp2=ax.boxplot(data1600[10:15,:],vert=True,sym='',patch_artist=True, labels=labels,
#                     boxprops=dict(facecolor=color2, color=color2),
#                     capprops=dict(color=color2),
#                     whiskerprops=dict(color=color2),
#                     flierprops=dict(color=color2, markeredgecolor=color2),
#                     medianprops=dict(color=color2))
# bp3=ax.boxplot(data4000[9:12,0:4],vert=True,sym='',patch_artist=True, labels=labels[:4],
#                     boxprops=dict(facecolor=color3, color=color3),
#                     capprops=dict(color=color3),
#                     whiskerprops=dict(color=color3),
#                     flierprops=dict(color=color3, markeredgecolor=color3),
#                     medianprops=dict(color=color3))

# ax.set_ylabel('height $[\mu m]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average platelet aggregation height',fontsize=fontsize)

# # ax.set_ylim(0,7000)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]], ['800 1/s', '1600 1/s', '4000 1/s'], loc=2, fontsize=12)
# # ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]], ['800 1/s', '1600 1/s', '4000 1/s'], loc=2, fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('hD3.png',bbox_inches='tight')
# plt.show()



####------------------------------------------------NOT USING------------------------------------------------####
# ### average maximum length vs. time
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(data800[18:24,0:6],axis=0),'*-',color=color1,label='800 1/s')
# ax.fill_between(time[0:6],np.mean(data800[18:24,0:6],axis=0)-np.std(data800[18:24,0:6],axis=0), np.mean(data800[18:24,0:6],axis=0)+np.std(data800[18:24,0:6],axis=0), color=color1, alpha=0.3)
# ax.plot(time[0:6],np.mean(data1600[15:20,0:6],axis=0),'*-',color=color2,label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(data1600[15:20,0:6],axis=0)-np.std(data1600[15:20,0:6],axis=0), np.mean(data1600[15:20,0:6],axis=0)+np.std(data1600[15:20,0:6],axis=0), color=color2, alpha=0.3)
# ax.plot(time[0:4],np.mean(data4000[12:16,0:4],axis=0),'*-',color=color3,label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(data4000[12:16,0:4],axis=0)-np.std(data4000[12:16,0:4],axis=0), np.mean(data4000[12:16,0:4],axis=0)+np.std(data4000[12:16,0:4],axis=0), color=color3, alpha=0.3)

# ax.set_ylabel('average maximum length $[\mu m]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)

# # ax.set_ylim(0,60000)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('avL.png',bbox_inches='tight')
# plt.show()


# ### average maximum height vs. time
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(data800[12:18,0:6],axis=0),'*-',color=color1,label='800 1/s')
# ax.fill_between(time[0:6],np.mean(data800[12:18,0:6],axis=0)-np.std(data800[12:18,0:6],axis=0), np.mean(data800[12:18,0:6],axis=0)+np.std(data800[12:18,0:6],axis=0), color=color1, alpha=0.3)
# ax.plot(time[0:6],np.mean(data1600[10:15,0:6],axis=0),'*-',color=color2,label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(data1600[10:15,0:6],axis=0)-np.std(data1600[10:15,0:6],axis=0), np.mean(data1600[10:15,0:6],axis=0)+np.std(data1600[10:15,0:6],axis=0), color=color2, alpha=0.3)
# ax.plot(time[0:4],np.mean(data4000[8:12,0:4],axis=0),'*-',color=color3,label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(data4000[8:12,0:4],axis=0)-np.std(data4000[8:12,0:4],axis=0), np.mean(data4000[8:12,0:4],axis=0)+np.std(data4000[8:12,0:4],axis=0), color=color3, alpha=0.3)

# ax.set_ylabel('average height $[\mu m]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)

# # ax.set_ylim(0,60000)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('avH.png',bbox_inches='tight')
# plt.show()


### average volume vs. time
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(data800[:6,0:6],axis=0),'*-',color=color1,label='800 1/s')
# ax.fill_between(time[0:6],np.mean(data800[:6,0:6],axis=0)-np.std(data800[:6,0:6],axis=0), np.mean(data800[:6,0:6],axis=0)+np.std(data800[:6,0:6],axis=0), color=color1, alpha=0.3)
# ax.plot(time[0:6],np.mean(data1600[:5,0:6],axis=0),'*-',color=color2,label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(data1600[:5,0:6],axis=0)-np.std(data1600[:5,0:6],axis=0), np.mean(data1600[:5,0:6],axis=0)+np.std(data1600[:5,0:6],axis=0), color=color2, alpha=0.3)
# ax.plot(time[0:4],np.mean(data4000[:4,0:4],axis=0),'*-',color=color3,label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(data4000[:4,0:4],axis=0)-np.std(data4000[:4,0:4],axis=0), np.mean(data4000[:4,0:4],axis=0)+np.std(data4000[:4,0:4],axis=0), color=color3, alpha=0.3)

# ax.set_ylabel('average volume $[\mu m^3]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)

# ax.set_ylim(0,60000)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('avV.png',bbox_inches='tight')
# plt.show()

