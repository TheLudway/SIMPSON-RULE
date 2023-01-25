import fractions

n = int(input("Ingrese el número de parejas ordenadas: " )) - 1 # Se ingresa la cantidad de n intervalos que se poseen
if n%2 == 1:  # Verificación ya que la regla de Simpson dice que n debe ser par
    print("El número de parejas ordenadas debe ser impar!")
    quit()

b = float(input("Último límite de integración: " ))  # Se ingresa el número del último límite de integración (eje x normalmente)
a = float(input("Primer límite de integración: " ))  # Se ingresa el númerl del primer límite de integración (eje x normalmente)
delta_x = (b-a)/n  # Se cálcula delta de x
diccionario = {}  # En este diccionario van a estar todas las parejas ordenadas
Resultado = 0  # Se asigna un resultado con una variable para poder manipular a futuro

for i in range(n+1):  # Se pide que se repita la acción de pedir datos n número de veces
    x = input("Valor x de la pareja ordenada: " ) # Se pide la coordenada x
    try:     #Verificación del x para ver si es una fracción o no
        if not x.isnumeric():
            x = fractions.Fraction(x)
    except ValueError:
        (x + "NO ES UN NÚMERO")
    doubleofx = float(x) 
    y = input("Valor y de la pareja ordenada: " ) # Se pide la coordenada y
    try:    #Verificación del y para ver si es una fracción o no
        if not y.isnumeric():
            y = fractions.Fraction(y)
    except ValueError:
        (y + "NO ES UN NÚMERO")
    doubleofy = float(y) 
    diccionario.update({doubleofx:doubleofy}) # x and y se almacenan en el diccionario

#OPERACIÓN PARA LA REGLA DEL TRAPECIO
Resultado += diccionario.get(a)
diccionario.pop(a)
contador = 1
for i in diccionario.values():
    contador += 1
    if i != diccionario.get(b):
        if contador % 2 == 0:
            Resultado += i * 4
        else:
            Resultado += i * 2
    else:
        Resultado += diccionario.get(b)
        
Resultado *= delta_x/3
print(Resultado)