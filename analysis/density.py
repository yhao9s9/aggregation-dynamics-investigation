## This script exclude d2_4000 from analysis

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


## High density
highvf800d11min = np.array([vf800d11min[vf800d11min>0.6]])
highvf800d12min = np.array([vf800d12min[vf800d12min>0.6]])
highvf800d14min = np.array([vf800d14min[vf800d14min>0.6]])
highvf800d16min = np.array([vf800d16min[vf800d16min>0.6]])
highvf800d19min = np.array([vf800d19min[vf800d19min>0.6]])
highvf800d112min = np.array([vf800d112min[vf800d112min>0.6]])

highvf800d21min = np.array([vf800d21min[vf800d21min>0.6]])
highvf800d22min = np.array([vf800d22min[vf800d22min>0.6]])
highvf800d24min = np.array([vf800d24min[vf800d24min>0.6]])
highvf800d26min = np.array([vf800d26min[vf800d26min>0.6]])
highvf800d29min = np.array([vf800d29min[vf800d29min>0.6]])
highvf800d212min = np.array([vf800d212min[vf800d212min>0.6]])

highvf800d31min = np.array([vf800d31min[vf800d31min>0.6]])
highvf800d32min = np.array([vf800d32min[vf800d32min>0.6]])
highvf800d34min = np.array([vf800d34min[vf800d34min>0.6]])
highvf800d36min = np.array([vf800d36min[vf800d36min>0.6]])
highvf800d39min = np.array([vf800d39min[vf800d39min>0.6]])
highvf800d312min = np.array([vf800d312min[vf800d312min>0.6]])

highvf800d51min = np.array([vf800d51min[vf800d51min>0.6]])
highvf800d52min = np.array([vf800d52min[vf800d52min>0.6]])
highvf800d54min = np.array([vf800d54min[vf800d54min>0.6]])
highvf800d56min = np.array([vf800d56min[vf800d56min>0.6]])
highvf800d59min = np.array([vf800d59min[vf800d59min>0.6]])
highvf800d512min = np.array([vf800d512min[vf800d512min>0.6]])

highvf800d61min = np.array([vf800d61min[vf800d61min>0.6]])
highvf800d62min = np.array([vf800d62min[vf800d62min>0.6]])
highvf800d64min = np.array([vf800d64min[vf800d64min>0.6]])
highvf800d66min = np.array([vf800d66min[vf800d66min>0.6]])
highvf800d69min = np.array([vf800d69min[vf800d69min>0.6]])
highvf800d612min = np.array([vf800d612min[vf800d612min>0.6]])

highvf1600d21min = np.array([vf1600d21min[vf1600d21min>0.6]])
highvf1600d22min = np.array([vf1600d22min[vf1600d22min>0.6]])
highvf1600d24min = np.array([vf1600d24min[vf1600d24min>0.6]])
highvf1600d26min = np.array([vf1600d26min[vf1600d26min>0.6]])
highvf1600d29min = np.array([vf1600d29min[vf1600d29min>0.6]])
highvf1600d212min = np.array([vf1600d212min[vf1600d212min>0.6]])

highvf1600d31min = np.array([vf1600d31min[vf1600d31min>0.6]])
highvf1600d32min = np.array([vf1600d32min[vf1600d32min>0.6]])
highvf1600d34min = np.array([vf1600d34min[vf1600d34min>0.6]])
highvf1600d36min = np.array([vf1600d36min[vf1600d36min>0.6]])
highvf1600d39min = np.array([vf1600d39min[vf1600d39min>0.6]])
highvf1600d312min = np.array([vf1600d312min[vf1600d312min>0.6]])

highvf1600d41min = np.array([vf1600d41min[vf1600d41min>0.6]])
highvf1600d42min = np.array([vf1600d42min[vf1600d42min>0.6]])
highvf1600d44min = np.array([vf1600d44min[vf1600d44min>0.6]])
highvf1600d46min = np.array([vf1600d46min[vf1600d46min>0.6]])
highvf1600d49min = np.array([vf1600d49min[vf1600d49min>0.6]])
highvf1600d412min = np.array([vf1600d412min[vf1600d412min>0.6]])

highvf1600d51min = np.array([vf1600d51min[vf1600d51min>0.6]])
highvf1600d52min = np.array([vf1600d52min[vf1600d52min>0.6]])
highvf1600d54min = np.array([vf1600d54min[vf1600d54min>0.6]])
highvf1600d56min = np.array([vf1600d56min[vf1600d56min>0.6]])
highvf1600d59min = np.array([vf1600d59min[vf1600d59min>0.6]])
highvf1600d512min = np.array([vf1600d512min[vf1600d512min>0.6]])

highvf1600d61min = np.array([vf1600d61min[vf1600d61min>0.6]])
highvf1600d62min = np.array([vf1600d62min[vf1600d62min>0.6]])
highvf1600d64min = np.array([vf1600d64min[vf1600d64min>0.6]])
highvf1600d66min = np.array([vf1600d66min[vf1600d66min>0.6]])
highvf1600d69min = np.array([vf1600d69min[vf1600d69min>0.6]])
highvf1600d612min = np.array([vf1600d612min[vf1600d612min>0.6]])

highvf4000d31min = np.array([vf4000d31min[vf4000d31min>0.6]])
highvf4000d32min = np.array([vf4000d32min[vf4000d32min>0.6]])
highvf4000d34min = np.array([vf4000d34min[vf4000d34min>0.6]])
highvf4000d36min = np.array([vf4000d36min[vf4000d36min>0.6]])
highvf4000d39min = np.array([vf4000d39min[vf4000d39min>0.6]])
highvf4000d312min = np.array([vf4000d312min[vf4000d312min>0.6]])

highvf4000d51min = np.array([vf4000d51min[vf4000d51min>0.6]])
highvf4000d52min = np.array([vf4000d52min[vf4000d52min>0.6]])
highvf4000d54min = np.array([vf4000d54min[vf4000d54min>0.6]])
highvf4000d56min = np.array([vf4000d56min[vf4000d56min>0.6]])

highvf4000d61min = np.array([vf4000d61min[vf4000d61min>0.6]])
highvf4000d62min = np.array([vf4000d62min[vf4000d62min>0.6]])
highvf4000d64min = np.array([vf4000d64min[vf4000d64min>0.6]])
highvf4000d66min = np.array([vf4000d66min[vf4000d66min>0.6]])


## Middle density
midvf800d11min = np.array([vf800d11min[(vf800d11min>=0.4)&(vf800d11min<=0.6)]])
midvf800d12min = np.array([vf800d12min[(vf800d12min>=0.4)&(vf800d12min<=0.6)]])
midvf800d14min = np.array([vf800d14min[(vf800d14min>=0.4)&(vf800d14min<=0.6)]])
midvf800d16min = np.array([vf800d16min[(vf800d16min>=0.4)&(vf800d16min<=0.6)]])
midvf800d19min = np.array([vf800d19min[(vf800d19min>=0.4)&(vf800d19min<=0.6)]])
midvf800d112min = np.array([vf800d112min[(vf800d112min>=0.4)&(vf800d112min<=0.6)]])

midvf800d21min = np.array([vf800d21min[(vf800d21min>=0.4)&(vf800d21min<=0.6)]])
midvf800d22min = np.array([vf800d22min[(vf800d22min>=0.4)&(vf800d22min<=0.6)]])
midvf800d24min = np.array([vf800d24min[(vf800d24min>=0.4)&(vf800d24min<=0.6)]])
midvf800d26min = np.array([vf800d26min[(vf800d26min>=0.4)&(vf800d26min<=0.6)]])
midvf800d29min = np.array([vf800d29min[(vf800d29min>=0.4)&(vf800d29min<=0.6)]])
midvf800d212min = np.array([vf800d212min[(vf800d212min>=0.4)&(vf800d212min<=0.6)]])

