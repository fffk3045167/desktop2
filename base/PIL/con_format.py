from PIL import Image
import os

# open()读取图像,convert()图像颜色转换,‘L’表示灰度图
pil_img = Image.open('tim1.jpg').convert('L')
one = Image.open('tim1.jpg').convert('L')

# 创建缩略图,thumbnail() 方法接受一个元组参数（该参数指定生成缩略图的大小）
pil_img.thumbnail((128, 128))

# crop()裁剪图像,接受一个四元组指定裁剪区域，四元组的坐标依次是（左，上，右，下），PIL 中指定坐标系的左上角坐标为（0，0）
box = (100, 100, 400, 400)
region = pil_img.crop(box)

# paste()粘贴
region = region.transpose(Image.ROTATE_180)
pil_img.paste(region, box)

# resize()调整尺寸，该方法的参数是一个元组，用来指定新图像的大小
out = pil_img.resize((128, 128))

# rotate()旋转，使用逆时针方式表示旋转角度
out = pil_img.rotate(45)

one.save(os.path.splitext('three.png')[0] + '.jpg')