import pandas as pd
import os

current_dir = os.path.dirname(os.path. abspath(__file__))
file_path = os.path.join(current_dir, 'exercicio_pandas.xlsx')

if os.path.isfile(file_path):
    df_vendas = pd.read_excel(file_path)

    # Contar o numero de vendas por vendedor
    vendas_por_vendedor = df_vendas['Vendedor'].value_counts()

    # Obter os 3 Vendedores com mais vendas
    top_3_vendedores = vendas_por_vendedor.head(3)

    # Obter os 3 Vendedores com menos vendas, classificados do pior para o melhor
    bottom_3_vendedores = vendas_por_vendedor.tail(3).iloc[::-1]
    print("Top 3 Vendedores com mais vendas:")
    for vendedor, quantidade in top_3_vendedores.items():
        print(f"{vendedor}: {quantidade} vendas")
    print("\nPiores 3 Vendedores com menos Vendas (do pior para o melhor):")
    for vendedor, quantidade in bottom_3_vendedores.items():
        print(f"{vendedor}: {quantidade} vendas")
else:
    print(f"O arquivo {file_path} não foi encontrado.")
