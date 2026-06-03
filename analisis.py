import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer archivo Excel
archivo = "encuesta.xlsx"

df = pd.read_excel(archivo)

# Crear carpeta para gráficos
os.makedirs("graficos", exist_ok=True)

print("=== RESUMEN DEL DATASET ===")
print("Número de encuestados:", len(df))
print()

# Analizar todas las columnas excepto la marca temporal
for columna in df.columns[1:]:

    print("\n" + "="*80)
    print(columna)

    frecuencias = df[columna].value_counts(dropna=False)

    print(frecuencias)

    plt.figure(figsize=(8,5))
    frecuencias.plot(kind="bar")

    plt.title(columna)
    plt.ylabel("Frecuencia")
    plt.tight_layout()

    nombre_archivo = (
        columna[:25]
        .replace("/", "-")
        .replace("?", "")
        .replace(":", "")
        + ".png"
    )

    plt.savefig(f"graficos/{nombre_archivo}")
    plt.close()

print("\nAnálisis completado.")
print("Los gráficos fueron guardados en la carpeta 'graficos'.")