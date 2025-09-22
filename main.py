import pandas as pd

def clean_excel(input_file: str, output_file: str):
    # Učitaj Excel fajl
    df = pd.read_excel(input_file)

    print("✅ Original data:")
    print(df.head())

    # Očisti podatke:
    # - Ukloni duplikate
    # - Ukloni redove sa praznim vrednostima
    df_clean = df.drop_duplicates().dropna()

    # Sačuvaj novi Excel fajl
    df_clean.to_excel(output_file, index=False)

    print(f"\n✅ Cleaned data saved to {output_file}")

if __name__ == "__main__":
    input_file = "sample_data.xlsx"
    output_file = "cleaned_data.xlsx"
    clean_excel(input_file, output_file)
