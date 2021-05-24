#!/bin/bash
for i in $(seq 1 9)
do
    for j in {a..z}
    do
        mkdir "/home/lzeng02/data/pdb25/pdb$i/$i$j/"
    done
    for k in $(seq 0 9)
    do
        mkdir "/home/lzeng02/data/pdb25/pdb$i/$i$k/"
    done
    for f  in  /home/lzeng02/data/pdb25/"pdb$i"/pdb*ent*
    do
        name=$(basename $f)
        num=${name:3:2}
        mv  $f /home/lzeng02/data/pdb25/"pdb$i"/"$num"/
    done
done
