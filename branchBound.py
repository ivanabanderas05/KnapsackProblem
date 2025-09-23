import time 
from queue import PriorityQueue

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


class Node:
    def __init__(self, Vacc, Wacc, Vpos, index, included = None):
        self.Vacc = Vacc
        self.Wacc = Wacc
        self.Vpos = Vpos
        self.index = index
        self.included = included

    def __lt__(self, other):
        return self.Vpos > other.Vpos


def branchBound(S, W, included = None):
    n = len(S) #este representara cuantos objetos hay en la lista de objetos

    if included is None:
        included = n*[False]   #si la lista no contiene algo, se iniciaran todos sus valores en falso

    best = Node(0, 0, 0, -1, included)
    frontier = PriorityQueue()
  
    frontier.put(best)

    while not frontier.empty():
        node = frontier.get()

        if node.Vacc > best.Vacc and node.Wacc <= W:
            best = node 

        if node.Vpos >= best.Vacc:
            index = node.index + 1

            if index < n:
                copyVpos = calculateVpos(S, W, node.Vacc, node.Wacc, index)
                copyIncluded = node.included.copy()
                if node.Wacc <= W:
                    frontier.put(Node(node.Vacc, node.Wacc, copyVpos, index, included))

                if node.Wacc + S[index][1] <= W:
                    copyVpos1 = calculateVpos(S, W, node.Vacc + S[index][0], node.Wacc + S[index][1], index)
                    copyIncluded[index] = True

                    new_node = Node(node.Vacc + S[index][0], node.Wacc + S[index][1], copyVpos1, index, copyIncluded)
                    frontier.put((new_node))   
                
    selected = best.included


    return best, selected
                        

objcts = [(20, 2), (30, 3), (66, 6), (40, 4), (60, 5), (70, 7), (100, 10),  (120, 12), (130, 13), (50, 6), (40, 4), (30, 4)]
W = 35	
S = [(v, w, v/w) for v, w in objcts]


inicio = time.time()
resultado, elementos = branchBound(S, W)
fin = time.time()

print("Mejor valor:", resultado.Vacc)
print("Lista original:", S)
print("Objetos seleccionados:", elementos)
print("Tiempo de ejecución:", fin - inicio, "segundos")