midvf800d31min = np.array([vf800d31min[(vf800d31min>=0.4)&(vf800d31min<=0.6)]])
midvf800d32min = np.array([vf800d32min[(vf800d32min>=0.4)&(vf800d32min<=0.6)]])
midvf800d34min = np.array([vf800d34min[(vf800d34min>=0.4)&(vf800d34min<=0.6)]])
midvf800d36min = np.array([vf800d36min[(vf800d36min>=0.4)&(vf800d36min<=0.6)]])
midvf800d39min = np.array([vf800d39min[(vf800d39min>=0.4)&(vf800d39min<=0.6)]])
midvf800d312min = np.array([vf800d312min[(vf800d312min>=0.4)&(vf800d312min<=0.6)]])

midvf800d51min = np.array([vf800d51min[(vf800d51min>=0.4)&(vf800d51min<=0.6)]])
midvf800d52min = np.array([vf800d52min[(vf800d52min>=0.4)&(vf800d52min<=0.6)]])
midvf800d54min = np.array([vf800d54min[(vf800d54min>=0.4)&(vf800d54min<=0.6)]])
midvf800d56min = np.array([vf800d56min[(vf800d56min>=0.4)&(vf800d56min<=0.6)]])
midvf800d59min = np.array([vf800d59min[(vf800d59min>=0.4)&(vf800d59min<=0.6)]])
midvf800d512min = np.array([vf800d512min[(vf800d512min>=0.4)&(vf800d512min<=0.6)]])

midvf800d61min = np.array([vf800d61min[(vf800d61min>=0.4)&(vf800d61min<=0.6)]])
midvf800d62min = np.array([vf800d62min[(vf800d62min>=0.4)&(vf800d62min<=0.6)]])
midvf800d64min = np.array([vf800d64min[(vf800d64min>=0.4)&(vf800d64min<=0.6)]])
midvf800d66min = np.array([vf800d66min[(vf800d66min>=0.4)&(vf800d66min<=0.6)]])
midvf800d69min = np.array([vf800d69min[(vf800d69min>=0.4)&(vf800d69min<=0.6)]])
midvf800d612min = np.array([vf800d612min[(vf800d612min>=0.4)&(vf800d612min<=0.6)]])

midvf1600d21min = np.array([vf1600d21min[(vf1600d21min>=0.4)&(vf1600d21min<=0.6)]])
midvf1600d22min = np.array([vf1600d22min[(vf1600d22min>=0.4)&(vf1600d22min<=0.6)]])
midvf1600d24min = np.array([vf1600d24min[(vf1600d24min>=0.4)&(vf1600d24min<=0.6)]])
midvf1600d26min = np.array([vf1600d26min[(vf1600d26min>=0.4)&(vf1600d26min<=0.6)]])
midvf1600d29min = np.array([vf1600d29min[(vf1600d29min>=0.4)&(vf1600d29min<=0.6)]])
midvf1600d212min = np.array([vf1600d212min[(vf1600d212min>=0.4)&(vf1600d212min<=0.6)]])

midvf1600d31min = np.array([vf1600d31min[(vf1600d31min>=0.4)&(vf1600d31min<=0.6)]])
midvf1600d32min = np.array([vf1600d32min[(vf1600d32min>=0.4)&(vf1600d32min<=0.6)]])
midvf1600d34min = np.array([vf1600d34min[(vf1600d34min>=0.4)&(vf1600d34min<=0.6)]])
midvf1600d36min = np.array([vf1600d36min[(vf1600d36min>=0.4)&(vf1600d36min<=0.6)]])
midvf1600d39min = np.array([vf1600d39min[(vf1600d39min>=0.4)&(vf1600d39min<=0.6)]])
midvf1600d312min = np.array([vf1600d312min[(vf1600d312min>=0.4)&(vf1600d312min<=0.6)]])

midvf1600d41min = np.array([vf1600d41min[(vf1600d41min>=0.4)&(vf1600d41min<=0.6)]])
midvf1600d42min = np.array([vf1600d42min[(vf1600d42min>=0.4)&(vf1600d42min<=0.6)]])
midvf1600d44min = np.array([vf1600d44min[(vf1600d44min>=0.4)&(vf1600d44min<=0.6)]])
midvf1600d46min = np.array([vf1600d46min[(vf1600d46min>=0.4)&(vf1600d46min<=0.6)]])
midvf1600d49min = np.array([vf1600d49min[(vf1600d49min>=0.4)&(vf1600d49min<=0.6)]])
midvf1600d412min = np.array([vf1600d412min[(vf1600d412min>=0.4)&(vf1600d412min<=0.6)]])

midvf1600d51min = np.array([vf1600d51min[(vf1600d51min>=0.4)&(vf1600d51min<=0.6)]])
midvf1600d52min = np.array([vf1600d52min[(vf1600d52min>=0.4)&(vf1600d52min<=0.6)]])
midvf1600d54min = np.array([vf1600d54min[(vf1600d54min>=0.4)&(vf1600d54min<=0.6)]])
midvf1600d56min = np.array([vf1600d56min[(vf1600d56min>=0.4)&(vf1600d56min<=0.6)]])
midvf1600d59min = np.array([vf1600d59min[(vf1600d59min>=0.4)&(vf1600d59min<=0.6)]])
midvf1600d512min = np.array([vf1600d512min[(vf1600d512min>=0.4)&(vf1600d512min<=0.6)]])

midvf1600d61min = np.array([vf1600d61min[(vf1600d61min>=0.4)&(vf1600d61min<=0.6)]])
midvf1600d62min = np.array([vf1600d62min[(vf1600d62min>=0.4)&(vf1600d62min<=0.6)]])
midvf1600d64min = np.array([vf1600d64min[(vf1600d64min>=0.4)&(vf1600d64min<=0.6)]])
midvf1600d66min = np.array([vf1600d66min[(vf1600d66min>=0.4)&(vf1600d66min<=0.6)]])
midvf1600d69min = np.array([vf1600d69min[(vf1600d69min>=0.4)&(vf1600d69min<=0.6)]])
midvf1600d612min = np.array([vf1600d612min[(vf1600d612min>=0.4)&(vf1600d612min<=0.6)]])

midvf4000d31min = np.array([vf4000d31min[(vf4000d31min>=0.4)&(vf4000d31min<=0.6)]])
midvf4000d32min = np.array([vf4000d32min[(vf4000d32min>=0.4)&(vf4000d32min<=0.6)]])
midvf4000d34min = np.array([vf4000d34min[(vf4000d34min>=0.4)&(vf4000d34min<=0.6)]])
midvf4000d36min = np.array([vf4000d36min[(vf4000d36min>=0.4)&(vf4000d36min<=0.6)]])
midvf4000d39min = np.array([vf4000d39min[(vf4000d39min>=0.4)&(vf4000d39min<=0.6)]])
midvf4000d312min = np.array([vf4000d312min[(vf4000d312min>=0.4)&(vf4000d312min<=0.6)]])

midvf4000d51min = np.array([vf4000d51min[(vf4000d51min>=0.4)&(vf4000d51min<=0.6)]])
midvf4000d52min = np.array([vf4000d52min[(vf4000d52min>=0.4)&(vf4000d52min<=0.6)]])
midvf4000d54min = np.array([vf4000d54min[(vf4000d54min>=0.4)&(vf4000d54min<=0.6)]])
midvf4000d56min = np.array([vf4000d56min[(vf4000d56min>=0.4)&(vf4000d56min<=0.6)]])

midvf4000d61min = np.array([vf4000d61min[(vf4000d61min>=0.4)&(vf4000d61min<=0.6)]])
midvf4000d62min = np.array([vf4000d62min[(vf4000d62min>=0.4)&(vf4000d62min<=0.6)]])
midvf4000d64min = np.array([vf4000d64min[(vf4000d64min>=0.4)&(vf4000d64min<=0.6)]])
midvf4000d66min = np.array([vf4000d66min[(vf4000d66min>=0.4)&(vf4000d66min<=0.6)]])

## Low density
lowvf800d11min = np.array([vf800d11min[vf800d11min<0.4]])
lowvf800d12min = np.array([vf800d12min[vf800d12min<0.4]])
lowvf800d14min = np.array([vf800d14min[vf800d14min<0.4]])
lowvf800d16min = np.array([vf800d16min[vf800d16min<0.4]])
lowvf800d19min = np.array([vf800d19min[vf800d19min<0.4]])
lowvf800d112min = np.array([vf800d112min[vf800d112min<0.4]])

