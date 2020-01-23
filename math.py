import math

# OPRACIONES MATEMÁTICAS BÁSICAS C/ FUNCIONES

# devolveme el factorial de un número
def returnFact(number):
    print(math.factorial(number))
# test : returnFact(25)

# devolveme x número elevado a x exponente 
def returnExp(number , exp):
    print(number ** exp)
# test : returnExp(544 , 32)

# redondeame un número para abajo
def returnFloor(number):
    print(math.floor(number))
# test : returnFloor(35.999)

# devolveme la raíz cuadrada de un número
def returnSqrt(number):
    print(math.sqrt(number))
# test : returnSqrt(64)

# devolveme el logaritmo natural de un número
def returnNL(number):
    print(math.log(number))
# test : returnNL(55)