import cv2
image = cv2.imread(r"C:\Users\oekpom\Desktop\passport.jpg")
gray_image =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r"C:\Users\oekpom\Desktop\image\gray.png", gray_image)
inverted_image = 255 - gray_image
cv2.imwrite(r"C:\Users\oekpom\Desktop\image\inv.png", inverted_image)
blurred = cv2.GaussianBlur(inverted_image, (21, 21),0)
cv2.imwrite(r"C:\Users\oekpom\Desktop\image\blur.png", blurred)
inverted_blurred = 255 - blurred
cv2.imwrite(r"C:\Users\oekpom\Desktop\image\invblur.png", inverted_blurred)
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=200.0)
cv2.imwrite(r"C:\Users\oekpom\Desktop\image\sketch.png", pencil_sketch)
