import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

cerror = 32 # adjust accordingly

img = Image.open("HSAR 019/images/americangothic.jpg")
M = np.asarray(img)

# default chromolithographic palette from the German school primary source
c1_ref = [242, 204, 157]
c2_ref = [249, 222, 43]
c3_ref = [64, 38, 39]
c4_ref = [127, 177, 200]
c5_ref = [230, 139, 157]
c6_ref = [45, 124, 181]
c7_ref = [172, 173, 166]
c8_ref = [189, 15, 34]
c9_ref = [130, 130, 138]
white = [255, 255, 255]

# renoir luncheon palette generated from imagecolorpicker.com
# c1_ref = [206,164,153]
# c2_ref = [41,43,53]
# c3_ref = [158,122,116]
# c4_ref = [170,177,180]
# c5_ref = [111,127,135]
# c6_ref = [139,153,177]
# c7_ref = [114,80,76]
# c8_ref = [64,90,95]
# c9_ref = [192,65,76]
# white = [255, 255, 255]

# kadinsky waterfall palette generated from imagecolorpicker.com
# c1_ref = [47,64,72]
# c2_ref = [141,108,83]
# c3_ref = [179,160,148]
# c4_ref = [92,122,116]
# c5_ref = [103,81,65]
# c6_ref = [148,150,157]
# c7_ref = [159,164,159]
# c8_ref = [165,89,120]
# c9_ref = [29,17,17]
# white = [255, 255, 255]

c1 = M.copy()
c2 = M.copy()
c3 = M.copy()
c4 = M.copy()
c5 = M.copy()
c6 = M.copy()
c7 = M.copy()
c8 = M.copy()
c9 = M.copy()

def check_bounds(testcolor, refcolor):
    if(abs(testcolor[0] - refcolor[0]) <= cerror and
       abs(testcolor[1] - refcolor[1]) <= cerror and
       abs(testcolor[2] - refcolor[2]) <= cerror):
        return True
    return False

plt.figure(figsize=(20, 8))

# OG
plt.subplot(2, 5, 1)
plt.imshow(M)
plt.title("Original")
plt.axis('off')

# c1
plt.subplot(2, 5, 2)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c1_ref)):
            c1[i][j] = c1_ref
        else:
            c1[i][j] = white
plt.imshow(c1)
plt.title("C1")
plt.axis('off')

# c2
plt.subplot(2, 5, 3)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c2_ref)):
            c2[i][j] = c2_ref
        else:
            c2[i][j] = white
plt.imshow(c2)
plt.title("C2")
plt.axis('off')

# c3
plt.subplot(2, 5, 4)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c3_ref)):
            c3[i][j] = c3_ref
        else:
            c3[i][j] = white
plt.imshow(c3)
plt.title("C3")
plt.axis('off')

# c4
plt.subplot(2, 5, 5)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c4_ref)):
            c4[i][j] = c4_ref
        else:
            c4[i][j] = white
plt.imshow(c4)
plt.title("C4")
plt.axis('off')

# c5
plt.subplot(2, 5, 6)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c5_ref)):
            c5[i][j] = c5_ref
        else:
            c5[i][j] = white
plt.imshow(c5)
plt.title("C5")
plt.axis('off')

# c6
plt.subplot(2, 5, 7)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c6_ref)):
            c6[i][j] = c6_ref
        else:
            c6[i][j] = white
plt.imshow(c6)
plt.title("C6")
plt.axis('off')

# c7
plt.subplot(2, 5, 8)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c7_ref)):
            c7[i][j] = c7_ref
        else:
            c7[i][j] = white
plt.imshow(c7)
plt.title("C7")
plt.axis('off')

# c8
plt.subplot(2, 5, 9)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c8_ref)):
            c8[i][j] = c8_ref
        else:
            c8[i][j] = white
plt.imshow(c8)
plt.title("C8")
plt.axis('off')

# c9
plt.subplot(2, 5, 10)
for i in range(len(M)):
    for j in range(len(M[i])):
        if(check_bounds(M[i][j], c9_ref)):
            c9[i][j] = c9_ref
        else:
            c9[i][j] = white
plt.imshow(c9)
plt.title("C9")
plt.axis('off')

plt.show()
