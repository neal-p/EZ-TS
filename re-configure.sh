#!/bin/bash
#check current directory and move to input
currentdir=`pwd`
if [[ "$currentdir" == *utilities* ]]
    then
    cd ../input
elif [[ "$currentdir" == *ts_guess* ]]
    then
    cd ../input
elif [[ "$currentdir" == *conf_search* ]]
    then
    cd ../input
elif [[ "$currentdir" == *conf_opt* ]]
    then
    cd ../input
elif [[ "$currentdir" == *lowest_ts* ]]
    then
    cd ../input
elif [[ "$currentdir" == *input* ]]
    then pass
else
    cd input
fi

#check if benchmarking was requested
benchmark=$(grep "--benchmark" summary -c)
if [[ $benchmark -gt 0 ]]
    then
    python3 ../utilities/generate-inputs.py -l ts_guess-list.txt --benchmark
    else
    python3 ../utilities/generate-inputs.py -l ts_guess-list.txt
fi
