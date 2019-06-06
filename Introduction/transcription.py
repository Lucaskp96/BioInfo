from Bio.Seq import Seq
my_seq = Seq("ATGGAT")
print("Sequência:\t\t\t"+my_seq)

# Sequencia complementar
seq_complementar = my_seq.complement()
print("Sequência complementar:\t\t"+seq_complementar)

#Sequencia reversa complementar
seq_comp_reversa = my_seq.reverse_complement()
print("Sequência complementar reversa: "+seq_comp_reversa)

#Transcrição da região codificante do DNA
seq_rna = my_seq.transcribe()
print("Transcrição RNA:\t\t"+seq_rna)

seq_dna = seq_rna.back_transcribe()
print("Transcrição reversa (RNA->DNA):\t"+seq_dna)
