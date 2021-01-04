#!/bin/bash

archivelocation=$1
if [ -z ${2+x} ]
    then 
    workdir=`pwd`
    name=$(basename $workdir)name=$2
    else
    name=$2
fi


echo -n "#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --job-name=EZTS-clean
#SBATCH --partition=short
#SBATCH --mem=5Gb
#SBATCH --output=EZTS-clean.o
#SBATCH --error=EZTS-clean.e
#SBATCH --time=1-00

cd $workdir

find $workdir -name '"*rwf"' -delete
find $workdir -name '"Gau*"' -delete
find $workdir -name '"*.chk"' -exec /work/lopez/g16/formchk {} \;
find $workdir -name '"*.chk"' -delete
find $workdir -name '"*gbw"' -delete
find $workdir -name '"*.*tmp*"' -delete
find $workdir -name '"*.scf*"' -delete
find $workdir -name '"*.prop*"' -delete

tar cf - lowest_ts | xz -z - > $1/$name-lowest_ts.tar.xz

" > EZTS-clean.sbatch

sbatch $workdir/EZTS-clean.sbatch
echo "Job submitted to archive and clean $workdir"

echo "Archive will be located at: /scratch/neal.pa/EZTS-runlog/archives/$name-lowest_ts.tar.xz"


