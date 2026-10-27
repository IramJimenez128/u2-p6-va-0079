import matplotlib.pyplot as plt
import numpy as np
# Iram Jimenez NC = 0079

cant_productos = [100, 150, 200, 350, 500]
precio = [4000, 7000, 9000, 12000, 18000]

#plt.plot(cant_productos, precio)
#plt.show()

# Personalizando la grafica
plt.plot(cant_productos, precio, color = "green", marker = "o", linestyle = "dashed", linewidth = 2, markersize = 12)
plt.title("Venta de Walmart 0079")
plt.xlabel("Cantidad de productos")
plt.ylabel("Precio")
plt.show()