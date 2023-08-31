import czifile
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import ndimage, misc
import seaborn as sns


## Density
def extract_vertices(directory_to_txt):
    TargetMSH = open(directory_to_txt, "r+")

    ### Read the total number of vertices(points) from .msh file
    line = TargetMSH.readline()
    words = line.strip().split()
    v_num = int(words[0])
    l_num = int(np.ceil(v_num/5))
    # print(l_num,v_num)
    TargetMSH.close()
    # print('TOTAL VERTICES:',v_num)

    ### Create a list and copy out all the boundary vertices
    VerticeList = []

    for i in range(1,l_num+1):
        with open(directory_to_txt,'r') as txt:

            text = txt.readlines()
            currentline = text[i]
            coordinates = currentline.strip().split()
            # print(coordinates)

            for j in range(len(coordinates)):
            	VerticeList.append(np.float64(coordinates[j]))

    return np.expand_dims(np.asarray(VerticeList),axis=1)



### read density
vf800d11min = extract_vertices('../../interpolation/d1_800/data/vf/1min.txt')
vf800d12min = extract_vertices('../../interpolation/d1_800/data/vf/2min.txt')
vf800d14min = extract_vertices('../../interpolation/d1_800/data/vf/4min.txt')
vf800d16min = extract_vertices('../../interpolation/d1_800/data/vf/6min.txt')
vf800d19min = extract_vertices('../../interpolation/d1_800/data/vf/9min.txt')
vf800d112min = extract_vertices('../../interpolation/d1_800/data/vf/12min.txt')

vf800d21min = extract_vertices('../../interpolation/d2_800/data/vf/1min.txt')
vf800d22min = extract_vertices('../../interpolation/d2_800/data/vf/2min.txt')
vf800d24min = extract_vertices('../../interpolation/d2_800/data/vf/4min.txt')
vf800d26min = extract_vertices('../../interpolation/d2_800/data/vf/6min.txt')
vf800d29min = extract_vertices('../../interpolation/d2_800/data/vf/9min.txt')
vf800d212min = extract_vertices('../../interpolation/d2_800/data/vf/12min.txt')

vf800d31min = extract_vertices('../../interpolation/d3_800/data/vf/1min.txt')
vf800d32min = extract_vertices('../../interpolation/d3_800/data/vf/2min.txt')
vf800d34min = extract_vertices('../../interpolation/d3_800/data/vf/4min.txt')
vf800d36min = extract_vertices('../../interpolation/d3_800/data/vf/6min.txt')
vf800d39min = extract_vertices('../../interpolation/d3_800/data/vf/9min.txt')
vf800d312min = extract_vertices('../../interpolation/d3_800/data/vf/12min.txt')

vf800d51min = extract_vertices('../../interpolation/d5_800/data/vf/1min.txt')
vf800d52min = extract_vertices('../../interpolation/d5_800/data/vf/2min.txt')
vf800d54min = extract_vertices('../../interpolation/d5_800/data/vf/4min.txt')
vf800d56min = extract_vertices('../../interpolation/d5_800/data/vf/6min.txt')
vf800d59min = extract_vertices('../../interpolation/d5_800/data/vf/9min.txt')
vf800d512min = extract_vertices('../../interpolation/d5_800/data/vf/12min.txt')

vf800d61min = extract_vertices('../../interpolation/d6_800/data/vf/1min.txt')
vf800d62min = extract_vertices('../../interpolation/d6_800/data/vf/2min.txt')
vf800d64min = extract_vertices('../../interpolation/d6_800/data/vf/4min.txt')
vf800d66min = extract_vertices('../../interpolation/d6_800/data/vf/6min.txt')
vf800d69min = extract_vertices('../../interpolation/d6_800/data/vf/9min.txt')
vf800d612min = extract_vertices('../../interpolation/d6_800/data/vf/12min.txt')

vf1600d21min = extract_vertices('../../interpolation/d2_1600/data/vf/1min.txt')
vf1600d22min = extract_vertices('../../interpolation/d2_1600/data/vf/2min.txt')
vf1600d24min = extract_vertices('../../interpolation/d2_1600/data/vf/4min.txt')
vf1600d26min = extract_vertices('../../interpolation/d2_1600/data/vf/6min.txt')
vf1600d29min = extract_vertices('../../interpolation/d2_1600/data/vf/9min.txt')
vf1600d212min = extract_vertices('../../interpolation/d2_1600/data/vf/12min.txt')

