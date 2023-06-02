###############################################################################
# Contagem de grãos em uma imagem.                                            #
# Disciplina: TEC434 - Computação Visual                                      #
# Professor: Cláudio Eduardo Goes                                             #
# Dupla: Allan Capistrano e João Erick Barbosa                                #
###############################################################################

import cv2
from pathlib import Path

from imutils import grab_contours

caminhoImagem = Path('images/rices.jpg')

image_rgb = cv2.imread(str(caminhoImagem))
image = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)

img_normalized = cv2.normalize(image,None,0, 255, cv2.NORM_MINMAX)
low_pass = cv2.GaussianBlur(img_normalized, (7,7), 0, 0)
threshold = cv2.adaptiveThreshold(
    low_pass, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, -3
)

cross_element = cv2.getStructuringElement(cv2.MORPH_CROSS, (15, 15))
elipse_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

erode = cv2.morphologyEx(threshold, cv2.MORPH_ERODE, cross_element)
dilate = cv2.morphologyEx(erode, cv2.MORPH_DILATE, elipse_element)

cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = grab_contours(cnts)

count = 0

for c in cnts:
    count += 1

    M = cv2.moments(c)

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    cv2.drawContours(image_rgb, [c], -1, (0, 0, 255), 2)
    cv2.putText(
        image_rgb, 
        f"{count}", 
        (cX, cY), 
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5, 
        (255, 0, 0), 
        1
    )

print(f"Existem {count} arroz na imagem!")

cv2.imshow("Contagem", image_rgb)

cv2.waitKey()
cv2.destroyAllWindows()