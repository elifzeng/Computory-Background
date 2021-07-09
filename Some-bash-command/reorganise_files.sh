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

# put output file to splited directories

#!/bin/bash
function TravelDir(){
    for file in `ls $1`
    do
        if [ -d "$1/$file" ]
        then
            TravelDir "$1/$file"
        else
            abpath="$1/$file"
            echo $abpath
            echo
            echo $(printf $abpath | cut -d '/' -f 3-4)
            echo
        fi
    done
}
TravelDir $1

# sh ./iterate_files.sh ./CPFrags>tmp.txt
# #cat tmp.txt
# ./CPFrags/extra_part_6/pdb6xzu.ent.MBZ.sdf

# extra_part_6/pdb6xzu.ent.MBZ.sdf

# ./CPFrags/extra_part_6/pdb6xzu.ent.MGDM.sdf

# extra_part_6/pdb6xzu.ent.MGDM.sdf

# ./CPFrags/extra_part_6/pdb6xzu.ent.MIMD.sdf

# extra_part_6/pdb6xzu.ent.MIMD.sdf

# ./CPFrags/extra_part_6/pdb6xzu.ent.MIME.sdf

# extra_part_6/pdb6xzu.ent.MIME.sdf

# ./CPFrags/extra_part_6/pdb6xzu.ent.MIND.sdf

# extra_part_6/pdb6xzu.ent.MIND.sdf
