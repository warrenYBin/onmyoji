
import cv2


image = cv2.imread("JT2.jpg")
image2 = image[398:426, 615:742, :]
cv2.imwrite("endagin.png", image2)
cv2.imshow("iamge-1", image2)
cv2.waitKey(0)

