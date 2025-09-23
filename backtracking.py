import time 

def backtracking(S, W, Vacc, Wacc, best = None, index = -1, included = None ):
    #s: lista de objetos
    #W: el peso maximo que esta permitido
    #Vacc: valor acumulado del nodo
    #Wacc:  peso acumulado

    n = len(S) #este representara cuantos objetos hay en la lista de objetos
    
    if included == None:
        included = n*[False]   #si la lista no contiene algo, se iniciaran todos sus valores en falso

    if best == None:
        best= {'Value':0, 'Objects' : included}   #se crea un diccionario

        
    if Vacc > best['Value'] and Wacc <= W:
        best['Value'] = Vacc
        best['Objects'] = included.copy() #copy para no modificar la lista original

    index += 1

    if index >= 0 and index < n and Wacc <= W:
        #primera opcion en la cual se incluye el objeto
        copyIncluded = included.copy()
        copyIncluded[index] = True   #marcamos que este objeto si se agrega a la mochila
        best = backtracking(S, W, Vacc + S[index][0],Wacc + S[index][1], best, index, copyIncluded)  #se le suma al valor y al peso

        #Seguna opcion en el cual no se incluye el objeto
        best = backtracking(S, W, Vacc, Wacc, best, index, included)  #el valor y peso permanecen igual

    return best

S = [(67, 10), (148, 20), (193, 30)]   # (valor, peso)
W = 40  # peso máximo

inicio = time.time()   #empieza el cronometro
resultado = backtracking(S, W, 0, 0)
fin = time.time()   #detiene el cronometro

print("Mejor valor: ", resultado['Value'])
print("Lista original: ", S)
print("Objetos seleccionados: ", resultado['Objects'])
print("Tiempo de ejecución: ", fin - inicio, "segundos")