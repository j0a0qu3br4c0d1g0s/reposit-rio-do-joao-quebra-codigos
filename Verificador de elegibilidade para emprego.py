idade = int(input("Digite a sua idade: "))
nacionalidade = str(input("Digite a sua nacionalidade: "))
experiência = int(input("Quantos anos de experiência você tem?: "))
if idade >= 18:
   print("Você tem a idade mínima para a vaga de emprego.")
else:
   print("Desculpe, você não tem a idade mínima para a vaga de emprego.")
if nacionalidade == "brasileiro" and "brasileira":
   print("Sua nacionalidade é elegível para a vaga de emprego")
else:
   print("Sua nacionalidade não é a exigida para a vaga de emprego")
if experiência >=2:
   print("Você tem a experiência mínima para a vaga de emprego")
else:
   print("Você não tem experiência mínima para a vaga de emprego")