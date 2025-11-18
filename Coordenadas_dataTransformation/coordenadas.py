import pandas as pd
import json

# Ruta del archivo JSON
ruta_json = "502153.json"

# Leer archivo JSON
with open(ruta_json, "r", encoding="utf-8") as file:
    data = json.load(file)

# Convertir a DataFrame
df = pd.DataFrame(data)

# Renombrar columnas para claridad
df = df.rename(columns={
    "externalIdCliente": "cliente",
    "lat": "latitud",
    "lng": "longitud"
})

# Exportar a CSV
df.to_csv("502153.csv", index=False, encoding="utf-8")

print("Archivo CSV generado correctamente!")