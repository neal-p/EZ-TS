from config import *
import os
import sys

# Input Parameters

name=sys.argv[1].split('.')[0]
workdir=os.getcwd()
ext='com'
os.chdir(workdir)
basename=name.split('-conf')[0]
charge='unknown'
multiplicity='unknown'

Dict={
    "6-31G":"pople",
    "6-31+G(d,p)":"pople-plusdp",
    "6-311+G(d,p)":"pople-tz",
    "cc-pvdz":"cc-pvdz",
    "cc-pvtz":"cc-pvtz",
    "aug-cc-pvdz":"aug-cc-pvdz",
    "aug-cc-pvtz":"aug-cc-pvtz"
}

if len(sys.argv) > 2:
    benchmark=sys.argv[2]
    benchmarkflag=benchmark.find('benchmark')
else:
    benchmarkflag= -1

# Error exit if no input is given
if len(sys.argv) <2:
    info="""
    no xyz input file was found
    """

    print(info)
    exit()

#template definitions

def generate_com(name,optcores,optmemory,optmethod,optbasis,optroute,charge,multiplicity,coord,benchmarkflag,specialopts):
    coord='\n'.join(coord)
    if  benchmarkflag > -1:
        basisname=Dict[optbasis]
        script="""%chk={0}-{1}-{2}.chk
%nprocs={3}
%mem={4}GB
# {5}/{6} {7} {8}

equillibrium database script

{9} {10}
{11}

""".format(name,optmethod,basisname,optcores,optmemory,optmethod,optbasis,optroute,specialopts,charge,multiplicity,coord)
    else:
        script="""%chk={0}.chk
%nprocs={1}
%mem={2}GB
# {3}/{4} {5} {6}

equillibrium database script

{7} {8}
{9}

""".format(name,optcores,optmemory,optmethod,optbasis,optroute,specialopts,charge,multiplicity,coord)
    return script

def Sbatch(optpartition,optcores,user,optmemory,opttime,workdir,title):
    sbatch="""#!/bin/bash
#SBATCH --job-name={0}
#SBATCH --output=out.o
#SBATCH --error=out.e
#SBATCH --partition={1}
#SBATCH --nodes=1
#SBATCH --ntasks={2}
#SBATCH --mail-type=END
#SBATCH --mail-user={3}
#SBATCH --mem={4}G
#SBATCH --time={5}
#SBATCH --array=1-210%20
hostname
work={6}
cd $work
input=$(sed "${{SLURM_ARRAY_TASK_ID}}q;d" {9}-coms.txt)
export INPUT=$input
export WORKDIR=$work
export GAUSS_SCRDIR=$work
export g16root=/work/lopez/
. $g16root/g16/bsd/g16.profile
cd $WORKDIR
$g16root/g16/g16 $INPUT
""".format(title,optpartition,optcores,user,optmemory,opttime,workdir,title,title,title)
    return sbatch

def Fixcbenchmarkopt(title,user,workdir,optroute,charge,multiplicity):
    batch="""#!/bin/bash
#SBATCH --job-name={0}
#SBATCH --output=resubmit.o
#SBATCH --error=resubmit.e
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mail-type=END
#SBATCH --mail-user={1}
#SBATCH --mem=1G
#SBATCH --time=00:20:00
hostname
work={2}
cd $work
touch failed-script-ran
if test -f {3}-resubmit.txt
    then
    nresub=$(sed "1q;d" {4}-resubmit.txt)
else
    nresub=0
fi
nresub=$((nresub+=1))
if [[ $nresub -lt 2 ]]
    then
    rm {5}-resubmit.txt
    echo $nresub >> {6}-resubmit.txt
    for i in {7}*log
        do
        finished=$(tail $i | grep 'Normal termination' -c )
        if [[ $finished -lt 1 ]]
            then
            maxiter=$(grep "Number of steps exceeded" $i)
            if [[ $maxiter -gt 0 ]]
                then
                sed -i '1,/{8} {9}/!d' ${{i%.*}}.com
                obabel $i -o xyz |tail -n +3 >> ${{i%.*}}.com
                echo " " >> ${{i%.*}}.com
                echo ${{i%.*}}.com >> {10}-resubmit.txt
            else
                sed -i '1,/{11} {12}/!d' ${{i%.*}}.com
                obabel $i -o xyz |tail -n +3 >> ${{i%.*}}.com
                echo " " >> ${{i%.*}}.com
                echo ${{i%.*}}.com >> {13}-resubmit.txt
            fi
        fi
    done
    toresub=$(cat {14}-resubmit.txt |wc -l)
    currentarray=$(sed "12q;d" {15}-submit.sbatch)
    sed -i "s/$currentarray/#SBATCH --array=2-$toresub/g" {16}-submit.sbatch
    sed -i "s/{17}-coms.txt/{18}-resubmit.txt/g" {19}-submit.sbatch
    ID=$(sbatch --parsable {20}-submit.sbatch)
    sbatch --dependency=afterok:$ID  {21}/{22}-lowest.sbatch
    sbatch --dependency=afternotok:$ID {23}-failed.sbatch
fi
""".format(title,user,workdir,title,title,title,title,title,charge, multiplicity,title,charge, multiplicity,title,title,title,title,title,title,title,title,workdir,title,title)
    return batch


#take xyz and make com
def writeinput(inputdir,basename,name,workdir,optcores,optmemory,optmethod,optbasis,optroute,specialopts,x,charge,multiplicity,benchmarkflag,user):
    if x ==0:
        with open('{0}/{1}.log'.format(inputdir,basename)) as logfile:
            log=logfile.read().splitlines()
        for n,line in enumerate(log):
            if 'Multiplicity =' in line:
                charge=line.split()[2]
                multiplicity=line.split()[5]
        if benchmarkflag == 0:
           sbatch=open('{0}/{1}-submit.sbatch'.format(workdir,name),'w')
           sbatch.write(Sbatch(optpartition,optcores,user,optmemory,opttime,workdir,name))
           sbatch.close()
           failed=open('{0}/{1}-failed.sbatch'.format(workdir,name),'w')
           failed.write(Fixcbenchmarkopt(name,user,workdir,optroute,charge,multiplicity))
           failed.close()

    coord=open('{0}.xyz'.format(name), 'r').read().splitlines()
    natom=int(coord[0])
    coord=coord[2:natom+2]
    if  benchmarkflag == 0:
        shll=open('{0}/{1}-{2}-{3}.com'.format(workdir,name,optmethod,Dict[optbasis]),'w')
        shll.write(generate_com(name,optcores,optmemory,optmethod,optbasis,optroute,charge,multiplicity,coord,benchmarkflag,specialopts))
        shll.close()
        return(charge,multiplicity)
    else:
        shll=open('{0}/{1}.com'.format(workdir,name),'w')
        shll.write(generate_com(name,optcores,optmemory,optmethod,optbasis,optroute,charge,multiplicity,coord,benchmarkflag,specialopts))
        shll.close()
#Generation Steps
if benchmarkflag == 0:
    for x,n in enumerate(benchmarkmethods):
        for m in benchmarkbasis:
            optmethod=n
            optbasis=m
            specialopts=benchmarkspecialopts[x]
            charge,multiplicity=writeinput(inputdir,basename,name,workdir,optcores,optmemory,optmethod,optbasis,optroute,specialopts,x,charge,multiplicity,benchmarkflag,user)
else:
    x=0
    writeinput(inputdir,basename,name,workdir,optcores,optmemory,optmethod,optbasis,optroute,specialopts,x,charge,multiplicity,benchmarkflag,user)