lowvf800d21min = np.array([vf800d21min[vf800d21min<0.4]])
lowvf800d22min = np.array([vf800d22min[vf800d22min<0.4]])
lowvf800d24min = np.array([vf800d24min[vf800d24min<0.4]])
lowvf800d26min = np.array([vf800d26min[vf800d26min<0.4]])
lowvf800d29min = np.array([vf800d29min[vf800d29min<0.4]])
lowvf800d212min = np.array([vf800d212min[vf800d212min<0.4]])

lowvf800d31min = np.array([vf800d31min[vf800d31min<0.4]])
lowvf800d32min = np.array([vf800d32min[vf800d32min<0.4]])
lowvf800d34min = np.array([vf800d34min[vf800d34min<0.4]])
lowvf800d36min = np.array([vf800d36min[vf800d36min<0.4]])
lowvf800d39min = np.array([vf800d39min[vf800d39min<0.4]])
lowvf800d312min = np.array([vf800d312min[vf800d312min<0.4]])

lowvf800d51min = np.array([vf800d51min[vf800d51min<0.4]])
lowvf800d52min = np.array([vf800d52min[vf800d52min<0.4]])
lowvf800d54min = np.array([vf800d54min[vf800d54min<0.4]])
lowvf800d56min = np.array([vf800d56min[vf800d56min<0.4]])
lowvf800d59min = np.array([vf800d59min[vf800d59min<0.4]])
lowvf800d512min = np.array([vf800d512min[vf800d512min<0.4]])

lowvf800d61min = np.array([vf800d61min[vf800d61min<0.4]])
lowvf800d62min = np.array([vf800d62min[vf800d62min<0.4]])
lowvf800d64min = np.array([vf800d64min[vf800d64min<0.4]])
lowvf800d66min = np.array([vf800d66min[vf800d66min<0.4]])
lowvf800d69min = np.array([vf800d69min[vf800d69min<0.4]])
lowvf800d612min = np.array([vf800d612min[vf800d612min<0.4]])

lowvf1600d21min = np.array([vf1600d21min[vf1600d21min<0.4]])
lowvf1600d22min = np.array([vf1600d22min[vf1600d22min<0.4]])
lowvf1600d24min = np.array([vf1600d24min[vf1600d24min<0.4]])
lowvf1600d26min = np.array([vf1600d26min[vf1600d26min<0.4]])
lowvf1600d29min = np.array([vf1600d29min[vf1600d29min<0.4]])
lowvf1600d212min = np.array([vf1600d212min[vf1600d212min<0.4]])

lowvf1600d31min = np.array([vf1600d31min[vf1600d31min<0.4]])
lowvf1600d32min = np.array([vf1600d32min[vf1600d32min<0.4]])
lowvf1600d34min = np.array([vf1600d34min[vf1600d34min<0.4]])
lowvf1600d36min = np.array([vf1600d36min[vf1600d36min<0.4]])
lowvf1600d39min = np.array([vf1600d39min[vf1600d39min<0.4]])
lowvf1600d312min = np.array([vf1600d312min[vf1600d312min<0.4]])

lowvf1600d41min = np.array([vf1600d41min[vf1600d41min<0.4]])
lowvf1600d42min = np.array([vf1600d42min[vf1600d42min<0.4]])
lowvf1600d44min = np.array([vf1600d44min[vf1600d44min<0.4]])
lowvf1600d46min = np.array([vf1600d46min[vf1600d46min<0.4]])
lowvf1600d49min = np.array([vf1600d49min[vf1600d49min<0.4]])
lowvf1600d412min = np.array([vf1600d412min[vf1600d412min<0.4]])

lowvf1600d51min = np.array([vf1600d51min[vf1600d51min<0.4]])
lowvf1600d52min = np.array([vf1600d52min[vf1600d52min<0.4]])
lowvf1600d54min = np.array([vf1600d54min[vf1600d54min<0.4]])
lowvf1600d56min = np.array([vf1600d56min[vf1600d56min<0.4]])
lowvf1600d59min = np.array([vf1600d59min[vf1600d59min<0.4]])
lowvf1600d512min = np.array([vf1600d512min[vf1600d512min<0.4]])

lowvf1600d61min = np.array([vf1600d61min[vf1600d61min<0.4]])
lowvf1600d62min = np.array([vf1600d62min[vf1600d62min<0.4]])
lowvf1600d64min = np.array([vf1600d64min[vf1600d64min<0.4]])
lowvf1600d66min = np.array([vf1600d66min[vf1600d66min<0.4]])
lowvf1600d69min = np.array([vf1600d69min[vf1600d69min<0.4]])
lowvf1600d612min = np.array([vf1600d612min[vf1600d612min<0.4]])

lowvf4000d31min = np.array([vf4000d31min[vf4000d31min<0.4]])
lowvf4000d32min = np.array([vf4000d32min[vf4000d32min<0.4]])
lowvf4000d34min = np.array([vf4000d34min[vf4000d34min<0.4]])
lowvf4000d36min = np.array([vf4000d36min[vf4000d36min<0.4]])
lowvf4000d39min = np.array([vf4000d39min[vf4000d39min<0.4]])
lowvf4000d312min = np.array([vf4000d312min[vf4000d312min<0.4]])

lowvf4000d51min = np.array([vf4000d51min[vf4000d51min<0.4]])
lowvf4000d52min = np.array([vf4000d52min[vf4000d52min<0.4]])
lowvf4000d54min = np.array([vf4000d54min[vf4000d54min<0.4]])
lowvf4000d56min = np.array([vf4000d56min[vf4000d56min<0.4]])

lowvf4000d61min = np.array([vf4000d61min[vf4000d61min<0.4]])
lowvf4000d62min = np.array([vf4000d62min[vf4000d62min<0.4]])
lowvf4000d64min = np.array([vf4000d64min[vf4000d64min<0.4]])
lowvf4000d66min = np.array([vf4000d66min[vf4000d66min<0.4]])

# print(highvf800d11min.shape[1],lowvf800d11min.shape[1])
# print(vf800d11min.shape[0])

## Mean density
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

mean4000d3 = np.array([np.mean(vf4000d31min),np.mean(vf4000d32min),np.mean(vf4000d34min),np.mean(vf4000d36min)])
mean4000d5 = np.array([np.mean(vf4000d51min),np.mean(vf4000d52min),np.mean(vf4000d54min),np.mean(vf4000d56min)])
mean4000d6 = np.array([np.mean(vf4000d61min),np.mean(vf4000d62min),np.mean(vf4000d64min),np.mean(vf4000d66min)])

mean800 = np.array([mean800d1,mean800d2,mean800d3,mean800d5,mean800d6])
mean1600 = np.array([mean1600d2,mean1600d3,mean1600d4,mean1600d5,mean1600d6])
mean4000 = np.array([mean4000d3,mean4000d5,mean4000d6])

## std
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

std4000d3 = np.array([np.std(vf4000d31min),np.std(vf4000d32min),np.std(vf4000d34min),np.std(vf4000d36min)])
std4000d5 = np.array([np.std(vf4000d51min),np.std(vf4000d52min),np.std(vf4000d54min),np.std(vf4000d56min)])
std4000d6 = np.array([np.std(vf4000d61min),np.std(vf4000d62min),np.std(vf4000d64min),np.std(vf4000d66min)])

std800 = np.array([std800d1,std800d2,std800d3,std800d5,std800d6])
std1600 = np.array([std1600d2,std1600d3,std1600d4,std1600d5,std1600d6])
std4000 = np.array([std4000d3,std4000d5,std4000d6])


## High ratio
high800d1 = np.array([highvf800d11min.shape[1]/vf800d11min.shape[0],highvf800d12min.shape[1]/vf800d12min.shape[0],highvf800d14min.shape[1]/vf800d14min.shape[0],\
                      highvf800d16min.shape[1]/vf800d16min.shape[0],highvf800d19min.shape[1]/vf800d19min.shape[0],highvf800d112min.shape[1]/vf800d112min.shape[0]])
