#!/bin/bash
# echo 'jksdkfsd $12'

v1=1
v2=2
# echo "scale=2; $v1/$v2" | bc
user=~/test.pdb
font=test

# if [ -e $user ]
# then
#     echo The $user exists.
#     if [ -d $user ] && [ -r $user ]
#     then
#         echo The $user is a directory and it is readable.
#     elif [ -f $user ] && [ -r $user ]
#     then
#         echo The $user is a file and it is readable.
#     fi
# else
#     echo The $user do not exist.
# fi

# case $v2 in
# 4 | 5)
#     echo haha;;
# 2)
#     echo hehe;;
# 1)
#     echo heihei;;
# *)
#     echo pei!;;
# esac
# for i in ~/*
# do
#     if [ -d $i ]
#     then 
#         echo $i is a directory
#     elif [ -f $i ]
#     then
#         echo $i is a file
#         break
#     else
#         echo I don\'t know the type of $i
#     fi
# done
# for (( a = 1; a < 4; a++ ))
# do
#     echo outer loop $a
#     for (( b = 2; b < 10; b = b+2))
#     do
#         if [ $b -gt 4 ]
#         then 
#             continue 2
#         fi
#         echo "  inner loop $b"
#     done
#     echo haha
# done

# f=1
# for (( n = 1; n <= $1; n++ ))
# do
#     f=$[ $f * $n ]
# done
# echo The f of $1 is $f.
# echo The second positional parameter is $0 $( basename $0 )

# name=$(basename $0)
# if [ $name = "addem" ]
# then
#     total=$[ $1+$2 ]
# elif [ $name = "multem" ]
# then
#     total=$[ $1*$2 ]
# fi
# echo The total number is ${!#}
# echo 
# while [ -n "$1" ]
# do
#     case "$1" in
#         -a) echo "Found $1" ;;
#         -b) echo "Found $1" ;;
#         -c) echo "Found $1" ;;
#          *) echo "$1 is not an option" ;;
#     esac
#     shift
# done


# echo
# while getopts :ab:cd opt
# do
#     case "$opt" in
#     a)
#         echo "Found the -a option"
#         echo $OPTIND ;;
#     b)
#         echo "Found the -b option, with value $OPTARG"
#         echo $OPTIND ;;
#     c)
#         echo "Found the -c option"
#         echo $OPTIND ;;
#     d)
#         echo "Found the -d option"
#         echo $OPTIND ;;
#     *)
#         echo "Unkown option: $opt"
#         echo $OPTIND
#     esac
# done
#
# echo "present optind is $OPTIND"
# shift $[ $OPTIND -1 ]
# echo "$@"

# read -p "enter options: " opt m n
# echo "opt $opt m $m n $n"
# echo $@

# tempfile=$(mktemp test19.XXXXXX)
# exec 3>$tempfile
# echo "This script writes to temp file $tempfile"
# echo "first line" >&3
# echo "second line" >&3
# exec 3>&-
# echo "the contents of temp file is:"
# cat $tempfile
# rm -f $tempfile

# #Testing signal trapping
# trap "echo ' Sorry, I have trapped Ctrl-C'" SIGINT
# echo This is a test script
# count=1
# while [ $count -le 5 ]
# do
#     echo "Loop #$count"
#     sleep 1
#     count=$[ $count + 1 ]
# done
# # remove the trap
# trap -- SIGINT
# echo "I just removed the trap"
# count=1
# while [ $count -le 5 ]
# do
#     echo "Second Loop #$count"
#     sleep 1
#     count=$[ $count + 1 ]
# done 