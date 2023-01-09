#ascii-art
#bash

#!/bin/bash

declare -A DICT=( ["a"]=0 ["b"]=1 ["c"]=2 ["d"]=3 ["e"]=4 ["f"]=5 ["g"]=6 ["h"]=7 ["i"]=8 ["j"]=9 ["k"]=10 ["l"]=11 ["m"]=12 ["n"]=13 ["o"]=14 ["p"]=15 ["q"]=16 ["r"]=17 ["s"]=18 ["t"]=19 ["u"]=20 ["v"]=21 ["w"]=22 ["x"]=23 ["y"]=24 ["z"]=25 ["A"]=0 ["B"]=1 ["C"]=2 ["D"]=3 ["E"]=4 ["F"]=5 ["G"]=6 ["H"]=7 ["I"]=8 ["J"]=9 ["K"]=10 ["L"]=11 ["M"]=12 ["N"]=13 ["O"]=14 ["P"]=15 ["Q"]=16 ["R"]=17 ["S"]=18 ["T"]=19 ["U"]=20 ["V"]=21 ["W"]=22 ["X"]=23 ["Y"]=24 ["Z"]=25 )
read -r L
read -r H
IFS= read -r T
#echo L:$L >&2
#echo T:$T >&2

for (( i=0; i<$H; i++ )); do
    IFS= read -r ROW
    R+="$ROW"
done
#echo len(R):"${#R}" >&2
#echo R: ${R[@]} >&2

for (( i=0; i<$H; i++ )); do
    SORTIE=''
    for (( j=0; j<${#T}; j++ )); do
        TMP="${T:$j:1}"
        #echo key:"$TMP" // "${DICT[$TMP]}" >&2
        if [ "${DICT[$TMP]+abc}" ]; then
            SORTIE+="${R:$(( ${DICT[$TMP]}*L + i*27*L )):$L}"
        else
            SORTIE+="${R:$(( 26*L + i*27*L )):$L}"
        fi
    done
    echo "$SORTIE"
done