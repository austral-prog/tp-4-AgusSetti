def line():
    import math
    coef_a = float(input("Ingrese el coeficiente A: "))
    coef_b = float(input("Ingrese el coeficiente B: "))
    coef_x1 = float(input("Ingrese el coeficiente X1: "))
    coef_x2 = float(input("Ingrese el coeficiente X2: "))
    print("El coeficiente A de su ecuación de la recta es:", coef_a)
    print("El coeficiente B de su ecuación de la recta es:", coef_b)
    print("El coeficiente X1 de su ecuación de la recta es:", coef_x1)
    print("El coeficiente X2 de su ecuación de la recta es:", coef_x2)
    print ("\n" "Para la siguiente ecuación:" "\n" + "\t" + "Y =" + " " + str(coef_a) + "X + " + str(coef_b))
    y1 = (coef_a * coef_x1 + coef_b)
    y2 = (coef_a * coef_x2 + coef_b)
    print("\n" "Dados los siguientes puntos:" "\n" + "\t" + "P1 (" + str(coef_x1) + ", " + str(y1) + ")" "\n" + "\t" + "P2 (" + str(coef_x2) + ", " + str(y2) + ")")
    P1=(coef_x1, y1)
    P2=(coef_x2, y2)
    distancia= math.dist(P1, P2)
    print("\n" "La distancia entre ellos es: " + str(distancia))

