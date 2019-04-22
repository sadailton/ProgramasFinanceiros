def valor_presente(juros, valorfuturo, pagamento, num_periodos):

    #pagamento = pagamento * (-1)
    juros = juros / 100
    vp: float = valorfuturo / pow(1+juros, num_periodos) + pagamento*(pow(1+juros, num_periodos)-1) / (pow(1 + juros, num_periodos + 1) - pow(1+juros, num_periodos))

    return vp

def valor_futuro(juros,pagamento,num_periodos):

    juros = juros / 100

    vf: float = pagamento*(1+juros)*((pow(1+juros,num_periodos)-1)/juros)

    return vf

def taxa_juros():
    return False

def imprime_menu():

    print("1 - Valor Presente")
    print("2 - Valor Futuro")
    print("3 - Taxa de juros")

def valida_entrada_usuario():
    return False

def main():

    while True:
        imprime_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            juros = float(input("Informe a taxa de juros: ").replace(',', '.'))
            pagamento = float(input("Informe o valor do pagamento: "))
            num_periodos = int(input("Informe a quantidade de depósitos: "))
            valorfuturo = float(input("Informe o valor futuro: ").replace(',', '.'))
            print("O valor presente é de R${:.4f}".format(valor_presente(juros, valorfuturo, pagamento, num_periodos)))
        elif opcao == "2":
            juros = float(input("Informe a taxa de juros: ").replace(',', '.'))
            pagamento = float(input("Informe o valor do pagamento: "))
            num_periodos = int(input("Informe a quantidade de depósitos: "))
            print("O valor a ser resgatado ao final do perído será de R${:.4f}".format(valor_futuro(juros,pagamento,num_periodos)))

        elif opcao == "3":
            taxa_juros()
        else:
            print("Opcao inválida!")


if __name__ == '__main__':

    main()
