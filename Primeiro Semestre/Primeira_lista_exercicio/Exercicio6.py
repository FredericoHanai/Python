salario = float(input("Digite seu salario --> "))
reajuste = float(input("Digite o percentual de reajuste -->" ))
porcent = salario * reajuste // 100
newsal = salario + porcent
print(f"O reajuste é de {reajuste}% e seu novo salario será de {newsal}")