vendedores = int(input("Quantidade de vendedores: "))
dias = int(input("Quantidade de dias: "))

total_equipe = 0

for i in range(vendedores):

    nome = input("Nome do vendedor: ")

    total_vendas = 0
    folgas = 0

    for j in range(dias):

        venda = float(input("Valor vendido: "))

        if venda == 0:
            folgas = folgas + 1

        else:
            total_vendas = total_vendas + venda

    media = total_vendas / dias

    print("Nome:", nome)
    print("Total vendido:", total_vendas)
    print("Media:", media)

    total_equipe = total_equipe + total_vendas

print("Total da equipe:", total_equipe)