high800d2 = np.array([highvf800d21min.shape[1]/vf800d21min.shape[0],highvf800d22min.shape[1]/vf800d22min.shape[0],highvf800d24min.shape[1]/vf800d24min.shape[0],\
                      highvf800d26min.shape[1]/vf800d26min.shape[0],highvf800d29min.shape[1]/vf800d29min.shape[0],highvf800d212min.shape[1]/vf800d212min.shape[0]])
high800d3 = np.array([highvf800d31min.shape[1]/vf800d31min.shape[0],highvf800d32min.shape[1]/vf800d32min.shape[0],highvf800d34min.shape[1]/vf800d34min.shape[0],\
                      highvf800d36min.shape[1]/vf800d36min.shape[0],highvf800d39min.shape[1]/vf800d39min.shape[0],highvf800d312min.shape[1]/vf800d312min.shape[0]])
high800d5 = np.array([highvf800d51min.shape[1]/vf800d51min.shape[0],highvf800d52min.shape[1]/vf800d52min.shape[0],highvf800d54min.shape[1]/vf800d54min.shape[0],\
                      highvf800d56min.shape[1]/vf800d56min.shape[0],highvf800d59min.shape[1]/vf800d59min.shape[0],highvf800d512min.shape[1]/vf800d512min.shape[0]])
high800d6 = np.array([highvf800d61min.shape[1]/vf800d61min.shape[0],highvf800d62min.shape[1]/vf800d62min.shape[0],highvf800d64min.shape[1]/vf800d64min.shape[0],\
                      highvf800d66min.shape[1]/vf800d66min.shape[0],highvf800d69min.shape[1]/vf800d69min.shape[0],highvf800d612min.shape[1]/vf800d612min.shape[0]])

high1600d2 = np.array([highvf1600d21min.shape[1]/vf1600d21min.shape[0],highvf1600d22min.shape[1]/vf1600d22min.shape[0],highvf1600d24min.shape[1]/vf1600d24min.shape[0],\
                      highvf1600d26min.shape[1]/vf1600d26min.shape[0],highvf1600d29min.shape[1]/vf1600d29min.shape[0],highvf1600d212min.shape[1]/vf1600d212min.shape[0]])
high1600d3 = np.array([highvf1600d31min.shape[1]/vf1600d31min.shape[0],highvf1600d32min.shape[1]/vf1600d32min.shape[0],highvf1600d34min.shape[1]/vf1600d34min.shape[0],\
                      highvf1600d36min.shape[1]/vf1600d36min.shape[0],highvf1600d39min.shape[1]/vf1600d39min.shape[0],highvf1600d312min.shape[1]/vf1600d312min.shape[0]])
high1600d4 = np.array([highvf1600d41min.shape[1]/vf1600d41min.shape[0],highvf1600d42min.shape[1]/vf1600d42min.shape[0],highvf1600d44min.shape[1]/vf1600d44min.shape[0],\
                      highvf1600d46min.shape[1]/vf1600d46min.shape[0],highvf1600d49min.shape[1]/vf1600d49min.shape[0],highvf1600d412min.shape[1]/vf1600d412min.shape[0]])
high1600d5 = np.array([highvf1600d51min.shape[1]/vf1600d51min.shape[0],highvf1600d52min.shape[1]/vf1600d52min.shape[0],highvf1600d54min.shape[1]/vf1600d54min.shape[0],\
                      highvf1600d56min.shape[1]/vf1600d56min.shape[0],highvf1600d59min.shape[1]/vf1600d59min.shape[0],highvf1600d512min.shape[1]/vf1600d512min.shape[0]])
high1600d6 = np.array([highvf1600d61min.shape[1]/vf1600d61min.shape[0],highvf1600d62min.shape[1]/vf1600d62min.shape[0],highvf1600d64min.shape[1]/vf1600d64min.shape[0],\
                      highvf1600d66min.shape[1]/vf1600d66min.shape[0],highvf1600d69min.shape[1]/vf1600d69min.shape[0],highvf1600d612min.shape[1]/vf1600d612min.shape[0]])

high4000d3 = np.array([highvf4000d31min.shape[1]/vf4000d31min.shape[0],highvf4000d32min.shape[1]/vf4000d32min.shape[0],highvf4000d34min.shape[1]/vf4000d34min.shape[0],\
                      highvf4000d36min.shape[1]/vf4000d36min.shape[0]])
high4000d5 = np.array([highvf4000d51min.shape[1]/vf4000d51min.shape[0],highvf4000d52min.shape[1]/vf4000d52min.shape[0],highvf4000d54min.shape[1]/vf4000d54min.shape[0],\
                      highvf4000d56min.shape[1]/vf4000d56min.shape[0]])
high4000d6 = np.array([highvf4000d61min.shape[1]/vf4000d61min.shape[0],highvf4000d62min.shape[1]/vf4000d62min.shape[0],highvf4000d64min.shape[1]/vf4000d64min.shape[0],\
                      highvf4000d66min.shape[1]/vf4000d66min.shape[0]])

high800 = np.array([high800d1,high800d2,high800d3,high800d5,high800d6])
high1600 = np.array([high1600d2,high1600d3,high1600d4,high1600d5,high1600d6])
high4000 = np.array([high4000d3,high4000d5,high4000d6])


## Middle ratio
mid800d1 = np.array([midvf800d11min.shape[1]/vf800d11min.shape[0],midvf800d12min.shape[1]/vf800d12min.shape[0],midvf800d14min.shape[1]/vf800d14min.shape[0],\
                      midvf800d16min.shape[1]/vf800d16min.shape[0],midvf800d19min.shape[1]/vf800d19min.shape[0],midvf800d112min.shape[1]/vf800d112min.shape[0]])
mid800d2 = np.array([midvf800d21min.shape[1]/vf800d21min.shape[0],midvf800d22min.shape[1]/vf800d22min.shape[0],midvf800d24min.shape[1]/vf800d24min.shape[0],\
                      midvf800d26min.shape[1]/vf800d26min.shape[0],midvf800d29min.shape[1]/vf800d29min.shape[0],midvf800d212min.shape[1]/vf800d212min.shape[0]])
mid800d3 = np.array([midvf800d31min.shape[1]/vf800d31min.shape[0],midvf800d32min.shape[1]/vf800d32min.shape[0],midvf800d34min.shape[1]/vf800d34min.shape[0],\
                      midvf800d36min.shape[1]/vf800d36min.shape[0],midvf800d39min.shape[1]/vf800d39min.shape[0],midvf800d312min.shape[1]/vf800d312min.shape[0]])
mid800d5 = np.array([midvf800d51min.shape[1]/vf800d51min.shape[0],midvf800d52min.shape[1]/vf800d52min.shape[0],midvf800d54min.shape[1]/vf800d54min.shape[0],\
                      midvf800d56min.shape[1]/vf800d56min.shape[0],midvf800d59min.shape[1]/vf800d59min.shape[0],midvf800d512min.shape[1]/vf800d512min.shape[0]])
mid800d6 = np.array([midvf800d61min.shape[1]/vf800d61min.shape[0],midvf800d62min.shape[1]/vf800d62min.shape[0],midvf800d64min.shape[1]/vf800d64min.shape[0],\
                      midvf800d66min.shape[1]/vf800d66min.shape[0],midvf800d69min.shape[1]/vf800d69min.shape[0],midvf800d612min.shape[1]/vf800d612min.shape[0]])

mid1600d2 = np.array([midvf1600d21min.shape[1]/vf1600d21min.shape[0],midvf1600d22min.shape[1]/vf1600d22min.shape[0],midvf1600d24min.shape[1]/vf1600d24min.shape[0],\
                      midvf1600d26min.shape[1]/vf1600d26min.shape[0],midvf1600d29min.shape[1]/vf1600d29min.shape[0],midvf1600d212min.shape[1]/vf1600d212min.shape[0]])
mid1600d3 = np.array([midvf1600d31min.shape[1]/vf1600d31min.shape[0],midvf1600d32min.shape[1]/vf1600d32min.shape[0],midvf1600d34min.shape[1]/vf1600d34min.shape[0],\
                      midvf1600d36min.shape[1]/vf1600d36min.shape[0],midvf1600d39min.shape[1]/vf1600d39min.shape[0],midvf1600d312min.shape[1]/vf1600d312min.shape[0]])
