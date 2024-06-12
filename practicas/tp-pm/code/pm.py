from algo1 import*
from linkedlist import*

#--EJERCICIO 7--
def reduceLen(string):
  pila = []

  for char in string:
      if pila and pila[-1] == char:
          pila.pop()  # Remueve  el último elemento del stack si es igual al actual
      else:
          pila.append(char)  # Agrega el caracter actual al stack

  return ''.join(pila)  # Convierte la lista a una cadena

#--EJERCICIO 8--
def isContained(main_str, sub_str):
  m, n = len(main_str), len(sub_str)
  i, j = 0, 0

  # Recorre los caracteres de main_str
  while i < m and j < n:
      if main_str[i] == sub_str[j]:
          j += 1  # Avanza el puntero de sub_str
      i += 1  # Avanza el puntero de main_str

  # Si hemos recorrido toda la sub_str, significa que está contenida en main_str
  return j == n

#--EJERCICIO 12--
def construirAEF(patron):
  m = len(patron)
  aef = [{} for _ in range(m + 1)] #lista con diccionarios {caracter: estado}}

  # defino el estado inicial
  aef[0][patron[0]] = 1
  X = 0  # Estado de fallo

  for j in range(1, m):
      for c in set(patron):
          aef[j][c] = aef[X].get(c, 0)
      aef[j][patron[j]] = j + 1
      X = aef[X].get(patron[j], 0)

  for c in set(patron):
      aef[m][c] = aef[X].get(c, 0)

  return aef

def buscar_patron(patron, texto):
  automata = construirAEF(patron)
  m, n = len(patron), len(texto)
  i, j = 0, 0  # i para texto, j para patrón (estado del DFA)

  while i < n:
      j = automata[j].get(texto[i], 0)
      if j == m:
          print(f"Patrón encontrado en la posición {i - m + 1}")
          j = 0  # Reiniciar para buscar más coincidencias
      i += 1


#--EJERCICIO 13--
def rabin_karp(p, t, q):
  m = len(p)  # Longitud del patrón
  n = len(t)  # Longitud del texto
  d = 256  # Número de caracteres en el alfabeto (por ejemplo, ASCII tiene 256 caracteres)
  hp = 0  # Hash del patrón
  ht = 0  # Hash del texto
  h = 1  # Valor de h usado en el cálculo del hash

  # Calcular h = d^(m-1) % q
  for i in range(m - 1):
      h = (h * d) % q

  # Calcular el hash inicial del patrón y del primer segmento del texto
  for i in range(m):
      hp = (d * hp + ord(p[i])) % q
      ht = (d * ht + ord(t[i])) % q

  # Buscar el patrón en el texto
  for i in range(n - m + 1):
      # Si los hashes coinciden, verificar carácter por carácter
      if hp == ht:
          match = True
          for j in range(m):
              if t[i + j] != p[j]:
                  match = False
                  break
          if match:
              print(f"{p} encontrado en la posición {i + 1}")

      # Actualizar el hash para la siguiente ventana de texto
      if i < n - m:
          ht = (d * (ht - ord(t[i]) * h) + ord(t[i + m])) % q
          if ht < 0:
              ht += q

  # Si no se encontró ninguna coincidencia
  print("Ninguna coincidencia encontrada")

#--EJERCICIO 14--
def KMP(t, p):
  n = len(t)  # Longitud del texto
  m = len(p)  # Longitud del patrón
  pi = computePrefixFunction(p)  # Calcular la función de prefijo del patrón
  q = 0  # Índice que indica cuántos caracteres coinciden

  for i in range(0, n):
      # Mientras exista un mismatch y q sea mayor que 0, retroceder según la función de prefijo
      while q > 0 and p[q] != t[i]:
          q = pi[q - 1]

      # Si el caracter actual del texto coincide con el caracter actual del patrón
      if p[q] == t[i]:
          q += 1  # Incrementar q, indicando un nuevo caracter coincidente

      # Si q es igual a la longitud del patrón m, se encontró una ocurrencia completa
      if q == m:
          print("Pattern occurs with shift", i - m + 2)
          break

  # Si q no es igual a m, significa que no se encontraron ocurrencias
  if q != m:
      print("None")

def computePrefixFunction(p):
  m = len(p)  # Longitud del patrón
  pi = [0] * m  # Inicializar arreglo para la función de prefijo
  k = 0  # Longitud del prefijo más largo que también es un sufijo

  for q in range(1, m):
      # Mientras exista un mismatch, retroceder según la función de prefijo
      while k > 0 and p[k] != p[q]:
          k = pi[k - 1]

      # Si el caracter siguiente coincide, incrementar k
      if p[k] == p[q]:
          k += 1

      pi[q] = k  # Asignar el valor de k a la posición q de la función de prefijo

  return pi  # Retornar la función de prefijo computada


