#horse-racing-duals
#bash

#!/bin/bash
read -r N
for (( i=0; i<$N; i++ )); do
    read -r Pi
    array+=($Pi)
done

#echo ${array[*]} >&2
IFS=$'\n' sorted=($(sort -n <<<"${array[*]}")); unset IFS

diff_min=9999999
for (( i=0; i<$N-1; i++ ));do
    d=$((sorted[$i+1] - sorted[$i])) 
    if [ $d -lt $diff_min ]; then diff_min=$d; fi
done
echo $diff_min