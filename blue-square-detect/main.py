###############################################################################
# Processamento de Imagens em Cores - Detecção de quadrado azul.              #
# Disciplina: TEC434 - Computação Visual                                      #
# Professor: Cláudio Eduardo Goes                                             #
# Dupla: Allan Capistrano e João Erick Barbosa                                #
###############################################################################

from cv2 import imread, GaussianBlur, getStructuringElement, inRange, cvtColor, \
    morphologyEx, imshow, findContours, drawContours, putText, waitKey, \
    destroyAllWindows, moments, COLOR_BGR2HSV, MORPH_CROSS, MORPH_OPEN, \
    RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, FONT_HERSHEY_SIMPLEX
from imutils import grab_contours

from pathlib import Path

from shapedetector import ShapeDetector

image_path = Path('images/algunas-figuras-geometricas.jpg')
image = imread(str(image_path))

blurred = GaussianBlur(image, (5, 5), 0)

image_in_HSV = cvtColor(blurred, COLOR_BGR2HSV)
cross_element = getStructuringElement(MORPH_CROSS, (3, 3)) # Elemento estruturante

initial_threshold = inRange(image_in_HSV, (66, 47, 226), (93, 82, 255))
threshold = morphologyEx(initial_threshold, MORPH_OPEN, cross_element)

imshow('Threshold', threshold)

cnts = findContours(threshold, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
cnts = grab_contours(cnts)

sd = ShapeDetector()

for c in cnts:
    M = moments(c)
    shape = sd.detect(c)

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    drawContours(image, [c], -1, (0, 0, 255), 6)
    putText(
        image, 
        "Quadrado Azul", 
        (cX, cY), 
        FONT_HERSHEY_SIMPLEX,
        0.5, 
        (0, 0, 0), 
        1
    )

imshow("Image", image)

waitKey(0)
destroyAllWindows()