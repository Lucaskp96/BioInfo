from Bio.Seq import Seq
my_seq = Seq("ATG")

#Transcrição
seq_rna = my_seq.transcribe()

#Tradução
seq_protein = seq_rna.translate()
print(seq_protein)
