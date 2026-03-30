import sys
import os
import pandas as pd


def csv_to_parquet(csv_path, parquet_path=None):
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")

    # Define o nome de saída se não for fornecido
    if parquet_path is None:
        base, _ = os.path.splitext(csv_path)
        parquet_path = base + ".parquet"

    # Lê o CSV
    df = pd.read_csv(csv_path)

    # Salva como Parquet
    df.to_parquet(parquet_path, index=False)

    print(f"Arquivo convertido com sucesso: {parquet_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <caminho_csv> [caminho_saida_parquet]")
        sys.exit(1)

    csv_path = sys.argv[1]
    parquet_path = sys.argv[2] if len(sys.argv) > 2 else None

    csv_to_parquet(csv_path, parquet_path)
