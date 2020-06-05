from PIL import Image
from pylab import *
from base.PIL.im_pca import pca

im_list = ['oip.jpg', 'lib.jpg', 'three.jpg', 'one.jpg']

im = array(Image.open(im_list[0]))
m, n = im.shape[0:2]

im_matrix = array(array(im.flatten(), 'f'))

V, S, im_mean = pca(im_matrix)


figure()
gray()
subplot(2, 4, 1)
imshow(im_mean.reshape(m, n))
for i in range(7):
    subplot(2, 4, i + 2)
    imshow(V[i].reshape(m, n))

show()
