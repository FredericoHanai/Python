combustivel = float(input("Digite o preço da gasolina: "))
desempenho = int(input("Digite o desempenho do carro km/l: "))
distancia = float(input("Digite a distancia entre as cidade (KM): "))
litros = distancia // desempenho
custo = litros * combustivel
print(f"A quantidade de gasolina para viajar entre as cidades é: {litros} litros")
print(f"O valor gasto em combustvel será R${custo:.2f}")