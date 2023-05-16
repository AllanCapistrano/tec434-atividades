###############################################################################
# Aplicando Threshold adaptativo em imagens de parafusos e encontrado as      #
# métricas de avaliação, a partir das taxas de erros e acertos .              # 
# Disciplina: TEC434 - Computação Visual                                      #
# Professor: Cláudio Eduardo Goes                                             #
# Dupla: Allan Capistrano e João Erick Barbosa                                #
###############################################################################

from pathlib import Path
from cv2 import imread, adaptiveThreshold, namedWindow, imshow, waitKey, destroyAllWindows, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, drawContours, RETR_CCOMP, CHAIN_APPROX_SIMPLE, findContours, bitwise_and, countNonZero
from numpy import concatenate, zeros, uint8

def fillHoles(src):
    contours,hierarchy = findContours(src, RETR_CCOMP, CHAIN_APPROX_SIMPLE)
    dst = zeros(src.shape, uint8)
    color = 255
    for i in range(len(contours)):
        drawContours(dst, contours,i, color, -1, 8, hierarchy, 0)
    return dst

if __name__ == '__main__':
    BLOCK_SIZE = 7

    for index in range(0, 7):
        path_images = Path(f'images/ground_truth/0{index + 1}.jpg')
        path_images_gt = Path(f'images/ground_truth/gt0{index + 1}.png')
        
        images = imread(str(path_images), 0)
        ground_truth = imread(str(path_images_gt), 0)

        images_th = adaptiveThreshold(
            images, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, BLOCK_SIZE, -3
        )

        result = concatenate((ground_truth, images_th), axis=1)

        namedWindow(f"Ground Truth 0{index + 1} x Imagem 0{index + 1}")
        imshow(f"Ground Truth 0{index + 1} x Imagem 0{index + 1}", result)

        #Verdadeiro Positivo
        image_true_positive = bitwise_and(ground_truth,images_th)
        #Verdadeiro Negativo
        image_false_positive = bitwise_and(~ground_truth,images_th)
        
        true_positive_rate = countNonZero(image_true_positive)/countNonZero(ground_truth) * 100
        ture_negative_rate = countNonZero(image_false_positive)/countNonZero(~ground_truth) * 100
        false_negative_rate = 100 - true_positive_rate
        false_positive_rate = 100 - ture_negative_rate

        print(f"---------Imagem {index + 1}---------")
        print("Verdadeiro Positivo: {:.2f} %".format(true_positive_rate)) 
        print("Verdadeiro Negativo: {:.2f} %".format(ture_negative_rate))
        print("Falso Positivo:      {:.2f} %".format(false_positive_rate))
        print("Falso Negativo:      {:.2f} %".format(false_negative_rate))
        print(f"------------------------------------\n")

    waitKey(0)
    destroyAllWindows()