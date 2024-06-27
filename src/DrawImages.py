# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:31:42 2021

@author: ALegaz
"""
import numpy as np
import matplotlib.pyplot as plt

class DrawImages:
    
    
    
     def ShowImgOVF(img,vx,vy,step,norm):
        """
        Display a orientation vector field over image
            img: image
            vx: x component of vector field
            vy: y component of vector field
            step: distance between vectors
            norm: bool var for normalized vector field
        
        """
        w, h = img.size;
        
        if norm == 1:
            eps = 0.0001;
            mod=np.sqrt(vx**2+vy**2);
            vx = vx/(mod+eps); 
            vy = vy/(mod+eps);
        
        x,y = np.meshgrid(np.linspace(1,w,w),np.linspace(1,h,h))
        x_step = x[::step,::step]
        y_step = y[::step,::step]
        vx_step=vx[::step,::step]
        vy_step=vy[::step,::step]
        

        imgplt = plt.imshow(img,cmap='gray', vmin=0, vmax=255);
        plt.axis('off')
        plt.quiver(x_step,y_step,-vx_step,vy_step,scale=50,color='r')
        plt.show()
        
        fig = plt.gcf()
        fig.set_size_inches(30, 30)
        
        return