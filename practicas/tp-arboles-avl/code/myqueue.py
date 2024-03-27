from algo1 import *
from linkedlist import *

def enqueue(Q,element):
  add(Q,element)
  return

def dequeue(Q):
  Current = Node()
  Current = Q.head
  cont = 0

  if Current != None:
    while Current.nextNode != None:
      cont+= 1
      Current = Current.nextNode
    delete(Q,Current.value)
    return Current.value
  else:
    return None

