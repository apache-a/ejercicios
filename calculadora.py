respuesta = None

print ("Calculadora personal de Python.\n")
respuesta = input(" 1- Suma.\n 2- Resta.\n 3- Multiplicacion.\n 4- Division.\n 5- Modulo.\n 6- Exponente.\n Elige que operacion que quieres hacer:")

if respuesta == "1":
    print ("Suma")
elif respuesta == "2":
    print ("Resta")
elif respuesta == "3":
    print ("Multiplicacion")
elif respuesta =="4":
    print ("Division")
elif respuesta == "5":
    print ("Modulo")
elif respuesta == "6":
    print ("Exponente")
else:
    print(" Error")

primer =float(input ("introduce el primer valor para la operacion: "))
segundo =float(input ("Introduce el segundo valor para la operacion: "))

if respuesta =="1":
    print (primer + segundo)
elif respuesta =="2":
    print (primer - segundo)
elif respuesta =="3":
    print (primer * segundo)
elif respuesta == "4":
    print (primer / segundo)
elif respuesta == "5":
    print (primer % segundo)
elif respuesta == "6":
    print (primer ** segundo)
    
"""
 
if respuesta =="1":
    total = round(primer + segundo, 2)
    print (f"El resultado de {primer} + {segundo} es :{total}.")
 
elif respuesta =="2":
    total = round(primer + segundo, 2)
    print (f"El resultado de {primer} - {segundo} es :{total}.")
 
elif respuesta =="3":
    total = round(primer + segundo, 2)
    print (f"El resultado de {primer} * {segundo} es :{total}.")
 
elif respuesta =="4":
    total = round(primer + segundo, 2)
    print (f"El resultado de {primer} / {segundo} es :{total}.")
 
elif respuesta =="5":
    total = round(primer + segundo, 2)
    print (f"El resultado de {primer} % {segundo} es :{total}.")
 
elif respuesta =="6":
    total = round(primer + segundo, 2)
    print (f"El resultado de {primer} ** {segundo} es :{total}.")

    
 """
