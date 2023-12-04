import cv2

# Чтение изображения
image = cv2.imread('nature.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение фильтра для обнаружения границ
# Можно использовать Canny или другие методы
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Нахождение контуров
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Рисование контуров на исходном изображении
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Отображение результата
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
