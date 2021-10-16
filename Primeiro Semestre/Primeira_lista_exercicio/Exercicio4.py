print("Conversao de dias, minutos e segundos para SEGUNDOS!")
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total = dias*24*60*60 + horas*60*60 + minutos * 60  + segundos

print(f"{dias}dias(s),{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s) convertido em segundos é {total}")