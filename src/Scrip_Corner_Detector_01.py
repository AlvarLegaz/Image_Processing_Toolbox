"""
Created on Sun Jun 27 08:26:05 2021

@author: ALegaz
"""

import matplotlib.pyplot as plt
from PIL import Image
from IOEToolBox import IOEToolBox
import numpy as np
from time import time


#! Title and version 
major_version = 1
minor_version = 0
print("\nScrip Corner Detection v"+str(major_version)+"."+str(minor_version))

#! Load input image
colorImage = Image.open('blocksTest.png')

img = colorImage.convert("L")
imgplot = plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()
print("\nInput image size = "+ str(img.size[0]) + "x" + str(img.size[1]))

#! Execute Harris corner detector
start_time = time()
corners_harris = IOEToolBox.CornerDetector(img, 3)
elapsed_time = time() - start_time

print("Harris Detector ->Elapsed time: %0.10f seconds." % elapsed_time)
plt.figure()
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
py, px = np.where(corners_harris>0.01*corners_harris.max())
plt.plot(px, py, 'g.')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
