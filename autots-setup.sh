#!/bin/bash

#Set up directories: conf_opt  conf_search  input  lowest_ts  ts_guess  utilities
workdir=`pwd`
if test -f input/ts_guess-list.txt
    then
    rm input/ts_guess-list.txt
    sed -i '1,/#local workflow variables/!d' utilities/config.py
    find ./ -name "*energies.txt" -delete
else
    mkdir utilities
    mkdir input
    mkdir ts_guess
    mkdir conf_search
    mkdir conf_opt
    mkdir lowest_ts
    mv *log input/
fi

for i in input/*log
    do
    echo -e "$workdir/$i\n$workdir/$i V1 175 R1   90 R2   0\n$workdir/$i V1 175 R1   90 R2 180\n$workdir/$i V1 175 R1  180 R2  90\n$workdir/$i V1 175 R1  180 R2 180\n$workdir/$i V1 175 R1  -90 R2   0\n$workdir/$i V1 175 R1  -90 R2  90" >> input/ts_guess-list.txt
done

cp /home/$USER/autots/config.py  utilities/
cp /home/$USER/autots/generate-inputs.py utilities/
cp /home/$USER/autots/get-lowest.sh utilities/
cp /home/$USER/autots/maestro-input.py utilities/
cp /home/$USER/autots/start.sh ./
cp /home/$USER/autots/xyz2com.py utilities/

echo "maindir='$workdir'" >> utilities/config.py
echo "utilities='$workdir/utilities'" >> utilities/config.py
echo "ts_guess='$workdir/ts_guess'" >> utilities/config.py
echo "conf_search='$workdir/conf_search'" >> utilities/config.py
echo "lowest_ts='$workdir/lowest_ts'" >> utilities/config.py
echo "conf_opt='$workdir/conf_opt'" >> utilities/config.py
echo "inputdir='$workdir/input'" >> utilities/config.py

cd input
python3 ../utilities/generate-inputs.py -l ts_guess-list.txt $1
