import pandas as pd

df = pd.read_excel("precios.xlsx")

df["Diferencia"] = df["Precio_propio"] - df["Precio_competencia"]
df["Estado"] = df["Diferencia"].apply(lambda x: "MAS CARO" if x > 0 else ("MAS BARATO" if x < 0 else "IGUAL"))

print("=== COMPARATIVA DE PRECIOS ===")
print(df.to_string(index=False))

print("\n=== RESUMEN ===")
print(f"Precio propio medio: {df['Precio_propio'].mean():.2f}")
print(f"Precio competencia medio: {df['Precio_competencia'].mean():.2f}")
print(f"Dias mas caro: {(df['Estado'] == 'MAS CARO').sum()}")
print(f"Dias mas barato: {(df['Estado'] == 'MAS BARATO').sum()}")

df.to_excel("comparativa_precios.xlsx", index=False)
print("\nResultados guardados en comparativa_precios.xlsx")
