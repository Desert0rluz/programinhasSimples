#definindo entradas
valorImovel = float(input("digite o valor do imovel R$: "))
rendaCliente = float(input("digite a renda mensal R$: "))
previsaoFinanciamento = int(input("Estimativa de duração do financiamento (em anos): "))

#calculos internos do programa
prestacao = valorImovel / (previsaoFinanciamento * 12)
minimo = rendaCliente * 30 / 100

#resultados 
print("Para pagar uma casa de R${:.2f} em {} anos" .format(valorImovel, previsaoFinanciamento), end="")
print(" a prestação será de R${:.2f}".format(prestacao))
#condição para aprovação
if prestacao <= minimo:
    print("Financiamento APROVADO")
else:
    print("Financiamento RECUSADO")
