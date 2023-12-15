import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("HSAR 019/images/rainbow.jpg")
M = np.asarray(img)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(M)
plt.title("Original")
plt.axis('off')

cerror = 0.1
red = np.zeros((len(M), len(M[0]), 3))
orange = np.zeros((len(M), len(M[0]), 3))
yellow = np.zeros((len(M), len(M[0]), 3))
green = np.zeros((len(M), len(M[0]), 3))
turquoise = np.zeros((len(M), len(M[0]), 3))
blue = np.zeros((len(M), len(M[0]), 3))
purple = np.zeros((len(M), len(M[0]), 3))

red = M.copy()
orange = M.copy()
yellow = M.copy()
green = M.copy()
turquoise = M.copy()
blue = M.copy()
purple = M.copy()

# red
plt.subplot(1, 2, 2)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(abs(red[i][j][0] - 211) >= cerror or
           abs(red[i][j][1] - 35) >= cerror or
           abs(red[i][j][2] - 46) >= cerror):
            red[i][j] = [255, 255, 255]
plt.imshow(red)
plt.title("Red Channel")
plt.axis('off')

plt.show()