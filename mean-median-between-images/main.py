###############################################################################
# Filtragem de ruído das imagens através de média e mediana.                 # 
# Disciplina: TEC434 - Computação Visual                                      #
# Professor: Cláudio Eduardo Goes                                             #
# Dupla: Allan Capistrano e João Erick Barbosa                                #
###############################################################################

from cv2 import imread, imshow, waitKey, destroyAllWindows, imwrite
from glob import glob
from numpy import array, zeros, sum, sort, uint8

file_list = glob('./images/*.png')
image_stack = array([array(imread(fname, 0)) for fname in file_list])

rows, columns = image_stack[0].shape

image_count = len(image_stack)
median = zeros((rows, columns), uint8)
mean = zeros((rows, columns), uint8)

for row in range(rows):
    for column in range(columns):
        sorted_pixels = sort(image_stack[:, row, column])
        median[row][column] = sorted_pixels[49]

        mean[row][column] = round(sum(image_stack[:, row, column]) / image_count)

imshow('Mediana da Imagem', median)
imshow('Media da Imagem', mean)

imwrite("result/median_image.png", median)
imwrite("result/mean_image.png", mean)

waitKey(0)
destroyAllWindows()
