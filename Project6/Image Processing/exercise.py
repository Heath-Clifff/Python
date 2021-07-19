import cv2
import glob

images = glob.glob("sample_images/*.jpg")
print(images)
for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imwrite("resized_"+image, re)
