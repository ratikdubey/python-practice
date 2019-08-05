import cv2
import time

video = cv2.VideoCapture(0)

check, frame = video.read()

time.sleep(3)

print(check)
print(frame)

# captures only first frame; use loop to capture video
#cv2.imshow('Capture', frame)

a = 1

while True:
    a += 1
    check, frame = video.read()
    print(frame)
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capture', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()

print('No. of frames captured: {}'.format(a))

cv2.destroyAllWindows()