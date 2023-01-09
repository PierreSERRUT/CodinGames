#the-descent
#bash

#!/bin/bash
while true; do
    declare -a mountains=()
    for (( i=0; i<8; i++ )); do
        # mountainH: represents the height of one mountain.
        read -r  mountainH
        mountains+=($mountainH)
    done

    max_hight=0
    index=0
    for (( j=0; j<8; j++ )); do
        if [ ${mountains[$j]} -gt $max_hight ]; then
            index=$j
            max_hight=${mountains[j]}
        fi
    done

    echo "$index" # The index of the mountain to fire on.
done