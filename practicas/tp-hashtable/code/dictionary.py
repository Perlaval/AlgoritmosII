
from math import sqrt
from algo1 import*
#from linkedlist import LinkedList
from linkedlist import*
from myStack import*
from sympy import prevprime


def hashDiv(key,m):
  pos = key % m
  #como la funcion es key mod 9 siempre me va a devolver valores menores o iguales a 8 el tamaño de D es 9
  return pos

def hashMult(key,m,A):
  pos = int(m*((key*A) - int(key*A)))
  return pos
  

#--------------------------------------------------------------INSERT
#salida: devuelve d
def insert(D,key,value):
  pos = key % 9
  m = 9
  #if len(D) == 0: #esto lo va a hacer solo una vez
    #for i in range(0,m):
     # D.append(None)
  if D[pos] == None:
    D[pos] = LinkedList()
  add(D[pos],key,value)
  return D

def insert1(D,key,value,m): #metodo div
  pos = hashDiv(key,m)
  #if len(D) == 0: #esto lo va a hacer solo una vez
    #for i in range(0,m):
      #D.append(None)
  if D[pos] == None:
    D[pos] = LinkedList()
  add(D[pos],key,value)
  return D

def insert2(D,key,value,m,A): #metodo mult
  pos = hashMult(key,m,A)
  if D[pos] == None:
    D[pos] = LinkedList()
  add(D[pos],key,value)
  return D

#-------------------------------------------------------------SEARCH
#salida: devuelve el value de la key o NONE
def search(D,key):
  pos = key % 9
  if D[pos] != None:
    node = searchNode(D[pos],key) 
    if node != None:
      return node.value #devuelve el value
  return None

def search1(D,key,m):
  pos = hashDiv(key,m)
  if D[pos] != None:
    return searchNode(D[pos],key) #devuelve el nodo 
  return None

#-------------------------------------------------------------DELETE
#salida: devuelve D
def delete(D,key):
  pos = key % 9
  if D[pos] != None:
    deleteNode(D[pos],key)
    return D
  return None

def delete1(D,key,m):
  pos = hashDiv(key,m)
  if D[pos] != None:
    deleteNode(D[pos],key)
    return D
  return None
#-------------------------------------------------------------NumPrimo
def numPrimo(n):
  if n/2 <= 2:
    m = prevprime(n)
  else:
    if (n/2) % 2 == 0 :
      m = prevprime(n/2)
    else:
      m = int(n/2)
  return m
#--------
def inicializaDic(D,m):
  for i in range(0,m):
    D.append(None)
  return D
 
  
#-------------------------------------------------------------EJERCICIO 4

def esPermutacion(S,P):
  D = inicializaDic([],len(S))
  
  if len(S) == len(P):
    m = numPrimo(len(S))
      
    for i in range(0,len(S)): #hago una hashT con los caracteres de S
      insert1(D,ord(S[i]),S[i],m)
      
    i = 0
    while i < len(P): #busco en la hashT los caracteres de P
      if search1(D,ord(P[i]),m) == None:
        print("Falso, ya que",P, "tiene al carácter",P[i], "que no se encuentra en",S,"por lo que no es una permutación de", S)
        return False
      delete1(D,ord(P[i]),m)
      i += 1
    print("True, ya que", P, "es una permutacion de", S)
    return True
  else:
    print("Falso, ya que las palabras no tienen el mismo tamaño")
    return False

#-------------------------------------------------------------EJERCICIO 5
def elementosUnicos(L):
  m = numPrimo(len(L))
  D = inicializaDic([],m)
  flag = True
  node = None
  for i in range(0,len(L)): #defino una hashT con lo elementos de L
    node = search1(D,L[i],m) #busco el elemento antes de insertarlo
    if node != None: #si ya se encuentra en la hashT, devuelve false
      print("Falso,", L[i],"se repite en la", node.value,"y en la", i+1,"posicion" )
      flag = False
    else: #sino lo ingresa
      insert1(D,L[i],i+1,m)
  return flag
  
#-------------------------------------------------------------EJERCICIO 6
def hashPostal(codigo): #C1024CWN
  val = 0
  D = inicializaDic([],1009)
  for i in range(1,5):
    val += int(codigo[i])
  
  key = ord(codigo[0])*10^3 + ord(codigo[5])*10^2 + ord(codigo[6])*10+ ord(codigo[7]) + val
  #sumo el valor entero y los codigos ascii de las letras con peso(para que las permutaciones de los caracteres no me devuelvan el mismo valor) segun su posicion esto me va a devolver un valor unico para cada codigo postal
  
  insert2(D,key,codigo,1009,(sqrt(5)-1)/2)

