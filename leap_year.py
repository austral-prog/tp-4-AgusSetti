def leap_year():
    print("TO DO")
    año= int(input("Ingrese un año: "))
    if (año%4==0) or (año%400==0):
        print("El año"+ " " + str(año)+ " " + "es bisiesto")
    else:
        print("El año"+ " " + str(año) + " " + "no es bisiesto")
