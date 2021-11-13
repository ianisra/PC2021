#!/bin/bash
#llave = cfccfca8a55b497f9f3c5b22a9cd132a

#Integrantes
#Angela Montoya Aldape
#Dariela Hurtado Torres
#Ian Israel Leija Medina
 
function verificacion {
	 sleep 5

        if [ "$invocacion" == "" ];
        then
                echo "Su correo no ha sido vulnerado :)"
	else
		servicios=$(echo $invocacion | grep -Po ':".*?"' | sed -e 's/^.//')
		if [ "$servicios" == "" ];
		then
			echo "Ha insertado mal su llave"
			exit
		else
			echo "Su correo ha sido vulnerado :(" 
			echo "Servicios donde ocurrió dicha vulneración:"       
        		echo $invocacion | grep -Po ':".*?"' | sed -e 's/^.//'

        	fi
	fi
}

read -sp "Inserte la llave:" key
while read p;
do
	invocacion=$(curl -s https://haveibeenpwned.com/api/v3/breachedaccount/"$p" -H 'hibp-api-key:'$key)
	echo -e "\nVerificando el correo: "$p
	verificacion 
done < E5_Emails.txt
