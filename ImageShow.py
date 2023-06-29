
# In[1]:

#Canny Edge detection

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('severe.jpg')
#280,320
edges = cv2.Canny(img,100,220)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image')

plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Image')

plt.show()

img.shape

from ImageProcessing import ImageProcessing

y = ImageProcessing(img)

y.plot_image_processing()

area = y.image_processing_area()

area