mid1600d4 = np.array([midvf1600d41min.shape[1]/vf1600d41min.shape[0],midvf1600d42min.shape[1]/vf1600d42min.shape[0],midvf1600d44min.shape[1]/vf1600d44min.shape[0],\
                      midvf1600d46min.shape[1]/vf1600d46min.shape[0],midvf1600d49min.shape[1]/vf1600d49min.shape[0],midvf1600d412min.shape[1]/vf1600d412min.shape[0]])
mid1600d5 = np.array([midvf1600d51min.shape[1]/vf1600d51min.shape[0],midvf1600d52min.shape[1]/vf1600d52min.shape[0],midvf1600d54min.shape[1]/vf1600d54min.shape[0],\
                      midvf1600d56min.shape[1]/vf1600d56min.shape[0],midvf1600d59min.shape[1]/vf1600d59min.shape[0],midvf1600d512min.shape[1]/vf1600d512min.shape[0]])
mid1600d6 = np.array([midvf1600d61min.shape[1]/vf1600d61min.shape[0],midvf1600d62min.shape[1]/vf1600d62min.shape[0],midvf1600d64min.shape[1]/vf1600d64min.shape[0],\
                      midvf1600d66min.shape[1]/vf1600d66min.shape[0],midvf1600d69min.shape[1]/vf1600d69min.shape[0],midvf1600d612min.shape[1]/vf1600d612min.shape[0]])

mid4000d3 = np.array([midvf4000d31min.shape[1]/vf4000d31min.shape[0],midvf4000d32min.shape[1]/vf4000d32min.shape[0],midvf4000d34min.shape[1]/vf4000d34min.shape[0],\
                      midvf4000d36min.shape[1]/vf4000d36min.shape[0]])
mid4000d5 = np.array([midvf4000d51min.shape[1]/vf4000d51min.shape[0],midvf4000d52min.shape[1]/vf4000d52min.shape[0],midvf4000d54min.shape[1]/vf4000d54min.shape[0],\
                      midvf4000d56min.shape[1]/vf4000d56min.shape[0]])
mid4000d6 = np.array([midvf4000d61min.shape[1]/vf4000d61min.shape[0],midvf4000d62min.shape[1]/vf4000d62min.shape[0],midvf4000d64min.shape[1]/vf4000d64min.shape[0],\
                      midvf4000d66min.shape[1]/vf4000d66min.shape[0]])

mid800 = np.array([mid800d1,mid800d2,mid800d3,mid800d5,mid800d6])
mid1600 = np.array([mid1600d2,mid1600d3,mid1600d4,mid1600d5,mid1600d6])
mid4000 = np.array([mid4000d3,mid4000d5,mid4000d6])


## Low ratio
low800d1 = np.array([lowvf800d11min.shape[1]/vf800d11min.shape[0],lowvf800d12min.shape[1]/vf800d12min.shape[0],lowvf800d14min.shape[1]/vf800d14min.shape[0],\
                      lowvf800d16min.shape[1]/vf800d16min.shape[0],lowvf800d19min.shape[1]/vf800d19min.shape[0],lowvf800d112min.shape[1]/vf800d112min.shape[0]])
low800d2 = np.array([lowvf800d21min.shape[1]/vf800d21min.shape[0],lowvf800d22min.shape[1]/vf800d22min.shape[0],lowvf800d24min.shape[1]/vf800d24min.shape[0],\
                      lowvf800d26min.shape[1]/vf800d26min.shape[0],lowvf800d29min.shape[1]/vf800d29min.shape[0],lowvf800d212min.shape[1]/vf800d212min.shape[0]])
low800d3 = np.array([lowvf800d31min.shape[1]/vf800d31min.shape[0],lowvf800d32min.shape[1]/vf800d32min.shape[0],lowvf800d34min.shape[1]/vf800d34min.shape[0],\
                      lowvf800d36min.shape[1]/vf800d36min.shape[0],lowvf800d39min.shape[1]/vf800d39min.shape[0],lowvf800d312min.shape[1]/vf800d312min.shape[0]])
low800d5 = np.array([lowvf800d51min.shape[1]/vf800d51min.shape[0],lowvf800d52min.shape[1]/vf800d52min.shape[0],lowvf800d54min.shape[1]/vf800d54min.shape[0],\
                      lowvf800d56min.shape[1]/vf800d56min.shape[0],lowvf800d59min.shape[1]/vf800d59min.shape[0],lowvf800d512min.shape[1]/vf800d512min.shape[0]])
low800d6 = np.array([lowvf800d61min.shape[1]/vf800d61min.shape[0],lowvf800d62min.shape[1]/vf800d62min.shape[0],lowvf800d64min.shape[1]/vf800d64min.shape[0],\
                      lowvf800d66min.shape[1]/vf800d66min.shape[0],lowvf800d69min.shape[1]/vf800d69min.shape[0],lowvf800d612min.shape[1]/vf800d612min.shape[0]])

low1600d2 = np.array([lowvf1600d21min.shape[1]/vf1600d21min.shape[0],lowvf1600d22min.shape[1]/vf1600d22min.shape[0],lowvf1600d24min.shape[1]/vf1600d24min.shape[0],\
                      lowvf1600d26min.shape[1]/vf1600d26min.shape[0],lowvf1600d29min.shape[1]/vf1600d29min.shape[0],lowvf1600d212min.shape[1]/vf1600d212min.shape[0]])
low1600d3 = np.array([lowvf1600d31min.shape[1]/vf1600d31min.shape[0],lowvf1600d32min.shape[1]/vf1600d32min.shape[0],lowvf1600d34min.shape[1]/vf1600d34min.shape[0],\
                      lowvf1600d36min.shape[1]/vf1600d36min.shape[0],lowvf1600d39min.shape[1]/vf1600d39min.shape[0],lowvf1600d312min.shape[1]/vf1600d312min.shape[0]])
low1600d4 = np.array([lowvf1600d41min.shape[1]/vf1600d41min.shape[0],lowvf1600d42min.shape[1]/vf1600d42min.shape[0],lowvf1600d44min.shape[1]/vf1600d44min.shape[0],\
                      lowvf1600d46min.shape[1]/vf1600d46min.shape[0],lowvf1600d49min.shape[1]/vf1600d49min.shape[0],lowvf1600d412min.shape[1]/vf1600d412min.shape[0]])
low1600d5 = np.array([lowvf1600d51min.shape[1]/vf1600d51min.shape[0],lowvf1600d52min.shape[1]/vf1600d52min.shape[0],lowvf1600d54min.shape[1]/vf1600d54min.shape[0],\
                      lowvf1600d56min.shape[1]/vf1600d56min.shape[0],lowvf1600d59min.shape[1]/vf1600d59min.shape[0],lowvf1600d512min.shape[1]/vf1600d512min.shape[0]])
low1600d6 = np.array([lowvf1600d61min.shape[1]/vf1600d61min.shape[0],lowvf1600d62min.shape[1]/vf1600d62min.shape[0],lowvf1600d64min.shape[1]/vf1600d64min.shape[0],\
                      lowvf1600d66min.shape[1]/vf1600d66min.shape[0],lowvf1600d69min.shape[1]/vf1600d69min.shape[0],lowvf1600d612min.shape[1]/vf1600d612min.shape[0]])

low4000d3 = np.array([lowvf4000d31min.shape[1]/vf4000d31min.shape[0],lowvf4000d32min.shape[1]/vf4000d32min.shape[0],lowvf4000d34min.shape[1]/vf4000d34min.shape[0],\
                      lowvf4000d36min.shape[1]/vf4000d36min.shape[0]])
low4000d5 = np.array([lowvf4000d51min.shape[1]/vf4000d51min.shape[0],lowvf4000d52min.shape[1]/vf4000d52min.shape[0],lowvf4000d54min.shape[1]/vf4000d54min.shape[0],\
                      lowvf4000d56min.shape[1]/vf4000d56min.shape[0]])
