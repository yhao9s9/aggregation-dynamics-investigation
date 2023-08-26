import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

vf800d11min=np.load("data/density/d1_800/1min.npy")
vf800d12min=np.load("data/density/d1_800/2min.npy")
vf800d14min=np.load("data/density/d1_800/4min.npy")
vf800d16min=np.load("data/density/d1_800/6min.npy")
vf800d19min=np.load("data/density/d1_800/9min.npy")
vf800d112min=np.load("data/density/d1_800/12min.npy")

vf800d21min=np.load("data/density/d2_800/1min.npy")
vf800d22min=np.load("data/density/d2_800/2min.npy")
vf800d24min=np.load("data/density/d2_800/4min.npy")
vf800d26min=np.load("data/density/d2_800/6min.npy")
vf800d29min=np.load("data/density/d2_800/9min.npy")
vf800d212min=np.load("data/density/d2_800/12min.npy")

vf800d31min=np.load("data/density/d3_800/1min.npy")
vf800d32min=np.load("data/density/d3_800/2min.npy")
vf800d34min=np.load("data/density/d3_800/4min.npy")
vf800d36min=np.load("data/density/d3_800/6min.npy")
vf800d39min=np.load("data/density/d3_800/9min.npy")
vf800d312min=np.load("data/density/d3_800/12min.npy")

vf800d51min=np.load("data/density/d5_800/1min.npy")
vf800d52min=np.load("data/density/d5_800/2min.npy")
vf800d54min=np.load("data/density/d5_800/4min.npy")
vf800d56min=np.load("data/density/d5_800/6min.npy")
vf800d59min=np.load("data/density/d5_800/9min.npy")
vf800d512min=np.load("data/density/d5_800/12min.npy")

vf800d61min=np.load("data/density/d6_800/1min.npy")
vf800d62min=np.load("data/density/d6_800/2min.npy")
vf800d64min=np.load("data/density/d6_800/4min.npy")
vf800d66min=np.load("data/density/d6_800/6min.npy")
vf800d69min=np.load("data/density/d6_800/9min.npy")
vf800d612min=np.load("data/density/d6_800/12min.npy")


vf1600d21min=np.load("data/density/d2_1600/1min.npy")
vf1600d22min=np.load("data/density/d2_1600/2min.npy")
vf1600d24min=np.load("data/density/d2_1600/4min.npy")
vf1600d26min=np.load("data/density/d2_1600/6min.npy")
vf1600d29min=np.load("data/density/d2_1600/9min.npy")
vf1600d212min=np.load("data/density/d2_1600/12min.npy")

vf1600d31min=np.load("data/density/d3_1600/1min.npy")
vf1600d32min=np.load("data/density/d3_1600/2min.npy")
vf1600d34min=np.load("data/density/d3_1600/4min.npy")
vf1600d36min=np.load("data/density/d3_1600/6min.npy")
vf1600d39min=np.load("data/density/d3_1600/9min.npy")
vf1600d312min=np.load("data/density/d3_1600/12min.npy")

vf1600d41min=np.load("data/density/d4_1600/1min.npy")
vf1600d42min=np.load("data/density/d4_1600/2min.npy")
vf1600d44min=np.load("data/density/d4_1600/4min.npy")
vf1600d46min=np.load("data/density/d4_1600/6min.npy")
vf1600d49min=np.load("data/density/d4_1600/9min.npy")
vf1600d412min=np.load("data/density/d4_1600/12min.npy")

vf1600d51min=np.load("data/density/d5_1600/1min.npy")
vf1600d52min=np.load("data/density/d5_1600/2min.npy")
vf1600d54min=np.load("data/density/d5_1600/4min.npy")
vf1600d56min=np.load("data/density/d5_1600/6min.npy")
vf1600d59min=np.load("data/density/d5_1600/9min.npy")
vf1600d512min=np.load("data/density/d5_1600/12min.npy")

