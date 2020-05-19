# Input Parameters
optcores=['7','28','28','28']
optmemory=['28','112','112','112']
optpartition="short,lopez"
optmethod="b3lyp"
optbasis="6-31G(d)"
#remeber force constants required for ts optimization
optroute="opt=(calcfc,ts,noeigen) freq=noraman"
opttime='1-00:00:00'
specialopts='empiricaldispersion=GD3bj'
benchmarkmethods=['M11L','SVWN','SVWN5','MN12SX','M062X','M06HF','N12SX','MPWb95','PBE1PBE','PBEh1PBE','OHSE2PBE','mPW1PBE','mPW1PW91','APFD','TPSSh','B3P86','tpsskcis','B3LYP','BHandH','BMK','MPWB95','MPWPW91','bb95','wb97xd','wb97','wb97x','cam-b3lyp','LC-wHPBE']
benchmarkspecialopts=['','','','','','','','IOp(3/76=0690003100)','empiricaldispersion=GD3bj','','','','','','','','IOp(3/76=0870001300)','empiricaldispersion=GD3bj','','empiricaldispersion=GD3bj','IOp(3/76=0560004400)','IOp(3/76=0572004280)','IOp(3/76=0580004200)','','','','empiricaldispersion=GD3bj','']
benchmarkbasis=[['6-31G(d)'],['6-31+G(d,p)','6-311+G(d,p)'],['cc-pvdz','aug-cc-pvdz','cc-pvtz','aug-cc-pvtz']]

#CONFORMATIONAL SEARCH:
CRESTcores=14
CRESTmem=55
CRESTtime='1-00:00:00'
CRESTpartition='short,lopez'
CRESTmethod=CRESTmethod='-xnam /work/lopez/xtb/xtb_6.2.3/bin/xtb -g H2O -ewin 500 -T 14 -opt crude -subrmsd --verbose'

ORCAmethod='B3LYP D3BJ 6-31G(d) def2/J NOAUTOSTART'
ORCAcores=7
ORCAmem=55
ORCApartition='lopez,short'
ORCAtime='1-00:00:00'


user='neal.pa@husky.neu.edu'
user='neal.pa@husky.neu.edu'
user='neal.pa@husky.neu.edu'
#local workflow variables
