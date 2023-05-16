###############################################################################
# Lista 4a - Processamento Morfológico de Imagens                             #
# Disciplina: TEC434 - Computação Visual                                      #
# Professor: Cláudio Eduardo Goes                                             #
# Dupla: Allan Capistrano e João Erick Barbosa                                #
###############################################################################

from os import system

from cv2 import getStructuringElement, namedWindow, morphologyEx, imshow, \
waitKey, destroyAllWindows, MORPH_CROSS, MORPH_RECT, MORPH_ERODE, \
WINDOW_GUI_EXPANDED, MORPH_DILATE, MORPH_OPEN, MORPH_CLOSE
from numpy import array, uint8

intensity = \
    [
        [0,255,255,0,0,0,0,0],
        [255,255,255,255,0,0,0,0],
        [0,255,255,255,0,0,0,0],
        [0,255,255,0,0,0,0,0],
        [0,0,255,255,0,255,255,0],
        [0,0,0,255,255,255,255,255],
        [0,0,0,0,255,255,255,255],
        [0,0,0,0,0,255,255,255]
    ]

image = array(intensity).astype(uint8)

elemento_cruz = getStructuringElement(MORPH_CROSS, (3, 3)) # Elemento estruturante
elemento_linha = getStructuringElement(MORPH_RECT, (3, 1)) # Elemento estruturante

while(True):
    system("clear")

    print("-------- Resoluções da Lista 4a --------\n")

    for i in range(0, 8):
        print(f"{i + 1} - Resposta da {i + 3}º Questão")
    
    try:
        value  = int(input("Selecione uma das opções ou '0' para sair: "))
    except:
        print("Opção inválida! Tente Novamente.")
        continue

    match(value):
        case 0:
            break
        case 1:
            # 3 Questão
            erosao = morphologyEx(image, MORPH_ERODE, elemento_cruz)

            namedWindow("Erosao Elemento 1", WINDOW_GUI_EXPANDED)
            imshow("Erosao Elemento 1", erosao)

            waitKey(0)
            destroyAllWindows()
        case 2:
            # 4 Questão
            erosao = morphologyEx(image, MORPH_ERODE, elemento_linha)

            namedWindow("Erosao Elemento 2", WINDOW_GUI_EXPANDED)
            imshow("Erosao Elemento 2", erosao)

            waitKey(0)
            destroyAllWindows()
        case 3:
            # 5 Questão
            dilatacao = morphologyEx(image, MORPH_DILATE, elemento_cruz)

            namedWindow("Dilatacao Elemento 1", WINDOW_GUI_EXPANDED)
            imshow("Dilatacao Elemento 1", dilatacao)

            waitKey(0)
            destroyAllWindows()
        case 4:
            # 6 Questão
            dilatacao = morphologyEx(image, MORPH_DILATE,  elemento_linha)

            namedWindow("Dilatacao Elemento 2", WINDOW_GUI_EXPANDED)
            imshow("Dilatacao Elemento 2", dilatacao)

            waitKey(0)
            destroyAllWindows()
        case 5:
            # 7 Questão
            abertura = morphologyEx(image, MORPH_OPEN, elemento_cruz)

            namedWindow("Abertura Elemento 1", WINDOW_GUI_EXPANDED)
            imshow("Abertura Elemento 1", abertura)

            waitKey(0)
            destroyAllWindows()
        case 6:
            # 8 Questão
            abertura = morphologyEx(image, MORPH_OPEN, elemento_linha)

            namedWindow("Abertura Elemento 2", WINDOW_GUI_EXPANDED)
            imshow("Abertura Elemento 2", abertura)

            waitKey(0)
            destroyAllWindows()
        case 7:
            # 9 Questão
            abertura = morphologyEx(image, MORPH_CLOSE, elemento_cruz)

            namedWindow("Fechamento Elemento 1", WINDOW_GUI_EXPANDED)
            imshow("Fechamento Elemento 1", abertura)

            waitKey(0)
            destroyAllWindows()
        case 8:
            # 10 Questão
            abertura = morphologyEx(image, MORPH_CLOSE, elemento_linha)

            namedWindow("Fechamento Elemento 2", WINDOW_GUI_EXPANDED)
            imshow("Fechamento Elemento 2", abertura)

            waitKey(0)
            destroyAllWindows()
        case _:
            print("Opção inválida! Tente Novamente.")
            continue