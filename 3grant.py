import numpy as np
import cv2
from cv2 import *
import mahotas as mh
import pylab

detector=cv2.imread('input/1.jpg',cv2.IMREAD_UNCHANGED)
# detectorf=mh.gaussian_filter(detector,7)


fig=pylab.figure()

ax1.imshow(detector)
# pylab.gray()
# pylab.show()

ax2=fig.add_subplot(2,1,2)
T=mh.thresholding.rc(detector)
pylab.imshow(detector>T)
pylab.show()