import cv2
image = cv2.imread("E:\0d31d0ff-00fa-49e5-bb25-f48bad4b4f55 (1).jpg") # Replace 'sample.jpg' with your image path
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