vf1600d61min=np.load("data/density/d6_1600/1min.npy")
vf1600d62min=np.load("data/density/d6_1600/2min.npy")
vf1600d64min=np.load("data/density/d6_1600/4min.npy")
vf1600d66min=np.load("data/density/d6_1600/6min.npy")
vf1600d69min=np.load("data/density/d6_1600/9min.npy")
vf1600d612min=np.load("data/density/d6_1600/12min.npy")


vf4000d21min=np.load("data/density/d2_4000/1min.npy")
vf4000d22min=np.load("data/density/d2_4000/2min.npy")
vf4000d24min=np.load("data/density/d2_4000/4min.npy")
vf4000d26min=np.load("data/density/d2_4000/6min.npy")
vf4000d29min=np.load("data/density/d2_4000/9min.npy")

vf4000d31min=np.load("data/density/d3_4000/1min.npy")
vf4000d32min=np.load("data/density/d3_4000/2min.npy")
vf4000d34min=np.load("data/density/d3_4000/4min.npy")
vf4000d36min=np.load("data/density/d3_4000/6min.npy")
vf4000d39min=np.load("data/density/d3_4000/9min.npy")
vf4000d312min=np.load("data/density/d3_4000/12min.npy")

vf4000d51min=np.load("data/density/d5_4000/1min.npy")
vf4000d52min=np.load("data/density/d5_4000/2min.npy")
vf4000d54min=np.load("data/density/d5_4000/4min.npy")
vf4000d56min=np.load("data/density/d5_4000/6min.npy")

vf4000d61min=np.load("data/density/d6_4000/1min.npy")
vf4000d62min=np.load("data/density/d6_4000/2min.npy")
vf4000d64min=np.load("data/density/d6_4000/4min.npy")
vf4000d66min=np.load("data/density/d6_4000/6min.npy")



time = np.array([1,2,4,6,9,12])

mean800d1 = np.array([np.mean(vf800d11min),np.mean(vf800d12min),np.mean(vf800d14min),np.mean(vf800d16min),np.mean(vf800d19min),np.mean(vf800d112min)])
mean800d2 = np.array([np.mean(vf800d21min),np.mean(vf800d22min),np.mean(vf800d24min),np.mean(vf800d26min),np.mean(vf800d29min),np.mean(vf800d212min)])
mean800d3 = np.array([np.mean(vf800d31min),np.mean(vf800d32min),np.mean(vf800d34min),np.mean(vf800d36min),np.mean(vf800d39min),np.mean(vf800d312min)])
mean800d5 = np.array([np.mean(vf800d51min),np.mean(vf800d52min),np.mean(vf800d54min),np.mean(vf800d56min),np.mean(vf800d59min),np.mean(vf800d512min)])
mean800d6 = np.array([np.mean(vf800d61min),np.mean(vf800d62min),np.mean(vf800d64min),np.mean(vf800d66min),np.mean(vf800d69min),np.mean(vf800d612min)])

mean1600d2 = np.array([np.mean(vf1600d21min),np.mean(vf1600d22min),np.mean(vf1600d24min),np.mean(vf1600d26min),np.mean(vf1600d29min),np.mean(vf1600d212min)])
mean1600d3 = np.array([np.mean(vf1600d31min),np.mean(vf1600d32min),np.mean(vf1600d34min),np.mean(vf1600d36min),np.mean(vf1600d39min),np.mean(vf1600d312min)])
mean1600d4 = np.array([np.mean(vf1600d41min),np.mean(vf1600d42min),np.mean(vf1600d44min),np.mean(vf1600d46min),np.mean(vf1600d49min),np.mean(vf1600d412min)])
mean1600d5 = np.array([np.mean(vf1600d51min),np.mean(vf1600d52min),np.mean(vf1600d54min),np.mean(vf1600d56min),np.mean(vf1600d59min),np.mean(vf1600d512min)])
mean1600d6 = np.array([np.mean(vf1600d61min),np.mean(vf1600d62min),np.mean(vf1600d64min),np.mean(vf1600d66min),np.mean(vf1600d69min),np.mean(vf1600d612min)])

