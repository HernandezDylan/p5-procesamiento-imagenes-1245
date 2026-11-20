import cv2
import numpy as np
import sys

# Hernadez Dylan NC:1245
print("Hernadez Dylan NC:1245")
print("+-+-+-+- 2. Lectura y visualizacion de imagenes +-+-+-+-")

# 1. Leer y mostrar imagen
image = cv2.imread('CarroRojo.jpg')

if image is None:
    print("Error: No se encontro CarroRojo.jpg")
    sys.exit()

cv2.imshow('Carro Rojo 1245', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg 1245', gray_image)

# 3. Redimensionar imagen
resized_image = cv2.resize(image, (300, 200))
cv2.imwrite('resized_image.jpg 1245', resized_image)

# 4. Rotar imagen 90 grados
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_image = cv2.warpAffine(image, matrix, (w, h))
cv2.imwrite('rotated_image.jpg 1245', rotated_image)

# 5. Aplicar desenfoque gaussiano
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite('blurred_image.jpg 1245', blurred_image)

# 6. Detectar bordes con Canny
edges = cv2.Canny(gray_image, 100, 200)
cv2.imwrite('edges.jpg 1245', edges)

# 7. Dibujar rectangulo y texto
output_image = image.copy()
cv2.rectangle(output_image, (50, 50), (200, 200), (255, 0, 0), 3)
cv2.putText(output_image, 'OpenCV', (60, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imwrite('output_image.jpg 1245', output_image)

# 8. Aplicar umbralizacion
_, thresh_image = cv2.threshold(
    gray_image, 127, 255, cv2.THRESH_BINARY
)
cv2.imwrite('threshold_image.jpg 1245', thresh_image)

# 9. Encontrar y dibujar contornos
contours, _ = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

contours_image = image.copy()
cv2.drawContours(contours_image, contours, -1, (0, 255, 0), 2)
cv2.imwrite('contours_image.jpg 1245', contours_image)

print("Todos los ejercicios se realizaron correctamente.")
print("Imagenes guardadas correctamente.")

print("+-+-+-+- Hernandez Dylan NC:1245 +-+-+-+-+-")