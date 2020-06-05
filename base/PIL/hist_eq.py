from PIL import Image
from pylab import *
from base.PIL.im_tools import hist_eq

im = array(Image.open('lib.jpg').convert('L'))

# 直方图均衡化
im2, cdf = hist_eq(im)

# imshow(im2)
# gray()
# axis('off')

# 新建一个图像,将原图和均衡化图之间对比
figure()

subplot(2, 2, 1)
# 不使用颜色信息
gray()
# 在原点左上角显示轮廓图像
# contour(im, origin='image')
imshow(im)
axis('equal')
axis('off')

subplot(2, 2, 2)
hist(im.flatten(), 128)

subplot(2, 2, 3)
# 不使用颜色信息
gray()
# 在原点左上角显示轮廓图像
# contour(im2, origin='image')
imshow(im2)
axis('equal')
axis('off')

subplot(2, 2, 4)
hist(im2.flatten(), 128)


show()
