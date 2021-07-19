import cv2

galaxy_img = cv2.imread("galaxy.jpg", 1)

print(type(galaxy_img))
print(galaxy_img.shape)

resized_img = cv2.resize(galaxy_img, (1000, 600))
cv2.imshow("Galaxy", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Galaxy_resized.jpg", resized_img)
