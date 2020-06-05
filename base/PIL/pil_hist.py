from PIL import Image
from pylab import *


# 读取图像到到数组中
im = array(Image.open('lib.jpg').convert('L'))

# 新建一个图像
figure()
subplot(1, 2, 1)
# 不使用颜色信息
gray()
# 在原点左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')


subplot(1, 2, 2)
hist(im.flatten(), 128)

# print(im.shape, im.dtype)
show()