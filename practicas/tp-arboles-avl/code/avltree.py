

from algo1 import*
from linkedlist import*
from myqueue import*

class AVLTree:
  root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None

def newAVLNode(key,value):
  newNode = AVLNode()
  newNode.value = value
  newNode.key = key
  return newNode

#----------------------------------------------------------------------
#Busca un elemento en el TAD arbol binario
#Devuelve la key asociada a la primera instancia del elemento. Devuelve None si el elemento no se encuentra.
def search(B,element):
  if B.root == None:
    return None
  else:
    #print(search(B.root,element))  DUDA: NO ME IMPRIME EL currentNode.key
    return searchR(B.root,element)
    
#-----------

def searchR(currentNode,element):
    if currentNode != None:
      if currentNode.value == element:
        return currentNode.key
      else:
        if currentNode.value > element:
         return searchR(currentNode.leftnode,element)
        else:
          if currentNode.value < element:
           return searchR(currentNode.rightnode,element)
    else:
      return None

def searchRkey(currentNode,key):
  if currentNode != None:
    if currentNode.key == key:
      return currentNode
    else:
      if currentNode.key > key:
        return searchRkey(currentNode.leftnode,key)
      else:
        if currentNode.key < key:
         return searchRkey(currentNode.rightnode,key)
  else:
    return None
      
#---------------------------------------------------------------------
#Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None.  
def insert(B,element,key):
  newNode = newAVLNode(key,element)
  currentNode = B.root

  if currentNode == None: #arbol vacio
    B.root = newNode
    return newNode.key
  else: #arbol NO vacío 
    if newNode.key > currentNode.key:
      if currentNode.rightnode == None:
        currentNode.rightnode = newNode
        newNode.parent = currentNode
        
        return newNode.key
      else:
        currentNode = currentNode.rightnode
        return insertR(currentNode,newNode)
    else:
      if newNode.key < currentNode.key:
        if currentNode.leftnode == None:
          currentNode.leftnode = newNode
          newNode.parent = currentNode
          return newNode.key
        else:
          currentNode = currentNode.leftnode
          return insertR(currentNode,newNode)
      else:
        #la key ya se encuentra en el arbol
       return None
