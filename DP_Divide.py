import time

#Caso de prueba 1
# S = [(60, 10), (100, 20), (120, 30)] 
# W = 50

#Caso de prueba 2

# S = [(20, 5), (40, 10), (100, 20), (95, 25)]
# W = 30

#Caso de prueba 3

# S = [(50, 5), (40, 4), (60, 6), (90, 10), (30, 3), (120, 15)]
# W = 20

#caso de prueba 4

S = [(20, 2), (30, 3), (66, 6), (40, 4), (60, 5), (70, 7), (100, 10),  (120, 12), (130, 13), (50, 6), (40, 4), (30, 4)]
W = 35


#Solución por recursión
start_recursion = time.time()

def knapsack(S,W):
    
    n = len(S)
    S2 = list(S[:-1])
    
    if n == 0 or  S[-1][1] > W: #Si el tamaño de la lista es 0 o el peso es 0 entonces regresa un 0 
        return 0
    
    else:
        return max(knapsack(S2, W), S[-1][0] + knapsack(S2, W-S[-1][1])) #Regresa el maximo comparando un caso donde no incluyes el ultimo elemento y un caso donde si 
    
      
    
#Solución con programación dinámica
#llamada 1
    """
    [(95,55), (4,10)]
    maximo valor de knapsack([(95,55)], 64) ooo 4 + knapsack([(95,55)], 54)
    
    """
#Llamada 2 (primera opcion)

    """
    maximo valor de knapsack([], 64) ooo 95  + knapsack([], 9)
                Llamada3: Regresa 0       Lamada 4: Regresa 95
    
    """
#Llamada 5: 
    """
    maximo valor de (95) ooo 4 + knapsack([95,55], 54)
                                    Regresa 4
    
    entonces el max(95, 4) = 95
    
    """
    
print("Solucion divide y venceras ", knapsack(S, W))

end_recursion = time.time()

print("Tiempo de ejecucion: " , end_recursion - start_recursion , " segundos")


start_DP = time.time()

def knapsack_dp(S, W):
    
    n = len(S)
    V = [[0]*(W + 1) for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if(S[i-1][1] > j):
                V[i][j] = V[i-1][j] #i representa las filas y j las columnas, por lo que si el peso del elemento i-1 es mayor a la capacidad de ese momento (j) entonces su valor toma al que tiene arriba (i-1)
            else:
                V[i][j] = max(V[i-1][j], S[i-1][0] + V[i-1][j - S[i-1][1]])
        
    return V[n][W]

    """
    
    Codigo ejemplififcaod:
    
    siendo S = [(20,2), (10,1)] (valor, peso)
    y pmax = 2 
    
    V[filas] = 0 * 2 + 1 = [0,0,0]
    v[columnas] = 0 * numero de elementos en S + 1 = 0 * 3
    
    V = [
        [0,0,0]
        [0,0,0]
        [0,0,0]
    ]
    
    por cada columna
        por cada fila
            si (S[i] > j): #si el peso del actual objeto es mayor a la capacidad actual (j) entonces el valor actual se convierte en el valor que tiene arriba
                V[i][j] = V[i-1][j]
            lo demas:
                V[i][j] = max(V[i-1][j], S[i][0] + V[i-1][j-S[i][1]] ) #La posicion actual se covierte en el maximo de incluir el objeto y no hacerlo
    
    rergresa V[n][pmax]
    
    ejemplo (debug):
    
    W = peso del objeto actual
    Valor = valor del objeto actual
    
             0,1,2 = j
           0 [0,0,0]     
        -> 1 [0,0,0] primer objeto = (20,2) -> 2 > 0? si, entonces la posicion V[1][1] = V[0][1] osea 0, asi será hasta llegar a j = 2 en donde W = 2 > jactual = 2? no,entonces calcula el maximo entre no inlcuirlo (V[i-1][j] = V[0][2] = 0) o valor = 20 + V[i-1][j - W = 2] = 2 + 0
           2 [0,0,0]
           
           0 [0,0,0]
           1 [0,0,20]
        -> 2 [0,0,0]  en j = 1 calcula el maximo entre no incluirlo o sea la posicion de arriba (V[i-1][j]) = 0 o incluirlo valor = 10 + la posicion de arriba en i menos su peso en j = V[i-1][j - peso actual] = 10 + 0
           
           
        0 [0,0,0]
        1 [0,0,20]
     -> 2 [0,10,0] en j = 2 calcula el maximo entre no incluirlo o sea la posicion de arriba (V[i-1][j]) = 20  o incluirlo valor = 10 + la posicion de arriba en i menos su peso en j = V[i-1][j - peso actual] = 10 + 0
     
     0  [0,0,0]
     1  [0,0,20]
     2  [0,10,20]
     
     Regresa V[n][W] = 20
    
    
    
    1
    """


#S = [(valor, peso)]


print("Solucion con programación dinamica" , knapsack_dp(S, W))

end_DP = time.time()


print("Tiempo de ejecucion: " , end_DP - start_DP , " segundos")


