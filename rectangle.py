import cv2
img = cv2.imread(r"C:\Users\VIJITHA REDDY\OneDrive\Desktop\computer vision\dhoni-chiku.jpg")
x, y = 250, 50
width, height = 400, 350
roi = img[y:y+height, x:x+width]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