low4000d6 = np.array([lowvf4000d61min.shape[1]/vf4000d61min.shape[0],lowvf4000d62min.shape[1]/vf4000d62min.shape[0],lowvf4000d64min.shape[1]/vf4000d64min.shape[0],\
                      lowvf4000d66min.shape[1]/vf4000d66min.shape[0]])

low800 = np.array([low800d1,low800d2,low800d3,low800d5,low800d6])
low1600 = np.array([low1600d2,low1600d3,low1600d4,low1600d5,low1600d6])
low4000 = np.array([low4000d3,low4000d5,low4000d6])



time = np.array([1,2,4,6,9,12])
time1 = np.array([1,3,5,7,9,11])
time2 = np.array([1,3,5,7])

labels=['1','2','4','6','9','12']
fontsize = 16
ticksize = 14

color1 = (235/255,153/255,156/255) ## pink
color2 = (161/255,125/255,180/255) ## purple
color3 = (142/255,165/255,200/255) ## blue
color4 = (131/255,157/255,68/255) ## green
color5 = (235/255,161/255,51/255) ## yellow
edgecolor = (102/255,100/255,100/255)

width = 0.4






# ### middle density ratio vs. time
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(mid800,axis=0)*100,'--^', color=color1, markersize=8, label='800 1/s')
# ax.fill_between(time[0:6],np.mean(mid800,axis=0)*100-np.std(mid800,axis=0)*100, np.mean(mid800,axis=0)*100+np.std(mid800,axis=0)*100, color=color1, alpha=0.2)
# ax.plot(time[0:6],np.mean(mid1600,axis=0)*100,'--o', color=color2, markersize=8, label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(mid1600,axis=0)*100-np.std(mid1600,axis=0)*100, np.mean(mid1600,axis=0)*100+np.std(mid1600,axis=0)*100, color=color2, alpha=0.2)
# ax.plot(time[0:4],np.mean(mid4000,axis=0)*100,'--s', color=color3, markersize=8, label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(mid4000,axis=0)*100-np.std(mid4000,axis=0)*100, np.mean(mid4000,axis=0)*100+np.std(mid4000,axis=0)*100, color=color3, alpha=0.2)

# ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('0.4 $\leq$ density $\leq$ 0.6', fontsize=fontsize)

# # ax.set_xlim(3,12)
# # ax.set_ylim(0,)

# # plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('DMr.png',bbox_inches='tight')
# plt.show()


# ### high density ratio vs. time
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(high800,axis=0)*100,'--^', color=color1, markersize=8, label='800 1/s')
# ax.fill_between(time[0:6],np.mean(high800,axis=0)*100-np.std(high800,axis=0)*100, np.mean(high800,axis=0)*100+np.std(high800,axis=0)*100, color=color1, alpha=0.2)
# ax.plot(time[0:6],np.mean(high1600,axis=0)*100,'--o', color=color2, markersize=8, label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(high1600,axis=0)*100-np.std(high1600,axis=0)*100, np.mean(high1600,axis=0)*100+np.std(high1600,axis=0)*100, color=color2, alpha=0.2)
# ax.plot(time[0:4],np.mean(high4000,axis=0)*100,'--s', color=color3, markersize=8, label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(high4000,axis=0)*100-np.std(high4000,axis=0)*100, np.mean(high4000,axis=0)*100+np.std(high4000,axis=0)*100, color=color3, alpha=0.2)

# ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('density > 0.6', fontsize=fontsize)

# # ax.set_xlim(3,12)
# ax.set_ylim(0,)

# # plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# # plt.legend(loc=2,fontsize=20,ncol=3,bbox_to_anchor=(-2, 0., 0.5, 0.5))
# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('DHr.png',bbox_inches='tight')
# plt.show()


# ### low density ratio vs. time
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(low800,axis=0)*100,'--^', color=color1, markersize=8, label='800 1/s')
# ax.fill_between(time[0:6],np.mean(low800,axis=0)*100-np.std(low800,axis=0)*100, np.mean(low800,axis=0)*100+np.std(low800,axis=0)*100, color=color1, alpha=0.2)
# ax.plot(time[0:6],np.mean(low1600,axis=0)*100,'--o', color=color2, markersize=8, label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(low1600,axis=0)*100-np.std(low1600,axis=0)*100, np.mean(low1600,axis=0)*100+np.std(low1600,axis=0)*100, color=color2, alpha=0.2)
# ax.plot(time[0:4],np.mean(low4000,axis=0)*100,'--s', color=color3, markersize=8, label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(low4000,axis=0)*100-np.std(low4000,axis=0)*100, np.mean(low4000,axis=0)*100+np.std(low4000,axis=0)*100, color=color3, alpha=0.2)

# ax.set_ylabel('ratio $[\%]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('density < 0.4', fontsize=fontsize)

# # ax.set_xlim(3,12)
# ax.set_ylim(0,)

# # plt.xticks(time1, labels=labels)
# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# # plt.legend(loc=2,fontsize=20,ncol=3,bbox_to_anchor=(-2, 0., 0.5, 0.5))
# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('DLr.png',bbox_inches='tight')
# plt.show()


## average density
fig, ax = plt.subplots()
ax.plot(time[0:6],np.mean(mean800,axis=0),'^--', color=color1, markersize=8, label='800 1/s')
ax.fill_between(time[0:6],np.mean(mean800,axis=0)-np.std(mean800,axis=0), np.mean(mean800,axis=0)+np.std(mean800,axis=0), color=color1, alpha=0.2)
ax.plot(time[0:6],np.mean(mean1600,axis=0),'o--', color=color2, markersize=8, label='1600 1/s')
ax.fill_between(time[0:6],np.mean(mean1600,axis=0)-np.std(mean1600,axis=0), np.mean(mean1600,axis=0)+np.std(mean1600,axis=0), color=color2, alpha=0.2)
ax.plot(time[0:4],np.mean(mean4000,axis=0),'s--', color=color3, markersize=8, label='4000 1/s')
ax.fill_between(time[0:4],np.mean(mean4000,axis=0)-np.std(mean4000,axis=0), np.mean(mean4000,axis=0)+np.std(mean4000,axis=0), color=color3, alpha=0.2)

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


# # average density -- 1600 1/s
# fig, ax = plt.subplots()
# ax.plot(time[0:6],mean1600d2,'^-', color=color1, markersize=6, label='case 1')
# ax.fill_between(time[0:6],mean1600d2-std1600d2, mean1600d2+std1600d2, color=color1, alpha=0.3)
# ax.plot(time[0:6],mean1600d3,'^-', color=color2, markersize=6, label='case 2')
# ax.fill_between(time[0:6],mean1600d3-std1600d3, mean1600d3+std1600d3, color=color2, alpha=0.3)
# ax.plot(time[0:6],mean1600d4,'^-', color=color3, markersize=6, label='case 3')
# ax.fill_between(time[0:6],mean1600d4-std1600d4, mean1600d4+std1600d4, color=color3, alpha=0.3)
# ax.plot(time[0:6],mean1600d5,'^-', color=color4, markersize=6, label='case 4')
# ax.fill_between(time[0:6],mean1600d5-std1600d5, mean1600d5+std1600d5, color=color4, alpha=0.3)
# ax.plot(time[0:6],mean1600d6,'^-', color=color5, markersize=6, label='case 5')
# ax.fill_between(time[0:6],mean1600d6-std1600d6, mean1600d6+std1600d6, color=color5, alpha=0.3)

# ax.set_ylabel('average density $[V/V]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average density -- 1600 $1/s$',fontsize=fontsize)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('avD1600.png',bbox_inches='tight')
# plt.show()

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



####------------------------------------------------NOT USING------------------------------------------------####
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


# ## low density ratio
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(low800,axis=0),'^-', color=color1, markersize=6, label='800 1/s')
# ax.fill_between(time[0:6],np.mean(low800,axis=0)-np.std(low800,axis=0), np.mean(low800,axis=0)+np.std(low800,axis=0), color=color1, alpha=0.3)
# ax.plot(time[0:6],np.mean(low1600,axis=0),'^-', color=color2, markersize=6, label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(low1600,axis=0)-np.std(low1600,axis=0), np.mean(low1600,axis=0)+np.std(low1600,axis=0), color=color2, alpha=0.3)
# ax.plot(time[0:4],np.mean(low4000,axis=0),'^-', color=color3, markersize=6, label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(low4000,axis=0)-np.std(low4000,axis=0), np.mean(low4000,axis=0)+np.std(low4000,axis=0), color=color3, alpha=0.3)

