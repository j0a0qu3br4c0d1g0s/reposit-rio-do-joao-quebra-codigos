minutos = int(input("Digite quantos minutos serão utilizados: "))
if minutos < 200:
    preco_por_pulso = 0.20
elif 200 <= minutos <= 400:
    preco_por_pulso = 0.18
else:
    preco_por_pulso = 0.15

total_pulsos = minutos * 60 // 6
preco_total = total_pulsos * preco_por_pulso

print("Preço total da conta: ", preco_total)