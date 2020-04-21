#!bin/bash
    search=$(basename ${1%.*})
    for i in $search*log;
        do
        freq=$(grep "Frequencies" -m1 $i |awk '{ print $3 }' )
        freqint=${freq%.*}
        if [[ $freqint -lt -200 ]]
            then
            energy=$(grep "Sum of electronic and thermal Free Energies" $i | awk '{ print $8 }')
            echo $i $energy >> $search-ts-energies.txt
        fi
     done
    if test -f "$search-ts-energies.txt"
        then
        lowestenergyts=$(sort -g -k2,2 $search-ts-energies.txt | head -1 |awk '{ print $1 }')

#if this is lowest energy guess_ts, then setup for conformational search, if this is final lowest TS move to lowest_ts
        if [[ $1 == 'ts_guess' ]]
            then
            obabel $lowestenergyts -o mol2 -O ../conf_search/$search.mol2
            python3 ../utilities/maestro-input.py $lowestenergyts $3 $4 $5 $6 $7
        elif [[ $1 == 'conf_opt' ]]
            then
            cp $lowestenergyts ../lowest_ts/
            grep "Sum of electronic and thermal Free Energies" ../lowest_ts/$1*log > ../lowest_ts/$1-lowest_ts-energies.txt
            echo " " >> ../lowest_ts/$1-lowest_ts-energies.txt
            cat $search-ts-energies.txt >> ../lowest_ts/$1-lowest_ts-energies.txt
        fi
    else
         echo "No valid TS found" >> $search-ts-energies.txt
fi

