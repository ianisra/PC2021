function show-passwd{
    param([Parameter(Mandatory)][string] $wifi)

    try{
        netsh wlan show profile name=$wifi key=clear
        Write-Host "Fin de la funcion"

    } catch{
        $_.ExceptionMessage
    }

}

function on-off{
    param([Parameter(Mandatory)][ValidateSet('enable','disabled')][string]$onoff)
    try{
        netsh interface set interface “Wi-Fi" $onoff
    }catch{
        $_.ExceptionMessage
    } 
}

function delete{
    param([Parameter(Mandatory)][string]$red)
    try{
        netsh wlan delete profile name=$red
    }catch{
        $_.ExceptionMessage
    }
}
