import cv2
import numpy

# Read image
img = cv2.imread('/Users/ratikdubey/Pictures/got_wallpaper.jpg')

resize = cv2.resize(img, (600 ,800))

# Select ROI
bo = cv2.selectROI(resize)

# Crop image
imgCrop = resize[int(bo[1]) :int(bo[1] + bo[3]), int(bo[0]) :int(bo[0] + bo[2])]

# Display cropped image
cv2.imshow("Image", imgCrop)
cv2.waitKey(0)
