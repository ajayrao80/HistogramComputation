import cv2
import math
import matplotlib.pyplot as plt


# Function to calculate histogram
def calcHist(img):
    hist = [[i*0] for i in range(256)]
    height, width = img.shape
    for i in range(height):
        for j in range(width):
            hist[img[i][j]][0] += 1
    
    return hist  

  

# Driver code
img = cv2.imread("sample.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.waitKey()
cv2.destroyAllWindows()

# show the plotting graph of an image using built in function
histr = cv2.calcHist([img],[0],None,[256],[0,256])
histr = [histr[i][0] for i in range(256)]
#plt.plot(histr)
plt.bar([i for i in range(1, 257)], histr)
plt.show()



# Plotting histogram
hist = calcHist(img)
hist = [hist[i][0] for i in range(256)]
#plt.plot(hist)
plt.bar([i for i in range(1, 257)], hist)
plt.show()









