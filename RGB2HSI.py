import cv2
import numpy as np
import math

def RGB_TO_HSI(rgb_img):
    with np.errstate(invalid='ignore'):
        row = np.shape(rgb_img)[0]
        col = np.shape(rgb_img)[1]

        hsi_img = rgb_img.copy()
        blue, green, red = cv2.split(rgb_img)
        [blue, green, red] = [ i / 255.0 for i in ([blue, green, red])]

        # Calculate Hue
        hue = np.zeros((row, col))
        for i in range(row):
            den = np.sqrt((red[i] - green[i])**2 + (red[i] - blue[i]) * (green[i] - blue[i]))
            thetha = np.arccos(0.5 * (red[i] - blue[i] + red[i] - green[i]) / den)
            h = np.zeros(col)
            h[blue[i] <= green[i]] = thetha[blue[i] <= green[i]]
            h[green[i] < blue[i]] = 2 * np.pi - thetha[green[i] < blue[i]]
            h[den == 0] = 0
            hue[i] = h / (2 * np.pi)

        # Calculate Saturation
        saturation = np.zeros((row,col))
        for i in range(row):
            min = []
            for j in range(col):
                arr = [blue[i][j],green[i][j],red[i][j]]
                min.append(np.min(arr))
            min = np.array(min)
            saturation[i] = 1 - min * 3 / (red[i] + blue[i] + green[i])
            saturation[i][red[i] + blue[i] + green[i] == 0] = 0

        # Calculate Intensity
        intensity = (red + green + blue) / 3.0
        
        hsi_img[:,:,0] = hue * 255
        hsi_img[:,:,1] = saturation * 255
        hsi_img[:,:,2] = intensity * 255

    return hsi_img
