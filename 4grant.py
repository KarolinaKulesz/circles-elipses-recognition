# import numpy as np
# import cv2
# from cv2 import *
# import mahotas as mh
# import pylab
#
# detector=cv2.imread('input/1.jpg',cv2.IMREAD_UNCHANGED)
# # detectorf=mh.gaussian_filter(detector,7)
#
#
# ret,th1 = cv2.threshold(detector,200,255,cv2.THRESH_BINARY)
# fig=pylab.figure()
# ax1=fig.add_subplot(2,1,1)
# ax1.imshow(detector)
#
# ax2 = fig.add_subplot(2, 1, 2)
# pylab.imshow(th1)
# pylab.show()

import matplotlib.pylab as plt
import cv2
import numpy as np



img = cv2.imread('input/1.jpg',0)
# img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

fig=plt.figure()
ax1=fig.add_subplot(4,1,1)
ax1.imshow(img)
ax1.axis('off')
# Apply threshold.
from skimage.filter import threshold_adaptive
from skimage import img_as_ubyte

bw = threshold_adaptive(img, 95, offset=10)

ax2=fig.add_subplot(4,1,2)
ax2.imshow(bw)
ax2.axis('off')

# ax2.set_title('Adaptive threshold', fontsize=24)

cv_image=img_as_ubyte(bw)
circles = cv2.HoughCircles(cv_image,cv2.HOUGH_GRADIENT,1,1,
                            param1=10,param2=15,minRadius=0,maxRadius=100)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # # draw the outer circle
    # cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

ax3=fig.add_subplot(4,1,3)
ax3.axis('off')
ax3.imshow(cimg)

ellipses=cv2.fitEllipse(cv_image)
ax4=fig.add_subplot(4,1,4)
ax4.axis('off')
ax4.imshow(ellipses)

plt.show()
cv2.waitKey(0)
# cv2.destroyAllWindows()