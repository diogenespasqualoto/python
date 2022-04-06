nome=input("digite seu nome: ")
idade=int(input("Digite sua idade:"))
if idade >= 65:
    print("o paciente: " + nome + " POSSUI atendimento prioritário!")
else:
    print("O paciente: " + nome + " NÂO possui atendimento prioritário!")