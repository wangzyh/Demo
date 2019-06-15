import matplotlib.pyplot as plt
from matplotlib import image
import cv2

for page in range(1, 102):
    filename = f'a.jpg'
    img = cv2.imread(filename)
    ret, thresh1 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
    # plt.subplot(2, 3, i + 1),
    plt.imshow(thresh1)
    plt.title('qushuiyin')
    plt.xticks([]), plt.yticks([])

plt.show()

