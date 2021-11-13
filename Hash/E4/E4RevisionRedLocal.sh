#! /bin/bash
#Nombre del equipo: Polinesios
#Angela Montoya Aldape
#Dariela Hurtado Torres
#Ian Israel Leija Medina

#El script en las capturas está bajo otro nombre, se modificó para que en la hora de entrega
#se viera mas formal y especifico
 
function escaneo() {
  ping -c 1 $1 > /dev/null 2>&1
  [ $? -eq 0 ] && echo "Node with IP: $i is up." >> resultados.txt
  if [ $? -eq 0 ]
  then 
        host=$i
      for ((counter=10; counter<=500; counter++))
      do
        (echo >/dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "Puerto $counter abierto en $i" >> resultados.txt 
      done
  fi
}

if type -t wevtutil &> /dev/null
then
    OS=MSWin
elif type -t scutil &> /dev/null
then
    OS=macOS
else
    OS=Linux
fi

echo "Tu sistema operativo es: $OS" > resultados.txt

read -p "Inserte los primeros octetos de su red local (ejemplo 192.168.100): " redlocal
echo "Muchas gracias, los resultados se irán escribiendo en el .txt, por favor espere."
for i in $redlocal.{1..255}
do
  escaneo $i & disown 
done
