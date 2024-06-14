from algo1 import*
from linkedlist import*


def fibonacci_dinamico(n):
    T = Array(n,0)
    T[0] = 0
    T[1] = 1
    for i in range(2,n):
        T[i] = T[i-1] + T[i-2]
    print(T)
    return

#ejercicio 1
def darCambio(cambio,monedas):
    dp = [float('inf')] * (cambio + 1) #inicializo la lista
    dp[0] = 0 #cambio de cero

    for moneda in monedas:
        for i in range(moneda, cambio + 1):
            dp[i] = min(dp[i],dp[i - moneda] + 1)
    return dp[cambio]