<#
.Description
Este script va a analizar todos los links que contenga una carpeta con archivos txt,
realizando web scraping a dichos links para finalmente extraer los títulos de las 
páginas

Solo es necesario ejecutar el script, lo demás lo pide por medio de Read-Host

#>

$Python = "python.exe"
$Script = Read-Host -Prompt "Inserte la ruta donde se encuentra el archivo de python"
$Path = Read-Host -Prompt "Inserte la ruta en donde se encuentran los archivos txt"
try {
    $files = Get-ChildItem $path"\*.txt"
    $txtlist = $files | Select-Object FullName | Format-Table -HideTableHeaders
    $txtlist | & $Python $Script
} catch {
    Write-Host "Escribió un path de manera erronea"
}
