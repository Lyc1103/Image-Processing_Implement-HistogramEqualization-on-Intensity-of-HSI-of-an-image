import cv2
from RGB2HSI import RGB_TO_HSI
from HistogramEqualization import Histogram_Equalization
from HSI2RGB import HSI_TO_RGB

img_name = input("Please input the image name you want to enhance: ")
img = cv2.imread(img_name, cv2.IMREAD_COLOR)

# Translate imge from RGB to HSI
hsi_img = RGB_TO_HSI(img)
cv2.imwrite("HSI-" + img_name, hsi_img)

# Apply the histogram equalization algorithm to the I component to obtain th i' component
hue, saturation, intensity = cv2.split(hsi_img)
equ_histr_intensity = Histogram_Equalization(intensity)
hsi_img[:,:,0] = hue
hsi_img[:,:,1] = saturation
hsi_img[:,:,2] = equ_histr_intensity

# Translate image from HSI to RGB
rgb_img = HSI_TO_RGB(hsi_img)
cv2.imwrite("RGB-" + img_name, rgb_img)

cv2.imshow("RGB Image", rgb_img)
cv2.imshow("HSI Image", hsi_img)
cv2.imshow("Original Image", img)
cv2.waitKey()
cv2.destroyAllWindows()
