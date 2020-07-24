import cv2
import numpy as np
from matplotlib import pyplot as plt
a = cv2.imread('mypic1.jpg',)
gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
x = cv2.GaussianBlur(gray,(3,3),0)
laplacian = cv2.Laplacian(x, cv2.CV_64F)
sobelx = cv2.Sobel(x, cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(x, cv2.CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),
plt.imshow(x, cmap = 'gray')
plt.title('Org'),
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),
plt.imshow(laplacian, cmap = 'gray')
plt.title('Lapl'),
plt.xticks([]),
plt.yticks([])
plt.subplot(2,2,3),
plt.imshow(sobelx,cmap = 'gray')
plt.title('SobX'),
plt.xticks([]),
plt.yticks([])
plt.subplot(2,2,4),
plt.imshow(sobely, cmap = 'gray')
plt.title('SobY'),
plt.xticks([]),
plt.yticks([])
plt.show()
