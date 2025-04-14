def leap_year():
    año = int(input("Ingrese un año: "))
    if (año%4 == 0) and (año%100 != 0):
        print(f"El año {año} es biciesto")
    elif año%400 == 0: 
        print(f"El año {año} es biciesto")
    else:
        print(f"El año {año} no es biciesto")
