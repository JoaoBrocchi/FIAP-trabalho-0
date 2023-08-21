''' relalizando a montagem do algoritimo percebi,
 que no calculo do montante podemos usar duas fomrulas :
("montante" = ("tempo fumando" x 365) x preço maço x quatos maços por dia)
 OU
 ("montante" = ("tempo fumando" x 12 * 30) x preço maço x quatos maços por dia)
    A 1a formula julgo estar mais correta,
no entanto para usar o mesmo modelo de testes da tarefa resolvi montar as duas '''



Quanto_tempo_fuma = float(input("A quanto tempo você fuma ? (em anos)"))
Quanto_custa_maço = float(input("Valor do Maço ?"))
Quanto_fuma_por_dia = float(input("Quantos maços fuma por dia ?"))

# formula 1
montante = Quanto_fuma_por_dia * Quanto_custa_maço * (Quanto_tempo_fuma * 12 * 30 )

# formula 2
montante2= Quanto_fuma_por_dia * Quanto_custa_maço * Quanto_tempo_fuma


if montante < 20000:
    print(f"Com o valor R$ {montante}, você poderia ter dado entrada em um carro.")
elif montante > 20000 and montante < 50000:
    print(f"Com o valor R$ {montante}, você poderia ter comprado um carro popular usado.")
elif montante > 50000:
    print(f"Com o valor R$ {montante}, você poderia ter comprado um carro zero.")


