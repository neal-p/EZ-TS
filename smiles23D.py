from rdkit.Chem import AllChem
import numpy as np

input=
allinputs=np.genfromtxt(input,dtype='str')
smiles=allinputs[:,0]
names=allinputs[:,1]
for b,c in enumerate(smiles):

    mol = AllChem.MolFromSmiles(c)
    mol = AllChem.AddHs(mol,addCoords=True)
    AllChem.EmbedMultipleConfs(mol,numConfs=5)
    energies=AllChem.UFFOptimizeMoleculeConfs(mol, numThreads=0)
    confs=np.zeros(len(energies))
    for x,i in enumerate(energies):
        confs[x]=i[1]
    min=np.argmin(confs)
    AllChem.MolToXYZFile(mol,'{0}.pdb'.format(names[b]),confId=int(min))
