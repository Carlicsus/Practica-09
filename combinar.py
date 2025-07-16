import pandas as pd

# 1. Cargar los dos archivos
df1 = pd.read_csv('./netflix_tv_shows_detailed_up_to_2025.csv')
df2 = pd.read_csv('netflix_movies_detailed_up_to_2025.csv')

# 2. Obtener todas las columnas presentes en ambos archivos
all_cols = set(df1.columns).union(df2.columns)

# 3. Asegurar que ambos DataFrames tengan todas las columnas
df1 = df1.reindex(columns=all_cols)
df2 = df2.reindex(columns=all_cols)

# 4. Combinar en un solo DataFrame
df_combinado = pd.concat([df1, df2], ignore_index=True)

# 5. Guardar en un nuevo CSV
df_combinado.to_csv('combinado.csv', index=False)

print("¡Listo! Archivo combinado guardado como 'combinado.csv'.")
