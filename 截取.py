
import cv2


image = cv2.imread("JT3.jpg")
image2 = image[563:575, 585:624, :]
cv2.imwrite("end777.png", image2)
cv2.imshow("iamge-1", image2)
cv2.waitKey(0)

