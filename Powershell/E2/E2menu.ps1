#Integrantes
#ÁngelaMontoya,IanLeija,DarielaHurtado
$contador = $True
while($contador -eq $True) {
  $opcion  = Read-Host -Prompt '¿Qué desea realizar? [1] Ver Status [2] Cambiar Status [3] Ver Perfil [4] Cambiar Perfil [5] Ver reglas de bloqueo [6] Agregar reglas de bloqueo [7] Eliminar reglas de bloqueo [8] Salir'
  switch($opcion){
    1 {
      Ver-StatusPerfil
    }
    2 {
      Cambiar-StatusPerfil
    }
    3 { 
      Ver-PerfilRedActual
    }
    4 {
      Cambiar-PerfilRedActual
    }
    5 {
      Ver-ReglasBloqueo
      }
    6 { 
      Agregar-ReglasBloqueo
    }
    7 {
      Eliminar-ReglasBloqueo
    }
    8 {
      exit
    }
    default {
    Write-Host "No insertó un carácter válido"
    }
  }
}
