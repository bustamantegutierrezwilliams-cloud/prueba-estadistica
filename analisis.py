import pandas as pd
import matplotlib.pyplot as plt

# Datos de edades válidas
edades = [18,19,19,19,23,22,18,18,18,18,
          18,19,18,19,18,20,20,20,20,21,
          32,19,21,24,19,19,30]

# Datos de género
genero = [
"Masculino","Masculino","Masculino","Masculino","Masculino",
"Masculino","Masculino","Masculino","Prefiero no decirlo",
"Masculino","Masculino","Masculino","Femenino","Masculino",
"Masculino","Masculino","Masculino","Masculino","Masculino",
"Femenino","Prefiero no decirlo","Femenino","Masculino",
"Femenino","Masculino","Masculino","Masculino","Masculino",
"Femenino"
]

# Tabla de edades
tabla_edades = pd.Series(edades).value_counts().sort_index()

print("TABLA DE FRECUENCIAS DE EDAD")
print(tabla_edades)

# Tabla de género
tabla_genero = pd.Series(genero).value_counts()

print("\nTABLA DE FRECUENCIAS DE GÉNERO")
print(tabla_genero)

# Gráfico de barras
plt.figure(figsize=(6,4))
tabla_genero.plot(kind='bar')
plt.title("Distribución por Género")
plt.xlabel("Género")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("grafico_genero.png")

# Histograma de edades
plt.figure(figsize=(6,4))
plt.hist(edades, bins=6)
plt.title("Histograma de Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("histograma_edades.png")

# Gráfico de torta
plt.figure(figsize=(6,6))
tabla_genero.plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.title("Distribución por Género")
plt.tight_layout()
plt.savefig("torta_genero.png")

print("\nGráficos generados correctamente.")