#-------------------------------------------------------------EJERCICIO 7
#aabcccccaaa
#a2blc5a3

def compresionCadenas(cad):
  m = numPrimo(len(cad)) #calculo el num primo
  D = inicializaDic([],m) #inicializa las pos de la hashT en none
  string = "" 
  for i in range(0,len(cad)):
    letra = cad[i]
    node = search1(D,ord(letra),m) #busco el node que tiene key=letra en la hashT
    if node == None:
      insert1(D,ord(letra),1,m) #si no esta lo inserto
      node = search1(D,ord(letra),m) #lo guardo en una var
    else:
      node.value += 1 #si esta aumento el value
      #el campo value me va a indicar la cantidad de rep de la letra
     
    if i < len(cad)-1: #no estamos en el ultimo caracter
      if cad[i+1] != letra: #si la letra que sigue es diferente 
        string += letra + str(node.value) #concateno la letra con el value
        node.value = 0 #reinicio el value porque la letra se puede repetir mas adelante
    else: #estamos en el ultimo caracter
      if i == len(cad)-1: #estoy en el ultimo char de la cadena
        string += letra + str(node.value) #concateno la letra con el value
        node.value = 0
  
  if len(string) < len(cad):
    return string
  else:
    return cad

#-------------------------------------------------------------EJERCICIO 8 
#S = ‘abracacadabra’ , P = ‘cada’
#4, índice de la primera ocurrencia de P dentro de S (abracadabra)

def primeraOcurrencia(S,P):
   
  for i in range(0,len(S)): #recorro la cadena S
    if S[i] == P[0]: #si el primer caracter de P es igual a un caracter de S
      if S[i:i+len(P)] == P: #si la subcadeba de S que sigue a partir de i de long = len(P) es igual a P
        print(i)
        return i
  return None
    
#------------------------------------------------------------------EJERCICIO9
#S = {s1, . . . , sn} y T = {t1, . . . , tm}
#S ⊆ T


#busco uno a uno los elementos del conjunto mas pequeño en la hashT

def esSubconjunto(S,T): #como son conjuntos los elementos no se repiten
  if len(S) > len(T):
    return False
  else:
    m = numPrimo(len(T))
    D = inicializaDic([],m)
    for i in range(0,len(T)): #hago una hashT con el conjunto mas grande
      insert1(D,T[i],T[i],m)
      
    for i in range(0,len(S)): #busco los elementos del conjunto las pequeño en la hashT
      if search1(D,S[i],m) == None:
        return False #si hay un elemento que no esta en la hashT no es subconjunto
    return True

#------------------------------------------------------------------EJERCICIO10
#inserción de las siguientes llaves: 10; 22; 31; 4; 15; 28; 17; 88; 59 en una hashT
# m = 11; h’(k) = k
#Linear probing
#Quadratic probing con c1 =  1 y c2 = 3 
#Double hashing con  h1(k) = k y  h2(k) = 1 +(k mod ( m - 1))

#direccionamiento abierto

def fHashAux(k):
  pos = k % 10
  return pos

def hash1(k):
  return k

def hash2(k,m):
  pos = 1 + (k % (m-1))
  return pos

def linearProbing(key,i,m):
  pos = (fHashAux(key) + i) % m
  return pos

def quadraticProbing(key,c1,c2,i,m):
  pos = (fHashAux(key) + c1*i + c2*(i^2)) % m
  return pos

def doubleHashing(key,i,m):
  pos = (hash1(key) + i*(hash2(key,m))) % m
  return pos

def insertDirAbierto(D,key,value): #no lleva value?
  m = 11
  i = 0
  
  while i < m:
    pos = doubleHashing(key,i,m)
    if D[pos] == None:
      D[pos] = value
      return D
    else:
      i += 1
  return D

def printHashTable(D):
  for i in range(0,len(D)):
    print(i, end=":")
    printList(D[i])
    print("")
  
  
  

 
  
  
  

  
 
    

    
  
 


  

  
      
  
    
    
    
    
      
    
      
  
  



      
    
      

 
      

      
    
    
  




      
    
    
 
    
    
   
  
        
      
      
        


    

      
      
      
      
      
  
  


    
   
  
 
  
    
    
    
    
    
  
    


 
    
    
    
    
 
  
   
  
    
        

    
  