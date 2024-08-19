import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(2)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, frame = cap.read()
if ret:
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.show()

cap.release()
