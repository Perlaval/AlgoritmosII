from algo1 import*
from linkedlist import*
from tadSet import*

#-------------------------------------------------------------------------------------------------
#EJERCICIO1  
#Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas
#donde por cada par de elementos representa una conexión entre dos vértices
                #vertices,aristas
def createGraph(listV,listA):
  graph = Array(length(listV),LinkedList())
  #guardo en los valores de los vertices en cada una de las celdas de graph
  current = listV.head
  i = 0
  while current != None: #el primer elemento de cada la lista es el vertice de la fila
    graph[i] = LinkedList()
    add(graph[i],current.value)
    current = current.nextNode
    i += 1
  
  current = listA.head
  while current != None:
    #guardo en la lista de vertices de cada celda de graph el vertice de la arista
    #search me devuelve la posicion del vertice en la lista de vertices
    add(graph[search(listV,current.value[0])],current.value[1])
    add(graph[search(listV,current.value[1])],current.value[0])
    current = current.nextNode
  return graph

#-----------------------------------------------------------------------------------------------
#EJERCICIO2
#Implementa la operación existe camino que busca si existe un camino entre dos vertices
#retorna True si existe camino entre v1 y v2, False en caso contrario

def existPath(grafo,v1,v2):
  if len(grafo) == 1: #caso 1: n = 1
    return True
  else: #caso 2
    #buscar la posicion de v1 en el arreglo (columna 0)
    pos = posicionElementoEnArray(grafo,v1) 
    if search(grafo[pos],v2): #si v2 esta en la linkedlist de v1
      return True
    else:
      L = list()
      L.append(v1) #hago una lista aux para guardar los vertices que ya he visitado
      return existPathR(grafo,grafo[pos],grafo[pos].head.nextNode,grafo[pos].head.nextNode,L,v2)
                            #lista de v1, nodo 1 de la lista de v1

def existPathR(grafo,list,current,node,L,v2):
  if node == None:#termino de recorrer list y no encontro v2
    if current.nextNode != None:
      current = current.nextNode #pasa al siguiente nodo de la lista de v1
      pos = posicionElementoEnArray(grafo,current.value)
      return existPathR(grafo,grafo[pos],current,grafo[pos].head.nextNode,L,v2)
    else:
      return False
  else:
    if search(list,v2): 
      return True
    else:
      if node.value in L: #si el vertice ya fue visitado
        return existPathR(grafo,list,current,node.nextNode,L,v2) #paso al siguiente vertice de list
      else: #si no fue visitado
        L.append(node.value) #lo agrego a la lista aux
        pos = posicionElementoEnArray(grafo,node.value) #busco la pos de la lista del v actual
        nodeListaNueva = grafo[pos].head.nextNode #tomo el primer vertice de la lista de v actual
        if nodeListaNueva != None:
          if nodeListaNueva.value not in L: #si no lo he visitado, voy a la list de v
            return existPathR(grafo,grafo[pos],current,nodeListaNueva,L,v2)
          else: 
            if nodeListaNueva.nextNode == None: #si ya no hya mas vertices por verficar en esa lista vuelvo a la lista anterior que es la lista del vertice L[-2] 
              pos = posicionElementoEnArray(grafo,L[-2])
              return existPathR(grafo,grafo[pos],current,grafo[pos].head.nextNode,L,v2)
            else: #si hay mas vertices por verificar paso al siguiente
              return existPathR(grafo,grafo[pos],current,nodeListaNueva.nextNode,L,v2)
        
     
      
def posicionElementoEnArray(arreglo,elemento):
  i = 0
  while i < len(arreglo):
    if arreglo[i].head.value == elemento:
      return i 
    i += 1

#--------------------------------------------------------------------------------------------------
#EJERCICIO3
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario

def isconnected(grafo):
  if len(grafo) == 1:
    return False
  else:
    for i in range(0,len(grafo)):
      for j in range(i+1,len(grafo)):
        if not existPath(grafo,grafo[i].head.value,grafo[j].head.value):
          return False
    return True

#--------------------------------------------------------------------------------------------------
#EJERCICIO4
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: retorna True si el grafo es un árbol.

def isTree(grafo):
  if isconnected(grafo):
    return not contieneCiclos(grafo)
  return False

def contieneCiclos(grafo): #esta funcion no sirve para grafos no conexos
  #si tiene n-1 aristas entonces no tiene ciclos
  if len(grafo) == 1:
    return True
  else:
    return contieneCiclosR(grafo,grafo[0],grafo[0].head,0,0,[])

def contieneCiclosR(grafo,lista,node,cantAristas,cont,L): #cont = contador
  if len(L) == len(grafo):
    return cantAristas >= len(grafo)
  else:
    if node != None:
      if node.value in L:
        return contieneCiclosR(grafo,lista,node.nextNode,cantAristas,cont,L)
      else:
        if node == lista.head:
          L.append(node.value) #guardo solo los valores de la lista de vert principal
          return contieneCiclosR(grafo,lista,node.nextNode,cantAristas,cont,L)
        else:
          return contieneCiclosR(grafo,lista,node.nextNode,cantAristas+1,cont,L) 
    else:
      if cont <= len(grafo)-1:
        return contieneCiclosR(grafo,grafo[cont+1],grafo[cont+1].head,cantAristas,cont+1,L)

#--------------------------------------------------------------------------------------------------
#EJERCICIO 5  
#Salida: retorna True si el grafo es completo.
#Tener en cuenta que  un grafo es completo cuando existe una arista entre todo par de vértice

def isComplete(grafo):
  if len(grafo) == 1: #si tiene un solo nodo no es completo
    return False
  else:
    cantVertices = len(grafo)
    i = 0
    while i < len(grafo):
      if length(grafo[i]) != cantVertices:
        return False
      i += 1
    return True

#--------------------------------------------------------------------------------------------------#EJERCICIO 6
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.

#si no es conexo convertirlo en conexo
#si el grafo resultante tiene ciclos, eliminarlos


#--------------------------------------------------------------------------------------------------
#EJERCICIO 7
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: retorna el número de componentes conexas que componen el grafo.

def countConnections(grafo):
  if isconnected(grafo):
    return 1
  else:
    return countConnectionsR(grafo,0,1,0)

def countConnectionsR(grafo,val,i,cantConnections):
  if i == len(grafo):
    if cantConnections >= 1:
      return cantConnections+1
    return cantConnections
  else:
    #si hay camino entre 1y2 y un camino entre 1y3 entonces hay conexion entre 1,2y3
    if existPath(grafo,grafo[val].head.value,grafo[i].head.value): 
      return countConnectionsR(grafo,val,i+1,cantConnections)
    else:
      return countConnectionsR(grafo,i,i+1,cantConnections+1)

#--------------------------------------------------------------------------------------------------
#EJERCICIO 8
#Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
#Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz

def convertToBFSTree(grafo,v):
  if isconnected(grafo):
    asignarValoresVertice(grafo)
    pos = posicionElementoEnArray(grafo,v)
    current = grafo[pos].head
    L = list()
    L.append(current.value)
    return convertToBFSTreeR(grafo,L)

def convertToBFSTreeR(grafo,L):
  if L == []:
    return grafo
  else:
    pos = posicionElementoEnArray(grafo,L[0]) #pos de la lista del vertice
    vertice = grafo[pos].head
    node = vertice.nextNode
    while node != None:
      posAux = posicionElementoEnArray(grafo,node.value) #la uso para actualizar/verificar el color del vertice
      if grafo[posAux].head.color == "B":
        #node.color = "G"
        #node.distance = vertice.distance + 1
        #node.parent = vertice
        L.append(node.value)
        grafo[posAux].head.color = "G"
        grafo[posAux].head.distance = vertice.distance + 1
        grafo[posAux].head.parent = vertice
      else:
        if grafo[posAux].head.color == "G":
          delete(grafo[pos],node.value)
          delete(grafo[posAux],vertice.value)
      node = node.nextNode
    del L[0]
    grafo[pos].head.color = "N"
    return convertToBFSTreeR(grafo,L)

