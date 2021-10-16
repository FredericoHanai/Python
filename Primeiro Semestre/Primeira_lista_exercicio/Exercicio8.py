percorrido = int(input("Digite a KM percorrida pelo carro: "))
dias = int(input("Quantos dias ficou alugado? "))
pagamento = 60 * dias
pagamento01 = 0.15*percorrido
pagamento02 = pagamento + pagamento01
print(f"Vc pagará {pagamento02:.2f}")