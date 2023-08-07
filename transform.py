import czifile
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import ndimage, misc


file = ["1min", "2min", "4min", "6min", "9min", "12min"]
starter = [6,6,6,5,5,5] ## Start layer for each data
for i in range(6):
    name = file[i]
    layer = starter[i]
    print("file "+name+" start from layer "+str(layer))

    img = czifile.imread(name+'.czi')

    img = np.squeeze(img)
    # print(img.shape)

    labelimg = img[1,layer:,:,:]
    # print(labelimg.shape[0])

    resultlist = np.empty([0,2208,2752])
    for i in range(labelimg.shape[0]):
    # for i in range(1):
        result = ndimage.uniform_filter(labelimg[i,:,:], size=44, mode='constant')
        # print(np.max(result),np.min(result))
        resultlist = np.append(resultlist, np.expand_dims(result,axis=0), axis=0)
    # print(resultlist.shape)

    np.savetxt("intensity/"+name+".txt", resultlist.reshape(1,-1), fmt='%1.1f')
    print(resultlist.reshape(1,-1).shape)

    filtered_image = sitk.GetImageFromArray(img[0,layer:,:,:])
    # print(filtered_image)
    # sitk.WriteImage(filtered_image, "outline/"+name+".vtk")
    # print("Finish transform...")

    # if name=="1min":
    #     plt.imshow(img[1,10,:,:])
    #     plt.colorbar()
    #     plt.show()
