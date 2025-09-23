import time

def calculateVpos(S, W, Vacc, Wacc, index = -1):
    n = len(S) #cantidad de objetos en la lista
    k = index + 1
    Vpos = Vacc
    W_tmp = Wacc

    while k < n and W_tmp + S[k][1] <= W:
        Vpos += S[k][0]
        W_tmp += S[k][1]  
        k += 1
    if k < n:
        Vpos += (W - W_tmp)*S[k][2]
    
    return Vpos


def bactrackingBound(S, W, Vacc, Wacc, Vpos, best = None, index = -1, included = None):
    #s: lista de objetos
    #W: el peso maximo que esta permitido
    #Vacc: valor acumulado del nodo
    #Wacc:  peso acumulado
    n = len(S) #para determinar la cantidad de objetos 

    if included == None:
        included = n*[False]   #si la lista no contiene algo, se iniciaran todos sus valores en falso

    if best == None:
        best = {'Value': 0, 'Objects': included} #se crea un diccionario

    if Vacc > best['Value'] and Wacc <= W:
        best['Value'] = Vacc
        best['Objects'] = included.copy() #copy para no modificar la lista original

    if index == -1:
        Vpos = calculateVpos(S, W, 0, 0, index)

    index += 1
    
    if index >= 0 and index < n and Wacc <= W and Vpos > best['Value']:
        #primera opcion en la cual se incluye el objeto
        copyIncluded = included.copy()
        copyIncluded[index] = True     

        best = bactrackingBound(S, W, Vacc + S[index][0], Wacc + S[index][1], Vpos, best, index, copyIncluded)  #se le suma al valor y al peso

        copy_Vpos = calculateVpos(S, W,Vacc, Wacc, index)
        best = bactrackingBound(S, W, Vacc, Wacc, copy_Vpos, best, index, included) #el valor y peso permanecen igual

    return best

#objcts = [(60, 10), (100, 20), (120, 30)]
objcts = [(20, 2), (30, 3), (66, 6), (40, 4), (60, 5), (70, 7), (100, 10),  (120, 12), (130, 13), (50, 6), (40, 4), (30, 4)]
W = 35	
S = [(v, w, v/w) for v, w in objcts]
#W = 50

inicio = time.time()   #empieza el cronometro
resultado = bactrackingBound(S, W, 0, 0, 0)
fin = time.time()   #detiene el cronometro

print("Mejor valor: ", resultado['Value'])
print("Lista original: ", S)
print("Objetos seleccionados: ", resultado['Objects'])
print("Tiempo de ejecución: ", fin - inicio, "segundos")