#_______
#funcion insert recursiva
def insertR(currentNode, newNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      currentNode.rightnode = newNode
      newNode.parent = currentNode
      return newNode.key
    else: 
      insertR(currentNode.rightnode,newNode)
  else:
    if newNode.key < currentNode.key:
      if currentNode.leftnode == None:
        currentNode.leftnode = newNode
        newNode.parent = currentNode
        return newNode.key
      else:
        insertR(currentNode.leftnode,newNode)

#----------------------------------------------------------------------
#Devuelve clave (key) del elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
def delete(B,element):
  #currentNode = B.root
  #nodo a eliminar
  node = searchRE(B.root,element)
  if node == None:
    print(element)
    return None
  else:
    
    #VERIFICA SI EL NODO A ELIMINAR TIENE HIJOS
    #SI TIENE HIJOS ENTONCES BUSCA EL NODO SUSTITUTO --->
    
    #1. EL NODO A ELIMINAR NO TIENE HIJOS (por lo tanto no hay nodo sustituto)
    if node.rightnode == None and node.leftnode == None:
      if node.parent.leftnode == node:
        node.parent.leftnode = None
      else:
        node.parent.rightnode = None
      return node.key
    else:
      #2. EL NODO A ELIMINAR TIENE HIJOS:
      #1.tiene un hijo del lado izquierdo
      if node.rightnode == None:
        newNode = nodoSustitutoI(node.leftnode)
      else:
        #2.tiene un hijo del lado derecho o dos hijos 
        newNode = nodoSustitutoD(node.rightnode)

      #ACTUALIZA LOS VALORES DEL NODO QUE HAY QUE ELIMINAR
      if node == B.root:
        B.root.value = newNode.value
        B.root.key = newNode.key
      else:
        node.value = newNode.value
        node.key = newNode.key
        
      #ELIMINA EL NODO SUSTITUTODEPENDIENDO DE LA CANT DE HIJOS QUE TENGA
      #el nodo sust esta del lado izquierdo del padre
      if newNode.parent.leftnode == newNode:
        if newNode.rightnode == None:
          #si tiene cero hijos
          newNode.parent.leftnode = None
        else:
          #si tiene un hijo
          newNode.parent.leftnode = newNode.rightnode
        return node.key
      #el nodo sustituto esta del lado derecho del padre
      else:
        if newNode.rightnode == None:
          #si tiene cero hijos
          newNode.parent.rightnode = None
        else:
          #si tiene un hijo
          newNode.parent.rightnode = newNode.rightnode
        return node.key
      
#-----------  
def searchRE(currentNode,element):
  if currentNode != None:
    if currentNode.value == element:
      print(currentNode.value)
      return currentNode
    else:
        if currentNode.value < element:
          return searchRE(currentNode.rightnode,element)
        else:
          return searchRE(currentNode.leftnode,element)
  
      #este código solo me sirve cuando comparó números si tengo que eleminar letras teno que usar 
  #return searchRE(currentNode.leftnode,element)
  
  else:
    return None
    
#----------
def nodoSustitutoD(currentNode):
  #currentNode es el primer nodo del lado derecho de la raiz
  #menor de sus mayores (solo va a tener hijo a la derecha)
  if currentNode.leftnode == None:
    return currentNode
  else:
    return nodoSustitutoD(currentNode.leftnode)
    
def nodoSustitutoI(currentNode):
  #currentNode es el primer nodo del lado izq de la raiz
  #mayor de sus menores (solo va a tener hijo a la derecha)
  if currentNode.rightnode == None:
    return currentNode
  else:
    return nodoSustitutoI(currentNode.rightnode)

#----------------------------------------------------------------------
#Devuelve clave (key) a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
def deleteKey(B,key):
  node = searchRE(B.root,key)
  
  if node == None:
    return None
  else:
    return delete(B,node.value)
#------------------------------------------------------------------------#Devuelve el valor de un elemento con una key del árbol binario, devuelve None si no existe elemento con dicha clave.
def access(B,key):
  node = searchRkey(B.root,key)
  if node == None: 
    return None
  else:
    return node.value
  
#------------------------------------------------------------------
#Devuelve None si no existe elemento para dicha clave. Caso contrario devuelve la clave del nodo donde se hizo el update.
def update(B,element,key):
  node = searchRkey(B.root,key)
  if node == None:
    return None
  else:
    node.value = element
    return node.key

#-----------------------------------------------------------------------
#Devuelve una lista (LinkedList) con los elementos del árbol en orden. Devuelve None si el árbol está vacío.
def traverseinOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    L = traverseinOrderAux(L,B.root)
    L = invertirLista(L)
    return L
    
def traverseinOrderAux(L,node):
  if node == None:
    return 
  else: 
    traverseinOrderAux(L,node.leftnode)
    add(L,node.value)
    traverseinOrderAux(L,node.rightnode)
    return L

#-----------------------------------------------------------------------------
#Devuelve una lista (LinkedList) con los elementos del árbol en post-orden. Devuelve None si el árbol está vacío.
def traverseInPostOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    traverseInPostOrderR(L,B.root)
    L = invertirLista(L)
    return L

def traverseInPostOrderR(L,node):
  if node == None:
    return
  else:
    traverseInPostOrderR(L,node.leftnode)
    traverseInPostOrderR(L,node.rightnode)
    add(L,node.value)
  return L
#-----------------------------------------------------------------------------
#Devuelve una lista (LinkedList) con los elementos del árbol en pre-orden. Devuelve None si el árbol está vacío.
def traverseInPreOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    traverseInPreOrderR(L,B.root)
    L = invertirLista(L)
    return L

def traverseInPreOrderR(L,node):
  if node == None:
    return
  else:
    add(L,node.value)
    traverseInPreOrderR(L,node.leftnode)
    traverseInPreOrderR(L,node.rightnode)
  return L

#---------- bALANCE FACTOR - TRAVERSE IN PREORDER
#traverse in pre-order usando node.bf para verificar que el balance factor de cada nodo este correcto
def traverseInPreOrderBF(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    traverseInPreOrderRBF(L,B.root)
    L = invertirLista(L)
    return L
    
def traverseInPreOrderRBF(L,node):
  if node == None:
    return
  else:
    add(L,node.bf)
    traverseInPreOrderRBF(L,node.leftnode)
    traverseInPreOrderRBF(L,node.rightnode)
  return L


#-----------------------------------------------------------------------------
# Devuelve una lista (LinkedList) con los elementos del árbol ordenados de acuerdo al modo primero en amplitud. Devuelve None si el árbol está vacío.
#por niveles
def traverseBreadFirst(B):
  L = LinkedList()
  LList = LinkedList()
  enqueue(L,B.root)
  while L.head != None:
    currentNode = dequeue(L)
    add(LList,currentNode.value)
    if currentNode.leftnode != None:
      enqueue(L,currentNode.leftnode)
    if currentNode.rightnode != None:
      enqueue(L,currentNode.rightnode)
  LList = invertirLista(LList)
  return LList

#-----------------------------------------------------------------------------
#EJERCICIO 1.1 - TP1 ARBOLES

#salida: retorna la nueva raiz del arbol
#ACOMODAR
def rotateLeft(Tree,avlnode):
  nuevaRaiz = avlnode.rightnode
  #si el nodo a rotar es la raiz
  if avlnode == Tree.root:
    #si la nueva raiz no tiene un hijo izquierdo
    if nuevaRaiz.leftnode == None:
      avlnode.rightnode = None
      
    else:
      #si la nueva raiz tiene un hijo derecho 
      avlnode.rightnode = nuevaRaiz.leftnode
      nuevaRaiz.leftnode.parent = avlnode

    nuevaRaiz.leftnode = avlnode
    avlnode.parent = nuevaRaiz
    Tree.root = nuevaRaiz
    return nuevaRaiz
  else: 
    
    if avlnode.parent.leftnode == avlnode:
      avlnode.parent.leftnode = nuevaRaiz
    else:
      avlnode.parent.rightnode = nuevaRaiz
    
    avlnode.parent = nuevaRaiz
    nuevaRaiz.parent = avlnode.parent
       
    if nuevaRaiz.leftnode == None:
      avlnode.rightnode = None
    else: 
      avlnode.rightnode = nuevaRaiz.leftnode

    nuevaRaiz.leftnode = avlnode
   
    return nuevaRaiz


#-----------------------------------------------------------------------------
#EJERCICIO 1.2 - TP1 ARBOLES
#salida: retorna la nueva raiz del arbol

def rotateRight(Tree,avlnode):
  nuevaRaiz = avlnode.leftnode
  #El nodo a rotar es la raiz 
  if avlnode == Tree.root:
    #si la nueva raiz tiene un hijo derecho
    if avlnode.leftnode.rightnode != None:
      #nuevaRaiz = avlnode.leftnode
      avlnode.leftnode = nuevaRaiz.rightnode
      nuevaRaiz.rightnode.parent = avlnode
    else:
      #si la nueva raiz no tiene un hijo derecho
      avlnode.leftnode = None
        
    nuevaRaiz.rightnode = avlnode
    avlnode.parent = nuevaRaiz
    Tree.root = nuevaRaiz
    return nuevaRaiz
      
  else:
    #si el nodo a rotar no es la raiz
    if avlnode.parent.leftnode == avlnode:
      #el hijo izquierdo del padre de avlnode (avlnode.parent.leftnode) 
      avlnode.parent.leftnode = nuevaRaiz
    else:
      avlnode.parent.rightnode = nuevaRaiz
    avlnode.parent = avlnode.leftnode
    #si la nueva raiz tiene un hijo derecho
    if avlnode.leftnode.rightnode == None:
      avlnode.leftnode.rightnode = avlnode
      avlnode.leftnode = None #importante, sino no se hace bien el arbol
      return nuevaRaiz
    else:
      #si la nueva raiz no tiene un hijo derecho
      avlnode.leftnode = avlnode.leftnode.rightnode
      avlnode.leftnode.parent.rightnode = avlnode
      return nuevaRaiz

#-----------------------------------------------------------------------------
#EJERCICIO 2 - TP1 ARBOLES
#Implementar una función  recursiva que calcule el elemento balanceFactor de cada subárbol
#Salida: AVL con el valor de balanceFactor para cada subarbol

def altura(node):
  #complejidad: O(n)
  if node == None:
    return 0
  else:
    return 1 + max(altura(node.leftnode),altura(node.rightnode))

def calculateBalance(AVL):
  #complejidad: O(n^2) porque calculateBalanceR pasa por cada nodo y le calcula el bf (bf = h(hijo izq) - h(hijo der). La funcion altura (h) tiene una complejidad de O(n) porque tiene que recorrer cada subarbol para ver cuantos nodos tiene a derecha y a izquierda
  if AVL.root == None:
    return 
  else:
    calculateBalanceR(AVL.root)
    return AVL

def calculateBalanceR(node):
  if node == None:
    return
  else:
    node.bf = altura(node.leftnode) - altura(node.rightnode)
    calculateBalanceR(node.leftnode)
    calculateBalanceR(node.rightnode)
    return node.bf
    
#-------------------------------------------------------------------------------------- REBALANCE
#Calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda
#salida: arbol binario de busqueda balanceado es decir el bf de cada nodo es 0, 1 o -1

def rebalance(AVLTree): 
  calculateBalance(AVLTree)
  if AVLTree.root == None:
    return 
  else:
    recorreAbajoR(AVLTree,AVLTree.root)
    return AVLTree

def recorreAbajoR(T,node):
  if node == None:
    return 
  else: 
    if node.bf < -1:
      recorreAbajoR(T,node.rightnode)
    else:
      if node.bf > 1:
        recorreAbajoR(T,node.leftnode)
      else:
        rebalanceAux(T,node.parent)

def recorreArribaR(T,node):
  if node == None:
    return T
  else:
    if node.bf < 1 and node.bf > -1:
      recorreArribaR(T,node.parent)
    else:
      rebalanceAux(T,node)
  
def rebalanceAux(T,node):
  if node == None:
    return
  else:
    if node.bf < -1:
      if node.rightnode.leftnode != None:
        #si el hijo derecho tiene un hijo izquierdo
        #hago rotacion a la derecha del hijoderecho
        rotateRight(T,node.rightnode)
        #hago rotacin a la izquierda del nodo
        rotateLeft(T,node)
      else:
        rotateLeft(T,node)
      calculateBalance(T)
    else: 
      if node.bf > 1:
        if node.leftnode.rightnode != None:
          rotateLeft(T,node.leftnode)
          rotateRight(T,node)
        else:
          rotateRight(T,node)
        calculateBalance(T)
      else:
        recorreArribaR(T,node)

#----------------------------------------------------------------------------------------------------------------INSERT AVLNODE (ejercicio 4)
#Implementar la operación insert() en  el módulo avltree.py garantizando que el árbol  binario resultante sea un árbol AVL

def insertAvlnode(T,element,key):
  insert(T,element,key)
  rebalance(T)

#---------------------------------------------------------------------------------------------------------------DELETE AVLNODE (ejercicio 5)
#Implementar la operación delete() en  el módulo avltree.py garantizando que el árbol  binario resultante sea un árbol AVL.

def deleteAvlnode(AVLTree,element):
  rebalance(AVLTree)
  delete(AVLTree,element)


 
"""
Queria usar esta funcion y no me anda

def rebalanceR(T,node):
  if node == None:
    return T
  else:
    if node.bf < -1:
      rebalanceR(T,node.rightnode)
      if node.rightnode.leftnode != None:
        rotateRight(T,node.rightnode)
        rotateLeft(T,node)
      else:
        rotateLeft(T,node)
    else: 
      if node.bf > 1:
        rebalanceR(T,node.leftnode)
        if node.leftnode.rightnode != None:
          rotateLeft(T,node.leftnode)
          rotateRight(T,node)
        else:
          rotateRight(T,node)
      else:
        return 
        
  calculateBalance(T)
  return rebalanceR(T,node.parent)
"""




    
      
        
        

    
        
      

      
  
  
  
    
    
    
  


  
 



      
      
      
      
    


      
    
    
    
      
   
    
    
    
      
     
        
        

    
  