import pandas as pd

# Wczytaj plik CSV (np. dane.csv)
csv_file = r"C:\Users\Kuba\Desktop\dane.csv"
excel_file = r"C:\Users\Kuba\Desktop\dane.xlsx"

# Odczyt CSV do DataFrame
df = pd.read_csv(csv_file)

# Zapis do Excela
df.to_excel(excel_file, index=False)

print(f"Plik {csv_file} został przekonwertowany do {excel_file}")