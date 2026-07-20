import pandas as pd
import matplotlib.pyplot as plt


# Cargar datos
datos = pd.read_csv("datos/datos.csv")


print("DATOS DE EMPLEO JUVENIL ECUADOR")
print(datos)


print("\nPROMEDIOS:")
print(datos.describe())


# Gráfico de desempleo juvenil

plt.figure(figsize=(8,5))

plt.plot(
    datos["Año"],
    datos["Desempleo_Juvenil"],
    marker="o"
)

plt.title("Evolución del desempleo juvenil en Ecuador")
plt.xlabel("Año")
plt.ylabel("Desempleo juvenil (%)")

plt.grid()

plt.savefig("dashboard/desempleo_juvenil.png")

plt.show()