import cv2

img = cv2.imread("/Users/ECEM/Desktop/image.jpg")
cv2.imshow("Picture", img)

(b, g, r) = cv2.split(img)
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)

print(img.shape)
minimum = (5, 10, 15)
maximum = (230, 240, 250)
r = cv2.inRange(img, minimum, maximum)

merge = cv2.merge([b, g, r])
cv2.imshow("Merged picture", merge)
image = cv2.putText(merge, 'created by Ecem', org=(50, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 20, 100),
                    thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("new", image)

cv2.waitKey(0)
