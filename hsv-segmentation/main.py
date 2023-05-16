###############################################################################
# Processamento de Imagens em Cores - Segmentação                             #
# Disciplina: TEC434 - Computação Visual                                      #
# Professor: Cláudio Eduardo Goes                                             #
# Dupla: Allan Capistrano e João Erick Barbosa                                #
###############################################################################

from cv2 import imread, cvtColor, getStructuringElement, inRange, morphologyEx
from cv2 import bitwise_and, bitwise_or, namedWindow, imshow, waitKey
from cv2 import destroyAllWindows, COLOR_BGR2HSV, MORPH_CROSS, WINDOW_GUI_EXPANDED, MORPH_OPEN

from pathlib import Path

image_path = Path('images/pecas_lego.jpg')
image = imread(str(image_path))

image_in_HSV = cvtColor(image, COLOR_BGR2HSV)
cross_element = getStructuringElement(MORPH_CROSS, (3, 3)) # Elemento estruturante

green_mask = inRange(image_in_HSV, (32, 124, 40), (81, 255, 255))
result_green_mask = bitwise_and(image, image, mask=green_mask)

blue_mask = inRange(image_in_HSV, (97, 73, 0), (121, 255, 255))
open_operation = morphologyEx(blue_mask, MORPH_OPEN, cross_element)
result_blue_mask = bitwise_and(image, image, mask=open_operation)

red_mask = bitwise_or(
    inRange(image_in_HSV, (0, 125, 110), (4, 255, 255)), 
    inRange(image_in_HSV, (120, 125, 110), (180, 255, 255)), 
)
open_operation = morphologyEx(red_mask, MORPH_OPEN, cross_element)
result_red_mask = bitwise_and(image, image, mask=open_operation)

namedWindow('Imagem Original', WINDOW_GUI_EXPANDED)
imshow('Imagem Original', image)

namedWindow('Segmentação da cor verde', WINDOW_GUI_EXPANDED)
imshow('Segmentação da cor verde', result_green_mask)

namedWindow('Segmentação da cor azul', WINDOW_GUI_EXPANDED)
imshow('Segmentação da cor azul', result_blue_mask)

namedWindow('Segmentação da cor vermelha', WINDOW_GUI_EXPANDED)
imshow('Segmentação da cor vermelha', result_red_mask)

waitKey(0)
destroyAllWindows()