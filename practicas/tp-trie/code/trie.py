from typing import List
from algo1 import*
#from linkedlist import LinkedList
from linkedlist import*
from myStack import*

class Trie:
  def __init__(self):
    self.root = None

class TrieNode:
  def __init__(self, parent=None, children=None, key=None, isEndOfWord=False):
      self.key = key
      self.parent = parent
      self.children = children 
      self.isEndOfWord = isEndOfWord

#------------------------------------------------------------------#INSERT
#inserte un elemento en T, siendo T un Trie.
#Sugerencia 1: Para manejar múltiples nodos, el campo children puede contener una estructura LinkedList conteniendo TrieNode

def insert(T,element):
  if T.root == None:
    T.root = TrieNode()
    T.root.children = LinkedList()
    insertR(T.root.children,None,element,0)
  else:
    insertR(T.root.children,T.root,element,0)

def insertR(lista,parent,element,i):
  if i >= len(element):
    parent.isEndOfWord = True
  else:
    ch = element[i]
    nodoLista = searchElementInList(lista,ch)
         
    if nodoLista == None:
      newTrieNode = TrieNode(parent,LinkedList(),ch,False)
      add(lista,newTrieNode)
      insertR(newTrieNode.children,newTrieNode,element,i+1)
    else:
      node = nodoLista.value
      #node es el trieNode que se almacena en el campo value del nodo de la lista
      insertR(node.children,node,element,i+1)
   

def searchElementInList(L,ch):
  current = L.head
  while current != None:
    if current.value.key == ch:
      return current
    current = current.nextNode
  return

#-----------------------------------------------------------------
#SEARCH
#Verifica que un elemento se encuentre dentro del Trie
#Salida:Devuelve False o True  según se encuentre el elemento.

def search(T,element):
  if T.root == None or T.root.children == None:
    return False
  else:
    #(lista,nodo,string,strIndex)
    #print("b: ", searchR(T.root.children,element,0))
    return searchR(T.root.children,element,0)

def searchR(list,element,i):
  if i >= len(element):
      return
  else:
      ch = element[i]
      node = searchElementInList(list,ch)
      if node == None:
        return False
      else:
        trieNode = node.value
        if i == len(element)-1:
          return trieNode.isEndOfWord
        else:
          return searchR(trieNode.children,element,i+1)

#------------------------------------------------------------
#SEARCH PREFIJO

def searchPrefijo(T,element):
  if T.root == None or T.root.children == None:
    return False
  else:
    #(lista,nodo,string,strIndex)
    return searchPrefijoR(T.root.children,element,0)

def searchPrefijoR(list,element,i):
  if i >= len(element):
      return
  else:
      ch = element[i]
      node = searchElementInList(list,ch)
      if node == None:
        return None
      else:
        trieNode = node.value
        if i == len(element)-1:
          return trieNode
        else:
          return searchPrefijoR(trieNode.children,element,i+1)

#-----------------------------------------------------------------
#DELETE
#Elimina un elemento se encuentre dentro del Trie
#Devuelve False o True  según se haya eliminado el elemento.

def delete(T,element):
  if search(T,element) == True:
    return deleteR(T,T.root.children,element,0)
  else: 
    return False

def deleteR(T,list,element,i):
  ch = element[i]
  node = searchElementInList(list,ch)
  trieNode = node.value
  if i == len(element)-1:
    if trieNode.children.head == None:
      deleteNode(list,ch)
      if length(list) >= 1:
        return True
      else:
          while trieNode.parent.parent != None and not trieNode.parent.isEndOfWord:
            deleteNode(trieNode.parent.parent.children,trieNode.parent.key)
            trieNode = trieNode.parent
          deleteNode(T.root.children,trieNode.parent.key)
          return True            
    else:
      trieNode.isEndOfWord = False
      return True
  else:
    return deleteR(T,trieNode.children,element,i+1) 

