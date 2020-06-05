from PIL import Image
from pylab import *


# 读取图像到数组中
im = array(Image.open('two.jpg'))

# 绘制图像
imshow(im)

# 不使用颜色信息
gray()

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
# 绘制四个点，连接其中两个
plot(x, y, 'r*')
plot(x[:2], y[:2])

# 不显示坐标轴
axis('off')

# 显示标题
title("plotting:one.jpg")

# 点击标注
x = ginput(3)
print("your clicked:" + str(x))

show()