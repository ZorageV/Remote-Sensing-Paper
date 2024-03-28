import numpy as np
import  matplotlib.pyplot as plt
import cv2 as cv
from PIL import Image
from patchify import patchify

img = cv.imread("./Final Dataset/train/River/River_1.jpg")
img = np.asarray(img)
print(img.shape)
patches = patchify(img,(16,16,3),step=16)
print(patches.shape)