vf1600d31min = extract_vertices('../../interpolation/d3_1600/data/vf/1min.txt')
vf1600d32min = extract_vertices('../../interpolation/d3_1600/data/vf/2min.txt')
vf1600d34min = extract_vertices('../../interpolation/d3_1600/data/vf/4min.txt')
vf1600d36min = extract_vertices('../../interpolation/d3_1600/data/vf/6min.txt')
vf1600d39min = extract_vertices('../../interpolation/d3_1600/data/vf/9min.txt')
vf1600d312min = extract_vertices('../../interpolation/d3_1600/data/vf/12min.txt')

vf1600d41min = extract_vertices('../../interpolation/d4_1600/data/vf/1min.txt')
vf1600d42min = extract_vertices('../../interpolation/d4_1600/data/vf/2min.txt')
vf1600d44min = extract_vertices('../../interpolation/d4_1600/data/vf/4min.txt')
vf1600d46min = extract_vertices('../../interpolation/d4_1600/data/vf/6min.txt')
vf1600d49min = extract_vertices('../../interpolation/d4_1600/data/vf/9min.txt')
vf1600d412min = extract_vertices('../../interpolation/d4_1600/data/vf/12min.txt')

vf1600d51min = extract_vertices('../../interpolation/d5_1600/data/vf/1min.txt')
vf1600d52min = extract_vertices('../../interpolation/d5_1600/data/vf/2min.txt')
vf1600d54min = extract_vertices('../../interpolation/d5_1600/data/vf/4min.txt')
vf1600d56min = extract_vertices('../../interpolation/d5_1600/data/vf/6min.txt')
vf1600d59min = extract_vertices('../../interpolation/d5_1600/data/vf/9min.txt')
vf1600d512min = extract_vertices('../../interpolation/d5_1600/data/vf/12min.txt')

vf1600d61min = extract_vertices('../../interpolation/d6_1600/data/vf/1min.txt')
vf1600d62min = extract_vertices('../../interpolation/d6_1600/data/vf/2min.txt')
vf1600d64min = extract_vertices('../../interpolation/d6_1600/data/vf/4min.txt')
vf1600d66min = extract_vertices('../../interpolation/d6_1600/data/vf/6min.txt')
vf1600d69min = extract_vertices('../../interpolation/d6_1600/data/vf/9min.txt')
vf1600d612min = extract_vertices('../../interpolation/d6_1600/data/vf/12min.txt')

vf4000d31min = extract_vertices('../../interpolation/d3_4000/data/vf/1min.txt')
vf4000d32min = extract_vertices('../../interpolation/d3_4000/data/vf/2min.txt')
vf4000d34min = extract_vertices('../../interpolation/d3_4000/data/vf/4min.txt')
vf4000d36min = extract_vertices('../../interpolation/d3_4000/data/vf/6min.txt')
vf4000d39min = extract_vertices('../../interpolation/d3_4000/data/vf/9min.txt')
vf4000d312min = extract_vertices('../../interpolation/d3_4000/data/vf/12min.txt')

vf4000d51min = extract_vertices('../../interpolation/d5_4000/data/vf/1min.txt')
vf4000d52min = extract_vertices('../../interpolation/d5_4000/data/vf/2min.txt')
vf4000d54min = extract_vertices('../../interpolation/d5_4000/data/vf/4min.txt')
vf4000d56min = extract_vertices('../../interpolation/d5_4000/data/vf/6min.txt')

vf4000d61min = extract_vertices('../../interpolation/d6_4000/data/vf/1min.txt')
vf4000d62min = extract_vertices('../../interpolation/d6_4000/data/vf/2min.txt')
vf4000d64min = extract_vertices('../../interpolation/d6_4000/data/vf/4min.txt')
vf4000d66min = extract_vertices('../../interpolation/d6_4000/data/vf/6min.txt')



### save in npy
np.save("data/density/d1_800/1min.npy", vf800d11min)
np.save("data/density/d1_800/2min.npy", vf800d12min)
np.save("data/density/d1_800/4min.npy", vf800d14min)
np.save("data/density/d1_800/6min.npy", vf800d16min)
np.save("data/density/d1_800/9min.npy", vf800d19min)
np.save("data/density/d1_800/12min.npy", vf800d112min)

np.save("data/density/d2_800/1min.npy", vf800d21min)
np.save("data/density/d2_800/2min.npy", vf800d22min)
np.save("data/density/d2_800/4min.npy", vf800d24min)
np.save("data/density/d2_800/6min.npy", vf800d26min)
np.save("data/density/d2_800/9min.npy", vf800d29min)
np.save("data/density/d2_800/12min.npy", vf800d212min)

