#Navegando em arquivos .pbd
from Bio.PDB import *
#SMCRA: Structure, Models, Chains, Residuous, Atoms.
parser = PDBParser()
estrutura = parser.get_structure("1BGA","1bga.pdb")

# atomo_100
#modelo = estrutura[0]
#cadeia_A = modelo['A']
#residuo_100 = cadeia_A[100]
#ca_residuo_100 = residuo_100['CA']

# E equivalente as 4 linhas acima resumidas
atomo_101 = estrutura[0]['A'][101]['CA']
atomo_100 = estrutura[0]['A'][100]['CA']
# DISTANCIA EUCLIDIANA
distancia = atomo_101 - atomo_100
print ("\n\nA distancia euclidiana entre CA do residuo 101 e 100 eh:")
print (distancia)
