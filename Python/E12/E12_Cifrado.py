import detectspanish as spanish
import argparse

universo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.' 

def cifrado(mensaje, clave, universo):

  key = len(clave)

  translated = ''

  for symbol in mensaje:
    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
    if symbol in universo:
        symbolIndex = universo.find(symbol)
        translatedIndex = symbolIndex + key
        
        if translatedIndex >= len(universo):
            translatedIndex = translatedIndex - len(universo)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(universo)

        translated = translated + universo[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

  return(translated)


def descifrado(mensaje, clave, universo):

 key = len(clave)

 translated = ''


 for symbol in mensaje:
    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
    if symbol in universo:
        symbolIndex = universo.find(symbol)
        translatedIndex = symbolIndex - key
        
        if translatedIndex >= len(universo):
            translatedIndex = translatedIndex - len(universo)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(universo)

        translated = translated + universo[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

 return(translated)


def crackeo(mensaje, universo):
  print('Hacking...')
  for key in range(len(universo)):

      translated = ''

      for simbolo in mensaje:
          if simbolo in universo:
              symbolIndex = universo.find(simbolo)
              translatedIndex = symbolIndex - key

              if translatedIndex < 0:
                  translatedIndex = translatedIndex + len(universo)

              translated = translated + universo[translatedIndex]

          else:
              translated = translated + simbolo

      if spanish.isSpanish(translated):
        # Ask user if this is the correct decryption.
        print()
        print('Possible encryption hack:')
        print('Key %s: %s' % (key, translated[:100]))
        print()
        print('Enter D if done, anything else to continue hacking:')
        response = input('> ')

        if response.strip().upper().startswith('D'):
          return translated

      #print('Key #%s: %s' % (key, translated))


if __name__ == "__main__":
  description="Este script tiene la finalidad de cifrar   descifrar o crackear mensajes"
  parser = argparse.ArgumentParser(description="E12", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('-modo', choices=['cifrado', 'descifrado', 'crackeo'] , help='Es necesario poner un modo para saber la finalidad para la cual se quiere utilizar el script.', required=True)
  parser.add_argument('-mensaje', type=str, help='Se debe poner un mensaje el cual se quiera cifrar o descifrar.',default = "Hola mundo mundial")
  parser.add_argument('-clave', type=str, help='Se utiliza para saber a base de cual palabra se quiere cifrar o descifrar un mensaje', default="mundo")
  params = parser.parse_args()
  mensaje = (params.mensaje)
  clave = (params.clave)
  modo = (params.modo)

if modo == 'cifrado':
  mensajecif = cifrado(mensaje, clave, universo)
  print(mensajecif)
elif modo == 'descifrado':
  mensajedes = descifrado(mensaje, clave, universo)
  print(mensajedes)
elif modo == 'crackeo':
  mensajecrack = crackeo(mensaje, universo)
  print(mensajecrack)
else:
  print("No se eligió una opción correcta")
