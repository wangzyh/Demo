import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import matplotlib.pyplot as plt

# (1) 使用linspace函数初始化变量t，即从-pi到pi上均匀分布的201个点
a = float(9)
b = float(8)

for i in range(6, 100):

    t = np.linspace(-np.pi, np.pi, i)

    # (2) 使用sin函数和NumPy常量pi计算变量x
    x = np.sin(a * t + np.pi/2)

    # (3) 使用sin函数计算变量y
    y = np.sin(b * t)

    plt.axis('off')
    plt.xticks([])
    plt.yticks([])

    plot(x, y)

    plt.savefig(f"./picture/{i}.png")
    plt.pause(0.1)
# show()

