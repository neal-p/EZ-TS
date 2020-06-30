#!/bin/bash

workdir=`pwd`
name=$(basename $workdir)

echo -n "#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --job-name=autots-clean
#SBATCH --partition=short
#SBATCH --mem=5Gb
#SBATCH --output=autots-clean.o
#SBATCH --error=autots-clean.e
#SBATCH --time=1-00

cd $workdir

find $workdir -name '"*rwf"' -delete
find $workdir -name '"Gau*"' -delete
find $workdir -name '"*.chk"' -exec /work/lopez/g16/formchk {} \;
find $workdir -name '"*.chk"' -delete
find $workdir -name '"*gbw"' -delete
find $workdir -name '"*.*tmp*"' -delete

tar cf - lowest_ts | xz -z - > /scratch/neal.pa/autots-runlog/archives/$name-lowest_ts.tar.xz
#tar -xf azobenzene.tar.xz -C test-unzip/

" > autots-clean.sbatch

sbatch $workdir/autots-clean.sbatch
echo "Job submitted to archive and clean $workdir"

echo "Archive will be located at: /scratch/neal.pa/autots-runlog/archives/$name-lowest_ts.tar.xz"


