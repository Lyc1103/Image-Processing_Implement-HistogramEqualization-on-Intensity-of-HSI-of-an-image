import cv2
import numpy as np

def HSI_TO_RGB(hsi_img):
    hue, saturation, intensity = cv2.split(hsi_img)
    [hue, saturation, intensity] = [ i / 255.0 for i in ([hue, saturation, intensity])]
    
    rgb_img = hsi_img.copy()
    red, green, blue = hue, saturation, intensity
    for i in range(hsi_img.shape[0]):
        H = hue[i] * 2 * np.pi
        
        # The condition: If 0 <= H < 2 * np.pi / 3
        a = (H >= 0) & (H < 2 * np.pi / 3)
        tmp = np.cos(np.pi / 3 - H)
        b = intensity[i] * (1 - saturation[i])
        r = intensity[i] * (1 + saturation[i] * np.cos(H) / tmp)
        g = 3 * intensity[i] - r - b
        blue[i][a] = b[a]
        red[i][a] = r[a]
        green[i][a] = g[a]
        # The condition: If 2 * np.pi / 3 <= H < 4 * np.pi / 3
        a = (H >= 2 * np.pi/3) & (H < 4 * np.pi/3)
        tmp = np.cos(np.pi - H)
        r = intensity[i] * (1 - saturation[i])
        g = intensity[i] * (1 + saturation[i] * np.cos(H - 2 * np.pi / 3) / tmp)
        b = 3 * intensity[i] - r - g
        red[i][a] = r[a]
        green[i][a] = g[a]
        blue[i][a] = b[a]
        # The condition: If 4 * np.pi / 3 <= H < 2 * np.pi
        a = (H >= 4 * np.pi / 3) & (H < 2 * np.pi)
        tmp = np.cos(5 * np.pi / 3 - H)
        g = intensity[i] * (1 - saturation[i])
        b = intensity[i] * (1 + saturation[i] * np.cos(H - 4 * np.pi / 3) / tmp)
        r = 3 * intensity[i] - g - b
        blue[i][a] = b[a]
        green[i][a] = g[a]
        red[i][a] = r[a]

    rgb_img[:,:,0] = blue*255
    rgb_img[:,:,1] = green*255
    rgb_img[:,:,2] = red*255
    return rgb_img