def asignarValoresVertice(grafo): #asigna valores adicionales a los nodos para el bfs
  for i in range(0,len(grafo)):
    current = grafo[i].head
    while current != None:
      current.color = "B"
      current.distance = 0
      current.parent = grafo[i].head
      current = current.nextNode

#--------------------------------------------------------------------------------------------------
#EJERCICIO 9
#Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
#Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz
#arcos arbol: pertenecen al bfs
#arcos retroceso, te llevan a un vertice gris
#arcos de avance, te llevan a un vertice negro, entre vertices del mismo arbol que no sea un ancestro

def convertToDFSTree(grafo,v):
  L = []
  for i in range(0,len(grafo)):
    grafo[i].head.color = "B"
    grafo[i].head.d = 0
    grafo[i].head.f = 0
    grafo[i].head.parent = None
    L.append(grafo[i].head.value)
  
  time = 0  
  pos = posicionElementoEnArray(grafo,v)
  if pos == None:
    return "el vertice no se encuentra en el grafo"
  else:
    if pos != 0:
      cont = 0
      while cont != pos:
        L.append(cont)
        cont += 1
    while pos <= len(grafo):
      if grafo[pos].head.color == "B":
        return dfsVisit(grafo,grafo[pos].head,time,L)
      pos += 1
      if pos == len(grafo)-1 and L != []:
        pos = L[0]
        L.pop(0)
        return dfsVisit(grafo,grafo[pos].head,time,L)
        
  

def dfsVisit(grafo,vertice,time,L):
  if vertice == None:
    return grafo
  else:
    time += 1
    pos = posicionElementoEnArray(grafo,vertice.value)
    current = grafo[pos].head
    
    current.d = time 
    current.color = "G"
    L.remove(vertice.value)
    current = current.nextNode
    while current:
      posAux = posicionElementoEnArray(grafo,current.value)
      if grafo[posAux].head.color == "B":
        grafo[posAux].head.parent = vertice
        dfsVisit(grafo,grafo[posAux].head,time,L)
      else:
        if grafo[posAux].head.color == "N":
          delete(grafo[pos],current.value)
          delete(grafo[posAux],vertice.value)
      current = current.nextNode
    grafo[pos].head.color = "N"
    time += 1
    grafo[pos].head.f = time
    return grafo
    

#-----------------------------------------------------------------------------------------------------EJERCICIO 10
#Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
#Salida: la lista de vértices que representan el camino más corto entre v1 y v2. 
#La lista resultante contiene al inicio a v1 y al final a v2. En caso que no exista camino se retorna la lista vacía.
    
#el BFS TREE permite encontrar el camino mas corto en terminos de cant de aristas 

def bestRoad(grafo,v1,v2):
  if not existPath(grafo,v1,v2):
    return []
  else:
    L = list()
    bfsTree = convertToBFSTree(grafo,v1)
    pos1 = posicionElementoEnArray(grafo,v1)
    pos2 = posicionElementoEnArray(grafo,v2)
    return bestRoadR(bfsTree,bfsTree[pos1].head.value,bfsTree[pos2].head,[])

def bestRoadR(grafo,v1,node,L):
  if node.value == v1:
    L.append(node.value)
    L.reverse()
    return L
  else:
    L.append(node.value)
    node = node.parent
    return bestRoadR(grafo,v1,node,L)


#-----------------------------------------------------------------------------------------------------EJERCICIO 14
#Entrada: Grafo con la representación de Matriz de Adyacencia.
#Salida: retorna el árbol abarcador de costo mínimo
#grafo = array(3,array(4,0)) 3 = filas; 4 = columnas

