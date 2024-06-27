import matplotlib.pyplot as plt
from PIL import Image
from IOEToolBox import IOEToolBox
from DrawImages import DrawImages
import numpy as np
from time import time


#! Title
major_version = 1;
minor_version = 0;
print("\nScrip Estimación Orientacion v"+str(major_version)+"."+str(minor_version))

eps = 0.00001

#! Load input image
colorImage = Image.open('blocksTest.png')
img = colorImage.convert("L")
imgplot = plt.imshow(img, cmap='gray', vmin=0, vmax=255);
plt.axis('off')
plt.show()

#! SOE by ASG
m = 11;
[vx, vy] = IOEToolBox.asg(img, m);

#! Display normalize ASG vector field
step = int(10)
DrawImages.ShowImgOVF(img,vx,vy,step,1);

# SOE by GASGVF
m = 11;
h = 30;
start_time = time()
[vxg, vyg] = IOEToolBox.gasgvf(img, m, h);
elapsed_time = time() - start_time
print("Harris Detector ->Elapsed time: %0.10f seconds." % elapsed_time)

#! Display normalize ASG vector field
step = int(10)
DrawImages.ShowImgOVF(img,vxg,vyg,step,1);



