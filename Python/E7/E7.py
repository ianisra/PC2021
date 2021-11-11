'''Equipo: 1 Integrantes: Aidan Eduardo Rodriguez Bautista, Ian Israel Leija
Medina, Melissa Jaqueline Mendieta González y Adrían Alejandro Treviño
Bautista'''

from pyhunter import PyHunter
from openpyxl import Workbook
from openpyxl.styles import Font
import getpass


def Busqueda(organizacion):
    resultado = hunter.domain_search(company=organizacion, limit=1, emails_type='personal')
    return resultado


def GuardarInformacion(organizacion, datosEncontrados):
    Libro = Workbook()
    FoundData = Libro.active
    FoundData = Libro.create_sheet(organizacion)
    FoundData['A1'].font = Font(bold=True)
    FoundData['A1'] = "Dominio"
    FoundData["A2"] = datosEncontrados['domain']

    FoundData['B1'].font = Font(bold=True)
    FoundData['B1'] = "Organizacion"
    FoundData['B2'] = datosEncontrados['organization']

    FoundData['C1'].font = Font(bold=True)
    FoundData['C1'] = "Pais"
    FoundData['C2'] = datosEncontrados['country']

    FoundData['D1'].font = Font(bold=True)
    FoundData['D1'] = "Correo(s)"
    FoundData['D2'] = datosEncontrados['emails'][0]['value']

    FoundData['E1'].font = Font(bold=True)
    FoundData['E1'] = "Nombre"
    FoundData['E2'] = datosEncontrados['emails'][0]['first_name']

    FoundData['F1'].font = Font(bold=True)
    FoundData['F1'] = "Apellido"
    FoundData['F2'] = datosEncontrados['emails'][0]['last_name']

    Libro.save("Hunter" + organizacion + ".xlsx")


print("= = = = = = Script para buscar información = = = = = =")
apikey = getpass.getpass("Ingresa tu API key: ")
hunter = PyHunter(apikey)
orga = input("Dominio a investigar: ")
datosEncontrados = Busqueda(orga)

if datosEncontrados is None:
    print("\nNo se ha encontrado ningun dato relacionado al dominio ingresado")
    exit()
else:
    GuardarInformacion(orga, datosEncontrados)
