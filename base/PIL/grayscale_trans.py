from PIL import Image
from pylab import *


im = array(Image.open('tim2.jpg').convert('L'))

# 对图像进行反相处理
im2 = 255 - im

# 将图像像素值变换到100-200之间
im3 = (100.0 / 255) * im + 100

# 对图像像素值求平方后得到的图像
im4 = 255.0 * (im / 255) ** 2


# print(int(im.min()), int(im.max()))

# 绘制图像
figure()

subplot(2, 2, 1)
imshow(im, cmap="gray")
axis('off')

subplot(2, 2, 2)
imshow(im2, cmap="gray")
axis('off')

subplot(2, 2, 3)
imshow(im3, cmap="gray")
axis('off')

subplot(2, 2, 4)
imshow(im4, cmap="gray")
axis('off')

show()