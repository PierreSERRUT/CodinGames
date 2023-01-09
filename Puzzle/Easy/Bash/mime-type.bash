#mime-type
#bash

#!/bin/bash
declare -A DICT
# N: Number of elements which make up the association table.
read -r N
# Q: Number Q of file names to be analyzed.
read -r Q
for (( i=0; i<$N; i++ )); do
    # EXT: file extension
    # MT: MIME type.
    read -r EXT MT
    EXT=${EXT^^}
    DICT[$EXT]=$MT
done

for (( i=0; i<$Q; i++ )); do
    IFS= read -r FNAME
    # echo $FNAME  >&2
    
    FEXT=${FNAME##*'.'}
    INDEX=$((${#FNAME} - ${#FEXT}))
    if [ $INDEX -ne 0 ]; then
        T=${FNAME:0:INDEX-1}
    else
        T=$FNAME
        FEXT=''
    fi
    FEXT=${FEXT^^}

    # echo index: $INDEX >&2
    # echo t:$T >&2
    # echo FEXT:$FEXT >&2

    if [ -v DICT[$FEXT] ]; then
        #echo sortie: ${DICT[$FEXT]}>&2
        echo ${DICT[$FEXT]}
    else 
        echo "UNKNOWN"
    fi
done