# ax.set_ylabel('ratio',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average ratio of low density volume \n with total volume', fontsize=fontsize)

# ax.set_ylim(0,)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('avLr.png',bbox_inches='tight')
# plt.show()


# ## High mean && std 
# meanhigh800d1 = np.array([np.mean(highvf800d11min),np.mean(highvf800d12min),np.mean(highvf800d14min),np.mean(highvf800d16min),np.mean(highvf800d19min),np.mean(highvf800d112min)])
# meanhigh800d2 = np.array([np.mean(highvf800d21min),np.mean(highvf800d22min),np.mean(highvf800d24min),np.mean(highvf800d26min),np.mean(highvf800d29min),np.mean(highvf800d212min)])
# meanhigh800d3 = np.array([np.mean(highvf800d31min),np.mean(highvf800d32min),np.mean(highvf800d34min),np.mean(highvf800d36min),np.mean(highvf800d39min),np.mean(highvf800d312min)])
# meanhigh800d5 = np.array([np.mean(highvf800d51min),np.mean(highvf800d52min),np.mean(highvf800d54min),np.mean(highvf800d56min),np.mean(highvf800d59min),np.mean(highvf800d512min)])
# meanhigh800d6 = np.array([np.mean(highvf800d61min),np.mean(highvf800d62min),np.mean(highvf800d64min),np.mean(highvf800d66min),np.mean(highvf800d69min),np.mean(highvf800d612min)])

# meanhigh1600d2 = np.array([np.mean(highvf1600d21min),np.mean(highvf1600d22min),np.mean(highvf1600d24min),np.mean(highvf1600d26min),np.mean(highvf1600d29min),np.mean(highvf1600d212min)])
# meanhigh1600d3 = np.array([np.mean(highvf1600d31min),np.mean(highvf1600d32min),np.mean(highvf1600d34min),np.mean(highvf1600d36min),np.mean(highvf1600d39min),np.mean(highvf1600d312min)])
# meanhigh1600d4 = np.array([np.mean(highvf1600d41min),np.mean(highvf1600d42min),np.mean(highvf1600d44min),np.mean(highvf1600d46min),np.mean(highvf1600d49min),np.mean(highvf1600d412min)])
# meanhigh1600d5 = np.array([np.mean(highvf1600d51min),np.mean(highvf1600d52min),np.mean(highvf1600d54min),np.mean(highvf1600d56min),np.mean(highvf1600d59min),np.mean(highvf1600d512min)])
# meanhigh1600d6 = np.array([np.mean(highvf1600d61min),np.mean(highvf1600d62min),np.mean(highvf1600d64min),np.mean(highvf1600d66min),np.mean(highvf1600d69min),np.mean(highvf1600d612min)])

# meanhigh4000d3 = np.array([np.mean(highvf4000d31min),np.mean(highvf4000d32min),np.mean(highvf4000d34min),np.mean(highvf4000d36min)])
# meanhigh4000d5 = np.array([np.mean(highvf4000d51min),np.mean(highvf4000d52min),np.mean(highvf4000d54min),np.mean(highvf4000d56min)])
# meanhigh4000d6 = np.array([np.mean(highvf4000d61min),np.mean(highvf4000d62min),np.mean(highvf4000d64min),np.mean(highvf4000d66min)])

# meanhigh800 = np.array([meanhigh800d1,meanhigh800d2,meanhigh800d3,meanhigh800d5,meanhigh800d6])
# meanhigh1600 = np.array([meanhigh1600d2,meanhigh1600d3,meanhigh1600d4,meanhigh1600d5,meanhigh1600d6])
# meanhigh4000 = np.array([meanhigh4000d3,meanhigh4000d5,meanhigh4000d6])

# stdhigh800d1 = np.array([np.std(highvf800d11min),np.std(highvf800d12min),np.std(highvf800d14min),np.std(highvf800d16min),np.std(highvf800d19min),np.std(highvf800d112min)])
# stdhigh800d2 = np.array([np.std(highvf800d21min),np.std(highvf800d22min),np.std(highvf800d24min),np.std(highvf800d26min),np.std(highvf800d29min),np.std(highvf800d212min)])
# stdhigh800d3 = np.array([np.std(highvf800d31min),np.std(highvf800d32min),np.std(highvf800d34min),np.std(highvf800d36min),np.std(highvf800d39min),np.std(highvf800d312min)])
# stdhigh800d5 = np.array([np.std(highvf800d51min),np.std(highvf800d52min),np.std(highvf800d54min),np.std(highvf800d56min),np.std(highvf800d59min),np.std(highvf800d512min)])
# stdhigh800d6 = np.array([np.std(highvf800d61min),np.std(highvf800d62min),np.std(highvf800d64min),np.std(highvf800d66min),np.std(highvf800d69min),np.std(highvf800d612min)])

# stdhigh1600d2 = np.array([np.std(highvf1600d21min),np.std(highvf1600d22min),np.std(highvf1600d24min),np.std(highvf1600d26min),np.std(highvf1600d29min),np.std(highvf1600d212min)])
# stdhigh1600d3 = np.array([np.std(highvf1600d31min),np.std(highvf1600d32min),np.std(highvf1600d34min),np.std(highvf1600d36min),np.std(highvf1600d39min),np.std(highvf1600d312min)])
# stdhigh1600d4 = np.array([np.std(highvf1600d41min),np.std(highvf1600d42min),np.std(highvf1600d44min),np.std(highvf1600d46min),np.std(highvf1600d49min),np.std(highvf1600d412min)])
# stdhigh1600d5 = np.array([np.std(highvf1600d51min),np.std(highvf1600d52min),np.std(highvf1600d54min),np.std(highvf1600d56min),np.std(highvf1600d59min),np.std(highvf1600d512min)])
# stdhigh1600d6 = np.array([np.std(highvf1600d61min),np.std(highvf1600d62min),np.std(highvf1600d64min),np.std(highvf1600d66min),np.std(highvf1600d69min),np.std(highvf1600d612min)])

# stdhigh4000d3 = np.array([np.std(highvf4000d31min),np.std(highvf4000d32min),np.std(highvf4000d34min),np.std(highvf4000d36min),np.std(highvf4000d39min),np.std(highvf4000d312min)])
# stdhigh4000d5 = np.array([np.std(highvf4000d51min),np.std(highvf4000d52min),np.std(highvf4000d54min),np.std(highvf4000d56min)])
# stdhigh4000d6 = np.array([np.std(highvf4000d61min),np.std(highvf4000d62min),np.std(highvf4000d64min),np.std(highvf4000d66min)])


# ## Low mean && std 
# meanlow800d1 = np.array([np.mean(lowvf800d11min),np.mean(lowvf800d12min),np.mean(lowvf800d14min),np.mean(lowvf800d16min),np.mean(lowvf800d19min),np.mean(lowvf800d112min)])
# meanlow800d2 = np.array([np.mean(lowvf800d21min),np.mean(lowvf800d22min),np.mean(lowvf800d24min),np.mean(lowvf800d26min),np.mean(lowvf800d29min),np.mean(lowvf800d212min)])
# meanlow800d3 = np.array([np.mean(lowvf800d31min),np.mean(lowvf800d32min),np.mean(lowvf800d34min),np.mean(lowvf800d36min),np.mean(lowvf800d39min),np.mean(lowvf800d312min)])
# meanlow800d5 = np.array([np.mean(lowvf800d51min),np.mean(lowvf800d52min),np.mean(lowvf800d54min),np.mean(lowvf800d56min),np.mean(lowvf800d59min),np.mean(lowvf800d512min)])
# meanlow800d6 = np.array([np.mean(lowvf800d61min),np.mean(lowvf800d62min),np.mean(lowvf800d64min),np.mean(lowvf800d66min),np.mean(lowvf800d69min),np.mean(lowvf800d612min)])

