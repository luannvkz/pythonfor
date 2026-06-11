vendedores = int(input("Quantidade de vendedores: "))
dias = int(input("Quantidade de dias: "))

for i in range(vendedores):

    nome = input("Nome: ")
    total = 0

    for j in range(dias):

        venda = float(input("Venda: "))
        total = total + venda

    media = total / dias

    print("Nome:", nome)
    print("Total:", total)
    print("Media:", media)