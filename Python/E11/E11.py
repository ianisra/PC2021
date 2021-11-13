from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os
from os import path
import requests, bs4
import argparse

if __name__ == "__main__":
  description="""Este programa tiene la finalidad de        descargar imagenes y sacar la metadata de cada una de   éstas, para ello debe usarse de la siguiente manera:
          -url "https://www.uanl.mx/" """
  parser = argparse.ArgumentParser(description="E11", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('-url', type=str, help='Se debe ingresar un link', default="https://www.uanl.mx/")
  params = parser.parse_args()
  url = (params.url)


def decode_gps_info(exif):
  gpsinfo = {}
  if 'GPSInfo' in exif:
    #Parse geo references.
    Nsec = exif['GPSInfo'][2][2]
    Nmin = exif['GPSInfo'][2][1]
    Ndeg = exif['GPSInfo'][2][0]
    Wsec = exif['GPSInfo'][4][2]
    Wmin = exif['GPSInfo'][4][1]
    Wdeg = exif['GPSInfo'][4][0]
    if exif['GPSInfo'][1] == 'N':
      Nmult = 1
    else:
      Nmult = -1
    if exif['GPSInfo'][3] == 'E':
      Wmult = 1
    else:
      Wmult = -1
    Lat = Nmult * (Ndeg + (Nmin + Nsec / 60.0) / 60.0)
    Lng = Wmult * (Wdeg + (Wmin + Wsec / 60.0) / 60.0)
    exif['GPSInfo'] = {"Lat": Lat, "Lng": Lng}
    input()


def get_exif_metadata(image_path):
  ret = {}
  image = Image.open(image_path)
  if hasattr(image, '_getexif'):
      exifinfo = image._getexif()
      if exifinfo is not None:
          for tag, value in exifinfo.items():
              decoded = TAGS.get(tag, tag)
              ret[decoded] = value
  decode_gps_info(ret)
  return ret


print("\nObteniendo imagenes de la url:"+ url)
    
try:
  response = requests.get(url)  
  soup = bs4.BeautifulSoup(response.text, "html.parser")
  fotos = soup.find_all('img', src=True)
  
  images = []
  for foto in fotos:
    fotoUrl = foto.get('src')
    images.append(fotoUrl)
  print ('Imagenes %s encontradas' % len(images))
    
  #create directory for save images
  if path.isdir("images"):
    pass
  else:
    os.system("mkdir images")
  for image in images:
    if image.startswith("http") == False:
      download = url + image
    else:
      download = image
      # download images in images directory
    try:
      r = requests.get(download)
      f = open('images/%s' % download.split('/')[-1], 'wb')
      f.write(r.content)
      f.close()
    except:
      continue
  print("Se han almacenado las imagenes")
                
except Exception as e:
  print(e)
  print ("Error conexion con " + url)
  pass

lista = []
num = 0
ruta = "images"
os.chdir(ruta)
for root, dirs, files in os.walk(".", topdown=False):
  for name in files:
      #print(os.path.join(root, name))
      hola = ("[+] Metadata for file: %s " % (name) + "\n")
      try:
          exifData = {}
          exif = get_exif_metadata(name)
          if len(exif) == 0:
            continue
          else:
            long = len(name)
            uwu = (name[:long-4])
            nombre = (uwu + ".txt")
            archivo = open(nombre, "a")
            archivo.write(hola)
            for metadata in exif:
              archivo.write("Metadata: %s - Value: %s " %
                      (metadata, exif[metadata]) + "\n")
            lista.append(nombre)
            num = num + 1
            archivo.write("\n")
            archivo.close()
     
      except:
        continue

if num == 0:
  print("No hubo metadata para ningun archivo")
else:
  print("Se almacenaron ", str(num), " .txt en la carpeta", ruta, "bajo los siguientes nombres:")
  for i in lista:
    print(i)
