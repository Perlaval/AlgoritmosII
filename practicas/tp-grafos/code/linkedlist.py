from algo1 import *

class LinkedList:
  head=None

class Node:
  value = None
  color = None
  parent = None
  distance = None
  nextNode=None
  

def add(L,element):
  newNode = Node()
  newNode.value = element
  newNode.nextNode = L.head
  L.head = newNode
  return L


def printList(L):
  Current = L.head
  cont = 0

  while Current != None:
    if cont != 0:
     print (end = ", ")
    else: 
      print (end = "L :")

    print(Current.value, end="")
    Current = Current.nextNode
    cont = cont + 1

def search(L,element):
  Current = Node()
  Current = L.head
  hallado = False
  cont = 0

  while Current != None and hallado == False:
    if Current.value == element:
      hallado = True
      return cont
    else:
      cont += 1
      Current = Current.nextNode

  if hallado == False:
    return None

def length(L):
  Current = Node()
  Current = L.head
  cont = 0

  while Current != None:
    cont += 1
    Current = Current.nextNode
  return cont
  

def insert(L, element, position):
  Current = Node()
  Current = L.head
  newNode = Node()
  newNode.value = element
  previous = Node()
  cont = 0

  if position <= length(L):
    if position == 0:
      newNode.nextNode = L.head
      L.head = newNode
      return position
    else:
      previous = None
      while Current != None and cont < position:
        previous = Current
        Current = Current.nextNode
        cont += 1
        if cont == position:
          previous.nextNode = newNode
          newNode.nextNode = Current
          return position



def delete(L,element):
  Current = Node()
  Current = L.head
  previousNode = Node()
  borrado = False
  cont = 0

  while Current != None and borrado == False:
    if Current.nextNode != None:
      if Current.value == element:
        if cont == 0: 
          L.head = Current.nextNode
          borrado = True
          return cont
        else: 
          previousNode.nextNode = Current.nextNode
          borrado = True
          return cont         
      else:
        previousNode = Current
        Current = Current.nextNode
        cont += 1
    else:
      if Current.value == element:
        if cont == 0 :
          L.head = None
          borrado = True
          return cont
        else:
          previousNode.nextNode = None
          borrado = True
          return cont
      else:
        return None

def deletePosicion(L,posicion):
  Current = Node()
  Current = L.head
  previousNode = Node()
  borrado = False
  cont = 0

  while Current != None and borrado == False:
    if Current.nextNode != None:
      if cont == posicion:
        if cont == 0: 
          L.head = Current.nextNode
          borrado = True
          return cont
        else: 
          previousNode.nextNode = Current.nextNode
          borrado = True
          return cont         
      else:
        previousNode = Current
        Current = Current.nextNode
        cont += 1
    else:
      if cont == posicion:
        if cont == 0 :
          L.head = None
          borrado = True
          return cont
        else:
          previousNode.nextNode = None
          borrado = True
          return cont
      else:
        return None

def access(L,position):
  Current = Node()
  Current = L.head
  existe = False
  cont = 0

  while Current != None and cont <= position and existe == False:
    if cont < position:
      Current = Current.nextNode
      cont += 1
    else:
      existe = True
      return Current.value

  if existe == False:
    return None


def update(L,element, position):
  Current = Node()
  Current = L.head
  actualizado = False
  cont = 0

  while Current != None and cont <= position and actualizado == False:
    if cont < position:
      Current = Current.nextNode
      cont += 1
    else:
      Current.value = element
      actualizado = True
      print("")
      return cont
  if actualizado == False:
    return None   



def invertirLista(L):
  Current = L.head
  pos = 0

  while Current != None:
    if Current != L.head:
      deletePosicion(L,pos)
      add(L,Current.value)

      Current = Current.nextNode
    else:
      Current = Current.nextNode
    pos += 1
  return L
