nome = input("Digite seu nome do produto:" )
codigo = input("Digite sua codigo do produto: ")
quantidade = float(input("Digite seu quantidade do produto: "))
preço = float(input("Digite seu preço do produto: "))

produto =[
    nome, codigo, quantidade, preço 
]

valor = quantidade * preço


print("Produto cadastrado foi:",produto)
print ("O valor final foi", valor)