mean4000d2 = np.array([np.mean(vf4000d21min),np.mean(vf4000d22min),np.mean(vf4000d24min),np.mean(vf4000d26min)])
mean4000d3 = np.array([np.mean(vf4000d31min),np.mean(vf4000d32min),np.mean(vf4000d34min),np.mean(vf4000d36min)])
mean4000d5 = np.array([np.mean(vf4000d51min),np.mean(vf4000d52min),np.mean(vf4000d54min),np.mean(vf4000d56min)])
mean4000d6 = np.array([np.mean(vf4000d61min),np.mean(vf4000d62min),np.mean(vf4000d64min),np.mean(vf4000d66min)])

mean800 = np.array([mean800d1,mean800d2,mean800d3,mean800d5,mean800d6])
mean1600 = np.array([mean1600d2,mean1600d3,mean1600d4,mean1600d5,mean1600d6])
mean4000 = np.array([mean4000d2,mean4000d3,mean4000d5,mean4000d6])

std800d1 = np.array([np.std(vf800d11min),np.std(vf800d12min),np.std(vf800d14min),np.std(vf800d16min),np.std(vf800d19min),np.std(vf800d112min)])
std800d2 = np.array([np.std(vf800d21min),np.std(vf800d22min),np.std(vf800d24min),np.std(vf800d26min),np.std(vf800d29min),np.std(vf800d212min)])
std800d3 = np.array([np.std(vf800d31min),np.std(vf800d32min),np.std(vf800d34min),np.std(vf800d36min),np.std(vf800d39min),np.std(vf800d312min)])
std800d5 = np.array([np.std(vf800d51min),np.std(vf800d52min),np.std(vf800d54min),np.std(vf800d56min),np.std(vf800d59min),np.std(vf800d512min)])
std800d6 = np.array([np.std(vf800d61min),np.std(vf800d62min),np.std(vf800d64min),np.std(vf800d66min),np.std(vf800d69min),np.std(vf800d612min)])

std1600d2 = np.array([np.std(vf1600d21min),np.std(vf1600d22min),np.std(vf1600d24min),np.std(vf1600d26min),np.std(vf1600d29min),np.std(vf1600d212min)])
std1600d3 = np.array([np.std(vf1600d31min),np.std(vf1600d32min),np.std(vf1600d34min),np.std(vf1600d36min),np.std(vf1600d39min),np.std(vf1600d312min)])
std1600d4 = np.array([np.std(vf1600d41min),np.std(vf1600d42min),np.std(vf1600d44min),np.std(vf1600d46min),np.std(vf1600d49min),np.std(vf1600d412min)])
std1600d5 = np.array([np.std(vf1600d51min),np.std(vf1600d52min),np.std(vf1600d54min),np.std(vf1600d56min),np.std(vf1600d59min),np.std(vf1600d512min)])
std1600d6 = np.array([np.std(vf1600d61min),np.std(vf1600d62min),np.std(vf1600d64min),np.std(vf1600d66min),np.std(vf1600d69min),np.std(vf1600d612min)])

std4000d2 = np.array([np.std(vf4000d21min),np.std(vf4000d22min),np.std(vf4000d24min),np.std(vf4000d26min),np.std(vf4000d29min)])
std4000d3 = np.array([np.std(vf4000d31min),np.std(vf4000d32min),np.std(vf4000d34min),np.std(vf4000d36min),np.std(vf4000d39min),np.std(vf4000d312min)])
std4000d5 = np.array([np.std(vf4000d51min),np.std(vf4000d52min),np.std(vf4000d54min),np.std(vf4000d56min)])
std4000d6 = np.array([np.std(vf4000d61min),np.std(vf4000d62min),np.std(vf4000d64min),np.std(vf4000d66min)])


labels=['1','2','4','6','9','12']
fontsize = 16
ticksize = 14

