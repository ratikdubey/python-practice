import cv2

img = cv2.imread('/Users/ratikdubey/Pictures/got_wallpaper.jpg', 1)

print(img.shape)

resize = cv2.resize(img, (600,600))

cv2.imshow('GOT', resize)
cv2.waitKey(0)

cv2.destroyAllWindows()