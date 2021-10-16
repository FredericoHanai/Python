num = int(input("Digite um numero de 0 a 999 "))
if num > 999:
    print("Numero invalido, favor escolher apenas de 0 a 999")
else:
    um = num // 100
    dois = num % 100 // 10
    tres = num % 10
    if um < dois and dois < tres:
        print("Esse numero é ascendente")
    else:
        print("Numero não é ascendente")
