import cv2
import numpy as np
from matplotlib import pyplot as plt

#AVGBlurr
x = cv2.imread('mypic2.jpg')
abl = cv2.blur(x,(7,7))
plt.subplot(121),plt.imshow(x),plt.title('Org')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(abl),plt.title('Blurr')
plt.xticks([]), plt.yticks([])
plt.show()


#GaussianBlurr
x1 = cv2.imread('mypic1.jpg')
gbl = cv2.GaussianBlur(x1,(7,7),0)
plt.subplot(121), plt.imshow(x1), plt.title('Org')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(gbl), plt.title('Blur')
plt.xticks([]), plt.yticks([])
plt.show()