# meanlow1600d2 = np.array([np.mean(lowvf1600d21min),np.mean(lowvf1600d22min),np.mean(lowvf1600d24min),np.mean(lowvf1600d26min),np.mean(lowvf1600d29min),np.mean(lowvf1600d212min)])
# meanlow1600d3 = np.array([np.mean(lowvf1600d31min),np.mean(lowvf1600d32min),np.mean(lowvf1600d34min),np.mean(lowvf1600d36min),np.mean(lowvf1600d39min),np.mean(lowvf1600d312min)])
# meanlow1600d4 = np.array([np.mean(lowvf1600d41min),np.mean(lowvf1600d42min),np.mean(lowvf1600d44min),np.mean(lowvf1600d46min),np.mean(lowvf1600d49min),np.mean(lowvf1600d412min)])
# meanlow1600d5 = np.array([np.mean(lowvf1600d51min),np.mean(lowvf1600d52min),np.mean(lowvf1600d54min),np.mean(lowvf1600d56min),np.mean(lowvf1600d59min),np.mean(lowvf1600d512min)])
# meanlow1600d6 = np.array([np.mean(lowvf1600d61min),np.mean(lowvf1600d62min),np.mean(lowvf1600d64min),np.mean(lowvf1600d66min),np.mean(lowvf1600d69min),np.mean(lowvf1600d612min)])

# meanlow4000d3 = np.array([np.mean(lowvf4000d31min),np.mean(lowvf4000d32min),np.mean(lowvf4000d34min),np.mean(lowvf4000d36min)])
# meanlow4000d5 = np.array([np.mean(lowvf4000d51min),np.mean(lowvf4000d52min),np.mean(lowvf4000d54min),np.mean(lowvf4000d56min)])
# meanlow4000d6 = np.array([np.mean(lowvf4000d61min),np.mean(lowvf4000d62min),np.mean(lowvf4000d64min),np.mean(lowvf4000d66min)])

# meanlow800 = np.array([meanlow800d1,meanlow800d2,meanlow800d3,meanlow800d5,meanlow800d6])
# meanlow1600 = np.array([meanlow1600d2,meanlow1600d3,meanlow1600d4,meanlow1600d5,meanlow1600d6])
# meanlow4000 = np.array([meanlow4000d3,meanlow4000d5,meanlow4000d6])

# stdlow800d1 = np.array([np.std(lowvf800d11min),np.std(lowvf800d12min),np.std(lowvf800d14min),np.std(lowvf800d16min),np.std(lowvf800d19min),np.std(lowvf800d112min)])
# stdlow800d2 = np.array([np.std(lowvf800d21min),np.std(lowvf800d22min),np.std(lowvf800d24min),np.std(lowvf800d26min),np.std(lowvf800d29min),np.std(lowvf800d212min)])
# stdlow800d3 = np.array([np.std(lowvf800d31min),np.std(lowvf800d32min),np.std(lowvf800d34min),np.std(lowvf800d36min),np.std(lowvf800d39min),np.std(lowvf800d312min)])
# stdlow800d5 = np.array([np.std(lowvf800d51min),np.std(lowvf800d52min),np.std(lowvf800d54min),np.std(lowvf800d56min),np.std(lowvf800d59min),np.std(lowvf800d512min)])
# stdlow800d6 = np.array([np.std(lowvf800d61min),np.std(lowvf800d62min),np.std(lowvf800d64min),np.std(lowvf800d66min),np.std(lowvf800d69min),np.std(lowvf800d612min)])

# stdlow1600d2 = np.array([np.std(lowvf1600d21min),np.std(lowvf1600d22min),np.std(lowvf1600d24min),np.std(lowvf1600d26min),np.std(lowvf1600d29min),np.std(lowvf1600d212min)])
# stdlow1600d3 = np.array([np.std(lowvf1600d31min),np.std(lowvf1600d32min),np.std(lowvf1600d34min),np.std(lowvf1600d36min),np.std(lowvf1600d39min),np.std(lowvf1600d312min)])
# stdlow1600d4 = np.array([np.std(lowvf1600d41min),np.std(lowvf1600d42min),np.std(lowvf1600d44min),np.std(lowvf1600d46min),np.std(lowvf1600d49min),np.std(lowvf1600d412min)])
# stdlow1600d5 = np.array([np.std(lowvf1600d51min),np.std(lowvf1600d52min),np.std(lowvf1600d54min),np.std(lowvf1600d56min),np.std(lowvf1600d59min),np.std(lowvf1600d512min)])
# stdlow1600d6 = np.array([np.std(lowvf1600d61min),np.std(lowvf1600d62min),np.std(lowvf1600d64min),np.std(lowvf1600d66min),np.std(lowvf1600d69min),np.std(lowvf1600d612min)])

# stdlow4000d3 = np.array([np.std(lowvf4000d31min),np.std(lowvf4000d32min),np.std(lowvf4000d34min),np.std(lowvf4000d36min),np.std(lowvf4000d39min),np.std(lowvf4000d312min)])
# stdlow4000d5 = np.array([np.std(lowvf4000d51min),np.std(lowvf4000d52min),np.std(lowvf4000d54min),np.std(lowvf4000d56min)])
# stdlow4000d6 = np.array([np.std(lowvf4000d61min),np.std(lowvf4000d62min),np.std(lowvf4000d64min),np.std(lowvf4000d66min)])



# ## average density -- low
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(meanlow800,axis=0),'^-', color=color1, markersize=6, label='800 1/s')
# ax.fill_between(time[0:6],np.mean(meanlow800,axis=0)-np.std(meanlow800,axis=0), np.mean(meanlow800,axis=0)+np.std(meanlow800,axis=0), color=color1, alpha=0.3)
# ax.plot(time[0:6],np.mean(meanlow1600,axis=0),'^-', color=color2, markersize=6, label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(meanlow1600,axis=0)-np.std(meanlow1600,axis=0), np.mean(meanlow1600,axis=0)+np.std(meanlow1600,axis=0), color=color2, alpha=0.3)
# ax.plot(time[0:4],np.mean(meanlow4000,axis=0),'^-', color=color3, markersize=6, label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(meanlow4000,axis=0)-np.std(meanlow4000,axis=0), np.mean(meanlow4000,axis=0)+np.std(meanlow4000,axis=0), color=color3, alpha=0.3)

# ax.set_ylabel('density $[V/V]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average density (<0.5)',fontsize=fontsize)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('avLD.png',bbox_inches='tight')
# plt.show()



# ## average density -- high
# fig, ax = plt.subplots()
# ax.plot(time[0:6],np.mean(meanhigh800,axis=0),'^-', color=color1, markersize=6, label='800 1/s')
# ax.fill_between(time[0:6],np.mean(meanhigh800,axis=0)-np.std(meanhigh800,axis=0), np.mean(meanhigh800,axis=0)+np.std(meanhigh800,axis=0), color=color1, alpha=0.3)
# ax.plot(time[0:6],np.mean(meanhigh1600,axis=0),'^-', color=color2, markersize=6, label='1600 1/s')
# ax.fill_between(time[0:6],np.mean(meanhigh1600,axis=0)-np.std(meanhigh1600,axis=0), np.mean(meanhigh1600,axis=0)+np.std(meanhigh1600,axis=0), color=color2, alpha=0.3)
# ax.plot(time[0:4],np.mean(meanhigh4000,axis=0),'^-', color=color3, markersize=6, label='4000 1/s')
# ax.fill_between(time[0:4],np.mean(meanhigh4000,axis=0)-np.std(meanhigh4000,axis=0), np.mean(meanhigh4000,axis=0)+np.std(meanhigh4000,axis=0), color=color3, alpha=0.3)

# ax.set_ylabel('density $[V/V]$',fontsize=fontsize)
# ax.set_xlabel('time $[min]$',fontsize=fontsize)
# plt.title('Average density (>0.5)',fontsize=fontsize)

# # ax.set_ylim(0,5)

# ax.tick_params(axis='x', labelsize= ticksize)
# ax.tick_params(axis='y', labelsize= ticksize)

# plt.legend(loc=1,fontsize=12)
# plt.grid(alpha=0.3)

# plt.savefig('avHD.png',bbox_inches='tight')
# plt.show()