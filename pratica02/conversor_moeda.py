moeda_real = 100
taxa_dolar = 5.20
taxa_euro = 6.15

cambio_dolar = moeda_real / taxa_dolar
cambio_euro = moeda_real / taxa_euro

print(f"R${moeda_real} reais convertidos na cotação de hoje equivalem a aproximadamente US${cambio_dolar:.2f} ou £ {cambio_euro:.2f}") 


