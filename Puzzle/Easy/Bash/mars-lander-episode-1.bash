#mars-lander-episode-1
#bash

#!/bin/bash

# surfaceN: the number of points used to draw the surface of Mars.
read -r surfaceN
for (( i=0; i<$surfaceN; i++ )); do
    # landX: X coordinate of a surface point. (0 to 6999)
    # landY: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    read -r landX landY
done

# game loop
while true; do
    # hSpeed: the horizontal speed (in m/s), can be negative.
    # vSpeed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    read -r X Y hSpeed vSpeed fuel rotate power

    if [ $vSpeed -lt -39 ]; then
        echo '0 4'
    else echo '0 0'
    fi
done