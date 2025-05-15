preco = 185 #valor do produto
desconto = 10 #valor do desconto

valor_final = preco - (preco * desconto / 100)
desconto_aplicado = preco - valor_final 
print(f"\n Você recebeu {desconto}% de desconto, o falor final ficou R${valor_final}")
print(f"\n Acabou de economizar R${desconto_aplicado}")


