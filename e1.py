# El volumen actual de un depósito de agua (en metros cúbicos)
volumen_reservorio = 4.445e8
# La cantidad de lluvia de una tormenta (en metros cúbicos)
lluvia = 5e6

# Escribe tu respuesta aqui ✍️

lluvia *= 0.9

volumen_reservorio += lluvia

volumen_reservorio *= 1.05

volumen_reservorio *= 0.98

volumen_reservorio -= 2.5e5


print(volumen_reservorio)