def PRIM(grafo): 
  listaAuxiliar = [] #lista auxiliar para guardar los vertices y acceder a ellos mas facil
  v1,v2 = aristaInicial(grafo) 
  listaAristas = primR(grafo,{},listaAuxiliar,v1,v2)
  
  for i in range(0,len(grafo)):
   for j in range(0,len(grafo)):
    grafo[i][j] = listaAristas.get((i,j),0)
  return grafo

def primR(grafo,listaAristas,listaAux,v1,v2):
  if len(listaAux) == len(grafo):
    return listaAristas
  else:
    listaAristas[(v1,v2)] = grafo[v1][v2] 
    listaAristas[(v2,v1)] = grafo[v1][v2] 
    grafo[v1][v2] = 0
    grafo[v2][v1] = 0
    
    if v1 not in listaAux:
      listaAux.append(v1)
    if v2 not in listaAux:
      listaAux.append(v2)
     
    min = float('inf')
        
    for vertice in listaAux:
      min,v1,v2 = aristaMinima(grafo,vertice,v1,v2,min,listaAux)

    return primR(grafo,listaAristas,listaAux,v1,v2)

def aristaInicial(g):
  min = float('inf')
  v1 = 0
  v2 = 0
  for i in range(0,len(g)):
    for j in range(0,len(g)):
      if g[i][j] > 0 and g[i][j] < min:
        min = g[i][j]
        v1 = i
        v2 = j
  return v1,v2

def aristaMinima(g,vertice,v1,v2,min,listaAux):
  
  for j in range(0,len(g)):
    if g[vertice][j] > 0 and g[vertice][j] <= min and j not in listaAux:
      min = g[vertice][j]
      v1 = vertice
      v2 = j
     
  return min,v1,v2

#-------------------------------------------------------------------------------------------------
#EJERCICIO 15
#Entrada: Grafo con la representación de Matriz de Adyacencia.
#Salida: retorna el árbol abarcador de costo mínimo

def KRUSKAL(grafo):
    
  # Inicializar conjuntos disjuntos para cada vértice
  sets = {i: {i} for i in range(len(grafo))}

  # Lista de todas las aristas (v1, v2) con sus pesos
  aristas = []
  for i in range(len(grafo)):
    for j in range(i + 1, len(grafo)):  # j empieza en i+1 para evitar duplicados
        if grafo[i][j] != 0:
            aristas.append((grafo[i][j], i, j))  # Añadir arista con peso
  
  # Ordenar aristas por peso
  aristas.sort()
  
  # Inicializar lista de aristas del árbol de expansión mínima
  mst_aristas = []

  def find_set(sets, vertex):
      for s in sets.values():
        if vertex in s:
            return s
      return None

  for peso, v1, v2 in aristas:
      set_v1 = find_set(sets, v1)
      print(set_v1)
      set_v2 = find_set(sets, v2)
      print(set_v2)
      if set_v1 != set_v2:
          # Añadir arista al árbol de expansión mínima
          mst_aristas.append((v1, v2, peso))
          # Unir los conjuntos de v1 y v2
          sets[v1].update(sets[v2])
          for v in sets[v2]:
            sets[v] = sets[v1]
              
  # Mostrar el resultado
  print(f"Aristas del MST: {mst_aristas}")
  print(f"Conjuntos finales: {sets}")

  return mst_aristas

      


    
 

  
      
  
      
      
    
      
      
    
  
  
    
  
    
    
    
  
    

  
    
        
      
  
      
    
  
    
    
    
    


      


    
 
    
  
  
  
          
 
    
  
    
    

    
      
        
        

    
        
      

      
  
  
  
    
    
    
  


  
 



      
      
      
      
    


      
    
    
    
      
   
    
    
    
      
     
        
        

    
  