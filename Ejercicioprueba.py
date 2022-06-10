import pandas as pd # necesitamos esta libreria para extraer los datos del excel (.xlsx)
import random #necesitamos esta libreria para usar la funcion de aleatorio


## la funcion niveles se encarga de seleccionar una pregunta al asar segun el nivel de dificutad
def niveles(a):
  if (a == 1):
    num = random.randint(0, 4)
  if (a == 2):
    num = random.randint(5, 9)
  if (a == 3):
    num = random.randint(10, 14)
  if (a == 4):
    num = random.randint(15, 19)
  if (a == 5):
    num = random.randint(20, 24)
  return num


## La funcion preguntas se encarga de extraer los datos de la pregunta, de la BD de preguntas
def pregunta(a):
  url = 'Preguntas.xlsx'
  doct = pd.read_excel(url)
  desc = doct.at[a,'Descripcion']
  ra = doct.at[a,'a']
  rb = doct.at[a,'b']
  rc = doct.at[a,'c']
  rd = doct.at[a,'d']
  rcorr = doct.at[a,'Correcta']
  nivel = doct.at[a,'Nivel']
  #print('la longitud:',len(doct.index))
  return (desc, ra, rb, rc, rd, rc, rcorr, nivel)

## la funcion selesccion se encarga de validar la respuesta del usuario para poder compararla con la respuesta correcta de la BD
def seleccion():
  eligio = input("Cual es tu respuesta: ")
  while True:
    if (eligio=="A") or (eligio=="a"):
      rpta = "A"
      break
    elif (eligio=="B") or (eligio=="b"):
      rpta = "B"
      break
    elif (eligio=="C") or (eligio=="c"):
      rpta = "C"
      break
    elif (eligio=="D") or (eligio=="d"):
      rpta = "D"
      break
    else:
      print("Opción no válida")
      eligio = input("Ingresa nuevamente tu respuesta: ")
  return rpta

## Esta funcion crea el premio del jugador
def premio(valor):
  return valor * 100000

## Esta funcion se crea para imprimir el numero con decimales
def imprimir_numero(numero):
  miles_translator = str.maketrans(".,", ",.")
  numero = f"{numero:,}".translate(miles_translator)
  return numero

## Funcion creada para guardar los registros de cada Jugador en un .txt
def Guardar_Jugador(Nombre,Nivel=None,gano=None,Ganado=None):
  with open("jugadores.txt","a") as File:
    File.write("++++++++++++++++++++++\n")
    File.write(f"Nombre: {Nombre}\n")
    File.write(f"Nivel:  {Nivel}\n")
    File.write(f"Ganó?:  {gano}\n")
    File.write(f"Valor:  ${imprimir_numero(Ganado)}\n")






##Pricipal
f=0
while f==0:
  try:
    print(f"\033[1m BIENVENIDO AL JUEGO!!! \033[0m")
    nombre = input("Por favor ingresa tu nombre ")
    print(f"Buena Suerte, \033[1m {nombre} \033[0m ")
  
    for i in [1, 2, 3, 4, 5]:
      m=0
      print("\nEstas en el nivel ",i,"\n")
      m = pregunta(niveles(i))
      print(f"Pregunta \n {m[0]} \n\033[1mA:\033[0m {m[1]}     \033[1mC:\033[0m {m[3]} \n\033[1mB:\033[0m {m[2]}     \033[1mD:\033[0m {m[4]}  \n")
      sel = seleccion()
      if sel == m[6]: #con este if verificamos que el usuario seleccione la respuesta correcta
        if i == 5: #este if nos verifica que el jugador este en el ultimo nivel
          print(f"\nExcelente haz Ganado el Juego\n \033[1m tu premio es de: $ {imprimir_numero(premio(i))} Pesos \033[0m")
          Guardar_Jugador(nombre,i,'SI',premio(i))
          break
        print(f"\nExcelente haz pasado al siguiente nivel \n \033[1m haz acumulado: $ {imprimir_numero(premio(i))} Pesos \033[0m")
        retiro = input(f"Para continuar presiona cualquier tecla, Para retirarte Presiona la letra (S)")
        if (retiro == "S") or (retiro == "s"):
          print(f"\033[1m  Felicitaciones haz Ganado: $ {imprimir_numero(premio(i))} Pesos \033[0m")
          Guardar_Jugador(nombre,i,'SI',premio(i))
          break
      else:
        print(f"Perdiste...  La respuesta correcta era {m[6]}" )
        Guardar_Jugador(nombre,i,'NO',0)
        break
    v = input(f"Si desea volver a jugar presiona cualquier tecla, Para retirarte Presiona la letra (S)")
    if (v == "S") or (v == "s"):
      print(f"\033[1m  Gracias por participar\033[0m")
      f=1
  except ValueError:
    print("UPP ....")
    break