from config import *
import os
import sys

# Input Parameters

name=sys.argv[1].split('.')[0]
workdir=os.getcwd()
ext='com'
os.chdir(workdir)
basename=name.split('-conf')[0]
# Error exit if no input is given
if len(sys.argv) <2:
    info="""
    no xyz input file was found
    """

    print(info)
    exit()

#template definitions

def generate_com(name,optcores,optmemory,optpartition,optmethod,optbasis,optroute,charge,multiplicity,coord):
    coord='\n'.join(coord)
    xyz=open("{}.xyz".format(name))
    script="""%chk={0}.chk
%nprocs={1}
%mem={2}GB
# {3}/{4} {5}

equillibrium database script

{6} {7}
{8}

""".format(name,optcores,optmemory,optmethod,optbasis,optroute,charge,multiplicity,coord)
    return script

#Generation Steps

#take xyz and make com
with open('{0}/{1}.log'.format(inputdir,basename)) as logfile:
    log=logfile.read().splitlines()
for n,line in enumerate(log):
    if 'Multiplicity =' in line:
        charge=line.split()[2]
        multiplicity=line.split()[5]
coord=open('{}.xyz'.format(name), 'r').read().splitlines()
natom=int(coord[0])
coord=coord[2:natom+2]
shll=open('{0}/{1}.com'.format(workdir,name),'w')
shll.write(generate_com(name,optcores,optmemory,optpartition,optmethod,optbasis,optroute,charge,multiplicity,coord))
shll.close()


