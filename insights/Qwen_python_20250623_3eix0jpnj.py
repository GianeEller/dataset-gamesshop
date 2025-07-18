import pandas as pd
import matplotlib.pyplot as plt

# Dados dos produtos mais vendidos
data = {
    'Produto': ['NEW MEGANIUM RG28XX', 'NEW MEGANIUM RG CubeXX', 'NEW MEGANIUM RG 40XXV',
                'NEW MEGANIUM RG35XX', 'MEGANIUM RG353M'],
    'Quantidade': [45, 44, 39, 38, 32]
}

df = pd.DataFrame(data)

# Gráfico de Barras - Produtos Mais Vendidos
plt.figure(figsize=(10,6))
plt.bar(df['Produto'], df['Quantidade'], color='skyblue')
plt.title('Top Produtos Mais Vendidos (Quantidade)')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()