np.save("data/density/d3_800/1min.npy", vf800d31min)
np.save("data/density/d3_800/2min.npy", vf800d32min)
np.save("data/density/d3_800/4min.npy", vf800d34min)
np.save("data/density/d3_800/6min.npy", vf800d36min)
np.save("data/density/d3_800/9min.npy", vf800d39min)
np.save("data/density/d3_800/12min.npy", vf800d312min)

np.save("data/density/d5_800/1min.npy", vf800d51min)
np.save("data/density/d5_800/2min.npy", vf800d52min)
np.save("data/density/d5_800/4min.npy", vf800d54min)
np.save("data/density/d5_800/6min.npy", vf800d56min)
np.save("data/density/d5_800/9min.npy", vf800d59min)
np.save("data/density/d5_800/12min.npy", vf800d512min)

np.save("data/density/d6_800/1min.npy", vf800d61min)
np.save("data/density/d6_800/2min.npy", vf800d62min)
np.save("data/density/d6_800/4min.npy", vf800d64min)
np.save("data/density/d6_800/6min.npy", vf800d66min)
np.save("data/density/d6_800/9min.npy", vf800d69min)
np.save("data/density/d6_800/12min.npy", vf800d612min)


np.save("data/density/d2_1600/1min.npy", vf1600d21min)
np.save("data/density/d2_1600/2min.npy", vf1600d22min)
np.save("data/density/d2_1600/4min.npy", vf1600d24min)
np.save("data/density/d2_1600/6min.npy", vf1600d26min)
np.save("data/density/d2_1600/9min.npy", vf1600d29min)
np.save("data/density/d2_1600/12min.npy", vf1600d212min)

np.save("data/density/d3_1600/1min.npy", vf1600d31min)
np.save("data/density/d3_1600/2min.npy", vf1600d32min)
np.save("data/density/d3_1600/4min.npy", vf1600d34min)
np.save("data/density/d3_1600/6min.npy", vf1600d36min)
np.save("data/density/d3_1600/9min.npy", vf1600d39min)
np.save("data/density/d3_1600/12min.npy", vf1600d312min)

np.save("data/density/d4_1600/1min.npy", vf1600d41min)
np.save("data/density/d4_1600/2min.npy", vf1600d42min)
np.save("data/density/d4_1600/4min.npy", vf1600d44min)
np.save("data/density/d4_1600/6min.npy", vf1600d46min)
np.save("data/density/d4_1600/9min.npy", vf1600d49min)
np.save("data/density/d4_1600/12min.npy", vf1600d412min)

np.save("data/density/d5_1600/1min.npy", vf1600d51min)
np.save("data/density/d5_1600/2min.npy", vf1600d52min)
np.save("data/density/d5_1600/4min.npy", vf1600d54min)
np.save("data/density/d5_1600/6min.npy", vf1600d56min)
np.save("data/density/d5_1600/9min.npy", vf1600d59min)
np.save("data/density/d5_1600/12min.npy", vf1600d512min)

np.save("data/density/d6_1600/1min.npy", vf1600d61min)
np.save("data/density/d6_1600/2min.npy", vf1600d62min)
np.save("data/density/d6_1600/4min.npy", vf1600d64min)
np.save("data/density/d6_1600/6min.npy", vf1600d66min)
np.save("data/density/d6_1600/9min.npy", vf1600d69min)
np.save("data/density/d6_1600/12min.npy", vf1600d612min)

np.save("data/density/d3_4000/1min.npy", vf4000d31min)
np.save("data/density/d3_4000/2min.npy", vf4000d32min)
np.save("data/density/d3_4000/4min.npy", vf4000d34min)
np.save("data/density/d3_4000/6min.npy", vf4000d36min)
np.save("data/density/d3_4000/9min.npy", vf4000d39min)
np.save("data/density/d3_4000/12min.npy", vf4000d312min)

np.save("data/density/d5_4000/1min.npy", vf4000d51min)
np.save("data/density/d5_4000/2min.npy", vf4000d52min)
np.save("data/density/d5_4000/4min.npy", vf4000d54min)
np.save("data/density/d5_4000/6min.npy", vf4000d56min)

np.save("data/density/d6_4000/1min.npy", vf4000d61min)
np.save("data/density/d6_4000/2min.npy", vf4000d62min)
np.save("data/density/d6_4000/4min.npy", vf4000d64min)
np.save("data/density/d6_4000/6min.npy", vf4000d66min)