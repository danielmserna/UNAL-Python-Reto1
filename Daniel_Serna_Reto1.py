def main(entrada):
  if(entrada >= 0):
    notaPedro = (entrada*2) + 4
    notaCamila = (notaPedro + entrada)//5
    print(str(entrada))
    print(str(notaPedro))
    print(str(notaCamila))
    if notaCamila <= 20 and notaCamila >= 0:
      print("uno")
    elif notaCamila <= 30 and notaCamila >= 21:
      print("dos")
    elif notaCamila <= 50 and notaCamila >= 31:
      print("tres")
    else:
      print("cuatro")
  else:
    nuevaEntrada = int(input("Ingrese una calificación válida obtenida por Juan "))
    main(nuevaEntrada)

main(int(input("Ingrese la calificación obtenida por Juan ")))