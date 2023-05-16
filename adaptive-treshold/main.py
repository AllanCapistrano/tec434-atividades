###############################################################################
# Aplicando Threshold adaptativo em imagens de parafusos.                      # 
# Disciplina: TEC434 - Computação Visual                                      #
# Professor: Cláudio Eduardo Goes                                             #
# Dupla: Allan Capistrano e João Erick Barbosa                                #
###############################################################################

from pathlib import Path
from cv2 import imread, adaptiveThreshold, namedWindow, imshow, waitKey, destroyAllWindows, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY
from numpy import concatenate

if __name__ == '__main__':
    BLOCK_SIZE = 7

    path_images = []
    images = []
    images_th = []
    result = []

    for index in range(1, 8):
        path_images.append(Path(f'images/ground_truth/0{index}.jpg'))
        images.append(imread(str(path_images[index - 1]), 0))

        images_th.append(
            adaptiveThreshold(
                images[index - 1], 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, BLOCK_SIZE, -3
            )
        )

        result.append(concatenate((images[index - 1], images_th[index - 1]), axis=1))

        namedWindow(f"Imagem 0{index}")
        imshow(f"Imagem 0{index}", result[index - 1])

    waitKey(0)
    destroyAllWindows()