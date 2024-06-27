import numpy as np
import scipy.signal
import cv2 as cv # Opencv: Image processing toolbox


class IOEToolBox:
        
    def asg(img, m):
        """
        Average square gradient is a single orientation estimation method
            
            image: input image
            m: low pass filter average window
        
        """
        eps = 0.0001
        Gy, Gx = np.gradient(img)
        aux = np.sign(Gx+eps)
        Gx = Gx*aux
        Gy = Gy*aux
        [Gtheta, Grho] = IOEToolBox.cart2pol(Gx,Gy)
        
        Gsx            = Gx**2 - Gy**2     
        Gsy            = 2*Gx*Gy
        
        B = (1/m**2) *np.ones([m, m], dtype = int)
        
        Gsxg           = IOEToolBox.filter2(B,Gsx)
        Gsyg           = IOEToolBox.filter2(B,Gsy)
        
        Phi            = 1/2*np.arctan2(Gsyg, Gsxg)
        theta          = Phi-(3.1416/2)*np.sign(Phi+eps)
        
        [vx,vy]        = IOEToolBox.pol2cart(theta, Grho**2)
        return vx,vy


    def gasgvf(img, m, h):
        [vx, vy] = IOEToolBox.asg(img, m)
        B = (1/h**2) *np.ones([h, h], dtype = int)
        vxg           = IOEToolBox.filter2(B,vx)
        vyg           = IOEToolBox.filter2(B,vy)
        return vxg,vyg
    
    
    def cart2pol(x, y):
        rho = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        return(theta, rho)
    

    def pol2cart(theta, rho):
        x = rho * np.cos(theta)
        y = rho * np.sin(theta)
        return(x, y)
    

    def filter2(B, X):
        res = scipy.signal.convolve2d(X, B,mode='same', boundary='fill', fillvalue=0)
        return res
    

    def CornerDetector(img, radiusSe):
        corner = IOEToolBox.HarrysDetector(img)
        SE = cv.getStructuringElement(cv.MORPH_RECT, (2 * radiusSe + 1, 2 * radiusSe + 1), (radiusSe, radiusSe))
        corner = cv.dilate(corner,SE)
        return corner


    def HarrysDetector(img):
        im1 = np.float32(img)
        corner = cv.cornerHarris(im1,2,3,0.04)
        return corner 
   
