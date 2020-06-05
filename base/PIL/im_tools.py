from PIL import Image
from pylab import *


def get_im_list(file_path):
    """返回目录中所有JPG图像的文件名列表"""

    return [os.path.join(file_path, f) for f in os.listdir(path) if f.endswith(".jpg")]


def im_resize(im, sz):
    """使用PIL 对象重新定义图像数组的大小"""

    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.size(sz))


def hist_eq(im, nbr_bins=256):
    """对一副灰度图像进行直方图均衡化"""

    # 计算图像的直方图
    im_hist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = im_hist.cumsum()  # 累积分布函数，cdf = cumulative distribution function
    cdf = 255 * cdf / cdf[-1]  # 归一化

    # 使用累计分布函数的插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf


def compute_average(im_list):
    """ 计算图像列表的平均图像"""

    # 打开第一幅图像，将其存储在浮点型数组中
    average_im = array(Image.open(im_list[0]), 'f')

    for im_name in im_list[1:]:
        try:
            average_im += array(Image.open(im_name))
        finally:
            print(im_name + '...skipped')
    average_im /= len(im_list)

    # 返回uint8 类型的平均图像
    return array(average_im, 'uint8')