color1 = (235/255,153/255,156/255) ## pink
color2 = (161/255,125/255,180/255) ## purple
color3 = (142/255,165/255,200/255) ## blue
color4 = (131/255,157/255,68/255) ## green
color5 = (235/255,161/255,51/255) ## yellow
edgecolor = (102/255,100/255,100/255)



## average density
fig, ax = plt.subplots()
ax.plot(time[0:6],np.mean(mean800,axis=0),'^-', color=color1, markersize=6, label='800 1/s')
ax.fill_between(time[0:6],np.mean(mean800,axis=0)-np.std(mean800,axis=0), np.mean(mean800,axis=0)+np.std(mean800,axis=0), color=color1, alpha=0.3)
ax.plot(time[0:6],np.mean(mean1600,axis=0),'^-', color=color2, markersize=6, label='1600 1/s')
ax.fill_between(time[0:6],np.mean(mean1600,axis=0)-np.std(mean1600,axis=0), np.mean(mean1600,axis=0)+np.std(mean1600,axis=0), color=color2, alpha=0.3)
ax.plot(time[0:4],np.mean(mean4000,axis=0),'^-', color=color3, markersize=6, label='4000 1/s')
ax.fill_between(time[0:4],np.mean(mean4000,axis=0)-np.std(mean4000,axis=0), np.mean(mean4000,axis=0)+np.std(mean4000,axis=0), color=color3, alpha=0.3)

ax.set_ylabel('density $[V/V]$',fontsize=fontsize)
ax.set_xlabel('time $[min]$',fontsize=fontsize)
plt.title('Average density',fontsize=fontsize)

# ax.set_ylim(0,5)

ax.tick_params(axis='x', labelsize= ticksize)
ax.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=1,fontsize=12)
plt.grid(alpha=0.3)

plt.savefig('avD.png',bbox_inches='tight')
plt.show()

# ## average density -- 800 1/s
# fig, ax = plt.subplots()
# ax.plot(time[0:6],mean800d1,'^-', color=color1, markersize=6, label='case 1')
# # ax.fill_between(time[0:6],mean800d1-std800d1, mean800d1+std800d1, color=color1, alpha=0.3)
# ax.plot(time[0:6],mean800d2,'^-', color=color2, markersize=6, label='case 2')
# # ax.fill_between(time[0:6],mean800d2-std800d2, mean800d2+std800d2, color=color1, alpha=0.3)
# ax.plot(time[0:6],mean800d3,'^-', color=color3, markersize=6, label='case 3')
# # ax.fill_between(time[0:6],mean800d3-std800d3, mean800d3+std800d3, color=color1, alpha=0.3)
# ax.plot(time[0:6],mean800d5,'^-', color=color4, markersize=6, label='case 4')
# # ax.fill_between(time[0:6],mean800d5-std800d5, mean800d5+std800d5, color=color1, alpha=0.3)
# ax.plot(time[0:6],mean800d6,'^-', color=color5, markersize=6, label='case 5')
# # ax.fill_between(time[0:6],mean800d6-std800d6, mean800d6+std800d6, color=color1, alpha=0.3)

# ax.set_ylabel('average density $[V/V]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average density',fontsize=fontsize)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('avD800.png',bbox_inches='tight')
# plt.show()


# ## density distribution -- 800
# fig, ax = plt.subplots()
# sns.kdeplot(np.squeeze(vf800d21min), color=color1, label='1 min')
# sns.kdeplot(np.squeeze(vf800d22min), color=color2, label='2 min')
# sns.kdeplot(np.squeeze(vf800d24min), color=color3, label='4 min')
# sns.kdeplot(np.squeeze(vf800d26min), color=color4, label='6 min')
# sns.kdeplot(np.squeeze(vf800d29min), color=color5, label='9 min')
# sns.kdeplot(np.squeeze(vf800d212min), color=edgecolor, label='12 min')

# # ax.set_ylabel('average density $[V/V]$',fontsize=fontsize)
# # ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Density distribution -- 800 1/s',fontsize=fontsize)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('dD800.png',bbox_inches='tight')
# plt.show()