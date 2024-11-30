import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import Triangulation as tri


left_imgPath = r"/home/lintan/Depth-Estimation/Images/rame_020_lft.png"
right_imgPath = r"/home/lintan/Depth-Estimation/Images/frame_020_rgt.png"

left_image = cv.imread(left_imgPath, cv.IMREAD_GRAYSCALE)
right_image = cv.imread(right_imgPath, cv.IMREAD_GRAYSCALE)

display = tri.Triangulation()
corners = display.img_rectification(left_image, right_image)
left_corners, right_corners = corners
fundamental_matrix, inliers1, inliers2 = display.fundamental_matrix_calculation(left_corners, right_corners)
print(fundamental_matrix)
print(inliers1)
print(inliers2)
