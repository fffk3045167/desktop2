from numpy import *
from numpy import random
from scipy.ndimage import filters
from imageio import imwrite
from base.PIL.rof import denoise


# 使用噪声创建合成图像
im = zeros((500, 500))
im[100:400, 100:400] = 128
im[200:300, 200:300] = 255

im = im + 30*random.standard_normal((500, 500))

U, T = denoise(im, im)
G = filters.gaussian_filter(im, 10)

U = uint8(U)
G = uint8(G)

# 保存生成结果,不能保存为jpg格式，因为jpg是压缩格式,会丢失一部分数据
imwrite('synth_rof.pdf', U)
imwrite('synth_gaussian.pdf', G)