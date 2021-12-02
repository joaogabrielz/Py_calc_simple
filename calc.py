option = 1
while option == 1:
    print('selecione')
    print('1-calular')
    print('2-sair')
    option = int(input("opção: "))
    if (option != 1):
        break
    n1 = int(input("Digite 1* numero: "))
    n2 = int(input("Digite 1* numero: "))

    print("Adição - press 1 (+)")
    print("Adição - press 2 (-)")
    print("Adição - press 3 (*)")
    print("Adição - press 4 (/)")
    operador =int(input("Qual calculo deseja fazer?:"))
    match operador:
        case 1:
            result = n1+n2
        case 2:
            result = n1-n2
        case 3:
            result = n1 * n2
        case 4:
            result = n1 / n2
        case _:
            print('opcao invalida!')
    #msg = 'result:' + str(result)
    print (result)
input("press Enter..")