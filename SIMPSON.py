import fractions

n = int(input("Ingrese el número de parejas ordenadas: " )) - 1 # n-couples
if n % 2 == 1:  # n must be even, so this try a validation if n it's even
    print("El número de parejas ordenadas debe ser impar!")
    quit()

b = float(input("Último límite de integración: " ))  # Last integration limit
a = float(input("Primer límite de integración: " ))  # First integration limit
delta_x = (b-a)/n  # Get delta x
diccionario = {}  # All couples get inside this dictionary
Resultado = 0  # Future variable

for i in range(n+1):  
"""get all the couples"""
    x = input("Valor x de la pareja ordenada: " ) # x axis
    try:     # See if x is a fraction
        if not x.isnumeric():
            x = fractions.Fraction(x)
    except ValueError:
        (x + "NO ES UN NÚMERO")
    doubleofx = float(x) 
    y = input("Valor y de la pareja ordenada: " ) # y axis
    try:    # See if y is a fraction
        if not y.isnumeric():
            y = fractions.Fraction(y)
    except ValueError:
        (y + "NO ES UN NÚMERO")
    doubleofy = float(y) 
    diccionario.update({doubleofx:doubleofy}) # Dictionary get updated by x and y axis

# Se a variable that follow with each iteration, if variable is even, the i that got a value of the dicionary in each iteration get multiply by 4
# Otherwise the variable i get multiply by 2
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
"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
"""
