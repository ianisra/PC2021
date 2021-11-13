import sys
import os
import requests
from bs4 import BeautifulSoup as bs
from prettytable import PrettyTable

def openfile(filename):
  lista_titulos = []
  lectura = open(filename, "r")
  for linea in lectura:
    try:
      pagina = requests.get(linea)
    except:
      continue
    soup = bs(pagina.content, "html.parser")
    titulo = (soup.find("title"))
    lista_titulos.append(titulo.get_text())   
  return lista_titulos


if __name__ == "__main__":
  txtlist = []
  for eachLine in sys.stdin:
    entry = eachLine.strip()
    if entry:
      txtlist.append(entry)
  diccionario_titulos = {} #a #baia
  for targetFile in txtlist:

    if os.path.isfile(targetFile):
      lista_titulos = openfile(targetFile)

      if (lista_titulos != None):
        diccionario_titulos[targetFile] = lista_titulos
      else:
        continue
    else:
      print("WARNING", " not a valid file", targetFile)

  # Create Result Table Display using PrettyTable
    
  ''' GENERATE RESULTS TABLE SECTION'''
    
  ''' Result Table Heading'''
  resultTable = PrettyTable(['File-Name', 'Title of links'])
    
  for key in diccionario_titulos:
    resultTable.add_row( [key, diccionario_titulos[key]])  
  
  resultTable.align = "l" 
  print(resultTable)

  """
  
  #ola JAKJAJA 
  listo
  """
