import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("HSAR 019/images/rainbow.jpg")
M = np.asarray(img)

plt.figure(figsize=(12, 6))

plt.subplot(2, 4, 1)
plt.imshow(M)
plt.title("Original")
plt.axis('off')

cerror = 20
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
plt.subplot(2, 4, 2)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(abs(red[i][j][0] - 211) >= cerror or
           abs(red[i][j][1] - 35) >= cerror or
           abs(red[i][j][2] - 46) >= cerror):
            red[i][j] = [255, 255, 255]
plt.imshow(red)
plt.title("Red Channel")
plt.axis('off')

# orange
plt.subplot(2, 4, 3)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(abs(orange[i][j][0] - 254) >= cerror or
           abs(orange[i][j][1] - 116) >= cerror or
           abs(orange[i][j][2] - 0) >= cerror):
            orange[i][j] = [255, 255, 255]
plt.imshow(orange)
plt.title("Orange Channel")
plt.axis('off')

# yellow
plt.subplot(2, 4, 4)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(abs(yellow[i][j][0] - 254) >= cerror or
           abs(yellow[i][j][1] - 205) >= cerror or
           abs(yellow[i][j][2] - 5) >= cerror):
            yellow[i][j] = [255, 255, 255]
plt.imshow(yellow)
plt.title("Yellow Channel")
plt.axis('off')

# green
plt.subplot(2, 4, 5)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(abs(green[i][j][0] - 116) >= cerror or
           abs(green[i][j][1] - 195) >= cerror or
           abs(green[i][j][2] - 26) >= cerror):
            green[i][j] = [255, 255, 255]
plt.imshow(green)
plt.title("Green Channel")
plt.axis('off')

# turquoise
plt.subplot(2, 4, 6)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(abs(turquoise[i][j][0] - 0) >= cerror or
           abs(turquoise[i][j][1] - 160) >= cerror or
           abs(turquoise[i][j][2] - 160) >= cerror):
            turquoise[i][j] = [255, 255, 255]
plt.imshow(turquoise)
plt.title("Turquoise Channel")
plt.axis('off')

# blue
plt.subplot(2, 4, 7)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(abs(blue[i][j][0] - 79) >= cerror or
           abs(blue[i][j][1] - 102) >= cerror or
           abs(blue[i][j][2] - 195) >= cerror):
            blue[i][j] = [255, 255, 255]
plt.imshow(blue)
plt.title("Blue Channel")
plt.axis('off')

# purple
plt.subplot(2, 4, 8)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(abs(purple[i][j][0] - 95) >= cerror or
           abs(purple[i][j][1] - 66) >= cerror or
           abs(purple[i][j][2] - 176) >= cerror):
            purple[i][j] = [255, 255, 255]
plt.imshow(purple)
plt.title("Purple Channel")
plt.axis('off')

plt.show()
