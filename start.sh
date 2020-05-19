#!/bin/bash
for i in input/*log
    do
    file=$(basename ${i%.*})
    ID=$(sbatch --parsable ts_guess/$file-submit.sbatch)
    echo "submitted autots workflow - $i"
done
touch status.txt
