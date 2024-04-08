from linkedlist import*

def contieneSuma(A,n):
  terminar = False
  encontro = False
  num = A.head
  while terminar == False and num.nextNode != None:
    valorBusc = n - num.value
    num2 = num.nextNode
    while encontro == False:
      if num2.value == valorBusc:
        encontro = True
        terminar = True
        return True
      else:
        num2 = num2.nextNode
        if num2 == None:
          break
    num = num.nextNode
    


