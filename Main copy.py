
# Python program to identify
#color in images
# Importing the libraries OpenCV and numpy

import cv2
import numpy as np

from HSVGenerator import RGBtoHSV2

def main():

    # Inicia a captura de vídeo da webcam
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return
    
    while True:
        # Captura um quadro da webcam
        ret, frame = cap.read()

        if not ret:
            print("Não foi possível capturar o quadro.")
            break

        # Convert Image to Image HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Vermelho
        HSV = RGBtoHSV2(255,0,0)
        lower = np.array([HSV-10, 100, 100])
        upper = np.array([HSV+10, 255, 255])
        mask_red = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Desenha retângulos ao redor dos contornos veremlhos
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filtra áreas pequenas para evitar ruído
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Desenha o retângulo em azul


        # laranja
        HSV = RGBtoHSV2(255,174,0)
        lower = np.array([HSV-10, 100, 100])
        upper = np.array([HSV+10, 255, 255])
        mask_orange = cv2.inRange(hsv, lower, upper)
        
        # branco
        HSV = RGBtoHSV2(255,255,255)
        lower = np.array([0, 0, 160])
        upper = np.array([180, 30, 255])
        mask_white = cv2.inRange(hsv, lower, upper)


        # Combina as duas máscaras
        combined_mask = cv2.bitwise_or(mask_red, cv2.bitwise_or(mask_orange, mask_white))
        
        res = cv2.bitwise_and(frame,frame,mask = combined_mask)

        # Display Image and Mask
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", combined_mask)
        cv2.imshow("Result", res)

        # Pressiona 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera a captura de vídeo e fecha todas as janelas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()