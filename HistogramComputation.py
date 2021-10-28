#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2
import math
import matplotlib.pyplot as plt


# In[26]:


img = cv2.imread("sample.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
cv2.imshow("Image", img)
cv2.waitKey()
cv2.destroyAllWindows()


# In[75]:


# show the plotting graph of an image using built in function
histr = cv2.calcHist([img],[0],None,[256],[0,256])

histr = [histr[i][0] for i in range(256)]
#plt.plot(histr)
plt.bar([i for i in range(1, 257)], histr)
plt.show()


# In[77]:


def calcHist(img):
    hist = [[i*0] for i in range(256)]
    height, width = img.shape
    for i in range(height):
        for j in range(width):
            hist[img[i][j]][0] += 1
    
    return hist    


# In[86]:


hist = calcHist(img)
hist = [hist[i][0] for i in range(256)]
#plt.plot(hist)
plt.bar([i for i in range(1, 257)], hist)
plt.show()


# In[ ]:




