import cv2
import numpy as np

def Histogram_Equalization(img):
    height,width=img.shape

    histogram = np.zeros(256)
    # finding histogram
    for i in range(height):
        for j in range(width):
            histogram[img[i][j]] += 1
    
    # Sigma(n)
    for i in range(1, 256):
        histogram[i] += histogram[i-1]
    
    # (255 / n) * Sigma(n)
    tmp = 255.0/(height*width)
    average = np.zeros((256,),dtype=np.float16)
    for i in range(256):
        average[i] = histogram[i] * tmp
    
    # 'average' now contains the equalized histogram
    average = average.astype(np.uint8)
    
    # Re-map values from equalized histogram into the image
    for i in range(height):
        for j in range(width):
            img[i][j] = average[img[i][j]]

    return img
