# Input Parameters
optcores="7"
optmemory="28" #GB
optpartition="short,lopez"
optmethod="b3lyp"
optbasis="6-31G"
#remeber force constants required for ts optimization
optroute="opt=(ts,noeigen,calcfc) freq=noraman"
opttime='1:00:00'
specialopts='empiricaldispersion=GD3bj'
benchmarkmethods=['M11L','SVWN','SVWN5','MN12SX','M062X','M06HF','N12SX','mPW2PLYP','MPWb95','PBE1PBE','B2PLYP','PBEh1PBE','OHSE2PBE','mPW1PBE','mPW1PW91','APFD','TPSSh','B3P86','tpsskcis','B3LYP','BHandH','BMK','MPWB95','MPWPW91','bb95','wb97xd','wb97','wb97x','cam-b3lyp','LC-wHPBE']
benchmarkspecialopts=['','','','','','','','','IOp(3/76=0690003100)','empiricaldispersion=GD3bj','empiricaldispersion=GD3bj','','','','','','empiricaldispersion=GD3bj','','IOp(3/76=0870001300)','empiricaldispersion=GD3bj','','empiricaldispersion=GD3bj','IOp(3/76=0560004400)','IOp(3/76=0572004280)','IOp(3/76=0580004200)','','','','empiricaldispersion=GD3bj','']
benchmarkbasis=['6-31G(d)','6-31+G(d,p)','6-311+G(d,p)','cc-pvdz','cc-pvtz','aug-cc-pvdz','aug-cc-pvtz']

#local workflow variables