#-----------------------------------------------------------------
#EJERCICIO 4
#Implementar un algoritmo que dado un árbol Trie T, un patrón p (prefijo) y un entero n, escriba todas las palabras del árbol que empiezan por p y sean de longitud n.

def imprimePalabras(T,p,n):
  trieNode = searchPrefijo(T,p)
  long = n-len(p)
  if trieNode == None or len(p) > n:
    return None
  else:
    imprimePalabrasR(trieNode.children.head,p,long,0)

def imprimePalabrasR(node,string,long,cont):
  if node == None:
    return 
  else:
    if cont <= long-1:
      if node.nextNode == None:
        if cont == long-1: 
          if node.value.isEndOfWord == True:
            string += node.value.key
            print(string)
            return
        else:
          if node.value.isEndOfWord != True: 
            string += node.value.key
          imprimePalabrasR(node.value.children.head,string,long,cont+1)
      else: #si la lista tiene mas de un nodo
        str = string
        while node != None:
          if cont == long-1:
            if node.value.isEndOfWord == True:
              string += node.value.key
              print(string)
          else:
            if node.value.isEndOfWord != True: 
              string += node.value.key
            imprimePalabrasR(node.value.children.head,string,long,cont+1)
          node = node.nextNode
          string = str

#----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 5

#Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario

def sonIguales(T1,T2):
  lista = recorreTrie(T1)
  #printList1(lista)
  current = lista.head
  while current != None:
    if search(T2,current.value) == False:
      print("Los trie no son iguales")
      return False
    current = current.nextNode
  print("Los trie son iguales")
  return True

def recorreTrie(T1):
  lista = LinkedList()
  recorreTrieR(T1.root.children.head,"",lista)
  return lista

def recorreTrieR(node,palabra,lista):
  if node == None: #llego al final del trie
    return lista

  if node.nextNode == None: #solo tiene un hijo (la lista solo tiene un nodo)
    palabra += node.value.key
    if node.value.isEndOfWord == True:
      add(lista,palabra)
    recorreTrieR(node.value.children.head,palabra,lista)
  else: #la lista tiene mas de un nodo
    string = palabra #guardo el prefijo que comparten las palabras
    while node != None:
      palabra += node.value.key
      if node.value.isEndOfWord == True:
        add(lista,palabra)
      recorreTrieR(node.value.children.head,palabra,lista)
      node = node.nextNode
      palabra = string

#--------------------------------------------------------------------------
#EJERCICIO 6
#abcd y dcba son cadenas invertidas
def cadInvertidas(T):
  lista = recorreTrie(T)
  current = lista.head
  while current != None:
    if search(T,invierteCadena(current.value)) == True:
      print("hay cadenas invertidas", current.value)
      return True
    current = current.nextNode
  print("no hay cadenas invertidas")
  return False
 

def invierteCadena(cadena):
  palabra = ""
  for i in range(len(cadena)-1,-1,-1):
    palabra += cadena[i]
  return palabra
    

#--------------------------------------------------------------------------
#EJERCICIO 7
#autoCompletar(T, ‘groen’) devolvería “land”, ya que podemos tener “groenlandia” o “groenlandés”

def autocompletar(T,cadena):
  node = searchPrefijo(T,cadena) #me devuelve el nodo.key = ultimo caracter de la cadena
  if node == None:
    return "" #cadena vacia
  else:
    
    return autocompletarR(node.children.head,"")

def autocompletarR(node,palabra):
  if node == None: #llego al final del trie
    return palabra
  if node.nextNode == None: #la lista solo tiene un nodo
    palabra += node.value.key
    return autocompletarR(node.value.children.head,palabra)
  else:
    return palabra
    
    
  
    
    









      
    
      

 
      

      
    
    
  




      
    
    
 
    
    
   
  
        
      
      
        


    

      
      
      
      
      
  
  


    
   
  
 
  
    
    
    
    
    
  
    


 
    
    
    
    
 
  
   
  
    
        

    
  