from PIL import Image
from pylab import *
from scipy.ndimage import filters

# 灰度图像的高斯模糊
im1 = array(Image.open('lib.jpg').convert('L'))

# 不同标准差的高斯核
im2 = filters.gaussian_filter(im1, 2)
im3 = filters.gaussian_filter(im1, 5)
im4 = filters.gaussian_filter(im1, 10)


# 绘制图像
figure()

subplot(2, 2, 1)
imshow(im1, cmap="gray")
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

# 彩色图像的高斯模糊(对每一个颜色通道进行高斯模糊)
im_c = array(Image.open('lib.jpg'))

im5 = zeros(im_c.shape)
for i in range(3):
    im5[:, :, i] = filters.gaussian_filter(im_c[:, :, i], 5)

im5 = array(im5, 'uint8')
# 或者im5 = uint(im5)


figure()
imshow(im5, cmap='gray')
axis('off')


show()
