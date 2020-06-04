import cv2

image = cv2.imread("D:/photo/1.png")

# 水平翻转
h_flip = cv2.flip(image, 1)
cv2.imwrite("D:/photo/h.jpg", h_flip)

# 垂直翻转
# v_flip = cv2.flip(image, 0)
# cv2.imwrite("v.jpg", v_flip)

# 水平垂直翻转
# hv_flip = cv2.flip(image, -1)
# cv2.imwrite("hv.jpg", hv_flip)

