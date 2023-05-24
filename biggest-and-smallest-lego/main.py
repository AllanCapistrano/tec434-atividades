###############################################################################
# Encontrar maior e menor peça de lego azul                                   #
# Disciplina: TEC434 - Computação Visual                                      #
# Professor: Cláudio Eduardo Goes                                             #
# Dupla: Allan Capistrano e João Erick Barbosa                                #
###############################################################################

from cv2 import imread, cvtColor, getStructuringElement, inRange, morphologyEx, \
    imshow, findContours, contourArea, boundingRect, rectangle, waitKey, \
    destroyAllWindows, COLOR_BGR2HSV, MORPH_CROSS, MORPH_OPEN, RETR_CCOMP, \
    CHAIN_APPROX_SIMPLE
from numpy import Inf

from pathlib import Path

image_path = Path('images/pecas_lego.jpg')
image = imread(str(image_path))

image_in_HSV = cvtColor(image, COLOR_BGR2HSV)
cross_element = getStructuringElement(MORPH_CROSS, (3, 3)) # Elemento estruturante

initial_threshold = inRange(image_in_HSV, (97, 73, 0), (121, 255, 255))
threshold = morphologyEx(initial_threshold, MORPH_OPEN, cross_element)

imshow('Threshold', threshold)

smallest_area = Inf 
smallest_contour_index = 0
largest_area = 0
largest_contour_index = 0

contours, _ = findContours(threshold, RETR_CCOMP, CHAIN_APPROX_SIMPLE)
largest_bounding_rect = None
smallest_bounding_rect = None

for index in range(len(contours)):
    #  Descobre a área do contorno
    contour_area = contourArea(contours[index],False)
    
    if(contour_area > largest_area):
        largest_area = contour_area

        # Armazena o índice do maior contorno
        largest_contour_index = index
        # Define o retângulo para o maior contorno
        largest_bounding_rect = boundingRect(contours[index])
    
    if(contour_area < smallest_area):
        smallest_area = contour_area

        # Armazena o índice do menor contorno
        smallest_contour_index = index
        # Define o retângulo para o menor contorno
        smallest_bounding_rect = boundingRect(contours[index])

rectangle(image, largest_bounding_rect, (0, 0, 255), 2, 8, 0)
rectangle(image, smallest_bounding_rect, (0, 255, 255), 2, 8, 0)

imshow('Imagem', image)

waitKey(0)
destroyAllWindows()