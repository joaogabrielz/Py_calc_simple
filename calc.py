#while option != 1:
print('selecione')
print('1-calular')
print('2-sair')
option = int(input("opção: "))
if (option == 1):
    n1 = int(input("Digite 1* numero: "))
    n2 = int(input("Digite 1* numero: "))
    result = n1+n2
    msg = 'result:' + str(result)
    print (msg)
input("press Enter..")