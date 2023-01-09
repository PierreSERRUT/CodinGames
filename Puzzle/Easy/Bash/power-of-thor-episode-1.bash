#power-of-thor-episode-1
#bash

#!/bin/bash

read -r lightX lightY initialTX initialTY

TX=$initialTX 
TY=$initialTY

update_pos()
{
    case $1 in 
        "N") TY=$((TY - 1));;
        "S") TY=$((TY + 1));;
        "E") TX=$((TX + 1));;
        "W") TX=$((TX - 1));;
        *);;
    esac
}

while true; do
    # remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
    read -r remainingTurns
    
    dest=""
    destX=""
    destY=""
    deltaX=$((lightX-TX))
    deltaY=$((lightY-TY))

    if [ $deltaY -gt 0 ];then 
        destY+="S"
    else if [ $deltaY -lt 0 ];then
        destY+="N"
        fi
    fi
    
    if [ $deltaX -gt 0 ];then 
        destX+="E"
    else if [ $deltaX -lt 0 ];then
        destX+="W"
        fi
    fi
    delta=$((${deltaX#-} - ${deltaY#-}))
    #echo "deltaX: $deltaX /deltaY: $deltaY /delta: $delta ">&2
    #echo "Tpos avant; TX: $TX /TY: $TY">&2
    if [ $delta -gt 0 ];then 
        dest="$destX"
        update_pos "$destX"
    else if [ $delta -lt 0 ]; then
            dest="$destY"
            update_pos "$destY"
        else 
            update_pos "$destX"
            update_pos "$destY"
            dest="$destY$destX"
        fi
    fi
    
    #echo "Tpos avant; TX: $TX /TY: $TY">&2

    # A single line providing the move to be made: N NE E SE S SW W or NW
    echo "$dest"
done