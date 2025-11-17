import json
import pandas as pd

# Leer el archivo JSON
with open('clientes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convertir a DataFrame
df = pd.DataFrame(data)

# Exportar a Excel
df.to_excel('clientes.xlsx', index=False)

print("✅ Archivo Excel generado: clientes.xlsx")
